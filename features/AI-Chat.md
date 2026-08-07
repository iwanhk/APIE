---
id: ai-chat
type: feature
name: AI Chat
tags: [ai, chat, assistant, conversational]
last_updated: 2026-08-07
---

# AI Chat

## Definition

A conversational interface where the user asks in natural language and the product responds with generated text — optionally grounded in product context, with actions attached to answers. The job: lower the floor for complex tasks by replacing menus and syntax with conversation.

## Core Loop

1. User asks (text, voice, or attached file)
2. Product assembles context (memory, workspace, retrieved documents)
3. Model generates a streaming response
4. Product shows the answer with citations and next-action affordances
5. User acts on the answer (apply, execute, copy, follow up)
6. Product updates memory/context for the next turn

## UX Flow

See [ux-flows/AI-Chat.md](../ux-flows/AI-Chat.md). Key decisions: entry point (persistent chat vs contextual inline), streaming (perceived speed), citations (trust), and whether answers can *do* things (edit, execute) or only *say* things.

## AI Integration

- Generation + retrieval (RAG) for grounded answers; agentic loops when actions are allowed
- Latency is UX: streaming hides it, but first-token latency sets the feel
- Cost control: model routing, caching, and context budgets — chat cost can silently eat margin
- Memory integration is what separates a chat widget from an assistant

## Metrics

- Engagement: messages per daily user, DAU/WAU retention of chat users
- Quality: resolution rate (did the answer end the need?), follow-up rate, thumbs-down rate
- Business: conversion of chat users to paid, cost per resolved session

## Examples

- **ChatGPT** — chat as the product; memory and artifacts turned it into a workspace
- **Perplexity** — chat + citations-first answer, proving trust through sources
- **Cursor** — chat that edits code; the chat is a control surface, not a wall
- **Intercom Fin** — chat in customer support with deflection as the metric

## Pitfalls

- Hallucination without citations destroys trust
- Chat that can't act (no apply/execute) becomes a dead end — answers must resolve into product actions
- Cost blowout on free tiers without metering
- Empty-state failure: users don't know what to ask — provide suggested starts

