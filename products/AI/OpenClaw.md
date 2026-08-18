---
id: openclaw
type: product
name: OpenClaw
category: AI
company: OpenClaw Foundation
founded: 2025
status: active
tags: [personal-ai-assistant, agent-gateway, local-first, open-source, skills-ecosystem]
last_updated: 2026-08-17
sources:
  - https://github.com/openclaw/openclaw
  - https://openclaw.ai
  - https://docs.openclaw.ai
  - https://clawhub.ai
  - https://www.bloomberg.com/news/articles/2026-02-15/openai-hires-openclaw-ai-agent-developer-peter-steinberg
  - https://indianexpress.com/article/technology/tech-news-technology/openclaw-founder-steinberger-joins-openai-open-source-bot-becomes-foundation-10534470/
  - https://m.thepaper.cn/newsDetail_forward_32622443
  - https://www.donews.com/news/detail/1/6432573.html
  - https://korben.info/en/openclaw-personal-ai-assistant-mac.html
  - https://zhuanlan.zhihu.com/p/2011890464383604275
  - https://landscape.jimmysong.io/projects/openclaw/
  - https://m.jiemian.com/article/14089107.html
  - https://deepwiki.com/hustcc/nano-claw/3.2-provider-configuration
---

# OpenClaw

## Overview

OpenClaw is an open-source, local-first personal AI assistant that runs on the user's own devices and is reached through the messaging channels they already use — WhatsApp, Telegram, Slack, Discord, Signal, iMessage, Feishu, LINE and more (as of 2026-08, [README](https://github.com/openclaw/openclaw)). Its one-sentence mechanism: a local **Gateway** acts as a single control plane for sessions, channels, tools and events, while an installable-skill registry (**ClawHub**) makes capability growth a community marketplace instead of a vendor roadmap. It is built around "local agent sovereignty" — the model, the tools and the data stay on hardware the operator controls.

## History

- **2025-11-24** — Repository created; project launched as "ClawdBot", a weekend project by Austrian developer Peter Steinberger (GitHub API; [landscape.jimmysong.io](https://landscape.jimmysong.io/projects/openclaw/); [DoNews](https://www.donews.com/news/detail/1/6432573.html)).
- **2026-01** — Goes viral in developer circles; featured as an AI "digital butler" running on a Mac mini M4, using Claude Opus 4.5 via the Anthropic API by default (as of 2026-01-27, [Korben](https://korben.info/en/openclaw-personal-ai-assistant-mac.html)).
- **2026-02-15/16** — Peter Steinberger announces he is joining OpenAI to work on personal agents; OpenClaw moves to an independent non-profit, the OpenClaw Foundation, funded by OpenAI (as of 2026-02-16, [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-15/openai-hires-openclaw-ai-agent-developer-peter-steinberg); [Indian Express](https://indianexpress.com/article/technology/tech-news-technology/openclaw-founder-steinberger-joins-openai-open-source-bot-becomes-foundation-10534470/); [The Paper](https://m.thepaper.cn/newsDetail_forward_32622443)).
- **2026-02 → 2026-03** — ClawHub skill registry grows from under 3,000 to ~13,729 community skills in about a month, with semver versioning and changelogs (as of 2026-03-01, [Zhihu](https://zhuanlan.zhihu.com/p/2011890464383604275)).
- **2026-03** — Chinese-language media dubs the craze "养龙虾" (raising lobsters); OpenClaw becomes a mainstream tech-culture phenomenon in China (as of 2026-03-08, [Jiemian](https://m.jiemian.com/article/14089107.html)).
- **2026-05** — Community sources report ClawHub exceeding 20,000 skills (as of 2026-05-13).
- **2026-08-17** — 386,473 stars / 81,208 forks; consistently top of GitHub Trending; sponsors include OpenAI, GitHub, NVIDIA, Vercel, Blacksmith and Convex (GitHub API + [README](https://github.com/openclaw/openclaw)); community variants such as NanoClaw (hustcc/nano-claw) are active.

## Target User

Primary user is a **single operator** — a developer or self-hoster who wants an assistant with agent sovereignty: their own model keys, their own hardware, their own data (README, as of 2026-08). Secondary users are non-technical individuals who interact through familiar messaging apps (WhatsApp/Telegram/Feishu), where onboarding is a pairing request rather than a new UI. Users and payers differ: users pay nothing; funding comes from the foundation and sponsors, and Steinberger personally underwrote roughly $10K/month of operating cost before the OpenAI arrangement (as of 2026-02, [The Paper](https://m.thepaper.cn/newsDetail_forward_32622443)).

## Business

Open source under the OpenClaw Foundation, a non-profit (as of 2026-08, [README](https://github.com/openclaw/openclaw)); the README shows an MIT badge while the GitHub API classifies the LICENSE file as unrecognized as of 2026-08-17. Monetization: `Unknown` — no paid tier is documented as of 2026-08. Distribution: GitHub stars, npm package `openclaw`, one-line installers (curl/PowerShell), Docker/Nix, and a Discord community (as of 2026-08, [README](https://github.com/openclaw/openclaw)). Institutional sponsorship (OpenAI, GitHub, NVIDIA, Vercel, Blacksmith, Convex) covers infrastructure and development (README sponsor list, as of 2026-08-17).

## Growth

The dominant loop is **open-source virality**: star history went from zero to ~386K in roughly nine months (GitHub API, 2026-08-17), propelled by GitHub Trending placement and developer word-of-mouth. A second loop is the **skill-marketplace network effect**: ClawHub's installable skills make the assistant more useful, which attracts more users, who publish more skills (13K+ in one month, 2026-03). A third loop is **channel-native distribution**: because the assistant lives inside channels users already have (WhatsApp, Telegram, Feishu), activation is one pairing, not a new app install. Cultural virality (the "养龙虾" phenomenon in China, 2026-03) acted as a mainstream marketing channel beyond developers.

## UX

Entry experience: one-line installer, then `openclaw onboard` — which verifies model access, creates the workspace and configures the Gateway — followed by a Control UI/dashboard message to confirm the assistant works (README, as of 2026-08). Core loop: the user sends a message from any connected channel → the Gateway routes it to model + tools → the result returns to the same channel. Information architecture: Gateway (control plane) → channels / tools / skills / plugins, with CLI, TUI and web UI as interchangeable front-ends. Security is UX: inbound messages are treated as untrusted, DM-capable channels require an explicit pairing approval, and sandboxing is configurable (README security section, as of 2026-08). Retention mechanics include a personality layer — the "Molty, space lobster" lore and "EXFOLIATE!" branding — which turns a utility into an identity.

## AI

Model-agnostic: hosted and local model providers are supported (as of 2026-08, [docs](https://docs.openclaw.ai/concepts/model-providers)); the default was Claude Opus 4.5 via the Anthropic API as of 2026-01 ([Korben](https://korben.info/en/openclaw-personal-ai-assistant-mac.html)), with OpenRouter as a popular gateway in the community (e.g., [NanoClaw docs](https://deepwiki.com/hustcc/nano-claw/3.2-provider-configuration), 2026-02). Capability comes from tools, skills and plugins rather than from model size alone; skills are packaged instructions/workflows installed from ClawHub with version management ([docs](https://docs.openclaw.ai/tools/skills)). Evals: `Unknown` — no public benchmark suite as of 2026-08. Data flywheel: the assistant's utility compounds per-operator as its workspace, skills and channel history accumulate on the user's own hardware.

## Architecture

Product-level architecture (README/docs, as of 2026-08): a **local-first Gateway** as the single control plane for sessions, channels, tools and events; **channel adapters** for messaging services (WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Feishu, LINE, Twitch, Tlon); a **workspace** holding configuration and state; a **tool/skill/plugin runtime** with a plugin SDK; **ClawHub registry integration** for install/update/versioning of skills; **companion apps and nodes** adding voice, Canvas, camera, screen and device-local actions; a **model-provider abstraction** across hosted and local models; a **sandboxing layer**; and a **pairing/auth layer** for DM channels. Runtime requirement is Node (22.22.3+/24.15+/25.9+), with installers for macOS, Linux and Windows/WSL2.

## Patterns

- [Open Protocol Ecosystem](../../patterns/Open-Protocol-Ecosystem.md) — the Gateway + channel adapters + installable skill packs are the same "open protocol, one control plane" move as MCP; OpenClaw is a full product instance of it.
- [Agent Skill Marketplace](../../patterns/Agent-Skill-Marketplace.md) — ClawHub is an app-store/npm-style registry of installable agent skills (semver, search, install, update), the pattern this teardown files.
- [Curation](../../patterns/Curation.md) — a registry that grew from <3K to ~14K skills in a month needs curation/moderation (ClawHub moderation tooling exists); curation becomes the quality gate of the marketplace.
- Emerging candidate (watching brief): **Session-as-Artifact** — sharing the raw agent session as a reviewable artifact, seen in Kimi Work's raw-session feedback reports (HN, 2026-08-16), Legbar's live agent sessions beside CI (Show HN, 2026-08-17) and Remarc's structured agent feedback (Show HN, 2026-08-17). Needs one more instance before filing.

## Lessons

Copy: meet users in channels they already use instead of forcing a new UI; make extensibility a marketplace (registry + semver + plugin SDK) rather than a roadmap; use local-first as a trust and sovereignty story that no hosted vendor can replicate; convert a utility into an identity (lore, mascot, catchphrase) for retention and cultural spread; plan governance (non-profit foundation) before virality forces it.

Avoid: treating inbound messages as trusted input — OpenClaw's own docs mandate pairing approval and sandboxing; letting a skill registry grow without curation, which floods the marketplace with low-quality or broken skills; and single-maintainer dependence, which the 2026-02 foundation transition had to resolve mid-hype.

## Innovation

OpenClaw industrialized the **personal agent OS**: local Gateway control plane + channel adapters + skill marketplace, with model/tool/data ownership staying with the operator. It also pioneered a governance template for viral open-source agents (founder → company → non-profit foundation funded by a strategic sponsor). Natural next transfers: enterprise desktop agents (device-local actions with IT policy layers), regulated operations where skills become jurisdiction-specific compliance packs (see [Agent Skill Marketplace → Regulatory Compliance Packs](../../cross-domain/Agent-Skill-Marketplace-to-Regulatory-Compliance-Packs.md)), and healthcare/caregiving personal assistants where local-first data handling is a feature, not a constraint.

## Sources

1. [GitHub — openclaw/openclaw README (as of 2026-08-17)](https://github.com/openclaw/openclaw)
2. [GitHub API — repo metadata: created 2025-11-24, 386,473 stars / 81,208 forks (2026-08-17)](https://api.github.com/repos/openclaw/openclaw)
3. [OpenClaw website](https://openclaw.ai)
4. [OpenClaw docs — Gateway, channels, skills, plugins](https://docs.openclaw.ai)
5. [ClawHub — skill registry](https://clawhub.ai)
6. [Bloomberg — OpenAI hires OpenClaw creator Peter Steinberger (2026-02-15)](https://www.bloomberg.com/news/articles/2026-02-15/openai-hires-openclaw-ai-agent-developer-peter-steinberg)
7. [Indian Express — OpenClaw becomes foundation as founder joins OpenAI (2026-02-16)](https://indianexpress.com/article/technology/tech-news-technology/openclaw-founder-steinberger-joins-openai-open-source-bot-becomes-foundation-10534470/)
8. [The Paper — founder joined OpenAI, foundation continues open source (2026-02-17)](https://m.thepaper.cn/newsDetail_forward_32622443)
9. [DoNews — OpenClaw origins as ClawdBot (2026-02-17)](https://www.donews.com/news/detail/1/6432573.html)
10. [Korben — OpenClaw on Mac mini, Claude Opus 4.5 default (2026-01-27)](https://korben.info/en/openclaw-personal-ai-assistant-mac.html)
11. [Zhihu — ClawHub 13,729 skills with semver (2026-03-01)](https://zhuanlan.zhihu.com/p/2011890464383604275)
12. [AI Native Landscape — OpenClaw project record (2025-11)](https://landscape.jimmysong.io/projects/openclaw/)
13. [Jiemian — "养龙虾" phenomenon (2026-03-08)](https://m.jiemian.com/article/14089107.html)
14. [DeepWiki — NanoClaw provider configuration (2026-02)](https://deepwiki.com/hustcc/nano-claw/3.2-provider-configuration)
