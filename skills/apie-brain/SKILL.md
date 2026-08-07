---
name: apie-brain
description: Product innovation engine that retrieves product/pattern knowledge, reasons over it, composes cross-domain concepts, evaluates them, and produces product concepts with full provenance. Use when the user asks to design or ideate a new product, reverse-engineer or analyze why a product succeeded, mine product design patterns, run an innovation challenge (two products into 20 ideas), generate product concepts, write a product teardown, or analyze product-market fit. Works with or without the APIE knowledge base (github.com/iwanhk/APIE); with a local clone it retrieves live datasets.
---

# APIE Brain

## Overview

APIE Brain is the reasoning engine of the APIE knowledge base: **Retrieve → Reason → Compose → Evaluate → Innovate**. Nothing is generated from nothing — every output traces back to patterns, products, or datasets.

## Prerequisites

Best with a local clone of `github.com/iwanhk/APIE` (use `products/`, `patterns/`, `features/`, `datasets/*.json`). If no clone is available, work from the bundled references plus web research and state that limitation in the output.

## Workflow

### 1. Retrieve

- Load datasets when the repo is available: `datasets/Products.json`, `Patterns.json`, `Features.json`, `Flows.json`, `CrossDomain.json` — or read the directories directly.
- Read [references/schemas.md](references/schemas.md) for entry formats before writing anything.
- Build a context pack: pattern candidates with evidence, each citing product/pattern IDs.

### 2. Reason

- Decompose the problem: who / what job / what constraint / what metric.
- Map each part onto patterns from the context pack.
- Identify the **engine** pattern versus supporting patterns.

### 3. Compose

- Combine patterns, preferring cross-domain pairs (e.g., a recommendation loop → investment products).
- Generate 10–30 concepts. Every idea names its source patterns in brackets; unprovenanced ideas are discarded.

### 4. Evaluate

- Score each concept on five axes, 1–5, with reasons: User value, Feasibility, Moat, Timing, Risk.
- Rank and state kill criteria loudly.

### 5. Innovate

- Winner writeup: target user, core loop, the one metric, pattern stack, first-90-days.
- File as `examples/Innovation-<Concept>.md` (in-repo) with full provenance.

## Task Outputs

| Task | Use |
| --- | --- |
| Product teardown | [references/product-template.md](references/product-template.md) — every section mandatory, facts sourced with "as of" dates |
| Pattern mining | [references/pattern-template.md](references/pattern-template.md) — ≥2 examples, When NOT To Use mandatory |
| Innovation challenge | 20 ideas + evaluation table + winner; see `examples/` for a worked sample |
| Daily pipeline run | [references/daily-task.md](references/daily-task.md) |

## Rules

1. **Compose, don't generate** — ideas without source patterns are discarded.
2. **Provenance everywhere** — cite product/pattern IDs in every output element.
3. **Evaluate honestly** — kill weak ideas; the five axes are not optional.
4. **Feedback** — failed concepts become pattern pitfalls; the brain learns by writing files.
5. **Facts** — every number/date carries a source and an "as of" date; write `Unknown` rather than guessing.
6. **Regulated domains** (finance, health) — explain consequences, never issue suitability verdicts or predictions; a constrained recommendation is education + guardrails, not advice.

## References

- [references/schemas.md](references/schemas.md) — the five APIE schemas, condensed
- [references/product-template.md](references/product-template.md) — teardown template
- [references/pattern-template.md](references/pattern-template.md) — pattern template
- [references/daily-task.md](references/daily-task.md) — daily pipeline playbook

