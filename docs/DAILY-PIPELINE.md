# Daily Product Intelligence Pipeline

This is the mechanism that makes APIE grow every single day. It is the difference between a static archive and a living knowledge base.

## Daily Outputs

Every day the pipeline produces five kinds of content:

### 1. New Products

**Sources to watch:**

- Product Hunt (`https://www.producthunt.com/` — API requires token)
- YC Demo Day / YC companies
- GitHub Trending
- Hacker News (Algolia API is free: `https://hn.algolia.com/api/v1/search_by_date`)
- AI leaderboards and launch newsletters

**Output:** add promising products to `datasets/Top100.json` watchlist and/or create `products/<Category>/<Product>.md` entries. Raw dumps go to `datasets/raw/` (gitignored).

**Filter:** what is *mechanism-new*? A clone with a different logo is not news. A product with a new loop, new AI capability, or new go-to-market is.

### 2. Pattern Mining

Analyze yesterday's new products. Ask: *is there a new pattern here?*

- If yes → create `patterns/<Pattern>.md` with status `emerging`
- If it extends an existing pattern → update that file and its Examples section
- If it contradicts a pattern → open a discussion

### 3. Reverse Engineering (Daily Teardown)

One product teardown per day, in order:

> Day 001 — Cursor ✅ · Day 002 — Lovable · Day 003 — Mercor · …

Follow `products/_TEMPLATE.md` and the Product Schema. Every teardown must add at least one pattern link or feature reference — teardowns that reference nothing are dead ends.

### 4. Innovation Challenge

Each day, pick two products (random or themed), then generate **20 innovations** by combining their patterns. Output: `examples/Innovation-Challenge-<A>-x-<B>.md`.

Quality rule: each idea must name the source pattern it combines. Ideas without provenance are discarded.

### 5. Weekly Pattern Report

Every week, synthesize the last 7 days: new patterns, pattern shifts, product launches worth studying. Output: `docs/reports/Weekly-YYYY-WW.md`.

## Automation Options

### Option A — GitHub Actions cron (recommended)

```yaml
name: daily-pipeline
on:
  schedule:
    - cron: "0 1 * * *"   # UTC daily
jobs:
  crawl:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python3 scripts/crawl_hn.py --days 1
      - run: python3 scripts/crawl_github.py --days 1
      - run: python3 scripts/build_dataset.py
      - uses: stefanzweifel/git-auto-commit-action@v5
```

### Option B — local cron

```cron
0 1 * * * cd /path/to/APIE && python3 scripts/crawl_hn.py --days 1 && python3 scripts/build_dataset.py
```

### Option C — manual

Run the crawlers, review, then write the five outputs by hand. Quality > quantity on days when the queue is short.

## Quality Gates

1. `python3 scripts/build_dataset.py --validate` must pass — schema violations block merges.
2. Every volatile fact has a source URL and an "as of" date.
3. Every teardown references at least one pattern; every pattern has ≥2 examples; every innovation idea names its source patterns.
4. Human review before merge for any claim about revenue, valuation, users, or market share.

## File Conventions

- Raw crawls: `datasets/raw/<source>_YYYY-MM-DD.json` (gitignored)
- Built datasets: `datasets/*.json` (committed, rebuilt by `build_dataset.py`)
- Weekly reports: `docs/reports/Weekly-YYYY-WW.md`
- Daily teardown log: maintained in `PRODUCTS.md`

