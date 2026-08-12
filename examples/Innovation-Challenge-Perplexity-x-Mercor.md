# Innovation Challenge — Perplexity × Mercor

**Daily Challenge #003** · 2026-08-12

Patterns abstracted:

- **Perplexity:** citation-grounded generation (every claim links to a source), subscription-first trust (ads killed Feb 2026), answer-as-finished-artifact (virality), model routing across frontier models, agent orchestration (Computer, 20 models), browser-as-distribution (Comet), local agent appliance (Personal Computer), API platform (Search/Agent/Embeddings/Sandbox), enterprise trust perimeter (SOC 2, private index).
- **Mercor:** AI-proctored vetting (Monty, machine-speed credentialing), expert-judgment marketplace (elastic expert-hours sold to AI labs), benchmark-as-positioning (APEX), portable verified credential (one interview gates all roles), take-rate marketplace economics (30–40%), performance-data flywheel (work quality recalibrates ranking), security-critical trust perimeter (LiteLLM breach as counter-example).

## 20 Innovations

### Build & Automate

1. **Interview-as-Research** — when a Perplexity answer needs deep or niche context, it dispatches a Mercor-vetted domain expert for a live AI-proctored interview and cites the verified transcript in the answer — search that calls people. [Expert-judgment-marketplace × Citation-grounded-generation]
2. **Agent Audit Bench** — Perplexity Computer agents are graded by Mercor's expert pool on real web tasks; every agent action gets an evidence trail and an expert score, published as a public leaderboard. [Benchmark-as-positioning × Agent-orchestration]
3. **Model Router with Expert Taste** — instead of cost-only routing, queries route by APEX-style expert quality scores per task family; the router learns which model humans trust per domain. [Benchmark-as-positioning × Model-routing]
4. **Credentialed Answer Feeds** — enterprise Perplexity instances ground answers only in company docs plus Mercor-verified experts, with each answer carrying an expert credential badge. [Citation-grounding × Portable-credential]
5. **Skill Verification Browser** — Comet browsing sessions become evidence: an expert's real research work (queries, sources vetted, synthesis) auto-builds a portable verified portfolio. [AI-proctored-vetting × Browser-as-distribution]

### Enterprise & Ops

6. **Dual-Authority Answers** — for money- or legal-stakes queries, answers require a second signature from a vetted domain expert who takes accountability; "co-signed AI" for regulated teams. [Expert-judgment × Trust-evidence-layer]
7. **Secure Research Agents for Regulated Firms** — Computer agents run inside SOC 2 perimeters with Mercor-vetted human oversight; every research claim is auditable end-to-end. [Trust-evidence × Agent-orchestration]
8. **Vetting-as-a-Service API** — Mercor's AI interview embedded in Perplexity enterprise onboarding: every employee gets a verified knowledge profile that personalizes and gates internal answers. [AI-proctored-vetting × Enterprise-search]
9. **Source-Rating Layer** — Mercor experts curate and rate the sources in Perplexity's index per domain; retrieval ranks citation quality by expert reputation, not just page rank. [Curation × Citation-grounding]
10. **Publisher Compensation as Trust** — Perplexity shares subscription revenue with publishers, with Mercor-style independent auditing of attribution — licensing as a trust feature, not a legal defense. [Subscription-first × Evidence-layer]

### Talent & Knowledge

11. **Hiring by Answer Traces** — candidates' public Perplexity research trails (how they search, what they cite, how they synthesize) become vetting evidence for recruiters evaluating real skills. [AI-proctored-vetting × Query-history]
12. **Expert-on-Demand Pro Search** — a Pro answer can escalate to a live expert consult; the transcript becomes a cited, reusable artifact in the answer's evidence layer. [Expert-judgment × Answer-artifact]
13. **Answer Quality Index** — a public benchmark ranking answer engines by expert-judged factual accuracy, run by Mercor's independent expert pool — APEX for search. [Benchmark-as-positioning × Citation-grounding]
14. **Expert-Curated Collections** — Mercor experts curate Perplexity Collections for specialized domains (M&A, clinical trials); users subscribe to expert-curated answer sets. [Curation × Persistent-context]
15. **Credentialed Follow-up Network** — follow-up answers can be routed to the specific expert who authored the cited source, turning citations into a human knowledge graph. [Expert-judgment × Citation-graph]

### Money & Distribution

16. **Incentivized Citation Authorship** — experts whose published sources are heavily cited in answers earn revenue share; the citation graph becomes a pay-per-answer economy. [Expert-judgment × Citation-grounding]
17. **Agent Employment Records** — Computer agents get Mercor-style task-battery vetting before handling money tasks; certified agents command premium usage pricing. [AI-proctored-vetting × Agent-orchestration]
18. **Benchmark-Linked Agent Pricing** — enterprise Computer plans price by agent certification tier, backed by the public audit leaderboard — "licensed agents, not rented black boxes." [Benchmark-as-positioning × Usage-based-pricing]
19. **Verified Knowledge Marketplace** — experts sell bounded knowledge units (verified answers, analyses, courses) on a marketplace where every unit carries its own citation and credential chain. [Portable-credential × Answer-artifact]
20. **Take-Rate Transparency Engine** — Mercor-style marketplace take rates applied to expert-answer commerce, with independent evidence of what experts actually earn — trust as the marketplace moat. [Marketplace-economics × Trust-evidence-layer]

## Evaluation — Top 5

| # | Concept | User value | Feasibility | Moat | Timing | Risk | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Interview-as-Research | 5 | 4 | 5 | 5 | 3 | 22 |
| 2 | Agent Audit Bench | 4 | 4 | 5 | 5 | 3 | 21 |
| 13 | Answer Quality Index | 4 | 4 | 5 | 5 | 2 | 20 |
| 7 | Secure Research Agents | 5 | 4 | 4 | 4 | 3 | 20 |
| 16 | Incentivized Citation Authorship | 4 | 3 | 5 | 4 | 3 | 19 |

## Winner — Interview-as-Research

- **Target user:** knowledge workers (analysts, researchers, journalists, due-diligence teams) who need answers beyond what the indexed web contains — niche, live, judgment-heavy topics.
- **Core loop:** query → Perplexity grounds the answer → detects a knowledge gap → dispatches a Mercor-vetted expert → AI-proctored live interview → expert transcript becomes a cited source → answer updated with "expert-sourced" evidence → expert earns, platform takes a fee, answer improves for everyone.
- **The one metric:** expert-cited answer rate — share of answers containing at least one live-expert source, as a proxy for "search that reaches human knowledge."
- **Pattern stack:** [Expert Judgment Marketplace](../patterns/Expert-Judgment-Marketplace.md) (elastic expert-hours) + [Citation-Grounded Generation](../patterns/Citation-Grounded-Generation.md) (the evidence contract) + [AI-Proctored Vetting](../patterns/AI-Proctored-Vetting.md) (credentialing the expert pool at scale).
- **First 90 days:** gap detection on high-traffic niche queries → interview pilot with 100 vetted experts in 3 domains → citation schema for interview transcripts → pricing pilot (answer-level expert fee) → publisher-style disputes and trust guardrails before scale.
- **Key risk (mitigation):** interview quality and latency → AI-proctored interviews keep cost/latency bounded (Mercor's Monty runs ~10K interviews/day), and "expert-sourced" answers are marked with the same as-of/verification metadata as web citations, so the evidence layer never degrades.
