---
id: effort-based-pricing
type: pattern
name: Effort-Based Pricing
status: emerging
tags: [pricing, consumption, agents, monetization, unit-economics]
last_updated: 2026-08-13
---

# Effort-Based Pricing

## Definition

AI products meter the price of an agentic outcome by the **actual compute and time the task consumed**, instead of a flat per-seat or per-message fee: a small edit costs less than a complex multi-file build, the unit of billing is the completed "checkpoint" of work, and the final price is only knowable after the task runs. The meter replaces the seat.

## Purpose

Tie revenue to the dominant cost line (inference/compute) so heavy users cannot arbitrage a flat subscription against model cost, and so usage intensity — not signups — becomes the growth engine. It converts an agent from a fixed-cost feature into a variable-revenue product.

## Problem

Flat-rate AI subscriptions let power users arbitrage compute: a $20 seat running hundreds of long autonomous tasks costs the vendor far more than it collects. Vendors face a margin gap, and pure per-message billing punishes simple tasks. Neither model prices the thing that actually costs money: effort.

## When To Use

- Agent products whose marginal cost is meaningful (long autonomous runs, multi-file builds, browser testing)
- Products where usage intensity varies 100x between light and heavy users
- A growing compute bill that seat pricing cannot cover

## When NOT To Use

- When the cost of metering and billing complexity exceeds the compute cost (cheap, short tasks)
- Consumer products where post-hoc, opaque prices destroy trust (the "pricing casino" failure mode)
- When competitors offer predictable flat pricing and switching costs are near zero

## Examples

- **Replit** (reference instance) — Agent checkpoints billed by task complexity since Jul 1, 2026: simple edits typically <$0.25, complex builds bundled into larger single checkpoints, Assistant baseline ~$0.05 and Agent baseline ~$0.25; subscribers get a monthly credit allowance. The shift accompanied a 75% ARR jump in four months (Dec 2025 → Apr 2026, per Sacra) — and a backlash over cost opacity, failure charges, and a Jul 11, 2026 billing glitch that overcharged ~6% of users.
- **Cursor** — usage-based AI fees on top of per-seat plans (Pro ~$20/mo + metered agent/premium-model usage; Ultra ~$200/mo), flagged in its own teardown as "usage-gated monetization": metered AI requests on top of per-seat pricing.
- **Lovable** — credit packs for AI generations layered over subscription seats, so heavy app-building consumes metered credits rather than unlimited builds.
- **OpenAI/Anthropic API ecosystem** — token-metered pricing is the upstream instance of the same logic (pay for actual compute), which Replit adapted from per-token to per-checkpoint for a consumer surface.

## Engineering

- **Billing unit design:** the checkpoint must be a visible, atomic unit of completed work — it doubles as the progress/recovery artifact (Replit's checkpoints are both the meter and the rollback point)
- **Cost correlation:** per-checkpoint price should track actual time+compute; Replit's Jul 2026 glitch shows what happens when the estimator is wrong
- **Predictability controls:** spending caps, price ceilings per task, pre-task estimates, and refunds for failed checkpoints — the pattern only works if users can bound the downside
- **Tiering:** subscription buys a credit allowance; overage is metered — the subscription remains the relationship, the meter is the revenue
- **Metrics:** revenue per checkpoint, checkpoint cost vs compute cost, spend per user, churn on price surprise, credit utilization

## UX

- Show cost **before** the task where possible; if the price is only knowable after, make the estimate, the cap, and the refund policy explicit
- Never charge on failure without visible failure attribution — charged-failed-checkpoints is the pattern's #1 trust killer
- Progress-to-budget affordances (credits remaining, projected spend this week) turn the meter into a control instead of a surprise

## Business

- Revenue decouples from seat count: usage intensity becomes the growth lever (Replit: +75% ARR in four months with flat user growth)
- Unit economics improve because price tracks cost; the risk is that price uncertainty churns the base (Bolt abandoned consumer/prosumer after discovering near-zero switching costs — unpredictable bills accelerate that churn)
- The category is repriceable upward: the market repriced Replit 3x ($3B → $9B) on consumption-driven ARR growth before the revenue target was hit

## Cross-Domain Transfers

- Candidates: **professional services** (consulting/legal billing metered by effort checkpoints instead of hours — see [Effort-Based Pricing → Professional Services](../cross-domain/Effort-Based-Pricing-to-Professional-Services.md)), **data/AI factories** (internal agent teams billed per completed task to business units), **healthcare AI** (per-intervention metering aligned to actual inference + clinician review time)
- Emerging cross-domain candidate: effort-based pricing for AI-driven investment research — per-memo or per-datapoint metering where the "checkpoint" is a verified, cited work product

## Pitfalls

- **Opaque costs kill trust:** post-hoc pricing without estimates or caps reads as a casino; the Jul 2026 Replit backlash is the canonical failure
- **Charging on failure:** billing for checkpoints that hung or errored punishes users for the product's bugs
- **Estimator bugs become billing fraud:** a pricing bug is a trust crisis, not an ops ticket — Replit's Jul 11, 2026 glitch hit headlines within days
- **Flat-price competitors win cautious users:** if switching costs are low, a predictable flat plan captures the risk-averse segment
