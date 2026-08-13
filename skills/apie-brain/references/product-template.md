# Product Teardown Template

Follow [APIE Product Schema v1](schemas.md). Fill every section; write `Unknown` where facts cannot be verified; every number/date needs a source and an "as of" date.

```markdown
---
id: product-id
type: product
name: Product Name
category: AI | FinTech | SaaS | Consumer | Healthcare | Education | Gaming | Enterprise | Other
company: Company Name
founded: YYYY
status: active | acquired | defunct | unknown
tags: [tag1, tag2]
last_updated: YYYY-MM-DD
sources: [https://…]
---

# Product Name

## Overview
What it is, who it is for, and the one-sentence mechanism of its success.

## History
Dated timeline; volatile facts include "as of" dates.

## Target User
Who uses it, who pays, and how they differ.

## Business
Model, pricing, revenue trajectory (sourced), distribution.

## Growth
The actual growth loop(s), named precisely.

## UX
Entry experience, core loop, information architecture, retention mechanics.

## AI
Models, agentic capabilities, latency decisions, data flywheels, evals.

## Architecture
Product-level architecture: the systems the product must contain.

## Patterns
Links to pattern files this product instantiates; emerging patterns worth filing.

## Lessons
Transferable rules — what to copy, what to avoid.

## Innovation
What it invented/industrialized and where its patterns could transfer next.

## Sources
1. [Title](https://example.com)
```
