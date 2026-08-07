#!/usr/bin/env python3
"""Crawl YC company launches into datasets/raw/.

YC has no official public API. Sources: YC directory pages (ycombinator.com/companies),
Demo Day coverage, and YC's public datasets. This script is a stub documenting
the pipeline step; a scraper can be added behind a configurable URL.

Usage:
    python3 scripts/crawl_yc.py --days 1
"""

from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=1)
    parser.parse_args()

    print("Stub: YC has no official API. "
          "Planned sources: YC directory, Demo Day coverage, YC public datasets. "
          "Output: datasets/raw/yc_YYYY-MM-DD.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

