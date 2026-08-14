---
id: capability-gated-release-to-financial-products
type: cross-domain
name: Capability-Gated Release → Financial Products
source_domain: AI Software (Frontier Models)
target_domain: Financial Products (Funds & Advisory)
source_pattern: patterns/Capability-Gated-Release.md
status: hypothesis
last_updated: 2026-08-14
---

# Capability-Gated Release → Financial Products

## Source

Anthropic industrialized capability-gated release with Fable 5 / Mythos 5 (Jun 9, 2026): one Mythos-class architecture, two access tiers — a public version whose classifiers route high-risk requests (cyber, bio/chem, distillation) to a safer fallback model, and a trusted version with lifted guardrails restricted to vetted partners (Project Glasswing) and select researchers. OpenAI (GPT-5.6 limited preview to government-approved partners, Jun 2026) and Google (Gemini 3.5 Flash Cyber, governments/trusted partners only, Jul 2026) run the same play. The pattern: **same capability, differentiated gates — release breadth and capability depth controlled independently.**

## Pattern

Abstracted: in any domain where a capability has high value but differentiated risk per user class, **ship one underlying engine and split access by guardrail + vetting rather than by feature parity.** The public tier routes the riskiest operations to a safer fallback (with user-visible notification); the trusted tier lifts the guardrails for vetted counterparties; the gate itself becomes the product story.

## Transfer

- **Transfers:** one strategy/research engine with tiered execution rights (read-only analysis vs deployable allocations vs leverage); classifier routing for high-risk operations (concentrated bets, margin, illiquid instruments) to a conservative fallback (index/liquidity-constrained sleeve); qualified-investor vetting as the "Glasswing" enrollment; user-visible fallback notifications; regulator co-design of the trusted list.
- **Adapts:** the risk classifier is not a model but a rule engine (position size, instrument class, leverage, counterparty) that routes orders to the safe execution path; the fallback is not a weaker model but a more constrained portfolio policy; vetting maps to existing suitability/eligibility regimes (accredited investor, IPS, MiFID II appropriateness).
- **Fails:** when the "gate" is purely regulatory theater with no operational difference; when routing errors silently execute the wrong tier (a leverage order slipping into the safe sleeve or vice versa); when the trusted tier leaks (unauthorized high-capability access destroys client and regulator confidence).

## Example

A digital wealth platform runs one portfolio-construction engine across two tiers: everyday clients get the "Fable" tier — their requests for concentrated crypto, leverage, or exotic instruments are classified and rerouted to a diversified, liquidity-constrained default with an explicit notice ("this allocation was handled by our conservative engine"); qualified investors (vetted + audited) get the "Mythos" tier with full strategy capability and their own risk budget. Same codebase, same models, differentiated gates — the gate becomes the compliance story ("we are the gatekeepers of high-risk products"), turning suitability regulation from cost into positioning.

## Future

Next step: **cross-product capability passports** — a client's verified qualification (accredited status, IPS limits, loss-absorption capacity) is a portable credential that gates capability tiers across products, the way Glasswing membership gates Mythos access. Early adopters: private-banking platforms that currently run separate suitability checks per product and would buy one gating layer.

## Risks

- A leaky gate (unauthorized access to the high-capability tier) is a brand and regulatory catastrophe — vetting and monitoring must be real
- Over-gating everyday users ("95% of sessions should never touch the fallback") is the cost target; friction kills adoption
- Regulators may reject vendor-defined trusted lists — the gate must be co-designed, not unilateral
