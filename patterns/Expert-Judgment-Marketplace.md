---
id: expert-judgment-marketplace
type: pattern
name: Expert Judgment Marketplace
status: emerging
tags: [marketplace, ai-training-data, rlhf, evaluation, expert-network, human-in-the-loop]
last_updated: 2026-08-09
---

# Expert Judgment Marketplace

## Definition

A two-sided platform that sources, vets, and manages domain experts whose work product is **human judgment** — evaluation, reasoning, grading, preference signals — sold to AI labs and enterprises to train, fine-tune, and benchmark models. The unit of commerce is the expert-hour; the differentiator is vetting quality and match precision, not the annotation task itself. The essence: **human intelligence is made elastic and purchasable, like compute.**

## Purpose

Industrialize the supply of human judgment that frontier models increasingly depend on for post-training (RLHF/DPO), evaluation, and agent benchmarking; let AI labs scale expert work up and down on demand without building recruiting, vetting, and payroll infrastructure.

## Problem

Public text is being exhausted as a training signal, and specialized model behavior requires judgment that generic crowdworkers cannot supply — a doctor grading medical reasoning, a lawyer assessing legal analysis. Labs need thousands of credentialed experts fast, and no traditional staffing firm can source, vet, and pay them at that velocity.

## When To Use

- The buyer is a model lab (or model-heavy enterprise) with bursty, elastic demand for expert hours
- Task quality depends on genuine domain expertise or taste, not just volume
- A benchmark economy exists or is forming: agents are graded against expert-human baselines (APEX-style)
- The platform can capture a meaningful take rate on a high-value, repeatable work category

## When NOT To Use

- Generic labeling at commodity prices — crowdsourcing wins on cost
- Highly sensitive work whose security requirements exceed marketplace controls (state secrets, pre-IPO data) — or when the supply chain itself is the attack surface
- When the "expertise" being sold cannot be credibly verified (the vetting cost exceeds the margin)

## Examples

- **Mercor** — vets ~5M candidates via AI interview, routes a ~30,000-contractor pool of engineers, doctors, lawyers, and bankers to frontier labs; ~$2B gross annualized run rate (Jun 2026), take rate ~30–40%; APEX benchmarks use the expert pool as the human reference standard. Mechanism: AI-proctored vetting + ML matching + managed payroll = expert judgment as elastic supply.
- **Scale AI / Outlier** — the data engine behind frontier labs' RLHF and evaluation pipelines; Scale reached a ~$29B valuation after Meta's stake purchase (2026), with Outlier as its contributor-facing generative-AI arm. Mechanism: enterprise-grade data/RLHF infrastructure + contributor marketplace.
- **Surge AI** — RLHF-specialist data provider focused on preference and evaluation data for frontier models. Mechanism: narrower category ownership (preference data) inside the same expert-labor marketplace.

## Engineering

- **Vetting pipeline:** credential checks + AI-proctored evaluation (see [AI-Proctored Vetting](AI-Proctored-Vetting.md))
- **Matching layer:** skill-cluster classification + ML routing; natural-language search over the verified pool
- **Quality loop:** completed work is scored by clients and/or automated checks; scores feed back into ranking and pay
- **Task infrastructure:** task queues, dedup, inter-rater-agreement measurement for grading work
- **Payments & compliance:** global payroll, tax/contractor classification, NDAs, and — critically — supply-chain security for contractor credentials
- **Benchmark engine (moat builder):** a task suite with expert-human reference scores (APEX pattern) turns internal data into an external standard

## UX

- **Expert side:** one-time evaluation → portable verified profile → proactive project offers; pay transparency per task
- **Lab side:** natural-language staffing ("I need 200 cardiologists for a grading sprint") with ranked, pre-vetted shortlists; one interface for contracts, invoicing, and delivery
- Cadence: recurring project work beats gig-by-gig bidding — experts return when work is steady

## Business

- **Take rate on expert-hours** is the core model (30–40% in Mercor's case; contractors keep 60–70% of billings)
- **Network effects:** larger verified supply → faster fulfillment → more lab demand → higher payouts → more expert applicants
- **Ancillary monetization:** benchmarks (APEX), evaluation-as-a-service, agent-training environments (Mercor + Deeptune) — moving from data supplier to full agent-training stack
- **Gross vs net discipline:** marketplace "run rates" are gross billings; net revenue is take-rate-adjusted

## Cross-Domain Transfers

- Candidates: financial research-as-a-service (expert analysis for fund due diligence), legal second opinions, healthcare clinical review, enterprise "human-in-the-loop" agent ops
- Natural adjacency: [Expert-Judgment-Marketplace → Fund Due Diligence] — a vetting/matching layer for specialist deal analysts, linked to [Curation](Curation.md) and [Trust-Evidence-Layer](Trust-Evidence-Layer.md)

## Pitfalls

- **Buyer concentration:** 90%+ of revenue from AI foundation-model companies is a single-category risk
- **Take-rate pressure:** experts disintermediate once the pool is established; platforms must keep adding value (payroll, security, benchmarks)
- **Security breaches:** a marketplace holding contractor PII is a supply-chain target (LiteLLM incident, Mar 2026)
- **Labor classification:** contractor models attract regulatory scrutiny as work volume and pay scale
- **Quality decay:** as volume grows, vetting standards drift unless calibrated against downstream performance
