---
id: mercor
type: product
name: Mercor
category: AI
company: Mercor (San Francisco, CA)
founded: 2023
status: active
tags: [ai-training-data, talent-marketplace, rlhf, ai-interview, expert-network, evaluation]
last_updated: 2026-08-09
sources:
  - https://techcrunch.com/2025/02/20/mercor-an-ai-recruiting-startup-founded-by-21-year-olds-raises-100m-at-2b-valuation/
  - https://techfundingnews.com/mercor-20b-valuation-talks-deeptune-acquisition/
  - https://www.36kr.com/p/3904682268034947
  - https://aiwiki.ai/wiki/mercor
  - https://www.kucoin.com/news/flash/mercor-hits-2b-annualized-run-rate-in-ai-human-feedback-services
  - https://www.forbes.com/sites/alexkonrad/2024/09/18/mercor-ai-interviewer-reaches-250-million-valuation/
  - https://talent.docs.mercor.com/support/ai-interview
---

# Mercor

## Overview

Mercor is a two-sided marketplace that connects vetted domain experts (engineers, lawyers, doctors, bankers, journalists) with frontier AI labs that need human judgment to train and evaluate models — RLHF/DPO preference data, expert grading, and long-horizon agent evaluation. It started in 2023 as an AI recruiting marketplace for freelance engineers and pivoted into the "human data" layer of the AI stack. Its success mechanism: **replace human screening with an AI interviewer that vets millions of candidates at machine speed, then sell the resulting credentialed expert pool to AI labs as elastic, hourly human intelligence — taking ~30–40% of every dollar that flows through the platform.**

## History

- **Jan 2023** — Mercor incorporated by Brendan Foody (CEO), Adarsh Hiremath (CTO), and Surya Midha (chairman) — high-school debate teammates from Bellarmine College Preparatory, San Jose; Hiremath at Harvard, Foody and Midha at Georgetown, all three drop out during their sophomore year. Initial model: connect freelance software engineers in India with US employers; the company bootstraps to seven-figure annual revenue from dorm rooms before outside capital.
- **Mar 2024** — The founders receive Thiel Fellowships ($100K each). Early angel backers include Peter Thiel, Jack Dorsey, Adam D'Angelo, and Larry Summers.
- **Jan 2024** — $3.6M seed led by General Catalyst; ~300,000 candidates evaluated at that point, talent across 25+ countries.
- **Sep 2024** — $32M Series A led by Benchmark at ~$250M valuation; AI interviewer has vetted 300,000+ candidates via ~20-minute video interviews (Forbes); 50% month-over-month revenue growth reported.
- **Feb 2025** — $100M Series B led by Felicis at $2B valuation (8x step-up in eight months); ~$75M ARR; working with "the world's top five AI labs"; hires former head of Human Data Operations at OpenAI and former head of Growth at Scale AI.
- **May 2025** — Sundeep Jain joins as first president (ex-Uber CPO/SVP Engineering, ex-Google Search Ads VP).
- **Sep 2025** — Launches APEX (AI Productivity Index), a benchmark measuring AI models on business tasks (consulting, investment banking, law), using Mercor's expert database as the human reference standard.
- **Oct 2025** — $350M Series C led by Felicis at $10B valuation (Robinhood Ventures new investor); ~30,000 contractors, ~$1.5M+ paid out daily, ~$500M annualized run rate; founders, at 22, become the youngest self-made billionaires on record per Forbes.
- **Jan 2026** — Releases APEX-Agents leaderboard: frontier agents complete <25% of professional tasks on first attempt, ~40% with up to eight retries (as of Jan 2026).
- **Mar 2026** — Supply-chain attack on LiteLLM, an open-source Python library, exposes up to 4TB of Mercor internal data and contractor records; Meta pauses all work with Mercor indefinitely; class-action lawsuits follow; Forbes reports suspicion that North Korean operatives infiltrated the contractor network with stolen credentials.
- **Jun 2026** — Annualized gross run rate crosses $2B (+100% in four months per CEO); H1 2026 gross revenue reported at $614M, over 90% of it from AI foundation-model companies (The Information via KuCoin, as of Jul 2026).
- **Jul 2026** — In talks to raise ~$500M at a $20B valuation (early, per Bloomberg via TFN); announces acquisition of Deeptune, an AI-agent training-environment startup (a16z had led Deeptune's $43M Series A in Mar 2026; Foody was an angel investor). Total funding ~$492M across four rounds (as of Jul 2026).

## Target User

- **Supply side:** domain experts worldwide — software engineers, physicians, lawyers, bankers, financial analysts, journalists — who pass the AI interview and join a rotating contractor pool (~30,000 contractors as of Oct 2025). Average pay exceeds $85/hour, far above generic annotation platforms.
- **Demand side:** frontier AI labs and enterprises needing human intelligence for post-training, evaluation, and agent benchmarks — documented customers include OpenAI, Anthropic, Google, Microsoft, and (until the 2026 breach pause) Meta.
- **The two differ structurally:** experts sell hours and keep 60–70% of billings; labs buy credentialed judgment at scale with zero recruiting overhead.

## Business

- **Model:** two-sided marketplace with a platform fee on contractor billings. AI labs pay hourly finder/matching fees; Mercor's take rate runs ~30–40% of gross contractor payments; experts keep the rest. Individual engagements can involve 5,000+ contractors simultaneously.
- **Revenue trajectory (sourced):** ~$75M ARR (Feb 2025) → ~$500M annualized run rate (Oct 2025) → ~$760M annualized (end of 2025) → ~$1B (early 2026) → $2B gross run rate (Jun 2026, +100% in four months); $614M gross revenue in H1 2026, 90%+ from AI foundation-model companies (The Information via KuCoin, Jul 2026). Net revenue after contractor pay is roughly $600–800M annualized at the $2B gross level (Bloomberg via TFN).
- **Distribution:** direct enterprise relationships with the top AI labs; brand from "youngest self-made billionaires" coverage; talent-side word of mouth and proactive offers (>50% of offers go to experts who never applied for the role, as of 2025).
- **Vertical expansion:** Deeptune acquisition (Jul 2026) adds RL environments where agents practice real workflows (hundreds of recreated enterprise apps, spreadsheets to Salesforce) — the stated goal is owning the full agent-training stack: environments, expert graders, and benchmarks (APEX).

## Growth

- **Core loop:** expert completes AI interview → structured verified profile enters the searchable pool → lab posts a project → matching algorithm shortlists → expert performs hours → performance data feeds back into ranking and interview scoring.
- **Supply flywheel:** more experts vetted → faster, cheaper fulfillment for labs → more lab demand → higher payouts → more experts apply. The AI interview removes the human-screening bottleneck that caps traditional staffing firms.
- **Benchmark as marketing:** APEX/APEX-Agents positions Mercor as the evaluator of AI capability, not just a data supplier — a thought-leadership wedge into every frontier lab.
- **Escalation path:** recruiting → RLHF/DPO data → agent training environments → benchmark standard. Each layer raises switching costs.

## UX

- **Expert-side entry:** upload resume → ~20-minute AI interview (half experience discussion, half live case study/coding) → verified profile with scores across dozens of parameters → matched to projects, often proactively.
- **Interview experience:** conversational voice AI over video; questions adapt to the resume and live answers; coding problems are generated dynamically with language-specific starter code; ~700ms median round-trip latency keeps it feeling human; three retake attempts (per community guidance, as of Jun 2026).
- **Lab-side UX:** natural-language search over the verified pool ("find me a cardiologist with RLHF experience") instead of job-board browsing; ranked shortlists; contracts, invoicing, and payroll inside one interface.
- **Retention mechanics:** recurring projects, proactive offers, and a portable profile that persists across applications — one interview gates all roles.

## AI

- **Monty, the AI interviewer:** ~10,000 interviews/day across hundreds of job categories; clusters assessments into skill types (Domain Expert ~2,800/day, Language ~750/day, Code ~600/day, Professional ~380/day — ~90% of volume).
- **Architecture specifics (as of 2025):** each session runs in an isolated container on Modal (~200 containers at peak, 80 floor, ~30 warm pre-booted) with <200ms session-startup latency; streaming end-to-end speech pipeline on Pipecat with Daily.co WebRTC, recorded to S3; automatic failover across commercial and open-source models at every stage (ASR, LLM, TTS); Smart-turn-v3 ONNX turn detection at ~150ms p50; ~700ms median silence-to-response, 900ms production threshold; blue-green config rollout over ~1 week.
- **Matching:** proprietary reinforcement-learning-style algorithms route experts to tasks; performance data from completed work refines future matching and interview scoring — a data flywheel where "who performs well" calibrates "who gets hired."
- **Evaluation layer:** APEX benchmarks grade AI agents against expert-human baselines drawn from the contractor database — AI capability evaluation as a product line.

## Architecture

- Vetting pipeline: resume parsing → adaptive AI interview → structured profile store (dozens of scored parameters)
- Matching/search layer: semantic search over verified profiles + ML routing
- Fulfillment: project management, contracts, invoicing, global payroll
- AI training operations: task queues for RLHF/DPO, expert grading, agent environment provisioning (Deeptune)
- Benchmark engine: APEX task suite + human reference scores
- Trust & security perimeter: identity checks, NDA/security reviews — and, after Mar 2026, a rebuilt supply-chain and contractor-credential layer (the LiteLLM incident exposed the cost of a weak one)

## Patterns

- Instantiates: [AI-Proctored Vetting](../../patterns/AI-Proctored-Vetting.md) (Monty credentializes the pool at machine scale), [Expert Judgment Marketplace](../../patterns/Expert-Judgment-Marketplace.md) (human intelligence sold as elastic expert-hours), [Trust-Evidence-Layer](../../patterns/Trust-Evidence-Layer.md) (verified profiles + APEX as checkable evidence — and the LiteLLM breach as the cautionary counter-example), [Suitability-Matching](../../patterns/Suitability-Matching.md) (experts are routed only to tasks within their verified skill categories), [Curation](../../patterns/Curation.md) (the platform owns the selection, not the catalog)
- Emerging pattern worth watching: **Benchmark-as-Positioning** (APEX converts an internal evaluation database into market-standard-setting)

## Lessons

1. **Vetting is the moat, not the matching.** Anyone can collect resumes; the AI interview's cost collapse is what lets Mercor vet 5M+ candidates and keep a 30K rotating pool liquid.
2. **Take-rate businesses need network effects on both sides.** Labs buy speed and quality; experts buy payouts and recurring work; the platform's fee is defensible only while both sides compound.
3. **Positioning matters: sell the bottleneck.** Mercor sells human judgment for post-training — the scarce input of the AI era — not "data labeling." That reframe explains a $20B valuation talk.
4. **Security is existential at marketplace scale.** One supply-chain compromise (LiteLLM, Mar 2026) cost Mercor its largest client and triggered class actions; a platform holding contractor credentials must treat its dependency graph as critical infrastructure.
5. **Gross vs net discipline:** the $2B "run rate" is gross billings; net revenue is ~30–40% of it. Evaluate the platform on take-rate-adjusted revenue.
6. **Founder-led narrative is a distribution asset** — youngest self-made billionaires, debate-team origin — but it also invites scrutiny (Foody's undisclosed angel stake in Deeptune ahead of the acquisition).

## Innovation

Mercor industrialized **AI-conducted credentialing at marketplace scale** — turning the interview from a one-time hiring step into a portable, reusable trust asset — and built the first large **expert-judgment marketplace** for the post-training era, with a benchmark (APEX) that positions it as the referee of AI capability. Its patterns transfer next to financial advisory (AI-proctored advisor credentialing, see [AI-Proctored Vetting → Investment Advisory](../../cross-domain/AI-Proctored-Vetting-to-Investment-Advisory.md)), legal services, and healthcare second opinions — any domain where verified human judgment is the scarce input.

## Sources

1. TechCrunch — Series B at $2B, founding, 20-minute AI interview, $75M ARR (Feb 2025): https://techcrunch.com/2025/02/20/mercor-an-ai-recruiting-startup-founded-by-21-year-olds-raises-100m-at-2b-valuation/
2. Tech Funding News — $20B valuation talks, Deeptune, LiteLLM breach, $2B run-rate caveats, 5M candidates vetted (Jul 2026): https://techfundingnews.com/mercor-20b-valuation-talks-deeptune-acquisition/
3. 36Kr / 硅兔赛跑 — $10B Series C, take rate 30–35%, $4M+ daily payouts, 30K experts (Jul 2026): https://www.36kr.com/p/3904682268034947
4. AI Wiki — Monty technical architecture, funding table, APEX, take-rate 30–40%, >$85/hr average pay (compiled May 2026): https://aiwiki.ai/wiki/mercor
5. KuCoin/The Information — H1 2026 $614M gross revenue, 90% from AI model firms, $2B run rate (Jul 2026): https://www.kucoin.com/news/flash/mercor-hits-2b-annualized-run-rate-in-ai-human-feedback-services
6. Forbes — 300,000 candidates vetted, 20-minute AI interview mechanics, $250M valuation (Sep 2024): https://www.forbes.com/sites/alexkonrad/2024/09/18/mercor-ai-interviewer-reaches-250-million-valuation/
7. Mercor Talent Docs — AI interview process and evaluation (as of Feb 2026): https://talent.docs.mercor.com/support/ai-interview
