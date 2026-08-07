# APIE Skill Specification v1

**Status:** ratified (initial release)
**Applies to:** `skills/<Skill>.md`
**Frontmatter `type`:** `skill`

## Purpose

An APIE skill is a **structured, executable workflow** for an AI agent — not a prompt. Skills implement the Brain pipeline (Retrieve → Reason → Compose → Evaluate → Innovate) and always cite their sources.

## Required Frontmatter

```yaml
---
id: product-reverse-engineer
type: skill
name: Product Reverse Engineer
skill_type: analysis | generation | evaluation | combination
tags: [reverse-engineering, teardown]
inputs: [product-name, urls]
outputs: [product-file]
last_updated: 2026-08-07
---
```

| Field | Notes |
| --- | --- |
| `skill_type` | `analysis` (understand), `generation` (create), `evaluation` (judge), `combination` (compose across domains) |
| `inputs` | what the executor must provide |
| `outputs` | what the executor must produce, with file destinations |

## Required Sections

### Purpose
One paragraph: what the skill does and when to use it.

### When To Use / When NOT To Use
Scoping rules so the skill is not misapplied.

### Workflow
Numbered steps. Each step states its input, action, and output. Steps must reference repository assets (schemas, datasets, templates) by path.

### Quality Checks
Verifiable exit criteria. Every skill must include: all outputs follow the relevant schema; every volatile fact has a source and as-of date; every claim is falsifiable.

### Provenance
How the skill records where each output element came from (product IDs, pattern IDs, dataset records).

### Example Output
Pointer to a real artifact in the repository (e.g., a product teardown).

## Example

[skills/Product-Reverse-Engineer.md](../skills/Product-Reverse-Engineer.md)

