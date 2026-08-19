---
id: speko
type: product
name: Speko
category: AI
company: Speko (San Francisco)
founded: 2026
status: active
tags: [voice-ai, model-router, benchmarks, stt, tts, llm, gateway, yc, api]
last_updated: 2026-08-19
sources:
  - https://speko.ai/
  - https://news.ycombinator.com/item?id=49332751
  - https://www.ycombinator.com/companies/speko
  - https://runtimewire.com/article/speko-voice-ai-router-language-benchmarks
  - https://runtimewire.com/article/speko-launches-benchmark-router-voice-ai-models
  - https://topaiproduct.com/2026/08/17/speko-yc-s26-openrouter-for-voice-ai-61-models-benchmarked-usage-up-25-a-week/
  - https://github.com/SpekoAI/gateway
  - https://www.ic.work/article/speko-voice-ai-router-benchmark-trust
  - https://aiproducthub.cn/launch/p/25580.html
  - https://pivot.uz/uzbek-founded-speko-launches-ai-voice-routing-platform-after-joining-y-combinator/
  - https://www.npmjs.com/package/@spekoai/sdk
---

# Speko

## Overview

Speko is a San Francisco-based voice AI routing layer (YC Summer 2026) that sits in front of the three-stage voice stack — speech-to-text (STT), LLM, text-to-speech (TTS) — and routes each leg to the model it measured as best for the caller's language and objective (accuracy, latency, cost, or balanced), behind one OpenAI-compatible API key ([speko.ai](https://speko.ai/), as of 2026-08-19). It was founded by Beknazar "Bek" Abdikamalov, who spent four years running the same benchmark-then-switch ritual by hand at Hupo for enterprise voice deployments in 10+ languages ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17). Its one-sentence mechanism: **"we measure, then we route" — continuously updated, language-by-language public benchmarks are the control plane, and the leaderboard is simultaneously the trust layer and the acquisition engine** ([YC profile](https://www.ycombinator.com/companies/speko), 2026-08).

## History

- **2019** — Abdikamalov begins working in voice technology; engineering roles include Tridge and Amazon before founding his own company ([Digital Business via RuntimeWire](https://runtimewire.com/article/speko-voice-ai-router-language-benchmarks), 2026-08-16).
- **2022** — Co-founds Ami (later renamed Hupo), a Singapore leadership-coaching platform, with Justin Kim; Hupo raises ~$4M from backers YC identifies as including DST Global, Meta, Goodwater Capital, and Collaborative Fund ([RuntimeWire](https://runtimewire.com/article/speko-voice-ai-router-language-benchmarks), 2026-08-16).
- **2026 (pre-YC)** — Speko raises $1.1M from US funds and angels before joining YC; founder reports production voice work at Hupo for clients including Morgan Stanley, Prudential, HSBC, and Grab ([Digital Business via RuntimeWire](https://runtimewire.com/article/speko-voice-ai-router-language-benchmarks), 2026-08-16; [YC profile](https://www.ycombinator.com/companies/speko), 2026-08).
- **2026-06** — Speko joins Y Combinator's Summer 2026 batch; YC's standard $500K via two safes brings the reported raised-or-committed total to ~$1.6M; YC profile lists team size 4, primary partner Tyler Bosmeny ([RuntimeWire](https://runtimewire.com/article/speko-voice-ai-router-language-benchmarks), 2026-08-16; [YC profile](https://www.ycombinator.com/companies/speko), 2026-08).
- **2026-06-27** — TypeScript SDK `@spekoai/sdk` published on npm with transcription/agent helpers ([npm](https://www.npmjs.com/package/@spekoai/sdk), 2026-06-27).
- **2026-07-28** — Enters public preview with three self-service price points: $100 signup credit, a router plan charging 5% above the underlying provider rate, and a Speko-hosted infrastructure plan at $0.09/minute ([RuntimeWire](https://runtimewire.com/article/speko-launches-benchmark-router-voice-ai-models), 2026-07-28).
- **2026-08-02** — Uzbek press covers the YC Summer 2026 acceptance and the product unveiling: continuous benchmarking across WER, finalize latency, time to first token, and cost per minute ([Pivot.uz](https://pivot.uz/uzbek-founded-speko-launches-ai-voice-routing-platform-after-joining-y-combinator/), 2026-08-02).
- **2026-08-17** — "Launch HN: Speko (YC S26) – OpenRouter for Voice AI" reaches the HN front page (90 points, 51 comments at crawl time); founder post details the benchmark pipeline, prefetched session plans, failover, open-source gateway, and BYOK mode ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17T15:36Z).
- **2026-08-17** — Launch coverage reports 61 voice models benchmarked across 10 languages and usage up ~25% per week since late June, with the Stripe/OpenRouter deal (~$7B+) framing the category ([Top AI Product](https://topaiproduct.com/2026/08/17/speko-yc-s26-openrouter-for-voice-ai-61-models-benchmarked-usage-up-25-a-week/), 2026-08-17).
- **2026-08-18** — Chinese industry analysis publishes the key critique: public quantified comparisons cover only the STT stage; test-set provenance, concurrency behavior, and failover data are not disclosed ([ic.work](https://www.ic.work/article/speko-voice-ai-router-benchmark-trust), 2026-08-18).

## Target User

Primary user is the **voice-agent developer**: teams building phone agents, customer support, property-management and medical intake systems that currently hand-pick an STT + LLM + TTS stack and freeze it. The founder's HN post cites concrete buyers: a founder who "did not know what to pick at all," a property-management AI on LiveKit that had not updated STT/TTS since launch, a team unsure which models work for Spanish, and a medical team needing STT that handles medical vocabulary ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17). Payer and user are the same developer team in API plans (usage-based), while the end-callers are the developer's own customers. YC provides a concentrated early pool of startups building voice products ([RuntimeWire](https://runtimewire.com/article/speko-voice-ai-router-language-benchmarks), 2026-08-16).

## Business

Usage-based infrastructure pricing, as of 2026-07-28: **router plan** = 5% fee above the upstream provider's public rate; **hosted infrastructure plan** = $0.09/minute covering STT + LLM + TTS; **$100 signup credit**; BYOK mode via the open-source gateway is free of Speko routing fees ([RuntimeWire](https://runtimewire.com/article/speko-launches-benchmark-router-voice-ai-models), 2026-07-28; Chinese pricing write-up confirms $0.09/min bundled billing and the +5% router fee, [aiproducthub.cn](https://aiproducthub.cn/launch/p/25580.html), 2026-08-17). Revenue and customer counts are not public as of 2026-08-19; the founder reports usage up ~25% per week since late June ([Top AI Product](https://topaiproduct.com/2026/08/17/speko-yc-s26-openrouter-for-voice-ai-61-models-benchmarked-usage-up-25-a-week/), 2026-08-17). Reported funding ~$1.6M (pre-YC $1.1M + YC $500K) ([RuntimeWire](https://runtimewire.com/article/speko-voice-ai-router-language-benchmarks), 2026-08-16). Distribution: HN launch, public benchmark site, LiveKit documentation/integration, npm/PyPI SDKs, and the YC network — no paid marketing observed.

## Growth

The primary loop is **benchmark-as-acquisition**: developers evaluating voice providers land on the public boards before choosing a vendor; each new model release becomes a fresh comparison and a reason to re-engage; teams that route through Speko get automatic re-routing when the numbers change, so they never have to run the bake-off again ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17; [RuntimeWire](https://runtimewire.com/article/speko-voice-ai-router-language-benchmarks), 2026-08-16). The second loop is **honest-loss publication**: the boards include cases where Speko's own selections perform worse than alternatives, which is positioned as the credibility that makes the paid router trustworthy ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17). The third loop is **integration-led growth**: because Speko speaks the OpenAI API and documents a LiveKit adapter, existing voice-agent projects can switch with a base-URL and model-string change, converting the incumbent stack into the cheapest possible entry point ([speko.ai](https://speko.ai/), as of 2026-08-19).

## UX

Entry experience: keep the framework you already use; change base URL to `https://api.speko.ai/v1`, set the Speko API key, and pass `model: 'auto'` for STT, LLM, and TTS ([speko.ai](https://speko.ai/), as of 2026-08-19). Core loop: developer sends a request with optimization criteria (accuracy, latency, cost, balanced), language and region → the router filters to models measured for that combination, selects the winner, and returns the response with headers naming provider, model, and scores — the routing decision is visible, not black-box ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17). Failover happens during connection setup: if the provider refuses the connection, Speko connects to runners-up ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17). Operational UX is a dashboard where a team "can literally go to this dashboard, switch the model, and it will do it for us" (customer quote in [Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17).

## AI

Speko does not train or sell models — impartial measurement is the positioning: "We don't train or sell models ourselves, that's precisely how we keep our rankings impartial" ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17). Measurement stack: WER, finalize latency, time to first token, and cost per minute, benchmarked language by language (English, Arabic, French, German, Hindi, Norwegian, Spanish, Tamil, Telugu, and more), with 61 models across 10 languages as of the 2026-08-17 launch coverage ([RuntimeWire](https://runtimewire.com/article/speko-voice-ai-router-language-benchmarks), 2026-08-16; [Top AI Product](https://topaiproduct.com/2026/08/17/speko-yc-s26-openrouter-for-voice-ai-61-models-benchmarked-usage-up-25-a-week/), 2026-08-17). Speko trained an automatic TTS-naturalness scorer on blind head-to-head listening votes; on providers it has never seen votes for, it picks the same winner as human raters about as often as raters agree with each other ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17). The measurement surface is public at benchmarks.speko.ai, updated with dated runs ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17). Data flywheel: routed traffic generates anonymous timing/error telemetry that improves routing and benchmark confidence (opt-out via `SPEKO_TELEMETRY_DISABLED=true`; [gateway README](https://github.com/SpekoAI/gateway), as of 2026-08-19).

## Architecture

Two-plane architecture ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17; [gateway README](https://github.com/SpekoAI/gateway), as of 2026-08-19): a **hosted control plane** (benchmark pipeline, routing/plan signing, credential broker, consolidated billing, and the `relay.speko.dev` relay for LLM legs) plus an **open customer-side data plane** — the MIT-licensed Speko Gateway, a single Go binary run as a sidecar in the agent's container, speaking a local Unix-socket protocol. Key mechanics: **prefetched signed session plans** — a warm pool of signed plans means a new session dials the provider straight from memory, with no control-plane round trip on the path a caller waits on; **BYOK mode** — provider credentials stay inside the Gateway process, pinned to official provider host allowlists over TLS:443, and traffic can bypass Speko entirely; **provider adapters** for 20+ vendors (Deepgram, ElevenLabs, OpenAI, AssemblyAI, Cartesia, Hume, xAI, Google, Alibaba, MiniMax, etc.); **fail-closed option handling** — a session routed to a provider that cannot honor a canonical ask is refused at create time rather than silently degraded. The public wire contract for the relay lives in the repo as OpenAPI + AsyncAPI ([gateway README](https://github.com/SpekoAI/gateway), as of 2026-08-19).

## Patterns

- [Benchmark-Driven-Routing](../../patterns/Benchmark-Driven-Routing.md) — the canonical instance: production voice traffic routed by continuously re-measured, language/objective-specific benchmarks rather than static selection or vendor leaderboards (filed 2026-08-19).
- [Open-Protocol-Ecosystem](../../patterns/Open-Protocol-Ecosystem.md) — the "open client, closed control plane" variant: MIT gateway + OpenAI-compatible API remove integration friction and disarm the new-middleman objection, while benchmarks and billing stay with Speko.
- [Trust-Evidence-Layer](../../patterns/Trust-Evidence-Layer.md) — public boards including losing cases are the trust product; benchmark credibility, not model capability, is the commercial moat ([ic.work](https://www.ic.work/article/speko-voice-ai-router-benchmark-trust), 2026-08-18).
- [Context-Economy-Engineering](../../patterns/Context-Economy-Engineering.md) — prefetched signed session plans spend memory to save the caller-facing latency of a control-plane round trip; warm-route prefetching covers the first session after deploy.

## Lessons

Copy: **make the measurement the moat** — in a churning multi-vendor layer, the continuously updated benchmark is more valuable than any single model pick; **publish the losses** — honest boards (including where your router picked wrong) are the cheapest credibility engine for an intermediary whose whole job is to be trusted; **open the consumer-side runtime** — an MIT gateway with BYOK mode answers "you're just another middleman" by giving the customer the ability to run the data plane themselves; **zero-config default** — `model: 'auto'` converts an evaluation product into a drop-in infrastructure change. Avoid: **closed methodology** — publishing only STT scores while withholding test-set provenance, concurrency, and failover data invites the "self-serving leaderboard" critique ([ic.work](https://www.ic.work/article/speko-voice-ai-router-benchmark-trust), 2026-08-18); **default-on telemetry** — anonymous telemetry on by default (even in BYOK mode) needs loud disclosure or it becomes a trust liability; **becoming the new lock-in** — a gateway that routes everything is a new binding point, and developers will demand manual pin/override plus BYOK as the escape hatch.

## Innovation

Speko industrialized **evaluation-as-infrastructure for real-time voice**: the bake-off that serious voice teams ran by hand — hire native raters, benchmark against the existing stack, update production if it improved — became an API, with routing as the automatic consequence of measurement ([Launch HN](https://news.ycombinator.com/item?id=49332751), 2026-08-17). It also shows the **warm-plan prefetch** trick for making a router invisible on a latency-critical path, and the **open-client/closed-control-plane** split that lets an intermediary monetize measurement without owning the data plane. Natural next transfers: routing for other multi-stage agent pipelines (vision+language+action), enterprise model procurement, cloud region/carrier selection, and investment research where fund selection is the same "benchmark once, freeze, drift" failure (see [Benchmark-Driven Routing → Investment Research](../../cross-domain/Benchmark-Driven-Routing-to-Investment-Research.md)).

## Sources

1. [Speko homepage — The Router for Voice AI (as of 2026-08-19)](https://speko.ai/)
2. [Launch HN: Speko (YC S26) – OpenRouter for Voice AI (2026-08-17)](https://news.ycombinator.com/item?id=49332751)
3. [YC directory — Speko profile (2026-08)](https://www.ycombinator.com/companies/speko)
4. [RuntimeWire — Speko routes voice AI across providers using language-specific benchmarks (2026-08-16)](https://runtimewire.com/article/speko-voice-ai-router-language-benchmarks)
5. [RuntimeWire — Speko launches benchmark-based router; pricing preview (2026-07-28)](https://runtimewire.com/article/speko-launches-benchmark-router-voice-ai-models)
6. [Top AI Product — 61 models benchmarked; usage up 25% a week (2026-08-17)](https://topaiproduct.com/2026/08/17/speko-yc-s26-openrouter-for-voice-ai-61-models-benchmarked-usage-up-25-a-week/)
7. [GitHub — SpekoAI/gateway (MIT) (as of 2026-08-19)](https://github.com/SpekoAI/gateway)
8. [ic.work — 自称「语音版OpenRouter」，Speko真正要闯的关是测评可信度 (2026-08-18)](https://www.ic.work/article/speko-voice-ai-router-benchmark-trust)
9. [aiproducthub.cn — Speko 定价与路由费 (2026-08-17)](https://aiproducthub.cn/launch/p/25580.html)
10. [Pivot.uz — Uzbek-founded Speko joins YC; product unveiling (2026-08-02)](https://pivot.uz/uzbek-founded-speko-launches-ai-voice-routing-platform-after-joining-y-combinator/)
11. [npm — @spekoai/sdk (2026-06-27)](https://www.npmjs.com/package/@spekoai/sdk)
