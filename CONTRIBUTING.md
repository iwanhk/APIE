# Contributing to APIE

Thank you for helping build the open knowledge base for AI product innovation.

APIE only works if its knowledge is **structured, sourced, and current**. Please follow these rules.

## What We Accept

- Product teardowns (`products/<Category>/<Product>.md`)
- Patterns (`patterns/<Pattern>.md`)
- Features (`features/<Feature>.md`)
- UX flows (`ux-flows/<Flow>.md`)
- Business models (`business-models/<Model>.md`)
- Cross-domain transfers (`cross-domain/<Source>-to-<Target>.md`)
- Skills (`skills/<Skill>.md`) — must follow the Skill Specification
- Innovation challenges (`examples/`)
- Weekly reports (`docs/reports/`)
- Improvements to scripts, schemas, and docs

## The Golden Rules

1. **Schema first.** Every content file starts with YAML frontmatter matching its schema (`docs/APIE-*-Schema-v1.md`). No frontmatter, no merge.
2. **Facts have sources.** Every material claim carries a `Sources` section or inline link. Numbers are impossible to verify later without them.
3. **"As of" dates.** Product facts change fast. Mark volatile facts with `as of YYYY-MM` (or the frontmatter `last_updated` field) and update `last_updated` when you touch a file.
4. **No marketing.** We describe *how* products work and *why* they worked — not how great they are. Praise without mechanism is removed.
5. **One file, one concept.** A pattern is a pattern; a feature is a feature; a product is a product. Do not merge concepts.

## How to Add a Product Teardown

1. Copy `products/_TEMPLATE.md` to `products/<Category>/<Product>.md`.
2. Fill every section honestly. Where data is unknown, write `Unknown` rather than guessing.
3. Verify numbers against primary or reputable secondary sources (company filings, official blogs, major press).
4. Link related patterns in the `Patterns` section — this is what makes the knowledge base *reusable*.
5. Run `python3 scripts/build_dataset.py` and confirm your file appears in `datasets/Products.json` without validation warnings.
6. Update `PRODUCTS.md` index.

## How to Add a Pattern

Patterns are the core of APIE. A pattern is a *repeatable mechanism* — not a single product's feature.

1. Copy `patterns/_TEMPLATE.md` to `patterns/<Pattern>.md`.
2. Fill `Definition`, `Problem`, `When To Use`, `When NOT To Use`, `Examples`, `Engineering`, `UX`, `Business`.
3. If you can describe a transfer to another domain, create a cross-domain file too.
4. Run the dataset builder and update `PATTERNS.md`.

## How to Propose a Schema Change

Schema changes affect every AI agent that indexes this repo. Treat them like RFCs:

1. Open a GitHub issue with the `schema` label and the title `APIE <Name> Schema vN: <change>`.
2. Describe the field, why it is needed, and which existing files would change.
3. Wait for maintainer review and a comment period (minimum 7 days).
4. Merge only with maintainer approval; bump the schema version, never silently mutate a released schema.

## Pull Request Checklist

- [ ] File follows the relevant schema (frontmatter + sections)
- [ ] All volatile facts include sources and as-of dates
- [ ] `scripts/build_dataset.py` runs without validation errors
- [ ] Index files (`PRODUCTS.md`, `PATTERNS.md`, `SKILLS.md`, …) updated
- [ ] Links are relative and resolve
- [ ] No secrets, credentials, or personal data

## Code of Conduct

All interactions are governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Be curious, be precise, and treat disagreements as data.
