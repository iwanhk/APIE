---
id: education-path
type: feature
name: Education Path
tags: [education, personalization, learning, finance, onboarding]
last_updated: 2026-08-07
---

# Education Path

## Definition

A personalized learning curriculum that adapts to the LP's knowledge level, goals, and interests — pure education with no action bias. The job: raise the user's competence so their own decision is an informed one, and make learning itself the habit.

## Core Loop

1. User completes a knowledge check (or the onboarding conversation infers level)
2. Path assembles: 加密基础 → 加密基金风险 → 3 只基金深潜（examples: 加密基金教育平台）
3. Short lessons with checks; AI answers follow-up questions with citations
4. Progress, streaks, and quarterly recaps (Wrapped moments) keep the habit
5. Path adapts to pace and interests — never to "what to buy"

## UX Flow

Starts from [LP Onboarding](../ux-flows/LP-Onboarding.md); deep-dives link to [Fund Deep-Dive](../ux-flows/Fund-Deep-Dive.md). Key decisions: 5-minute lessons, plain language, progress visible, streaks on *learning* (never on trading).

## AI Integration

- Adaptive difficulty and quiz generation from grounded content
- Citation enforcement on every answer (see [Trust / Evidence Layer](../patterns/Trust-Evidence-Layer.md))
- "Explain like I'm 5" toggle — one product, many registers

## Metrics

Lesson completion rate, quiz accuracy improvement over time, "复述测试" pass rate (user can restate a fund's risks in their own words), 90-day education engagement.

## Examples

- Mechanism: Duolingo streaks + Khan Academy mastery + Fidelity Learn's content depth
- Contrast: Robinhood's education layer — readable but shallow, and overshadowed by action prompts; education that coexists with purchase nudges isn't really education

## Pitfalls

- Gamifying money: streaks on trading frequency incentivize the wrong behavior
- Knowledge ≠ risk capacity: passing quizzes must never be treated as suitability proof
- Content rot: crypto fund mechanics change; courses need refresh cycles
