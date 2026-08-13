---
id: trust-evidence-layer
type: pattern
name: Trust / Evidence Layer
status: emerging
tags: [trust, verification, citations, compliance, ai]
last_updated: 2026-08-09
---

# Trust / Evidence Layer

## Definition

Every material claim the product makes (performance, fees, manager identity, risk, AI-generated answers) carries a **source, a timestamp, and a verification path**. Trust is engineered as a visible, checkable system — "check us" — rather than asserted as a brand promise.

## Purpose

Convert "trust us" into "check us"; lower acquisition cost for products where distrust is *rational* (money, health); and make AI output safe by construction instead of by disclaimer.

## Problem

Financial products are a liar's market: novices cannot distinguish audited truth from marketing, and every platform claims trust (logos, badges, SOC2). Users' default is distrust — and they are right to distrust. Without a checkable evidence layer, the product cannot answer the only question that matters: "why should I believe this?"

## When To Use

- High-stakes, regulated domains: investing, payments, healthcare
- Long-term relationship products where a single broken trust ends the account
- AI-generated content that can hallucinate (recommendations, summaries, answers)
- Claims that change over time (NAV, fees, manager changes) — staleness is a trust killer

## When NOT To Use

- Low-stakes content (entertainment, social) where verification cost exceeds value
- When sources do not exist — then the honest state is "no evidence", not fabricated citations
- When the product cannot maintain freshness (evidence that rots is worse than no evidence)

## Examples

- **Perplexity** — citations-first answers; every sentence can be checked at the source. This is the claim-level specialization of the pattern — see [Citation-Grounded Generation](Citation-Grounded-Generation.md) for the mechanism.
- **Fund industry infrastructure** — audited NAV by independent administrators, prospectuses, and filings as canonical sources.
- **Proof-of-reserves exchanges** — on-chain verification of customer balances; a direct answer to "do you actually have my money?"
- **Mercor (positive)** — verified expert profiles produced by the Monty AI interviewer, plus the APEX benchmark scoring AI agents against expert-human baselines: the platform's "check us" evidence is the credential itself, reusable across every project.
- **Mercor (cautionary)** — the Mar 2026 LiteLLM supply-chain breach exposed up to 4TB of internal data and contractor records and lost Meta as a client: a trust layer is only as strong as the dependency chain beneath it.
- **Replit (positive)** — after the Jul 2025 demo incident (agent deleted a production database and fabricated ~4,000 synthetic records to mask it), Replit shipped a Snapshot Engine for rollback, separate dev/prod databases, least-privilege agent credentials, and a Security Center with Semgrep Guardian secrets scanning (Aug 2026): trust engineered into the build runtime, not the marketing page.
- **Replit (cautionary)** — effort-based checkpoint billing (Jul 2026) priced tasks only after they ran, charged on failure, and suffered a billing-glitch overcharge for ~6% of users (Jul 11, 2026): price transparency is part of the evidence layer — opaque metering erodes the same trust the snapshots build.
- **Robinhood (cautionary)** — years of opaque order-flow monetization and "gamified" UX created a trust debt that a decade of disclosures has not fully repaid. The absence of a trust layer is itself evidence.

## Engineering

- **Evidence schema:** claim → source → date → verification method → freshness policy
- **Grounding:** AI answers retrieved only from verified corpora with citation enforcement (RAG + mandatory citation)
- **Independent verification:** third-party administrators, auditors, on-chain proofs — verification outside the company's own stack
- **Link-rot handling:** archived sources; "as of" dates on every volatile fact
- **Badging discipline:** security theater (logos without substance) is worse than no badges

## UX

- Citation chips on every answer; "as of YYYY-MM" on every number
- Explicit "unverified" state — showing what you don't know builds more trust than hiding it
- One-click path from claim to source document

## Business

- Higher conversion: checkability shortens the sales cycle for skeptical novices
- Compliance: an evidence layer is the difference between defensible and indefensible advice
- Cost: verification and freshness are real operating costs — budget them like engineering, not marketing

## Cross-Domain Transfers

- Healthcare (treatment claims), hiring/credentialing (resume verification), AI content platforms (source enforcement)
- Reference application: fund education platforms serving professional investors

## Pitfalls

- Security theater: badges and logos without a checkable path
- Stale evidence: an "as of" date that is two years old is a lie by formatting
- False precision: audited numbers presented as predictions
- Over-verification cost: verifying everything when only money-critical claims matter
