# Daily Pipeline Playbook

Run daily (e.g., 10:00 local time). Automation may handle crawls/datasets; the content below is the human/agent part.

## Daily outputs

1. **New products** — scan HN / Product Hunt / GitHub Trending / YC; add mechanism-new products to the watchlist or teardown queue.
2. **Daily teardown (Day N)** — follow [product-template.md](product-template.md); link ≥1 pattern; update indexes.
3. **Pattern mining** — new mechanism → new `patterns/<Pattern>.md` (status: emerging); variant → update existing Examples.
4. **Innovation challenge** — two random products → 20 combinations, each tagged with its source pattern pair; score top 5; pick a winner.
5. **Weekly report (Fridays)** — synthesize the last 7 days: new patterns, shifts, launches worth studying.

## Quality gates

- Schema validation passes (`python3 scripts/build_dataset.py --validate`)
- Every fact has a source and "as of" date
- Teardown links ≥1 pattern; pattern has ≥2 examples
- Commit messages in Conventional Commits format

## Red line

Never commit real commercial arrangements, unreleased business plans, or confidential terms to public repositories. Keep such content out of git or in a private/ignored location.

