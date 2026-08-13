---
id: parallel-agent-orchestration-to-investment-research
type: cross-domain
name: Parallel Agent Orchestration → Investment Research
source_domain: AI Software (Agentic Coding)
target_domain: Investment Research & Due Diligence
source_pattern: patterns/Parallel-Agent-Orchestration.md
status: hypothesis
last_updated: 2026-08-13
---

# Parallel Agent Orchestration → Investment Research

## Source

Replit Agent 4 splits one user prompt into parallel specialized subagents (frontend, backend, database, auth) that work on isolated forks and are merged into a single coherent project with agent-assisted conflict resolution (~90% auto-resolve claim; up to 10x throughput claims). Cursor does the same with worktree-isolated parallel agents; Factory organizes manager + worker droids. The mechanism: **decompose → parallelize with isolation → merge with a human reviewable result.**

## Pattern

Abstracted: in any domain where a deliverable is composed of separable expert workstreams, run **parallel specialist agents per workstream, isolate their state, and merge into one coherent artifact the human reviews at the end** — collapsing wall-clock time (days → hours) while keeping a single human review surface instead of per-workstream babysitting.

## Transfer

- **Transfers:** per-domain agents with isolated state (filings agent, market-data agent, news/on-chain agent, valuation agent); a merge layer that composes sections and flags conflicts; checkpoint-level rollback per workstream; approval at the integrated result, not per worker.
- **Adapts:** the merge conflict is a **fact conflict**, not a code conflict — two agents citing different revenue numbers for the same company must be resolved by a citation-grounded arbitration step, not a diff tool; the "project state" is the evidence corpus (sources, as-of dates, data snapshots) that all workstreams share.
- **Fails:** when workstreams are not separable (a single judgment call that depends on all inputs simultaneously); when the merge layer composes sections without reconciling the numbers — a memo that says "EBITDA $12.4M" in one section and "$14.1M" in another is worse than a serial analyst's output.

## Example

An investment-research agent team for an IC memo: one subagent gathers filings and financial statements, one pulls market/benchmark data, one monitors news and on-chain signals, one runs valuation scenarios — all isolated, all writing into a shared evidence corpus with citation-grounded facts. A merge layer composes the memo, runs cross-section number reconciliation (every figure must match its cited source and appear consistently across sections), and surfaces conflicts for the human reviewer. Wall-clock: a multi-day diligence memo compresses to a few hours with the human reviewing intent and evidence at the end — the same "orchestrate a team without knowing you're orchestrating" UX Replit gives a non-developer, applied to an analyst.

## Future

Natural next step: **spec-driven research** — the memo is written as a spec (claims required, evidence required, acceptance criteria), parallel agents satisfy it, and each checkpoint is a verified, cited section; the merge gate is the IC review. Regulated asset managers and due-diligence teams are the first buyers; the merge-layer conflict rate ("how many fact conflicts surfaced per memo") becomes a research-quality KPI.

## Risks

- Parallel agents amplify hallucination: four agents can fabricate four consistent-looking but wrong sections; the citation/evidence gate is the counterweight
- Fact conflicts at merge are the hard part — the merge layer must arbitrate sources, not average them
- Compute cost: parallel research multiplies token spend; effort-based metering per completed section keeps it bounded
- Over-parallelization on small memos adds latency and cost with no quality gain — apply at workstream boundaries, not inside them
