# Datasets

Machine-readable output of the knowledge base. **This is the API surface** — any AI agent can load these files without parsing Markdown.

## Files

| Dataset | Schema | Contents | Built by |
| --- | --- | --- | --- |
| [Products.json](Products.json) | APIE Product Schema v1 | product teardown index | `build_dataset.py` |
| [Patterns.json](Patterns.json) | APIE Pattern Schema v1 | pattern library index | `build_dataset.py` |
| [Features.json](Features.json) | APIE Feature Schema v1 | feature index | `build_dataset.py` |
| [Flows.json](Flows.json) | (flow frontmatter) | UX flow index | `build_dataset.py` |
| [Skills.json](Skills.json) | APIE Skill Specification v1 | skill index | `build_dataset.py` |
| [CrossDomain.json](CrossDomain.json) | APIE Cross-Domain Schema v1 | transfer index | `build_dataset.py` |
| [Top100.json](Top100.json) | curated | the 100 most important products (watchlist) | manual + pipeline |

## Regenerate

```bash
python3 scripts/build_dataset.py
```

`raw/` holds crawler dumps (gitignored) — see [docs/DAILY-PIPELINE.md](../docs/DAILY-PIPELINE.md).

