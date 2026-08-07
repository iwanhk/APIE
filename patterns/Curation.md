---
id: curation
type: pattern
name: Curation
status: established
tags: [trust, selection, discovery, premium]
last_updated: 2026-08-07
---

# Curation

## Definition

A trusted party selects a small, bounded set from a much larger space — and **takes responsibility for the selection**. The selection itself is the product: the curator's judgment, process, and accountability are what users pay for.

## Purpose

Convert choice overload into a decision; transfer trust from the product to a named curator; enable premium positioning. Where personalization optimizes *for the user's revealed behavior*, curation optimizes *for the user's stated trust*.

## Problem

When the option space is large but the user is not competent or motivated to evaluate it (money, health, wine, code libraries), an open catalog produces paralysis, not discovery. Pure algorithmic ranking fails because the user cannot judge whether the ranking is good — they need someone to *vouch*.

## When To Use

- Small-to-medium option space (tens to low hundreds) where each item needs judgment to evaluate
- High-stakes or trust-sensitive decisions: investing, healthcare, hiring
- Users are novices or time-poor; brand or human trust is available
- Selection quality can be maintained (monitoring, refresh, review)

## When NOT To Use

- Massive catalogs where implicit-signal personalization dominates (TikTok-style feeds) — curation cannot scale linearly
- Expert users who want tools and data, not opinions (they will resent the gate)
- When the curator cannot be held accountable or selection quality decays
- When curation revenue depends on the selectees (pay-to-play) — the pattern collapses into corruption

## Examples

- **Private banking / fund-of-funds gatekeeping** — a named investment committee picks a fund pool and owns the choice; LPs buy the committee's judgment, not the catalog.
- **Apple App Store editorial** — "Today" hand-picked stories coexist with algorithmic search; curation builds the store's taste and trust.
- **Netflix editorial rows** — human-curated rows ("Trending Now") sit inside a recommendation machine; curation adds taste, algorithm adds scale.
- **Spotify editorial playlists** — named human playlists remain trust anchors beside Discover Weekly.

## Engineering

- **Curation pipeline:** screen (inclusion criteria) → verify (evidence, references) → monitor (ongoing) → refresh (retire stale items)
- **Documentation per item:** every curated item carries a rationale and evidence file (see [Trust-Evidence-Layer](Trust-Evidence-Layer.md))
- **Scale limit:** curation does not scale linearly; hybrid = algorithm-assisted curation with human-in-the-loop review
- **Accountability layer:** who curates, by what process, when was it last reviewed — machine-readable

## UX

- Show the curator's face and name — anonymous curation has no trust value
- Show the criteria and the rejected set ("why not the other 500 funds")
- Fixed cadence (weekly letter) beats infinite browsing — cadence is part of the product

## Business

- Premium pricing: bounded choice is worth more than infinite choice to novices
- Trust compounds as a moat: history of good picks is hard to copy
- **Conflict rule:** revenue must come from the user (subscription) or be fully disclosed; commission from selectees poisons the mechanism

## Cross-Domain Transfers

- [Netflix → Investment](../cross-domain/Netflix-Recommendation-to-Investment.md) — curation is the small-catalog correction to recommendation
- Candidates: healthcare (care-pathway curation), hiring (candidate shortlists), code dependencies (vetted library picks)

## Pitfalls

- Gatekeeper bias: the curator's blind spot becomes the user's ceiling
- Pay-to-play corruption — the #1 failure mode in finance
- Liability: a curated pick that fails is the curator's failure, not the market's
- Stagnation: curated sets rot without refresh; selection quality decays silently

