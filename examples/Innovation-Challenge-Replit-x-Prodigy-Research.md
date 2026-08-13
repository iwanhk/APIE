# Innovation Challenge — Replit × Prodigy Research

**Daily Challenge #004** · 2026-08-13

Patterns abstracted:

- **Replit:** prompt-to-production (a deployed working app, not code), parallel agent orchestration (Agent 4 subagents with auto-merge), effort-based pricing (checkpoint billing tied to compute), spec-driven development (Plan mode + editable markdown plan), trust evidence layer (Snapshot Engine, dev/prod separation, Security Center), in-browser self-testing (agent tests its own output in a real browser), agent-builds-agents (sub-agents/automations authored in natural language), credit-allowance subscription + metered overage, mobile-first building and publishing.
- **Prodigy Research:** AI quant fund loop (model-driven signal → trade → claimed return), headline-return marketing (the "108% in two months" claim is the distribution hook — as-of 2026-08-12, YC S26, unverified), black-box strategy opacity (no public evidence chain for claimed performance), fund-as-product (strategy sold as a fund vehicle).

## 20 Innovations

### Build & Automate

1. **Thesis-as-Spec** — an investment thesis is written as a spec (claims, required evidence, acceptance criteria); agents must satisfy every criterion before capital deploys, and the spec is versioned like code. [Spec-driven-development × Investment-research]
2. **Prompt-to-Strategy Fund** — a non-developer types a thesis, and a Replit-style agent builds the full fund: data pipeline, backtest harness, execution, monitoring dashboard, and LP-facing report site — deployed, not scaffolded. [Prompt-to-production × AI-quant-fund]
3. **Agent-Built Factor Hunters** — agents author sub-agents, each hunting one factor class (momentum, low-vol, cross-asset); surviving sub-agents get promoted into the live research team. [Agent-builds-agents × Factor-research]
4. **Design Canvas for Allocations** — an infinite canvas where a user generates portfolio-allocation variants side by side and tunes risk/return sliders visually before committing. [Design-canvas × Portfolio-construction]
5. **Self-Testing Strategies** — the agent backtests its own strategy in a real simulated environment (fills, slippage, fees), clicks through the dashboard, and fixes what breaks before it ever touches live money. [In-browser-self-testing × Quant-pipeline]

### Trust & Evidence

6. **Return-Claim Evidence Portal** — every claimed return links to a verified checkpoint: date, capital, P&L, fees, and the model version that produced it — "check us" instead of "trust us". [Trust-evidence-layer × Performance-claims]
7. **Snapshot Engine for Trades** — every strategy deployment and trade is snapshot-able and rollback-able; a bad week restores the last verified state, and the snapshot is the audit trail. [Trust-evidence-layer × Trading-loop]
8. **Plan-Mode Trading Agents** — agents must write a plan and wait for human approval before any destructive move (deploying capital, changing leverage, halting a strategy). [Spec-driven-development × Trading-governance]
9. **Audit-Ready Deploy Logs** — every deployed strategy ships with a Semgrep-style scan: data dependencies, counterparty configs, secrets, and model versions scanned before go-live. [Trust-evidence-layer × Deployment]
10. **Billing-Glitch Insurance** — metered research/trading bills include automatic refunds for failed or errored checkpoints and a published pricing estimator — Replit's Jul 2026 lesson applied to fund ops. [Effort-based-pricing × Trust-evidence]

### Money & Ops

11. **Checkpoint-Billed Research** — research and diligence bill per completed, verified section (a filings memo = one checkpoint) instead of per hour or per seat; clients hold credit allowances with caps. [Effort-based-pricing × Research-ops]
12. **Parallel Analyst Swarm** — one memo request spawns parallel specialist agents (filings, market data, news, valuation) that merge into a single coherent IC memo with conflict flags. [Parallel-agent-orchestration × Investment-research]
13. **Spend-Capped Strategy Credits** — every strategy/research task draws from a visible credit budget with a hard cap — an agent loop cannot run up a surprise bill. [Effort-based-pricing × Budget-control]
14. **Auto-Merge Risk Reports** — parallel risk agents (market, liquidity, counterparty) merge into one report; the merge layer reconciles conflicting numbers and surfaces the disagreement, not an average. [Parallel-agent-orchestration × Risk-reporting]
15. **Metered Fund Infrastructure** — the fund's internal tooling bills each business unit per completed work unit (onboarding, reporting, NAV checks), so infrastructure cost is attributed to usage, not headcount. [Effort-based-pricing × Fund-ops]

### Distribution & UX

16. **Hedge-Fund-in-a-Phone** — a mobile app where a creator launches a micro-strategy and shares a live performance link — the deployed artifact is the marketing. [Mobile-first × Prompt-to-production]
17. **Live-Monitoring Strategy Agents** — mobile-first alerts where strategy agents watch positions and surface "checkpoint" events (rebalance, drawdown, data stall) instead of raw numbers. [Mobile-first × Fund-monitoring]
18. **Single-Surface Strategy Studio** — one browser surface to build, test, and analyze strategy dashboards — the code, data, and chart live in the same project context. [Prompt-to-production × Data-visualization]
19. **Agentic Onboarding Flows** — agents build KYC/onboarding flows on demand for new fund structures, with parallel verification agents checking identity evidence against sources. [Prompt-to-production × Verification]
20. **Performance-Link Network** — verified strategy links become shareable artifacts; anyone landing on one can fork the thesis, not the trades — an open-source culture applied to fund ideas. [Prompt-to-production × Evidence-portal]

## Evaluation — Top 5

| # | Concept | User value | Feasibility | Moat | Timing | Risk | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Thesis-as-Spec | 5 | 4 | 5 | 5 | 3 | 22 |
| 6 | Return-Claim Evidence Portal | 5 | 4 | 5 | 5 | 2 | 21 |
| 8 | Plan-Mode Trading Agents | 4 | 4 | 4 | 5 | 2 | 19 |
| 7 | Snapshot Engine for Trades | 4 | 4 | 4 | 4 | 3 | 19 |
| 11 | Checkpoint-Billed Research | 4 | 4 | 4 | 4 | 3 | 19 |

## Winner — Thesis-as-Spec

- **Target user:** fund operators, due-diligence teams, and allocators who must decide "is this strategy worth believing" — the exact trust gap Prodigy Research's headline claim (108% in two months, as-of 2026-08-12, unverified) exposes.
- **Core loop:** thesis written as a spec (claims, evidence requirements, acceptance criteria) → parallel research agents gather evidence against the spec → citation-grounded verification gate flags unsupported claims → spec compliance score gates capital deployment → the versioned spec becomes the fund's audit trail → every performance claim links back to the spec's evidence layer.
- **The one metric:** spec-compliance score at deployment — share of required evidence criteria satisfied with citable, as-of-dated sources before any capital moves.
- **Pattern stack:** [Spec-Driven Development](../patterns/Spec-Driven-Development.md) (the thesis-spec is the contract agents implement against) + [Trust Evidence Layer](../patterns/Trust-Evidence-Layer.md) (claim → source → date → verification) + [Parallel Agent Orchestration](../patterns/Parallel-Agent-Orchestration.md) (filings/market/news agents merge into one evidence corpus) + [Effort-Based Pricing](../patterns/Effort-Based-Pricing.md) (research billed per verified checkpoint).
- **First 90 days:** thesis-spec template for 3 strategy archetypes (equities, crypto, macro) → parallel evidence agents per archetype → citation gate with as-of enforcement → pilot with 5 allocators reviewing a live fund's spec → publish spec-compliance score as the public trust metric.
- **Key risk (mitigation):** spec theater — verbose theses with no executable acceptance criteria. Counter: the verification gate is automated (each acceptance criterion maps to a checkable evidence set), and the compliance score is public, so the spec cannot be performative; unsupported claims are surfaced, not asserted.
