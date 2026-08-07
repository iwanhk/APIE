---
id: suitability-matching
type: pattern
name: Suitability Matching
status: emerging
tags: [finance, compliance, risk, personalization, guardrails]
last_updated: 2026-08-07
---

# Suitability Matching

## Definition

Before any ranking, recommendation, or advice, the product **constrains the option set to what is appropriate for this user** — by risk capacity, risk tolerance, horizon, and knowledge. Suitability is a hard filter, not a soft ranking layer: nothing outside the user's band is ever shown or recommended.

## Purpose

Protect the user, comply with regulation, and — crucially — make personalization *honest*. Recommendation engines optimize engagement; in finance, engagement-optimized recommendations are dangerous. Suitability matching is the guardrail that lets personalization exist safely.

## Problem

Users misreport risk appetite (they say "moderate" and panic at -5%), and platforms optimize for what keeps users transacting. The result: products recommended because they monetize well, not because they fit. Regulatory regimes (MiFID II suitability, KYC/appropriateness) exist precisely because unfiltered recommendation in finance destroys users and trust.

## When To Use

- Regulated advice or distribution to retail users (funds, insurance, credit)
- AI agents that recommend financial products — the guardrail must be architectural, not conversational
- Novice users who cannot self-assess

## When NOT To Use

- Pure information/search products with no recommendation (a fund database is not advice)
- Sophisticated users under discretionary mandates where the IPS replaces profiling
- When suitability data is fabricated (checkbox compliance with fake questionnaires)

## Examples

- **Robo-advisors (Wealthfront, Betterment)** — risk questionnaires produce an allocation band; the product only trades within it.
- **MiFID II suitability regimes** — firms must record appropriateness before recommending; the mechanism is a documented gate.
- **Private banking IPS** — investment policy statements encode the client's band before any product discussion.
- **Robinhood (cautionary)** — historically minimal suitability gating + gamified onboarding + options access for novices produced regulatory and trust damage; the lesson is the gate must come first.

## Engineering

- **Profile from two sources:** explicit questionnaire + implicit behavior (what they hold through, how they react to drawdowns) — see [Memory](Memory.md) for the profile lifecycle
- **Risk capacity vs risk tolerance are different inputs** — capacity (money, horizon) is factual; tolerance (feelings) is behavioral
- **Hard gates, not soft scores:** the suitability band is a set-membership filter applied before ranking
- **Re-profiling cadence:** profiles rot; re-profile on material changes and periodic review
- **Audit trail:** every recommendation must be able to answer "why was this in scope for this user?" on demand

## UX

- Show the band ("your portfolio range: 30–60% growth assets") — users should see the fence
- Show what was excluded and why ("not shown: leveraged products, >18-month lockups")
- Override only with friction and disclosure — a one-click override defeats the purpose

## Business

- Regulatory compliance is a license to operate, not a tax
- Fewer bad outcomes → lower churn and fewer complaints → compounding trust
- Discipline costs some short-term conversion; it is repaid in retention (see [Trust-Evidence-Layer](Trust-Evidence-Layer.md))

## Cross-Domain Transfers

- Healthcare (contraindications before prescribing), credit underwriting, hiring
- Reference application: constrained-advice fund education platforms serving professional investors

## Pitfalls

- Checkbox compliance: a questionnaire with no enforcement is a lie that regulators will find
- Stale profiles: a two-year-old risk score is not suitability
- Gaming the questionnaire: users who lie to get access need implicit-behavior correction
- Over-conservatism: excluding users from legitimate opportunity is also a failure mode
