---
id: windsurf
type: product
name: Windsurf
category: AI
company: Cognition AI (acquired Windsurf/Codeium, July 2025)
founded: 2021
status: acquired
tags: [developer-tools, agentic-coding, ai-ide, context-engine, mcp, memory]
last_updated: 2026-08-16
sources:
  - https://www.latent.space/p/windsurf
  - https://baike.baidu.com/item/Varun%20Mohan/66220031
  - https://www.techspot.com/downloads/7708-windsurf.html
  - https://www.cnbc.com/2025/07/14/cognition-to-buy-ai-startup-windsurf-days-after-google-poached-ceo.html
  - https://www.nytimes.com/2025/07/14/technology/cognition-ai-windsurf.html
  - https://www.moneycontrol.com/technology/cognition-ai-buys-windsurf-after-google-hires-ceo-varun-mohan-and-top-executives-in-2-4-billion-deal-article-13279533.html
  - https://www.mitsloanindia.com/article/cognition-raises-1-billion-at-26-billion-valuation/
  - https://www.kucoin.com/news/flash/cognition-s-annual-revenue-exceeds-500m-after-acquiring-windsurf
  - https://cognition.com/blog/devin-in-windsurf
  - https://devin.ai/blog/devin-review-windsurf
  - https://docs.devin.ai/windsurf/plugins/cascade/workflows
  - https://docs.devin.ai/zh/desktop/devin-desktop-faq
  - https://www.morphllm.com/comparisons/cursor-vs-windsurf-vs-copilot
  - https://ofox.ai/zh/blog/vibe-coding-tools-comparison-cursor-windsurf-roo-code-claude-code-2026/
  - https://shiporskip.io/tool/windsurf-wave-11-cascade-agent-multi-file-edits-memory
  - https://shiporskip.io/tool/windsurf-wave-12-swe-1-model-cascade-agents
  - https://awesomeagents.ai/reviews/review-windsurf/
  - https://github.com/OnlyTerp/windsurf-unlocked
---

# Windsurf

## Overview

Windsurf is the AI-first IDE (originally Codeium) whose Cascade agent — a deep context engine that watches the cursor, the codebase, and the developer's intent in real time — made "agent-in-the-editor" a product category. It was the fastest-growing AI code editor of 2024–2025, then became the second pillar of Cognition's autonomous-coding platform after its July 2025 acquisition: local Cascade agents and cloud Devin agents merged into one workspace (Windsurf 2.0, April 2026), and the editor was renamed Devin Desktop in June 2026. Its success mechanism: **an editor that sells context awareness, not completions** — the product reads more of the developer's work than any competitor's, and it monetizes that awareness through credit-metered agent actions, in-house coding models (SWE-1/1.5), and an MCP-based tool ecosystem.

## History

- **2021** — Codeium founded by MIT classmates Varun Mohan and Douglas Chen; the company operated briefly as Exafunction before rebranding to Codeium in 2022 (as of 2025-07-11, Moneycontrol).
- **Nov 2024** — Codeium launches **Windsurf**, a standalone AI-first IDE built around Cascade, combining deep codebase understanding with real-time awareness of developer actions (as of 2026-05-31, TechSpot).
- **Dec 2024** — Latent Space interview: "over 800,000 developers" use the product, with large-enterprise adoption (as of 2024-12-12, Latent Space).
- **Jul 11, 2025** — Google hires CEO Varun Mohan and top executives in a ~$2.4B talent-plus-licensing deal (as of 2025-07-13, CNBC).
- **Jul 14, 2025** — **Cognition acquires Windsurf** days after the Google deal, securing the product, team, and business (as of 2025-07-14, NYT / Moneycontrol).
- **Apr 14–15, 2026** — **Windsurf 2.0** ships: Agent Command Center, local agents, built-in Devin cloud agent (virtual machine + browser), and unified PRs/files/context in one workspace; Devin available to all Windsurf subscribers in phased rollout (as of 2026-04-15, Cognition blog / KuCoin).
- **Apr 2026** — SWE-1.5, Windsurf's in-house coding model, reported ~13x faster than Claude Sonnet 4.5 with higher multi-step completion rates (as of 2026-04-19, ofox.ai).
- **May 5, 2026** — **Devin Review / Quick Review** bring code verification into the editor (as of 2026-05-05, Devin blog).
- **May 27, 2026** — Cognition raises **$1B at a $26B valuation**; revenue run rate $492M, enterprise usage up >10x since the start of 2026 (as of 2026-05-27, MIT Sloan India).
- **Jun 2, 2026** — Windsurf is **renamed Devin Desktop**; all Windsurf settings auto-migrate to Devin paths (as of 2026-06-02, Devin docs FAQ).
- **Jul 2026** — **Wave 11**: Cascade persistent memory across sessions + enhanced multi-file editing (reviewed 2026-07-03, Ship or Skip). **Wave 12**: SWE-1 model + **Cascade Agents** that autonomously browse documentation, execute test suites, and submit pull requests (reviewed 2026-07-21, Ship or Skip).
- **Jul 14, 2026** — Cognition's annualized revenue reported to exceed **$500M** (from $73M pre-acquisition), team grown from 44 to ~350 (as of 2026-07-14, KuCoin flash / The Block Beats).

## Target User

- **Individual developers and indie "vibe coders"** — free tier with 25 credits and $15/mo Pro with 500 credits (as of 2026-02-28, Morph LLM comparison); low-friction entry from code completion to full agent tasks.
- **Teams** — Teams plan ~$30–60 per user/month depending on review date and feature bundle (Morph, Feb 2026: $30/user; Ship or Skip Wave 12 review, Jul 2026: $60/mo Teams).
- **Enterprises** — the original Codeium pitch was enterprise AI assistance (large-enterprise installs per Latent Space, Dec 2024); post-Cognition, enterprises buy the combined Devin + Windsurf platform; system-level `SKILL.md` deployment via MDM and custom MCP registries (as of Mar–Apr 2026, windsurf-unlocked).
- **Who pays vs who uses:** the developer is both user and (often) the buyer on self-serve plans; team/enterprise seats are bought by engineering leads and IT who also get admin controls (MCP whitelists, skill libraries, usage governance).

## Business

- **Model:** freemium subscription on credit-metered agent work. Free = 25 credits; Pro = $15/mo for 500 credits; Teams/Enterprise seats add governance (as of 2026-02-28, Morph; 2026-07-21, Ship or Skip). Credits meter agent actions and premium model usage — an [Effort-Based Pricing](../../patterns/Effort-Based-Pricing.md) instance where the meter is the agent task, not the seat.
- **Revenue trajectory:** Cognition's annualized revenue grew from **$73M (June 2025)** to **$492M (May 2026)** to **>$500M (July 2026)** after the Windsurf acquisition; ARR grew >30% in seven weeks post-acquisition; enterprise usage >10x in 2026; headcount 44 → ~350 (as of 2026-05-27 MIT Sloan India; 2026-07-14 KuCoin/The Block Beats; c114.net.cn May 2026).
- **Distribution:** product-led growth (free IDE + completion), plus the Cognition channel: Devin enterprise contracts and platform sales now carry Windsurf/Devin Desktop. Post-renaming (June 2026), brand equity consolidates into one Devin product family.
- **Unit economics note:** in-house models (SWE-1/1.5) lower marginal inference cost vs renting frontier models — a structural margin advantage over IDE rivals, though model quality/evals remain the binding constraint.

## Growth

- **The core loop is developer-led, not viral:** a free editor with best-in-class completion converts to Pro when the developer first runs a multi-file agent task; every Cascade task produces visible artifacts (edited files, PRs, test runs) that get shared inside teams → seat expansion.
- **Two-sided ecosystem loop:** MCP servers and community skills add tools → Cascade becomes more capable → more developers choose Windsurf → more tool authors target it (as of Apr 2026, windsurf-unlocked documents a 100-tool MCP ceiling and public Marketplace).
- **Post-acquisition compounding:** Cognition's Devin cloud agent becomes the "escalation tier" of the editor (local → cloud), giving one product two acquisition surfaces: developers who start in the IDE and enterprises who start with Devin agents (as of 2026-04-15, Cognition blog).
- **Trend ownership:** Windsurf owns the "context awareness" narrative in the IDE wars (Cascade reads codebase + cursor trajectory); each Wave release (11, 12…) converts feature work into earned press and community documentation.

## UX

- **Entry experience:** install a familiar VS Code-derived IDE, get free completion immediately; Cascade is surfaced as a persistent panel rather than a chat popup — the agent is ambient, not interruptive.
- **Core loop:** developer types → Cascade predicts intent from cursor position and codebase context (reads context before and after the cursor, "predicts your next moves" per Morph, Feb 2026) → agent proposes multi-file edits → developer accepts/rejects per change → verification (tests, Devin Review) closes the loop.
- **Information architecture:** one workspace unifies local files, cloud agent sessions, PRs, and context (Windsurf 2.0, Apr 2026); Cascade Memories persist architectural patterns, naming conventions, and config quirks between conversations (as of Feb 2026, awesomeagents review).
- **Friction points historically:** MCP setup/OAuth friction — addressed Feb 2026 with auto-triggered OAuth login flows and Streamable HTTP migration (as of Apr 2026, windsurf-unlocked).
- **Retention mechanics:** Memories and workflows (markdown `workflows` files with slash commands) accumulate project knowledge, making the editor more valuable the longer it is used — switching costs rise with context depth (as of Jun 2026, Devin docs).

## AI

- **Models:** Cascade routes across models; Windsurf ships in-house coding models — SWE-1.5 (Apr 2026, ~13x faster than Claude Sonnet 4.5 with better multi-step completion) and SWE-1 (Wave 12, Jul 2026) — plus frontier-model routing (Claude, GPT) for complex tasks (as of 2026-04-19 ofox.ai; 2026-07-21 Ship or Skip).
- **Agentic capabilities:** Cascade Agents (Wave 12, Jul 2026) autonomously browse docs, execute test suites, and open PRs; Devin cloud agent brings a virtual machine + browser for end-to-end tasks (as of Apr–Jul 2026, Cognition/Devin blogs, Ship or Skip).
- **Context engineering:** the differentiated layer — deep codebase indexing, real-time action awareness, Memories distilled between sessions, and a 100-tool MCP ceiling to bound context (as of Feb–Apr 2026, awesomeagents, windsurf-unlocked).
- **Data flywheel:** anonymized agent trajectories + user accept/reject signals feed model and routing evals; in-house models close the loop between product telemetry and model training.
- **Evals:** multi-step task completion and speed are the published differentiators (SWE-1.5 claims); verification moved into the product via Devin Review/Quick Review (May 2026).

## Architecture

- **Local agent runtime:** codebase index (embeddings/static analysis), cursor/intent tracker, session memory store (Memories), tool-execution sandbox inside the editor.
- **Cloud agent tier:** Devin's VM + browser + long-horizon task runner, reachable from the editor with one click — local/cloud handoff is the architectural seam (as of Apr 2026, Cognition blog).
- **Tool ecosystem:** MCP client with three transports (stdio, Streamable HTTP, legacy SSE), OAuth auto-trigger, org-level MCP registries/whitelists, 100-tool runtime ceiling (as of Apr 2026, windsurf-unlocked).
- **Skills layer:** `SKILL.md`-based skills per project/global, and system-level skills deployed via MDM for enterprise (as of Mar 2026, windsurf-unlocked) — the agent's "training manual" lives in the repo, not in the model.
- **Workflow engine:** reusable Cascade workflows as markdown files under `.windsurf/workflows/`, invoked via slash commands (as of Jun 2026, Devin docs).
- **Identity/governance:** admin controls for MCP whitelists, skill libraries, and registry overrides; OAuth flows for HTTP/SSE servers.

## Patterns

- [Ambient Activity Memory](../../patterns/Ambient-Activity-Memory.md) — Cascade Memories: passively observed codebase behavior distilled into durable context between sessions.
- [Open Protocol Ecosystem](../../patterns/Open-Protocol-Ecosystem.md) — MCP client with Marketplace, registries, and a 100-tool governance ceiling.
- [Effort-Based Pricing](../../patterns/Effort-Based-Pricing.md) — credit-metered agent work on top of free completion.
- [Parallel Agent Orchestration](../../patterns/Parallel-Agent-Orchestration.md) — local Cascade + cloud Devin split with one-click handoff.
- **Emerging (this teardown):** [Context-Economy Engineering](../../patterns/Context-Economy-Engineering.md) — deep context indexing, Memories distillation, and tool ceilings all exist to make each token do more work.

## Lessons

- **Copy — context is the product:** the durable differentiator is how much of the user's work the agent actually sees (cursor, codebase, history), not which model is behind it; rivals caught up on completion, not on awareness.
- **Copy — in-house model economics:** owning the model turns usage growth into margin instead of API bills; the tradeoff is eval discipline (speed claims need benchmarks).
- **Copy — escalate, don't replace:** local agent for cheap fast loops + cloud agent for heavy tasks means one UX with two price points and two acquisition funnels.
- **Avoid — brand churn:** renaming Windsurf → Devin Desktop (June 2026) traded a beloved consumer brand for portfolio consolidation; community docs and tutorials had to be rewritten, and "what is this product called" became a support question.
- **Avoid — ecosystem debt:** supporting SSE and third-party transports that the industry is deprecating creates silent breakage; the 2026 SSE→Streamable HTTP migration was friction that could have been planned earlier (as of Apr 2026, windsurf-unlocked).

## Innovation

Windsurf industrialized **agent-in-editor context awareness**: an IDE whose central artifact is a continuously-updated model of what the developer is doing, backed by memories that persist across sessions and workflows that live in the repo. It invented the local→cloud agent handoff as a product pattern and demonstrated that an acquired IDE can become the wedge for an autonomous-coding platform (Devin) rather than an also-ran. Where the pattern transfers next: any tool where "the assistant should know what I'm doing" beats "the assistant should answer my prompts" — design tools (Figma), spreadsheet/analysis surfaces, legal document workspaces, and ops consoles; the [Context-Economy Engineering → Mobile Markets](../../cross-domain/Context-Economy-Engineering-to-Mobile-Markets.md) transfer is a concrete candidate.

## Sources

1. [Latent Space: Windsurf – The Enterprise AI IDE (Dec 2024)](https://www.latent.space/p/windsurf)
2. [Moneycontrol: Varun Mohan background (Jul 2025)](https://www.moneycontrol.com/technology/who-is-varun-mohan-the-indian-origin-ceo-who-rejected-3-billion-openai-deal-for-google-deepmind-article-13270840.html)
3. [CNBC: Cognition to buy Windsurf after Google poached CEO (Jul 2025)](https://www.cnbc.com/2025/07/14/cognition-to-buy-ai-startup-windsurf-days-after-google-poached-ceo.html)
4. [NYT: Cognition AI Buys Windsurf (Jul 2025)](https://www.nytimes.com/2025/07/14/technology/cognition-ai-windsurf.html)
5. [MIT Sloan India: Cognition raises $1B at $26B valuation (May 2026)](https://mitsloanindia.com/article/cognition-raises-1-billion-at-26-billion-valuation/)
6. [KuCoin Flash: Cognition revenue exceeds $500M (Jul 2026)](https://www.kucoin.com/news/flash/cognition-s-annual-revenue-exceeds-500m-after-acquiring-windsurf)
7. [Cognition: Devin in Windsurf (Apr 2026)](https://cognition.com/blog/devin-in-windsurf)
8. [Devin blog: Devin Review in Windsurf (May 2026)](https://devin.ai/blog/devin-review-windsurf)
9. [Devin docs: Cascade workflows (Jun 2026)](https://docs.devin.ai/windsurf/plugins/cascade/workflows)
10. [Devin docs FAQ: Windsurf renamed Devin Desktop (Jun 2026)](https://docs.devin.ai/zh/desktop/devin-desktop-faq)
11. [Morph: Cursor vs Windsurf vs Copilot pricing (Feb 2026)](https://www.morphllm.com/comparisons/cursor-vs-windsurf-vs-copilot)
12. [ofox.ai: 2026 vibe-coding tools comparison incl. SWE-1.5 (Apr 2026)](https://ofox.ai/zh/blog/vibe-coding-tools-comparison-cursor-windsurf-roo-code-claude-code-2026/)
13. [Ship or Skip: Windsurf Wave 11 review (Jul 2026)](https://shiporskip.io/tool/windsurf-wave-11-cascade-agent-multi-file-edits-memory)
14. [Ship or Skip: Windsurf Wave 12 review (Jul 2026)](https://shiporskip.io/tool/windsurf-wave-12-swe-1-model-cascade-agents)
15. [awesomeagents: Windsurf review incl. Cascade Memories (Feb 2026)](https://awesomeagents.ai/reviews/review-windsurf/)
16. [windsurf-unlocked: MCP/skills/enterprise feature notes (Apr 2026)](https://github.com/OnlyTerp/windsurf-unlocked)
