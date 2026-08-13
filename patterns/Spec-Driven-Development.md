---
id: spec-driven-development
type: pattern
name: Spec-Driven Development
status: emerging
tags: [ai-coding, workflow, specs, verification, developer-tools]
last_updated: 2026-08-12
---

# Spec-Driven Development

## Definition

AI coding workflows are reordered so that a **written specification is the contract the agent implements against**: humans write (or approve) a spec that states behavior, scope, and acceptance criteria; agents generate code; automated checks verify the code against the spec. The spec — not the prompt, not the diff — becomes the durable artifact of the project.

## Purpose

Make AI-generated code reviewable by intent instead of by implementation: reviewers read "what should happen" rather than thousands of generated lines, and agents get a stable target that survives context loss, model swaps, and multi-session work.

## Problem

Prompt-driven coding produces code whose intent lives only in a conversation: unverifiable, unmaintainable, and unreviewable. Humans cannot review AI output line-by-line at scale, and agents drift without a stable specification. Without specs, AI-generated projects rot the moment the chat history ends.

## When To Use

- Agentic coding at any scale beyond a single throwaway script — the code will outlive the session
- Teams that must review AI contributions (spec review is cheaper than diff review)
- Multi-agent or multi-session builds where a shared contract prevents conflicts
- Regulated or enterprise code where an audit trail of intent → implementation is required

## When NOT To Use

- One-off explorations and quick prototypes where the spec overhead exceeds the build time
- Vibe-coding products whose core promise is skipping documentation (Lovable-style chat → app) — unless the spec is generated automatically behind the scenes
- Teams that cannot maintain specs — a stale spec is worse than no spec (agents implement confidently against wrong intent)

## Examples

- **GitHub SpecKit** — GitHub's toolkit for spec-driven development with AI coding assistants; provides a structured workflow for writing, versioning, and executing specs (126K+ stars as of the 2026-08-12 GitHub trending crawl). Mechanism: spec files as the shared contract between human and agent.
- **Fission-AI/OpenSpec** — open-source "spec-driven development (SDD) for AI coding assistants": specs plus automated verification gates for agent-generated changes (64K+ stars as of 2026-08-12). Mechanism: acceptance-criteria-driven implementation loop.
- **Replit Agent (v2 → Agent 4)** — since Feb 2025, the agent writes an editable markdown plan in the project root that users can read, edit, and re-prompt; Agent 4 makes this explicit as a Plan mode where the agent asks clarifying questions and must wait for human approval before destructive changes. Mechanism: the plan/spec artifact is the contract the agent implements against — spec-as-by-product for vibe builders (2026-08-13).
- **Spec-first agent workflows in practice** — the broader 2026 trend of agent harnesses (Cursor, Claude Code, Codex ecosystems) adopting spec/plan artifacts before implementation, with review of intent rather than diff. Mechanism: planning artifact → implementation → verification.

## Engineering

- **Spec format:** plain-text/markdown specs with behavior, scope, constraints, and acceptance criteria — machine-parseable enough for agents, human-readable enough for review
- **Versioning:** specs live in the repo and change via PRs like code; the spec is the source of truth, code is derived
- **Verification gate:** automated tests/checks map each acceptance criterion to an executable check — no spec compliance, no merge
- **Drift control:** when the implementation forces a spec change, the spec changes first (documented), then the code follows
- **Metrics:** spec-change churn, acceptance-criteria pass rate, time-to-review (spec review vs diff review), and agent first-pass compliance

## UX

- Review the spec, not the diff: intent is the review surface; code details are delegated to tests
- Generated specs for vibe-builders: the tool writes the spec, the human approves it, agents implement — documentation becomes a by-product
- Visible spec-compliance status on every PR/change ("3/5 criteria verified") instead of opaque agent output

## Business

- **Enterprise unlock:** specs give compliance and audit teams a reviewable contract for AI-written code — the difference between "agents can help" and "agents can be shipped"
- **Quality economics:** catching wrong intent at the spec stage is orders of magnitude cheaper than debugging generated code; fewer agent-rewrite cycles lower token spend
- **Ecosystem play:** the spec format is the battleground — whichever vendor's spec format becomes standard owns the workflow (GitHub's position via SpecKit)

## Cross-Domain Transfers

- Candidates: spec-driven **compliance** (regulatory intent → controls → evidence), spec-driven **data pipelines** (data contract → implementation → tests), spec-driven **agent operations** (SLA spec → agent behavior → verification)
- Emerging cross-domain candidate: spec-driven research — an investment memo written as a spec (claims, required evidence, acceptance criteria) that agents must satisfy before it ships

## Pitfalls

- **Stale specs:** spec rot silently misleads agents; freshness policy required
- **Spec theater:** verbose documents with no executable acceptance criteria — the verification gate is the pattern, the prose is not
- **Overhead on small tasks:** specing everything kills velocity; apply the pattern at task boundaries, not inside them
- **Lock-in risk:** a proprietary spec format can capture the workflow — standards/open formats are the counter
