#!/usr/bin/env python3
"""Build APIE datasets from Markdown frontmatter.

Scans the repository content directories, parses the YAML frontmatter of every
Markdown file, validates it against its schema, and writes datasets/*.json.

Usage:
    python3 scripts/build_dataset.py                # build all datasets
    python3 scripts/build_dataset.py --validate     # validate only, exit 1 on errors
    python3 scripts/build_dataset.py --quiet        # suppress per-file output
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATASETS = ROOT / "datasets"

# type -> (directory, required fields, allowed values for specific fields)
SCHEMAS = {
    "product": {
        "dir": "products",
        "recursive": True,
        "required": [
            "id", "type", "name", "category", "company", "founded",
            "status", "tags", "last_updated", "sources",
        ],
        "allowed": {
            "category": {"AI", "FinTech", "SaaS", "Consumer", "Healthcare",
                         "Education", "Gaming", "Enterprise", "Other"},
            "status": {"active", "acquired", "defunct", "unknown"},
        },
    },
    "pattern": {
        "dir": "patterns",
        "recursive": False,
        "required": ["id", "type", "name", "status", "tags", "last_updated"],
        "allowed": {"status": {"established", "emerging", "hypothesis"}},
    },
    "feature": {
        "dir": "features",
        "recursive": False,
        "required": ["id", "type", "name", "tags", "last_updated"],
        "allowed": {},
    },
    "flow": {
        "dir": "ux-flows",
        "recursive": False,
        "required": ["id", "type", "name", "tags", "last_updated"],
        "allowed": {},
    },
    "skill": {
        "dir": "skills",
        "recursive": False,
        "required": [
            "id", "type", "name", "skill_type", "tags", "inputs",
            "outputs", "last_updated",
        ],
        "allowed": {"skill_type": {"analysis", "generation", "evaluation", "combination"}},
    },
    "cross-domain": {
        "dir": "cross-domain",
        "recursive": False,
        "required": [
            "id", "type", "name", "source_domain", "target_domain",
            "source_pattern", "status", "last_updated",
        ],
        "allowed": {"status": {"hypothesis", "in-practice", "validated"}},
    },
}

# Plural dataset filenames, matching the public API surface (datasets/README.md).
DATASET_NAMES = {
    "product": "Products",
    "pattern": "Patterns",
    "feature": "Features",
    "flow": "Flows",
    "skill": "Skills",
    "cross-domain": "CrossDomain",
}


def parse_frontmatter(text: str) -> dict | None:
    """Parse the YAML frontmatter of a Markdown file (stdlib-only, strict subset)."""
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None

    data: dict = {}
    i = 1
    while i < end:
        line = lines[i]
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not m:
            i += 1
            continue
        key, raw = m.group(1), m.group(2).strip()
        if raw == "":
            # block list (lines starting with "- ")
            values = []
            j = i + 1
            while j < end and re.match(r"^\s*-\s+", lines[j]):
                values.append(re.sub(r"^\s*-\s+", "", lines[j]).strip().strip("\"'"))
                j += 1
            data[key] = values
            i = j
            continue
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            data[key] = [v.strip().strip("\"'") for v in inner.split(",") if v.strip()]
        else:
            data[key] = raw.strip("\"'")
        i += 1
    return data


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def collect_files(type_name: str, schema: dict) -> list[Path]:
    base = ROOT / schema["dir"]
    if schema["recursive"]:
        files = base.rglob("*.md")
    else:
        files = base.glob("*.md")
    # READMEs and templates are guidance, not data.
    return sorted(f for f in files if f.name not in ("README.md", "_TEMPLATE.md"))


def validate_item(type_name: str, schema: dict, item: dict, path: Path, errors: list[str]) -> None:
    rel = path.relative_to(ROOT).as_posix()
    for field in schema["required"]:
        if field not in item or item[field] in (None, "", []):
            errors.append(f"{rel}: missing required field '{field}'")
    if item.get("type") != type_name:
        errors.append(f"{rel}: frontmatter type '{item.get('type')}' != '{type_name}'")
    for field, allowed in schema["allowed"].items():
        if field in item and item[field] not in allowed:
            errors.append(f"{rel}: field '{field}' = '{item[field]}' not in {sorted(allowed)}")
    lu = item.get("last_updated")
    if lu:
        try:
            datetime.strptime(str(lu), "%Y-%m-%d")
        except ValueError:
            errors.append(f"{rel}: last_updated '{lu}' must be YYYY-MM-DD")
    if type_name == "cross-domain":
        if item.get("source_pattern") and not (ROOT / str(item["source_pattern"])).exists():
            errors.append(f"{rel}: source_pattern '{item['source_pattern']}' does not resolve")


def build(schema_type: str, schema: dict, quiet: bool) -> tuple[dict, list[str]]:
    items, errors = [], []
    for path in collect_files(schema_type, schema):
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{path.relative_to(ROOT).as_posix()}: no frontmatter")
            continue
        validate_item(schema_type, schema, fm, path, errors)
        items.append({
            **fm,
            "file": path.relative_to(ROOT).as_posix(),
            "title": first_heading(text),
        })
        if not quiet:
            print(f"  {schema_type:>12}  {fm.get('id', '?')}")
    dataset = {
        "schema": f"APIE-{schema_type.title()}-Schema-v1",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "count": len(items),
        "items": items,
    }
    return dataset, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", action="store_true", help="validate only; exit 1 on errors")
    parser.add_argument("--quiet", action="store_true", help="suppress per-file output")
    args = parser.parse_args()

    all_errors: list[str] = []
    for type_name, schema in SCHEMAS.items():
        if not args.quiet:
            print(f"[{type_name}] scanning {schema['dir']}/")
        dataset, errors = build(type_name, schema, args.quiet)
        all_errors.extend(errors)
        if not args.validate:
            (DATASETS / f"{DATASET_NAMES[type_name]}.json").write_text(
                json.dumps(dataset, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )

    if all_errors:
        print("\nValidation errors:")
        for e in all_errors:
            print(f"  ✗ {e}")
        print(f"\n{len(all_errors)} error(s).")
        return 1

    if not args.quiet:
        print("\nAll files valid. Datasets written to datasets/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
