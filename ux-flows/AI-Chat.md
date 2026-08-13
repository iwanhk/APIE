---
id: ai-chat-session
type: flow
name: AI Chat Session
tags: [ai, chat, assistant, conversational]
last_updated: 2026-08-07
---

# AI Chat Session

## Goal

The user asks a question or gives a task in natural language and reaches a usable answer or action in the fewest, most trust-preserving steps.

## Entry Points

- Global chat button / keyboard shortcut (Cmd+L style) from anywhere
- Contextual chat attached to a document, code file, or selection
- Empty-state "ask me anything" with suggested starts

## Steps

1. **Input** — text/voice/file attachment. The input affordance signals capability: "Ask about your workspace" > a bare text box.
2. **Context assembly** — product pulls relevant context (memory, workspace docs, @-mentions, model picker). Visible context builds trust: "Reading: 3 files, memory: 2 facts."
3. **Generation** — stream tokens immediately; show source chips as they resolve.
4. **Output** — answer + citations + action affordances (copy, apply, execute, save). The answer ends with a verb, not a period.
5. **Follow-up** — threaded conversation; references persist.
6. **Memory** — offer to save useful facts ("Remember that I use Python 3.12?") rather than silently storing everything.

## Decision Points & Failure Paths

- **Slow first token** → user perceives failure before the answer starts. Mitigate: streaming, optimistic UI, model routing.
- **Hallucination** → without citations, the answer is untrustworthy. Mitigate: grounded retrieval, "I couldn't verify" honesty mode.
- **Context too thin** → generic answers. Mitigate: retrieval + explicit grounding UI.
- **Action failure** (apply/execute fails) → show the error inside the chat with a retry, never a dead end.
- **Cost guard** → surface usage ("15% of monthly limit used") before the hard block.

## Success Criteria

The user reaches a correct, actionable answer; the session resolves with an action taken or an explicit "not needed" — not an abandoned thread.

## Metrics

Completion rate, time-to-first-useful-token, resolution rate, follow-up rate, cost per resolved session, retention of chat users.
