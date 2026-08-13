---
id: ai-proctored-vetting-to-investment-advisory
type: cross-domain
name: AI-Proctored Vetting → Investment Advisory
source_domain: AI Talent Marketplace / Certification
target_domain: FinTech / Investment Advisory
source_pattern: patterns/AI-Proctored-Vetting.md
status: hypothesis
last_updated: 2026-08-09
---

# AI-Proctored Vetting → Investment Advisory

## Source

AI talent marketplaces proved that **AI-conducted evaluation can credential human capability at machine scale**. Mercor's Monty interviewer vets ~10,000 candidates a day and turns each session into a portable verified profile that gates a 30,000-contractor marketplace; Duolingo English Test industrializes the same idea in certification — an adaptive, AI-proctored exam that undercuts incumbent credentials on cost and latency. In both cases the mechanism is identical: standardized adaptive evaluation → structured portable credential → trust that transfers across transactions.

## Pattern

**AI-proctored vetting:** a machine conducts a standardized, adaptive evaluation; the output is a reusable trust asset (credential/score) that gates access to opportunities; downstream performance data calibrates the evaluation. The pattern's leverage comes from credential *reuse* — one evaluation amortized across many transactions — and from *portability* — the credential travels with the person, not with a single employer or platform.

## Transfer

- **Transfers directly:** the adaptive interview format (resume-driven questions + live case studies), the skill-cluster rubric design (domain expert / professional / language), the calibration loop (credential → downstream performance), and the proactive-matching mechanic (pre-vetted supply matched to demand without re-screening).
- **Needs adaptation:** evaluation content — an advisor's "case study" must test suitability process, regulatory knowledge (KYC, suitability rules), and product mechanics, not code; the credential must be auditable by regulators, not just by the platform.
- **Fails without:** independent oversight. In talent markets the platform owns the credential; in regulated advice, a third party (regulator or accredited body) must be able to inspect the evaluation design, the rubric, and the adverse-impact analytics. Pure black-box scoring is a regulatory non-starter (see HireVue's 2021 retreat).

## Example

**"Advisor Verified" — an AI-proctored credentialing layer for constrained-advice platforms.** A platform for professional investors (or a fund-education product with advisory features) requires every advisor who appears on the network to complete a ~30-minute AI-proctored evaluation: adaptive questions on suitability process, fee structures, product mechanics, and a live "client interview" case study where the AI plays a novice investor. Output: a verified advisor profile scored on competency, communication, and regulatory discipline, with an evidence trail of the full session. The credential is portable — an advisor keeps it across firms — and the platform matches advisors to investors only within each advisor's verified scope. Every recommendation carries the credential link ("why this advisor: verified scope + session evidence"), closing the loop with [Suitability-Matching](../patterns/Suitability-Matching.md) and [Trust-Evidence-Layer](../patterns/Trust-Evidence-Layer.md).

## Future

- Extension to fund managers: AI-proctored operational-DD interviews that produce standardized, comparable manager profiles for LP-facing platforms
- Reciprocal credentialing: an advisor's verified profile could transfer to education, insurance distribution, and tax advisory — one evaluation, many licensed surfaces
- Benchmark economy: an "APEX for advisors" — AI agents graded against verified human advisors on suitability tasks — would let platforms prove their advice engines against a human reference standard

## Risks

- **Regulation:** AI-based employment/credential decisions are under scrutiny (NYC Local Law 144, EU AI Act high-risk classification); the evaluation design must be auditable and bias-tested before launch
- **Liability:** a credentialed advisor who misfits clients transfers blame to the platform — the credential must be evidence, not immunity
- **Security:** credential stores are high-value targets (Mercor's LiteLLM breach); PII and session records require hardened supply-chain controls
- **Gaming:** advisors will optimize for the interview; the rubric needs behavioral correction (post-match performance, complaint data) rather than a one-time score
- **Over-conservatism:** if the credential gates too hard, it shrinks legitimate supply and recreates the incumbency problem it was meant to solve
