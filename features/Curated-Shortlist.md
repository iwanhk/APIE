---
id: curated-shortlist
type: feature
name: Curated Weekly Shortlist
tags: [curation, suitability, discovery, finance, personalization]
last_updated: 2026-08-07
---

# Curated Weekly Shortlist

## Definition

A weekly delivery of 3–5 funds, all inside the user's suitability band, each with a "为什么适合你" card (one sentence, the reason, the risk, the source). The job: turn an open fund universe into a bounded weekly decision.

## Core Loop

1. System reads LP profile + suitability band
2. Curation engine (research team approves; AI assists) picks 3–5 in-band funds
3. Each card explains the fit in plain language with evidence
4. User keeps or skips; skip reasons and reading behavior feed back
5. Next week's list adapts

## UX Flow

See [Weekly Shortlist](../ux-flows/Weekly-Shortlist.md). Key decisions: 3–5 items max (scarcity is the feature), every card answers "why you" and "why not you", one-tap to the [Fund Passport](Fund-Passport.md).

## AI Integration

- [Suitability Matching](../patterns/Suitability-Matching.md) is the hard gate — nothing outside the band is ever listed
- AI generates the explainable "why for you" reasons; ranking is light because the pool is curated (see [Curation](../patterns/Curation.md))
- Feedback loop (keep/skip/read) refines the profile, not the curation criteria — criteria are human-owned

## Metrics

Adoption rate (funds invested from the shortlist), weekly completion rate, skip-reason distribution, band-violation rate (must be 0), list diversity over time.

## Examples

- Mechanism: Spotify's Discover Weekly (personalized weekly delivery) + private banking fund pools (named gatekeepers) + Netflix's "Because you watched" explainability
- Anti-example: open fund marketplaces with thousands of listings — the choice paralysis this product exists to kill

## Pitfalls

- Filling the list to hit a quota (3 bad funds beat 1 great one)
- Drift outside the suitability band under user pressure — the gate is not a soft score
- Feedback overfitting: skip behavior can be noise, not signal

