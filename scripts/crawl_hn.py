#!/usr/bin/env python3
"""Fetch Hacker News stories matching product/AI keywords into datasets/raw/.

Uses the free Algolia HN API (no key required).

Usage:
    python3 scripts/crawl_hn.py --days 1
    python3 scripts/crawl_hn.py --days 1 --keywords "AI,launch,YC"
"""

from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


RAW_DIR = Path(__file__).resolve().parent.parent / "datasets" / "raw"
DEFAULT_KEYWORDS = ["AI", "launch", "YC", "product", "LLM", "agent"]


def fetch_stories(days: int, keywords: list[str]) -> list[dict]:
    since = int((datetime.now(timezone.utc) - timedelta(days=days)).timestamp())
    query = " OR ".join(keywords)
    # Algolia treats "+" as AND, which breaks multi-keyword OR queries;
    # percent-encode spaces so "AI OR launch" is a real boolean query.
    url = (
        "https://hn.algolia.com/api/v1/search_by_date"
        f"?query={urllib.parse.quote(query, safe='')}"
        f"&tags=story&numericFilters=created_at_i%3E{since}&hitsPerPage=50"
    )
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8")).get("hits", [])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=1)
    parser.add_argument("--keywords", default=",".join(DEFAULT_KEYWORDS))
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    stories = fetch_stories(args.days, [k.strip() for k in args.keywords.split(",") if k.strip()])
    out = RAW_DIR / f"hn_{date.today().isoformat()}.json"
    out.write_text(json.dumps(stories, indent=2), encoding="utf-8")
    print(f"Saved {len(stories)} stories to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
