---
id: memory
type: pattern
name: Memory
status: emerging
tags: [ai, personalization, context, retention]
last_updated: 2026-08-15
---

# Memory

## Definition

Giving an AI product persistent, retrievable context about the user, the task, or the workspace across sessions — so that every new interaction starts from what was already learned instead of from zero. The essence: **stateless intelligence becomes stateful service.**

## Purpose

Turn one-off AI answers into a compounding relationship: less repetition, better personalization, higher switching costs.

## Problem

Default LLM behavior is stateless — it forgets everything between sessions. For recurring users (workflows, creative work, personal assistants), statelessness is the core UX failure: users re-explain, re-paste, and re-discover the same context endlessly.

## When To Use

- Users return repeatedly with the same domain (coding, writing, health, investing)
- The task is long-horizon and context-rich (a project, a codebase, a relationship)
- Memory content is user-owned and can be shown/edited (trust prerequisite)

## When NOT To Use

- One-shot, low-stakes interactions (a single FAQ answer)
- Sensitive domains without explicit consent, clear deletion controls, and audit (health data, legal)
- When users must not be assumed consistent (memory that "locks in" a wrong identity is worse than no memory)

## Examples

- **ChatGPT Memory** — saved facts about the user (name, job, preferences) retrieved at prompt time; user-visible, editable, deletable.
- **Claude (consumer)** — automatic memory of preferences and project context shipped for Team/Enterprise Sep 10, 2025 and expanded to Pro/Max Oct 23, 2025; memory persists across chats and is searchable; memories stay scoped to their project.
- **Claude (developer)** — file-based memory tool (Sep 2025) stores and consults files in a dedicated memory directory that persists across conversations outside the context window — memory as storage, not just retrieval; Claude Science (Jun 2026) adds searchable memory plus resource-use monitoring for long research runs; Claude Tag (Jun 2026) keeps a persistent context layer per Slack channel, learning projects and monitoring ambient conversation.
- **Cursor** — project context and codebase index persist across sessions; the editor "knows" the code without re-explanation.
- **Notion AI** — workspace knowledge is the context; answers reflect your own documents.
- **Replit** — session/workspace state persists so an agent can resume long builds.
- **ChatGPT (2026)** — saved facts upgraded (Jun 4, 2026) to automatic memory synthesis ("Dreaming"): memories self-update as facts age (e.g., "you are going to Singapore in July" becomes "you went to Singapore"), 2x capacity for Plus/Pro; **Computer History** (Aug 13, 2026) extends memory to a recorded activity timeline on macOS — the bridge to the [Ambient-Activity-Memory](Ambient-Activity-Memory.md) pattern.
- **Mosaic Ocean (YC S26, Aug 2026)** — shared memory for multiplayer AI agents: a team of agents reads/writes one memory store so context survives across agents and sessions — memory as a collaboration bus, not just a per-user profile.
- **mem0 / MemPalace** — open-source memory layers (Universal Memory Layer, MemPalace benchmarked storage) industrializing memory as a reusable service between apps and models.

## Engineering

- **Storage:** profile store (facts) + vector store (retrievable content) + optional event timeline
- **Retrieval at prompt time:** assemble memory into context (relevant facts, not everything)
- **Memory timeline:** what was learned, when, and from what evidence — enables correction and audit
- **Lifecycle:** create (extract from conversation), update (new evidence overrides), delete (user request), TTL for stale facts
- **Privacy architecture:** local-first or encrypted storage, opt-in, "memory off" mode

## UX

- **Visible memory:** users should see what the system knows about them
- **Edit/delete as first-class actions:** memory without control is surveillance
- **Use-justification:** "I remembered you're in New York" — surfaced context builds trust
- **Silence is also a feature:** don't dump memory into every answer

## Business

- Retention and compounding value: each session is better than the last
- Switching costs: accumulated memory is hard to leave
- Quality driver: memory-enabled answers are better, justifying subscription pricing (usage-gated + memory = the AI-native subscription stack)

## Cross-Domain Transfers

- Candidates: Memory → CRM (customer history as shared memory), Memory → healthcare (continuity of care), Memory → investment advisory (knowing the client, with audit), Memory → multiplayer agent teams (shared agent memory bus — see Mosaic Ocean)

## Pitfalls

- Stale or wrong memory that persists (harder to notice than to create)
- Privacy/regulatory exposure (GDPR right to erasure, health data rules)
- Memory bloat: retrieving everything = context overflow = worse answers
- The creepy factor: remembering without showing or asking erodes trust
