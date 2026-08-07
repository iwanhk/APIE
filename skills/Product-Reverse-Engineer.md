---
id: product-reverse-engineer
type: skill
name: Product Reverse Engineer
skill_type: analysis
tags: [reverse-engineering, teardown, analysis]
inputs: [product-name, source-material-or-urls]
outputs: [products/<Category>/<Product>.md, PRODUCTS.md update]
last_updated: 2026-08-07
---

# Product Reverse Engineer

## Purpose

Produce a sourced product teardown that explains the mechanism of a product's success and connects it to the pattern library. One teardown per day is the pipeline's engine (see [DAILY-PIPELINE.md](../docs/DAILY-PIPELINE.md)).

## When To Use / When NOT To Use

Use when: a product is on the watchlist, is mechanism-new, or has a milestone worth documenting.
Do not use for: pure feature comparisons, PRD writing, or products with no verifiable public information.

## Workflow

1. **Retrieve** — read `docs/APIE-Product-Schema-v1.md` and `products/_TEMPLATE.md`; gather product materials (official site, blog, filings, press, community).
2. **Collect facts** — build a fact sheet: founding, milestones, funding, revenue, users, pricing, architecture. Every volatile fact gets a source URL and an "as of" date.
3. **Reconstruct history** — dated timeline; mark conflicting sources rather than averaging them.
4. **Identify the mechanism** — one sentence: the loop that makes the product work.
5. **Walk the product** — target user, business model, growth loop, UX core loop, AI stack, architecture.
6. **Map to patterns** — link existing `patterns/*.md`; name emerging patterns for future files.
7. **Write lessons & innovation** — transferable rules; what the product invented; where patterns could go next.
8. **Write the file** — fill `products/_TEMPLATE.md`, keep every section, delete the instruction blockquote.
9. **Validate** — run `python3 scripts/build_dataset.py`; confirm the product appears in `datasets/Products.json` with no warnings.
10. **Index** — update `PRODUCTS.md`.

## Quality Checks

- Every section present; `Unknown` used honestly
- Every number/date has a source and as-of date
- At least one pattern link (existing file or clearly named emerging pattern)
- Dataset builder passes with no validation warnings
- No marketing claims — mechanisms only

## Provenance

The `Sources` section records where each volatile fact came from. Pattern links record which library entries the teardown instantiates. The dataset record (`datasets/Products.json`) stores the frontmatter for machine lookup.

## Example Output

[products/AI/Cursor.md](../products/AI/Cursor.md)

