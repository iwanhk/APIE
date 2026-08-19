---
id: benchmark-driven-routing-to-investment-research
type: cross-domain
name: Benchmark-Driven Routing → Investment Research
source_domain: AI / Voice Infrastructure
target_domain: Investment Research
source_pattern: patterns/Benchmark-Driven-Routing.md
status: hypothesis
last_updated: 2026-08-19
---

# Benchmark-Driven Routing → Investment Research

## Source

In voice AI, Speko routes production STT/LLM/TTS calls by continuously re-measured, language-and-objective-specific benchmarks (WER, finalize latency, time-to-first-token, cost per minute), publishes the boards — including cases where its own pick lost — and re-routes automatically when the numbers change ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17). OpenRouter is the text-side proof that a routing layer can be a standalone business (reported ~$7B+ Stripe acquisition, 2026). The proven mechanism: **the measurement surface is the moat, not the model choice** — whoever maintains the most credible live ranking owns the routing decision, and the public scoreboard is simultaneously the trust layer and the acquisition engine.

## Pattern

In any domain where the "best choice" churns frequently and quality differs by context, a neutral measurement layer continuously re-scores the option set per context (language → mandate, objective → risk preference), publishes the scores, and routes decisions automatically — switching when measurements change. The customer never re-runs the evaluation; the router does, and the router's credibility is the product.

## Transfer

**Transfers:**
- Language → investor mandate / asset class (a "best fund" is only meaningful per mandate, just as a "best model" is only meaningful per language)
- WER → risk-adjusted return (Sharpe/Sortino), drawdown, NAV quality
- Finalize latency → liquidity terms (redemption frequency, gates, notice periods)
- Cost per minute → fees (management fee, performance allocation, expense drag)
- Objective decomposition (accuracy/latency/cost/balanced) → mandate decomposition (growth / income / capital preservation / liquidity-constrained)
- Public boards with honest losses → published fund-score histories including past mis-ranks
- Auto re-routing when numbers change → periodic re-allocation triggered by score changes, not calendar habit

**Adapts:** a fund's score changes slowly and is measured from reported NAV with lag, so routing cadence is monthly/quarterly, not per-call; routing applies to new contributions and rebalancing, not to existing illiquid positions.

**Fails if copied literally:** per-transaction routing is wrong for locked-up capital; switching costs are material (redemption gates, tax, market impact); and fund managers have stronger incentives to game the score than model vendors, because the score directly allocates their capital.

## Example

An institutional research desk maintains a continuously re-benchmarked fund universe: verified NAV series normalized into per-mandate scores (risk-adjusted return, max drawdown, liquidity, fees, data quality flags). Each period, new contributions are routed toward the best-measured options for the mandate — an allocator seeking income gets a different ranking than one seeking capital preservation, just as a French call center gets a different model stack than a Hindi voice assistant. Past routing decisions are published with their scores (including picks that underperformed), and the desk's credibility — methodology, data provenance, stale-mark detection — is the moat that justifies routing capital through it rather than through static manager selection.

## Future

- The natural build target is a fund database where NAV series, drawdowns, and fee schedules replace "model cards," and mandate-based routing replaces static shortlists — the same data pipeline as Speko's benchmark boards, with quarterly re-measurement cadence
- Extends to credit/lending pricing (routing applicants to continuously re-scored risk segments), insurance (carrier/plan routing by live claims quality), and any allocation problem with churning options and measurable quality
- Adjacent: routing *research workflows* — spawning the best-measured analysis stack per question (existing parallel-agent and citation patterns become the routed legs)

## Risks

- **Measurement lag and gaming:** NAV smoothing, illiquid marks, and manager incentives to shape to the score make "measure then route" much harder than WER; independent verification and stale-mark detection are non-negotiable
- **Switching costs:** locked-up capital and redemption gates mean routing can strand allocations; routing must be defined at contribution/rebalancing time, not per unit
- **Trust collapse:** a fund-score board with hidden methodology is worse than none — the Speko critique (only one metric public, methodology undisclosed) applies with multiplied stakes
- **Concentration:** routing all capital to the current "winner" creates crowding and herding; capacity and health signals must enter the score
- **Fiduciary exposure:** an automated router that silently switches fund picks has accountability requirements a voice router does not; every routed decision needs a replayable, auditable rationale
