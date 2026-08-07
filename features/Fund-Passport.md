---
id: fund-passport
type: feature
name: Fund Passport
tags: [finance, trust, plain-language, evidence, funds]
last_updated: 2026-08-07
---

# Fund Passport

## Definition

One-page, plain-language dossier for a fund: what it does, who manages it, fees, risks, track record, and evidence — every number with a source and an "as of" date. The job: turn a 200-page offering document into a decision a novice can actually make.

## Core Loop

1. User opens a fund (from a shortlist, search, or alert)
2. Sees a 5-section passport: 一句话是什么 → 谁在管 → 收费 → 风险 → 业绩（带来源）
3. Asks AI questions; answers are grounded only in verified fund documents and cite passport sections
4. User understands enough to keep, skip, or act

## UX Flow

Part of [Weekly Shortlist Review](../ux-flows/Weekly-Shortlist.md). Key decisions: plain-language first (one sentence before any detail), risk warnings visible not buried, one-click path from every number to its source document, explicit "unverified" state when evidence is missing.

## AI Integration

- RAG over the verified fund corpus; citation enforcement on every answer (see [Trust / Evidence Layer](../patterns/Trust-Evidence-Layer.md))
- "白话" generation must not distort: simplification is allowed, false precision is not
- Freshness monitoring: NAV, fees, and manager changes invalidate stale passports

## Metrics

Passport completion rate (all 5 sections opened), "看懂了" rate (passport → action), questions-per-passport (engagement depth), time-to-understanding, stale-passport rate (must be ~0).

## Examples

- Mechanism: Perplexity's citations-first answers applied to fund documents
- Contrast: traditional fund fact sheets (accurate but unreadable) and Robinhood's thin education layer (readable but shallow)
- For the curator: the passport is the evidence artifact of [Curation](../patterns/Curation.md) — curation without documentation is opinion

## Pitfalls

- Stale data (a passport is a promise; staleness is a lie)
- Oversimplification that misleads (plain language ≠ wrong language)
- Fabricated citations when sources are missing — the "unverified" state must be the honest default

