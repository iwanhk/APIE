# Innovation Challenge — Speko × Perplexity

**Daily Challenge #010** · 2026-08-19

Patterns abstracted:

- **Speko (YC S26):** benchmark-driven routing ("we measure, then we route" — language/objective-specific STT/LLM/TTS scores, public boards including losing cases), one-key multi-provider gateway (OpenAI-compatible, drop-in), per-request objective decomposition (accuracy / latency / cost / balanced), prefetched signed session plans (zero control-plane round trip on the caller path), failover at connection setup, open consumer-side gateway with BYOK mode (trust by escape hatch), automatic quality scorer grounded in human head-to-head votes, usage-skim pricing (5% router fee / $0.09 per minute hosted).
- **Perplexity:** citations-first answer engine (answer + proof), search compressed into a cited answer, subscription-first monetization (ads deliberately killed Feb 2026), Sonar API usage pricing, Computer agent orchestrating up to 20 frontier models, Comet browser as a new default surface, enterprise tiers (SOC 2, private index), publisher revenue share.

## 20 Innovations

### Voice Answer Engines

1. **Language-Native Voice Search** — a Perplexity voice answer routed per language to the best-measured STT/LLM/TTS stack for that language, so a Hindi caller never runs on an English-optimized pipeline; the router's language boards are the feature. [Benchmark-driven-routing × Citation-grounded-generation]
2. **Citation in the Voice Channel** — every spoken answer returns provenance headers (source list, model IDs, scores) so the app can display or replay citations in real time; the citation lives next to the audio, not buried in a transcript. [Citation-grounded-generation × Benchmark-driven-routing]
3. **The Answer Ledger** — each voice answer ships as a replayable artifact: audio, transcript, sources, model stack, latency and cost — a session-as-artifact for spoken answers, exportable for audits, education, and compliance. [Session-as-Artifact × Trust-evidence-layer]
4. **Per-Query Router** — the user declares the objective on every query ("fast", "cheap", "deep"); the router picks the model stack per query instead of per account — cost mode for battery and budget, research mode for depth. [Benchmark-driven-routing × Effort-based-pricing]
5. **Honest-Benchmark Feed** — a public "we got this one wrong" feed where Perplexity publishes answers that underperformed and what today's router would do instead — failure as a subscription-worthy trust product. [Trust-evidence-layer × Benchmark-driven-routing]
6. **Voice Deep Research Agent** — Perplexity Computer's 20-model orchestration becomes a routed multi-leg pipeline: best STT for the user's accent, best reasoning model per question type, best TTS for the final read-out, all selected from live benchmarks — a swarm where every leg is routed. [Parallel-agent-orchestration × Benchmark-driven-routing]

### Provenance & Trust

7. **Router Health Page** — enterprise-grade visibility: which models served which queries, failover incidents, score drift, and benchmark methodology — the evidence layer for procurement and compliance reviews. [Trust-evidence-layer × AI-Proctored-vetting]
8. **Live Fact-Check Loop** — claims in the voice answer are scored against source consensus in real time; low-confidence answers automatically drop to a slower, deeper reasoning leg — failover applied to confidence, not just connections. [Trust-evidence-layer × Benchmark-driven-routing]
9. **Regional Voice Profiles** — routing per region and regulatory domain: GDPR-hosted models, on-device STT for sensitive audio, jurisdiction-scoped sources — compliance tiers as routing constraints. [Capability-gated-release × Benchmark-driven-routing]
10. **Mandate Profiles** — users pick a mandate (student, clinician, trader, caregiver) and the router optimizes vocabulary, latency, and depth accordingly — suitability matching expressed as routing criteria. [Suitability-matching × Benchmark-driven-routing]
11. **Query Memory Routing** — ambient memory of prior queries tunes the objective: a user who always asks follow-ups gets low-latency stacks; a user who never re-asks gets accuracy-first stacks — memory as a routing input. [Memory × Benchmark-driven-routing]
12. **Voice Q&A Streaks** — users confirm or correct spoken answers; corrections feed the router's per-language, per-domain scores, and streak mechanics reward users who verify — gamified measurement. [Recommendation × Benchmark-driven-routing]

### Developer & Infrastructure

13. **Router API for Developers** — expose Speko-style benchmark-driven routing as a Perplexity API product: one key, drop-in OpenAI-compatible endpoints, per-routed-minute pricing like Sonar — Perplexity's measurement layer becomes the voice-agent developer's control plane. [Effort-based-pricing × Benchmark-driven-routing]
14. **BYOK Research Gateway** — enterprises bring their own model keys and data plane (Speko-style open gateway) while Perplexity supplies measurement and routing; sensitive queries never leave the customer's infra — the escape hatch is the enterprise sales pitch. [Open-protocol-ecosystem × Trust-evidence-layer]
15. **Skill-based Answer Packs** — installable answer skills (tax, medical vocabulary, code) each ship with their own benchmark board; the marketplace is the router, and routing per skill is the discovery mechanism. [Agent-skill-marketplace × Benchmark-driven-routing]
16. **Spec-Driven Answer Contracts** — enterprise teams declare answer specs (sources allowed, latency, language, citation format) and the router treats the spec as routing constraints, with conformance reports per query. [Spec-driven-development × Benchmark-driven-routing]
17. **LiveKit-Native Comet Voice** — the Comet browser gets a voice mode where the router selects the best real-time speech stack for browsing-by-voice; the browser becomes the default surface for the routed voice answer engine. [Benchmark-driven-routing × Context-economy-engineering]

### Monetization & Ecosystem

18. **Publisher Voice Share** — the publisher revenue share extends to voice: when a spoken answer reads a publisher's content, the TTS leg can use the publisher's branded voice and earn attribution — citation economics meets voice branding. [Citation-grounded-generation × Open-protocol-ecosystem]
19. **Answer SLA Tiers** — per-query SLA pricing: "guaranteed 3-second voice answer" vs. "deep research, minutes allowed" — capability-gated release monetized like Comet's Max tier. [Capability-gated-release × Effort-based-pricing]
20. **The Spoken Digest** — a daily routed brief where the router picks the best TTS voice per topic and the best model depth per section, with a shareable "my listening profile" for retention — Wrapped mechanics over a routed pipeline. [Recommendation × Benchmark-driven-routing]

## Evaluation — Top 5

| # | Concept | User value | Feasibility | Moat | Timing | Risk | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | Voice Deep Research Agent | 5 | 4 | 5 | 5 | 2 | 21 |
| 13 | Router API for Developers | 5 | 4 | 5 | 5 | 3 | 22 |
| 2 | Citation in the Voice Channel | 5 | 4 | 4 | 5 | 2 | 20 |
| 8 | Live Fact-Check Loop | 4 | 3 | 5 | 4 | 3 | 19 |
| 3 | The Answer Ledger | 4 | 4 | 4 | 4 | 2 | 18 |

## Winner — Router API for Developers

- **Target user:** voice-agent developers who need Perplexity-grade research but don't want to manage model selection — the same teams Speko courts, plus Perplexity's existing Sonar API developers who want voice without building a voice stack.
- **Core loop:** developer calls the Router API with an objective (accuracy / latency / cost / balanced) and a language → the router selects the best-measured STT/LLM/TTS stack, executes the research, and returns audio + citations + routing headers (provider, models, scores) → the developer's voice agent answers with provenance → answer outcomes and corrections flow back into the benchmark pipeline → scores update and future routing improves. Measurement compounds; the developer never re-benchmarks.
- **The one metric:** routed-answer acceptance rate (share of voice answers the developer's users accept without correction), benchmarked against static-stack baselines; secondary: routing-change-to-quality correlation (do score-driven switches actually improve outcomes) and per-minute margin on routed traffic.
- **Pattern stack:** [Benchmark-Driven-Routing](../patterns/Benchmark-Driven-Routing.md) (the measurement surface is the moat) + [Effort-Based-Pricing](../patterns/Effort-Based-Pricing.md) (per-routed-minute pricing meters the value) + [Citation-Grounded-Generation](../patterns/Citation-Grounded-Generation.md) (research answers with sources) + [Open-Protocol-Ecosystem](../patterns/Open-Protocol-Ecosystem.md) (drop-in OpenAI-compatible surface + BYOK gateway as the trust escape hatch) + [Session-as-Artifact](../patterns/Session-as-Artifact.md) (routing headers and answer ledgers make every call auditable).
- **First 90 days:** ship the Router API as a Sonar add-on — one key, `model: 'auto'`, OpenAI-compatible endpoints → publish per-language boards including losing picks and open the BYOK gateway → onboard 50 voice-agent teams from the LiveKit ecosystem in private beta and measure routed-answer acceptance vs. their previous stacks → add per-query objective headers and the Answer Ledger export → price at Sonar-style usage plus a small routing skim, and let the honest-loss board double as the marketing engine.
