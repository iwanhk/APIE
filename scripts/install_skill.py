#!/usr/bin/env python3
"""Install the APIE Brain skill into mainstream AI coding tools.

APIE Brain is tool-agnostic. This installer copies the skill package
(skills/apie-brain/) into the location each tool expects:

    Codex        ~/.codex/skills/apie-brain        (CODEX_HOME respected)
    Claude Code  ~/.claude/skills/apie-brain
    Cursor       ~/.cursor/rules/apie.mdc          (generated rule)
    generic      --dest <dir>

Usage:
    python3 scripts/install_skill.py --list
    python3 scripts/install_skill.py --tool codex
    python3 scripts/install_skill.py --tool claude --force
    python3 scripts/install_skill.py --tool cursor
    python3 scripts/install_skill.py --tool generic --dest ./vendor/skills
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "apie-brain"


def tool_targets() -> dict[str, Path]:
    home = Path.home()
    codex_home = Path(os.environ.get("CODEX_HOME", home / ".codex"))
    return {
        "codex": codex_home / "skills" / "apie-brain",
        "claude": home / ".claude" / "skills" / "apie-brain",
        "cursor": home / ".cursor" / "rules" / "apie.mdc",
    }


def parse_skill_md(path: Path) -> tuple[str, str]:
    """Return (description, body) from a SKILL.md with YAML frontmatter."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit(f"bad SKILL.md: {path}")
    fm, body = m.group(1), m.group(2)
    dm = re.search(r"^description:\s*(.+)$", fm, re.M)
    description = dm.group(1).strip() if dm else "APIE Brain: product innovation engine"
    return description, body


def install_dir(src: Path, dest: Path, force: bool) -> None:
    if dest.exists():
        if force:
            shutil.rmtree(dest)
        else:
            raise SystemExit(f"already installed: {dest} (use --force to replace)")
    shutil.copytree(src, dest)
    print(f"installed: {dest}")


def install_cursor(src: Path, dest: Path, force: bool) -> None:
    if dest.exists() and not force:
        raise SystemExit(f"already installed: {dest} (use --force to replace)")
    description, body = parse_skill_md(src / "SKILL.md")
    mdc = f"---\ndescription: {description}\nglobs: **/*.md\n---\n{body}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(mdc, encoding="utf-8")
    print(f"installed: {dest}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="show install targets")
    parser.add_argument("--tool", choices=["codex", "claude", "cursor", "generic"])
    parser.add_argument("--dest", help="target directory (required for --tool generic)")
    parser.add_argument("--force", action="store_true", help="replace existing install")
    args = parser.parse_args()

    if not SKILL.exists():
        raise SystemExit(f"skill package not found: {SKILL}")

    if args.list or not args.tool:
        for name, dest in tool_targets().items():
            print(f"{name:8s} -> {dest} {'(installed)' if dest.exists() else ''}")
        if not args.tool:
            return 0

    if args.tool == "generic":
        if not args.dest:
            raise SystemExit("--tool generic requires --dest <dir>")
        install_dir(SKILL, Path(args.dest).expanduser() / "apie-brain", args.force)
    elif args.tool == "cursor":
        install_cursor(SKILL, tool_targets()["cursor"], args.force)
    else:
        install_dir(SKILL, tool_targets()[args.tool], args.force)

    print("Done. The skill will be available on the tool's next session/turn.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

