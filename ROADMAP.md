# APIE Roadmap

The goal: from a GitHub repository to the **open standard for AI product innovation knowledge**.

## Phase 0 — Foundation (v0.1) ✅

- [x] Repository scaffold (all directories)
- [x] Five open standards: Product, Pattern, Feature, Cross-Domain, Skill — v1
- [x] Seed content: Cursor teardown, Recommendation & Memory patterns, Netflix → Investment transfer
- [x] Dataset builder (`scripts/build_dataset.py`) producing `datasets/*.json`
- [x] Daily pipeline documentation

## Phase 1 — Seed the Library (v0.2)

Goal: 50 product teardowns, 30 patterns, 20 features, 15 flows, 15 cross-domain transfers.

- [ ] Teardowns: ChatGPT, Claude, Perplexity, Lovable, Replit, Gamma, Granola
- [ ] Teardowns: Robinhood, Coinbase, Carta, Stripe, Plaid
- [ ] Teardowns: Notion, Linear, Figma, Slack, GitHub, Shopify
- [ ] Teardowns: TikTok, Netflix, Spotify, Pinterest, Airbnb, Uber
- [ ] Pattern library: Authentication, Navigation, Feed, Workspace, Recommendation, Notification, Realtime, Knowledge, Memory, AI, Marketplace, Gamification, Search, Trust, Growth, Community, Payment, Dashboard, Analytics, Security
- [ ] Cross-domain: TikTok → CRM, GitHub → Investment Review, Cursor → Healthcare
- [ ] Top100.json watchlist with 100 verified entries

## Phase 2 — Ratify the Standard (v0.3)

- [ ] Schema v1 ratification after community review
- [ ] Schema validation in CI (PRs rejected on schema violations)
- [ ] Product/Pattern ID registry (stable, permanent IDs)

## Phase 3 — Automate the Pipeline (v0.4)

- [ ] GitHub Actions cron for daily crawls (HN, GitHub Trending, Product Hunt, YC)
- [ ] Automatic pattern mining from `datasets/raw/`
- [ ] Innovation Challenge generator
- [ ] Weekly Pattern Report builder

## Phase 4 — Make It Machine-Native (v0.5)

- [ ] `datasets/*.json` declared as stable API surface
- [ ] `apie` CLI (`apie new-product`, `apie search`, `apie index`)
- [ ] MCP server so any agent can query APIE at runtime
- [ ] Structured citations from every innovation back to source files

## Phase 5 — Community & Ecosystem (v0.6)

- [ ] GitHub Discussions as the innovation forum
- [ ] Translation program (README and core schemas)
- [ ] Website with searchable pattern library
- [ ] 100 contributors milestone

## Phase 6 — Open Standard Adoption (v0.7)

- [ ] External projects adopting APIE schemas
- [ ] Versioned schema release process (semver)
- [ ] Governance model: maintainers, RFC process, pattern-of-the-week

Suggestions welcome via GitHub Issues. The fastest way to help: submit one teardown or one pattern.

