# APIE Pattern Schema v1

**Status:** ratified (initial release)
**Applies to:** `patterns/<Pattern>.md`
**Frontmatter `type`:** `pattern`

## Purpose

A pattern is a **repeatable mechanism** — a solution structure that recurs across products and can be transferred across domains. The pattern library is the core of APIE. Everything else (products, features, flows) points at patterns.

## Required Frontmatter

```yaml
---
id: recommendation
type: pattern
name: Recommendation Engine
status: established | emerging | hypothesis
tags: [personalization, ranking, discovery]
last_updated: 2026-08-07
---
```

`status` meanings:

- `established` — observed across many products with strong evidence
- `emerging` — observed in a few AI-native products, mechanism still forming
- `hypothesis` — proposed transfer or synthesis, not yet widely observed

## Required Sections

### Definition
One paragraph: the mechanism, precisely. What repeats across instances?

### Purpose
What strategic job the pattern does for a product.

### Problem
The underlying user or market problem the pattern exists to solve.

### When To Use
Concrete preconditions: catalog size, data availability, user behavior, business model.

### When NOT To Use
Equally concrete conditions where the pattern is wrong or harmful.

### Examples
At least two product instances, each with the *mechanism* used, not just the product name. Include Apple, Netflix, TikTok, Spotify, Amazon where relevant — but any well-evidenced instance works.

### Engineering
How to build it: algorithms/approaches, data signals, cold-start strategies, metrics (offline and online).

### UX
How the pattern surfaces to users: explainability, controls, serendipity vs relevance, refresh cadence.

### Business
How the pattern creates business value: retention, engagement, conversion, monetization.

### Cross-Domain Transfers
Links to `cross-domain/*.md` files that source this pattern. If none exist, name two candidate domains and file a cross-domain entry.

### Pitfalls
Known failure modes: filter bubbles, cold start, opacity, gaming, regulatory risk.

## Example

[patterns/Recommendation.md](../patterns/Recommendation.md)

