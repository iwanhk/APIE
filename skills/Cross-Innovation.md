---
id: cross-innovation
type: skill
name: Cross-Innovation
skill_type: combination
tags: [ideation, cross-domain, combination]
inputs: [product-a, product-b]
outputs: [examples/Innovation-Challenge-<A>-x-<B>.md]
last_updated: 2026-08-07
---

# Cross-Innovation

## Purpose

Generate product concepts by combining the mechanisms of two products from different domains. This is the Brain's Compose + Evaluate stages, run daily as the Innovation Challenge.

## When To Use / When NOT To Use

Use when: two products have rich, complementary patterns and the goal is new concepts, not analysis.
Do not use when: the goal is a teardown (use Product Reverse Engineer) or when a single pattern transfer is already documented (file it in `cross-domain/` instead).

## Workflow

1. **Retrieve** — teardowns for both products (from `products/` or the datasets).
2. **Abstract** — list each product's 3 core patterns as mechanisms without domain vocabulary.
3. **Compose** — generate 20 concepts pairing mechanisms; group by theme; each idea cites its pattern combination.
4. **Evaluate** — score top 5 on User value, Feasibility, Moat, Timing, Risk (1–5) with reasons.
5. **Innovate** — write the #1 concept: target user, core loop, one metric, pattern stack, first-90-days.
6. **Write & file** — output `examples/Innovation-Challenge-<A>-x-<B>.md`; add new pattern discoveries to `patterns/` if a combination reveals one.

## Quality Checks

- Every idea names source patterns — no unprovenanced concepts
- Evaluation table complete with reasons, not just scores
- Financial assumptions are labeled as assumptions
- Any transfer worth keeping is promoted to `cross-domain/` within a week

## Provenance

Every idea records its pattern combination in brackets; the evaluation table records why each concept passed or died; the winner's pattern stack links back to pattern files.

## Example Output

[examples/Innovation-Challenge-Spotify-x-Robinhood.md](../examples/Innovation-Challenge-Spotify-x-Robinhood.md)

