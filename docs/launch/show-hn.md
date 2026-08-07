# Show HN 发布稿

## 标题（三选一）

1. Show HN: I reverse-engineer one AI product per day and encode the patterns
2. Show HN: APIE – an open knowledge base that teaches AI how great products are built
3. Show HN: Every great product starts with A PIE – structured teardowns + patterns + JSON datasets

## 正文

```text
The problem: knowledge about why great products work is locked inside a few essays
and paywalled analyses. "Awesome" lists point you to links; they don't teach you
the mechanism. LLMs can't index them either.

APIE is an open knowledge base where every product teardown, design pattern, feature,
and cross-domain transfer follows a unified schema, and everything compiles into
JSON datasets any AI agent can read directly.

What's inside right now:
- Teardowns: Cursor (SpaceX acquisition, $4B ARR, 2.0/Composer), Lovable ($500M ARR,
  146 employees, vibe coding), Robinhood (zero-commission + the trust debt)
- 5 patterns: Recommendation, Memory, Curation, Trust/Evidence, Suitability Matching
- 6 features + 4 UX flows + cross-domain transfers (Netflix → Investment)
- 5 open standards (schemas v1) so anyone can contribute without breaking the index
- A daily pipeline: one teardown per day, pattern mining, innovation challenges,
  weekly pattern reports (docs/DAILY-TASK.md)

The differentiator vs. awesome lists: cross-domain transfer. Netflix's recommendation
loop → investment products. TikTok's feed → CRM. That's where new products come from.

It's MIT. Everything is Markdown so LLMs can read it; datasets/*.json so they don't
even have to parse.

Feedback wanted: is the schema the right granularity? What's the first pattern you'd
want documented?
```

## 回复区第一帖（自问自答，选发）

```text
Why I'm doing this: I noticed AI agents are great at writing PRDs but terrible at
knowing WHY a product worked. APIE is the missing knowledge layer. Day 001 was
Cursor, Day 002 was Lovable. I intend to keep going for 365 days.
```

