---
id: semantic-search
type: feature
name: Semantic Search
tags: [search, embeddings, retrieval, knowledge]
last_updated: 2026-08-07
---

# Semantic Search

## Definition

Search that matches on meaning rather than exact keywords: the user can find things they can't name. The job: make unstructured knowledge reachable through natural language.

## Core Loop

1. User types a natural-language query
2. Query and corpus are embedded; nearest neighbors retrieved (often hybrid: lexical + semantic)
3. Results reranked and shown with snippets
4. User refines or clicks; behavior logs improve ranking

## UX Flow

Search bar + instant results + snippet previews + filters. Semantic search shines when the user doesn't know the exact term (concepts, fuzzy memories, code behavior).

## AI Integration

- Embedding models for retrieval, rerankers for precision
- Hybrid retrieval (BM25 + vectors) beats pure vector search in most real corpora
- Optionally, generative answer synthesis on top of retrieved chunks (search → answer)

## Metrics

Success rate (click-through on first result), zero-result rate, time-to-answer, retrieval precision@k, index freshness.

## Examples

- **Notion** — semantic search over your notes; finds things you can't name
- **Linear** — fast issue search with semantic matching
- **Perplexity** — web-scale retrieval + synthesis
- **Cursor** — codebase semantic search ("where is the payment retry logic?")

## Pitfalls

- Stale index: retrieval quality decays silently; freshness must be monitored
- Cost: re-embedding large corpora is expensive; incremental indexing required
- Relevance illusions: vector similarity ≠ user intent without reranking
- Security: semantic search can surface documents the user shouldn't see — permission-aware indexing is mandatory

