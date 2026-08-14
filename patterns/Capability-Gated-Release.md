---
id: capability-gated-release
type: pattern
name: Capability-Gated Release
status: emerging
tags: [ai, safety, access-control, dual-use, enterprise, tiering]
last_updated: 2026-08-14
---

# Capability-Gated Release

## Definition

A vendor ships **one underlying capability in two access tiers**: a public tier wraps the capability in guardrails that detect high-risk requests and route them to a safer fallback, while a trusted tier with lifted guardrails is available only to vetted partners, governments, or researchers. The same architecture, different gates — release breadth and capability depth are controlled independently.

## Purpose

Capture the commercial value of a dual-use frontier capability without bearing the full misuse and regulatory risk of a wide open release — and convert safety governance into a positioning asset ("we are the gatekeepers, not the accelerant") that wins enterprise and government procurement.

## Problem

Frontier AI capabilities (vulnerability discovery, bio/chem design, model distillation) are dual-use: the same reasoning that helps defenders can help attackers. Full public release risks misuse and regulator backlash; full restriction forfeits value, revenue, and mindshare. Single-tier release forces a binary choice that loses on one side.

## When To Use

- The capability is dual-use with a measurable risk gradient (cyber, biology, chemistry, surveillance)
- Regulators or governments are watching the launch (the tiered release becomes the negotiable artifact)
- Request classification is accurate enough to route risky requests without wrecking UX (fallback share should be small)
- A credible vetting program exists or can be built (trusted partners, red-teamers, researchers)

## When NOT To Use

- When the risk gradient is small or the classification layer fails often — a leaky gate is worse than no gate
- When competitors ship unrestricted and the gate is your only differentiator without buyer demand
- When the trusted tier is not actually secure (unauthorized access destroys the trust brand faster than a plain release)
- When gating is purely performative — a public relations tier with no operational difference

## Examples

- **Anthropic — Fable 5 / Mythos 5 (Jun 9, 2026):** same Mythos-class architecture priced identically ($10/$50 per MTok). Fable 5 is public; request classifiers route cybersecurity, biology/chemistry, and model-distillation requests to Claude Opus 4.8 (users notified), and >95% of sessions reportedly run on Fable 5 without fallback. Mythos 5 lifts those guardrails and is restricted to Project Glasswing cyber partners (announced Apr 2025) and select biology researchers. The launch followed the earlier Mythos Preview, also Glasswing-only.
- **OpenAI — Trusted Access previews (2026):** GPT-5.4-Cyber shipped under a Trusted Access programme for vetted security teams; GPT-5.6 launched (Jun 2026) as a limited preview for a small group of government-approved trusted partners before wider rollout, per a US government request — access approved customer by customer.
- **Google — Gemini 3.5 Flash Cyber (Jul 22, 2026):** a specialized vulnerability-hunting model "exclusively available to governments and trusted partners" through a limited-access CodeMender pilot, no public API or pricing — the dual-use rationale stated explicitly.

## Engineering

- **Request classifier:** domain detection (cyber, bio/chem, distillation) with low false-positive targets; the fallback path must be visible to the user
- **Fallback routing:** risky requests route to a capable-but-safer model (Anthropic: Fable 5 → Opus 4.8); the route itself must be auditable
- **Vetting & access control:** trusted-tier enrollment (partners, government agencies, researchers), per-customer approval, usage monitoring
- **Red-teaming:** pre-release adversarial testing with a defined bar (Anthropic claimed 1,000+ hours and "no universal jailbreaks" pre-Fable 5)
- **Metrics:** fallback rate, unauthorized-access incidents, trusted-tier misuse, regulator engagement, enterprise win rate attributable to the gate

## UX

- Be transparent when a request is routed to the fallback ("this request was handled by Opus 4.8 for safety") — hidden routing destroys trust
- Make the tier visible to buyers (public vs trusted) so the gate itself is a product feature, not a rumor
- Avoid over-gating everyday work: the public tier should feel indistinguishable for 90%+ of sessions

## Business

- The gate is a pricing and positioning instrument: trusted tiers can command premium contracts with governments/institutions; the public tier gets the developer ecosystem
- Gatekeeper status becomes procurement leverage (enterprise security reviews, public-sector deals) and a brand moat — until a leak inverts it
- The pattern converts regulation from a threat into a co-design process (governments approve the trusted list; vendors set the terms)

## Cross-Domain Candidates

- [Capability-Gated Release → Financial Products](../cross-domain/Capability-Gated-Release-to-Financial-Products.md) — same architecture, same limits: strategy/fund tiers by investor qualification and access controls
- Pharmaceutical access (tiered clinical programs), defense tech, and industrial control systems are natural analogs
