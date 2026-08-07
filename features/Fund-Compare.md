---
id: fund-compare
type: feature
name: Fund Compare
tags: [finance, comparison, plain-language, transparency]
last_updated: 2026-08-07
---

# Fund Compare

## Definition

Side-by-side, plain-language comparison of a small number of funds (typically 2–3), normalized into identical fields: 是什么、谁在管、费率、锁定期/流动性、风险、业绩（带来源）。The job: make trade-offs visible without ever declaring a winner.

## Core Loop

1. User opens compare view with 2–3 funds
2. Sees aligned rows with identical fields (no jargon cells)
3. Asks AI "这两只的差别到底是什么" — answer states differences, not preferences
4. User leaves with a clear mental model of the trade-offs

## UX Flow

Used inside [Fund Deep-Dive](../ux-flows/Fund-Deep-Dive.md). Key decisions: same-field alignment (fee structures normalized with footnotes), risk rows visually prominent, one-click jump to each fund's [Fund Passport](Fund-Passport.md).

## AI Integration

- AI generates normalized plain-language summaries from verified fund documents (RAG + citations)
- **Hard rule: compare, never rank.** "基金 A 锁定期更长" is allowed; "基金 A 更好" is not — in a free education product, ranking is advice
- Footnote every normalization ("业绩口径不同，见原文")

## Metrics

Compare completion rate, time-to-understanding, follow-up questions per compare, "could not compare" rate (fields with no source — must be visible, not hidden).

## Examples

- Mechanism: car configurator comparisons and broker fee tables — alignment turns differences into a decision input
- Contrast: fund platform comparison pages that bury fees or rank by "score" (ranking creep is the anti-pattern)

## Pitfalls

- False normalization: different fee/performance definitions forced into one column
- Ranking creep: a "best for you" sort converts education into advice
- Empty cells: missing data shown as "—" invites assumption; must show "无数据（来源缺失）"

