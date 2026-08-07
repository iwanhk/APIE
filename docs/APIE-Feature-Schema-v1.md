# APIE Feature Schema v1

**Status:** ratified (initial release)
**Applies to:** `features/<Feature>.md`
**Frontmatter `type`:** `feature`

## Purpose

A feature entry documents one capability as reusable knowledge: its core loop, UX flow, AI integration, metrics, and pitfalls. Features are smaller than patterns and are instantiated by products.

## Required Frontmatter

```yaml
---
id: ai-chat
type: feature
name: AI Chat
tags: [ai, chat, assistant]
last_updated: 2026-08-07
---
```

## Required Sections

### Definition
One paragraph: what the feature is and what job it does.

### Core Loop
The user's repeated loop in 3–5 steps.

### UX Flow
Link or summary of the flow in `ux-flows/`, plus the key UX decisions (input affordance, streaming, citations, error handling).

### AI Integration
Which AI capabilities are required (generation, retrieval, agentic loops, memory) and the product decisions around latency and cost.

### Metrics
The metrics that show the feature works: usage, retention, resolution, conversion.

### Examples
Products that implement this feature well, with the mechanism.

### Pitfalls
Failure modes: hallucination, cost blowout, opaque errors, poor fallback.

## Example

[features/AI-Chat.md](../features/AI-Chat.md)

