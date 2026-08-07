#!/usr/bin/env python3
"""Crawl GitHub Trending / search into datasets/raw/.

GitHub Trending has no official API. Use the GitHub Search API (rate-limited;
GITHUB_TOKEN recommended) for repos created recently with AI keywords.

Usage:
    GITHUB_TOKEN=... python3 scripts/crawl_github.py --days 1
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


RAW_DIR = Path(__file__).resolve().parent.parent / "datasets" / "raw"


def search_repos(days: int, token: str | None) -> list[dict]:
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    query = urllib.parse.quote(f'AI topic:ai pushed:>={since} sort:stars')
    url = f"https://api.github.com/search/repositories?q={query}&per_page=50"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "apie-daily-pipeline",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8")).get("items", [])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=1)
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    try:
        repos = search_repos(args.days, os.environ.get("GITHUB_TOKEN"))
    except urllib.error.HTTPError as exc:
        print(f"GitHub API error {exc.code}: {exc.reason}. "
              "Set GITHUB_TOKEN to raise the rate limit.")
        return 1
    out = RAW_DIR / f"github_{date.today().isoformat()}.json"
    out.write_text(json.dumps(repos, indent=2), encoding="utf-8")
    print(f"Saved {len(repos)} repos to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

