---
id: lovable
type: product
name: Lovable
category: AI
company: Lovable (Stockholm, Sweden)
founded: 2023
status: active
tags: [vibe-coding, app-generation, no-code, ai-developer, full-stack]
last_updated: 2026-08-07
sources:
  - https://lovable.dev/gpt-engineer
  - https://en.wikipedia.org/wiki/Lovable_(company)
  - https://techcrunch.com/2026/03/11/lovable-says-it-added-100m-in-revenue-last-month-alone-with-just-146-employees/
  - https://www.businessinsider.com/lovable-arr-hit-500-million-surprising-facts-about-its-users-2026-6
  - https://www.forbes.com/sites/rashishrivastava/2026/06/05/ai-coding-startup-lovable-in-talks-to-raise-funding-at-a-12-billion-valuation/
  - https://europeanbusinessmagazine.com/business-lovable-price-bets-suppliers/
  - https://www.kucoin.com/news/flash/ai-startup-lovable-projects-1b-arr-attracts-crypto-vcs
  - https://www.taskade.com/blog/lovable-history
---

# Lovable

## Overview

Lovable is a browser-based platform that generates full-stack applications from natural-language prompts — the flagship "vibe coding" product. Instead of assisting developers in an editor (Cursor's lane), it **replaces the editor for people who never were developers**: type what you want, watch the app appear, keep talking to change it. Its success mechanism: **collapse the time from idea to working, shareable app from weeks to minutes, for the 80% of builders who are not technical — then let every generated app act as a distribution unit.**

## History

- **Mid-2023** — Anton Osika creates GPT Engineer, an open-source experiment in AI-driven code generation; it becomes one of the fastest-growing GitHub repositories at the time, passing 50K stars.
- **Nov 2023** — Lovable founded in Stockholm by Anton Osika (CEO) and Fabian Hedin (CTO); the open-source project is commercialized into a web app (GPT Engineer App).
- **2024** — Rebranded to Lovable; pivots to a visual, iteration-driven platform rather than a one-shot code generator.
- **Jul 2025** — $200M Series A at a $1.8B valuation (per reports).
- **Dec 2025** — $330M Series B at a $6.6B valuation, backed by CapitalG and Menlo Ventures (per reports); total funding reaches ~$553M.
- **Feb 2026** — ARR crosses $400M; payments feature goes live (users begin charging inside generated apps).
- **Mar 2026** — TechCrunch reports Lovable added ~$100M of revenue in a single month, with only 146 employees.
- **Jun 2026** — ARR exceeds $500M (up 25%+ from $400M); 8M users; a survey of 14,300 users shows ~80% are non-technical builders; CEO claims more than half of the Fortune 500 use Lovable (customers include Klarna, HubSpot).
- **Jun–Jul 2026** — Reports of a ~$300M raise at a $12–13.2B valuation (unconfirmed at time of writing).

## Target User

- **Core:** non-technical builders — founders, marketers, operators, students — who have product ideas but cannot code (survey: ~80% non-technical)
- **Growing into:** technical users who want fast prototypes; enterprises (more than half of Fortune 500 per CEO claims) using it to "supercharge creativity"
- **Not served:** professional teams needing production-grade control, audit, and security (that is Cursor/Claude Code territory)

## Business

- **Model:** subscription SaaS (free tier + paid tiers); enterprise contracts; payments take-rate is a new layer (Feb 2026)
- **Revenue trajectory (sourced):** crossed $400M ARR (Feb 2026) → +$100M revenue in one month (Mar 2026) → $500M+ ARR (Jun 2026); 146 employees at the time — extreme revenue-per-employee for the era
- **Funding (sourced):** ~$553M raised through late 2025; in talks for ~$300M at $12–13.2B (mid-2026, unconfirmed)
- **Distribution:** shareable app URLs (every generated app is a marketing unit), social virality of "vibe coding" demos, open-source heritage as the trust seed, enterprise bottom-up adoption

## Growth

- **Core loop:** prompt → working app → share link → new users try → new users prompt. The shareable artifact is the viral unit — no install, no explanation needed.
- **Vibe-coding wave:** timing rode the "AI can build your app" moment (2024–2026); Lovable became the default name for it.
- **Feedback loop:** iteration speed (seconds-to-minutes per change) keeps users in the loop; project memory makes each session start from the previous state.

## UX

- **Chat-first build surface:** the conversation *is* the IDE — prompt, see the app update, prompt again
- **Zero-setup:** no local environment, no dependencies, no deployment config; custom domain and share in clicks
- **Visual editor layered on chat:** for users who want pixel control without code
- **Working software as feedback:** the artifact, not a diff, is what the user evaluates — a fundamentally different UX contract than code editors

## AI

- **Generation + iteration:** LLMs write frontend and backend code from natural language; Supabase integration provides auth/database/storage scaffolding so "full-stack" actually works
- **Iteration is the product:** the model must understand the existing app (project context/memory) and apply deltas, not regenerate from scratch
- **Latency economics:** speed and cost per iteration are the binding constraints; usage metering is the pricing model
- **Model risk:** Lovable's value sits on top of underlying frontier models; the moat must come from workflow, project state, and ecosystem, not the model itself

## Architecture

- Browser-based builder + hosted preview/sandbox + generation backend (multi-model)
- Supabase integration for generated backend (auth, database, storage)
- Project state/memory across iterations (the app as the artifact)
- Deploy pipeline (custom domains, hosting) + payments layer (Feb 2026)
- Enterprise controls (team management, security review) as the B2B layer

## Patterns

- Instantiates: [AI Chat](../../features/AI-Chat.md) (chat as the build surface), [Memory](../../patterns/Memory.md) (project context across iterations)
- Emerging patterns worth filing: **Iterative Artifact Loop** (chat with a living artifact, not a chat log), **Shareable Artifact as Distribution** (every generated app is a marketing unit), **Vibe Coding** (natural language as the primary interface to software creation)
- Contrast: Lovable = build-for-me (replaces the builder); Cursor = assist-me (augments the builder). Both monetize AI coding but from opposite sides of the same market.

## Lessons

1. **Open source is a distribution weapon** — GPT Engineer's 50K stars seeded trust and a funnel that no ad campaign could buy.
2. **Pick the user the incumbents ignore** — 80% non-technical builders were never served by code editors; "vibe coding" met them where they were.
3. **The artifact is the feedback loop** — showing a working app (not a diff) changes who can participate in software creation.
4. **Leverage is the metric** — $500M ARR with 146 employees is AI-native unit economics; design for it, don't apologize for it.
5. **Moats are workflow and state, not the model** — generation is commoditizing; project memory, ecosystem integrations, and payments are the durable layers.
6. **Enterprise claims need verification** — "more than half of Fortune 500" is CEO marketing until audited; treat as directional.

## Innovation

Lovable industrialized **vibe coding for non-developers** and made **shareable app URLs** the distribution unit — a template every AI app builder now copies. Cross-domain transfers: the Iterative Artifact Loop → any "create by conversation" domain (internal tools, agent workflows, and — with guardrails — conversational build experiences in regulated education); Shareable Artifact as Distribution → education and portfolio products.

## Sources

1. Lovable — GPT Engineer origin story: https://lovable.dev/gpt-engineer
2. Wikipedia — Lovable (company): https://en.wikipedia.org/wiki/Lovable_(company)
3. TechCrunch — $100M revenue month, 146 employees, Fortune 500 claim (Mar 2026): https://techcrunch.com/2026/03/11/lovable-says-it-added-100m-in-revenue-last-month-alone-with-just-146-employees/
4. Business Insider — $500M ARR, 14,300-user survey, 80% non-technical (Jun 2026): https://www.businessinsider.com/lovable-arr-hit-500-million-surprising-facts-about-its-users-2026-6
5. Forbes — $400M ARR, talks at $12B (Jun 2026): https://www.forbes.com/sites/rashishrivastava/2026/06/05/ai-coding-startup-lovable-in-talks-to-raise-funding-at-a-12-billion-valuation/
6. European Business Magazine/Sifted — $300M at $13.2B talks (Jul 2026): https://europeanbusinessmagazine.com/business-lovable-price-bets-suppliers/
7. KuCoin News — $553M raised, $6.6B late-2025 valuation (Jul 2026): https://www.kucoin.com/news/flash/ai-startup-lovable-projects-1b-arr-attracts-crypto-vcs
8. Taskade — founding history, founders (Feb 2026): https://www.taskade.com/blog/lovable-history
