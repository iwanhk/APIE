# APIE Product Schema v1

**Status:** ratified (initial release)
**Applies to:** `products/<Category>/<Product>.md`
**Frontmatter `type`:** `product`

## Purpose

A product teardown that explains *how* a product works and *why* it worked — the mechanism, not the marketing. Every teardown is a node in the knowledge graph: it references patterns, features, flows, and business models that live elsewhere.

## Required Frontmatter

```yaml
---
id: cursor
type: product
name: Cursor
category: AI
company: Anysphere
founded: 2022
status: active | acquired | defunct | unknown
tags: [developer-tools, agentic-coding]
last_updated: 2026-08-07
sources: [https://…, https://…]
---
```

| Field | Required | Notes |
| --- | --- | --- |
| `id` | yes | permanent kebab-case ID |
| `type` | yes | must be `product` |
| `name` | yes | display name |
| `category` | yes | one of: AI, FinTech, SaaS, Consumer, Healthcare, Education, Gaming, Enterprise, Other |
| `company` | yes | legal/operating entity |
| `founded` | yes | year |
| `status` | yes | active / acquired / defunct / unknown |
| `tags` | yes | lowercase kebab-case |
| `last_updated` | yes | date of last edit |
| `sources` | yes | primary or reputable secondary URLs used for volatile facts |

## Required Sections

Every section heading below is mandatory. If knowledge is missing, write `Unknown` — never guess.

### Overview
Three to five sentences: what the product is, who it is for, and the one-sentence mechanism of its success.

### History
A dated timeline. Every event with a year or month. Volatile business facts get an "as of" date.

### Target User
Who uses it, who pays, and how they differ. Include tiers if known (individual / team / enterprise).

### Business
Business model, pricing, revenue trajectory (with sources), unit economics if known, and distribution channels.

### Growth
The growth loops and acquisition channels. Name the actual loop: viral, paid, product-led, marketplace, network effect, etc.

### UX
Key UX decisions: entry experience, core loop, information architecture, friction points, retention mechanics.

### AI
How AI is used in the product: models, agentic capabilities, latency/product decisions, data flywheels, evals.

### Architecture
Product-level architecture: what the system must contain (indexes, context, sandboxes, queues). Not implementation detail.

### Patterns
Links to `patterns/*.md` that this product instantiates, plus emerging patterns observed here that deserve their own file. Link format: `[Recommendation](../patterns/Recommendation.md)`.

### Lessons
The transferable lessons — what another product team should copy, and what to avoid.

### Innovation
What this product invented or industrialized, and where its patterns could transfer next (link to `cross-domain/`).

### Sources
Numbered list of URLs used. Required whenever numbers or dates appear.

## Optional Sections

Competition, Risks, Quotes, Related Products.

## Example

[products/AI/Cursor.md](../products/AI/Cursor.md)

