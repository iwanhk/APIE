# Tools

Planned tooling for APIE. Current status: `scripts/` covers the pipeline; the rest is roadmap (Phase 4).

## Planned

| Tool | Purpose | Status |
| --- | --- | --- |
| `apie new-product` | scaffold a product teardown from the template | planned |
| `apie search` | semantic search over the knowledge base | planned |
| `apie index` | rebuild datasets with validation | planned (equivalent: `scripts/build_dataset.py`) |
| APIE MCP server | let any agent query products/patterns/datasets at runtime | planned |
| APIE CLI schema lint | validate PRs against schemas in CI | planned |

## Design Principles

1. Datasets are the API — `datasets/*.json` is a stable machine surface.
2. Scripts never edit content files; they read and validate.
3. Everything runs on stdlib Python today; no dependency tax for contributors.

