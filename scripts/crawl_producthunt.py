#!/usr/bin/env python3
"""Crawl Product Hunt launches into datasets/raw/.

Product Hunt requires an API token. Set PH_API_TOKEN (see
https://www.producthunt.com/v2/docs) or run this as a stub that documents
the query used by the daily pipeline.

Usage:
    PH_API_TOKEN=... python3 scripts/crawl_producthunt.py --days 1
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import date
from pathlib import Path


RAW_DIR = Path(__file__).resolve().parent.parent / "datasets" / "raw"
QUERY = """
query PostsByDate($from: String!, $to: String!) {
  posts(order: VOTES, postedAfter: $from, postedBefore: $to, first: 50) {
    edges { node { id name tagline url votesCount createdAt } }
  }
}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=1)
    args = parser.parse_args()

    token = os.environ.get("PH_API_TOKEN")
    if not token:
        print("PH_API_TOKEN not set. Stub mode: recording query for the pipeline.")
        print(QUERY)
        return 0

    # Real implementation goes here once a token is configured:
    #   POST https://api.producthunt.com/v2/api/graphql with Authorization: Bearer <token>
    # and write posts into RAW_DIR / f"producthunt_{date.today().isoformat()}.json".
    print("Token detected but fetch implementation is pending. No data written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

