# Scripts

The APIE pipeline. All scripts are stdlib-only Python — no dependency tax.

| Script | Purpose | Status |
| --- | --- | --- |
| [build_dataset.py](build_dataset.py) | scan Markdown frontmatter → validate → write `datasets/*.json` | ✅ working |
| [crawl_hn.py](crawl_hn.py) | fetch HN stories matching AI/product keywords (Algolia API, no key) | ✅ working |
| [crawl_github.py](crawl_github.py) | search GitHub repos with AI topic (token recommended) | ⚠️ needs token for volume |
| [crawl_producthunt.py](crawl_producthunt.py) | Product Hunt launches via GraphQL | ⚠️ needs `PH_API_TOKEN` |
| [crawl_yc.py](crawl_yc.py) | YC launches | 🔶 stub (no official API) |

Planned: `merge_patterns.py` (pattern dedup/merge), `weekly_report.py` (weekly synthesis), `new_product.py` (scaffold a teardown).

## Commands

```bash
# Build all datasets from the Markdown content
python3 scripts/build_dataset.py

# Validate content against schemas (exit 1 on errors) — this is the CI gate
python3 scripts/build_dataset.py --validate

# Daily crawl
python3 scripts/crawl_hn.py --days 1
```

Outputs land in `datasets/*.json`; raw crawls land in `datasets/raw/` (gitignored).

