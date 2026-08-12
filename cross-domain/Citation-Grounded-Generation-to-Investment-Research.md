---
id: citation-grounded-generation-to-investment-research
type: cross-domain
name: Citation-Grounded Generation → Investment Research
source_domain: AI Search & Answer Engines
target_domain: Investment Research & Due Diligence
source_pattern: patterns/Citation-Grounded-Generation.md
status: hypothesis
last_updated: 2026-08-12
---

# Citation-Grounded Generation → Investment Research

## Source

Perplexity industrialized citation-grounded generation: every answer claim carries a numbered, checkable source, enforced by the retrieval→synthesis pipeline. Google AI Overviews, ChatGPT Search, and You.com/Bing Copilot adopted the same contract. The mechanism: **an output is not finished until every material claim points to a source the user can open.**

## Pattern

Abstracted: in any domain where claims are the product and verification is cheap relative to the cost of being wrong, make **claim → source → as-of-date** a mandatory output contract. The consumer verifies; the producer is disciplined by the constraint; trust becomes checkability instead of authority.

## Transfer

- **Transfers:** per-claim source links; "as of" dating on volatile facts; visible "no source" state instead of silent confidence; user verification as feedback.
- **Adapts:** sources become filings, databases, primary interviews, and audited statements instead of web pages; the "user" is an analyst or investment committee member; freshness is per-datapoint (NAV monthly, reserves annually, news daily).
- **Fails:** pure judgment claims (fair-value opinions, management quality) have no single source — the pattern must allow "judgment, based on sources X, Y, Z" rather than fake-precise citations.

## Example

An AI investment-research assistant that drafts an IC memo with every number linked: "EBITDA $12.4M (source: FY2025 FS, p.14, as of 2026-03-31)" and every qualitative claim linked to an interview note or public filing; a claim with no source is auto-flagged as **unsupported** rather than silently asserted. The committee reviews evidence density ("what share of material claims are sourced?") as a quality gate before any deal decision. Perplexity's own evaluation of agents (APEX-style) suggests such a tool is feasible: agents complete a minority of professional tasks on first attempt, so the citation gate doubles as the agent's safety rail.

## Future

The natural next step is **spec-driven research**: the memo is written as a spec (claims required, evidence required, acceptance criteria) and agents must satisfy it — combining Citation-Grounded Generation with Spec-Driven Development. Regulated asset managers and due-diligence teams are the first buyers; a "citation coverage ratio" becomes a standard research KPI.

## Risks

- Citation theater in finance is fraud-adjacent: a link that doesn't support the claim is materially worse than no link — enforcement must be real
- Stale financial evidence (an "as of" date on a number that has since moved) misleads committees; freshness policies are non-negotiable
- Sources can be gamed (paywalled, taken down, selectively cited); an archive layer is required
- Over-reliance: citation density is a quality proxy, not a quality guarantee — it cannot replace human judgment on valuation and judgment calls
