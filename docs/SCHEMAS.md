# APIE Open Standards — Overview

APIE is an **open standard**, not a content dump. Five schemas define every file in the knowledge base. Any AI agent that reads the schemas can index the repository without cleaning.

## The Five Standards

| # | Standard | Applies to | File | Frontmatter `type` |
| --- | --- | --- | --- | --- |
| 1 | APIE Product Schema v1 | `products/**/*.md` | [APIE-Product-Schema-v1.md](APIE-Product-Schema-v1.md) | `product` |
| 2 | APIE Pattern Schema v1 | `patterns/*.md` | [APIE-Pattern-Schema-v1.md](APIE-Pattern-Schema-v1.md) | `pattern` |
| 3 | APIE Feature Schema v1 | `features/*.md` | [APIE-Feature-Schema-v1.md](APIE-Feature-Schema-v1.md) | `feature` |
| 4 | APIE Cross-Domain Schema v1 | `cross-domain/*.md` | [APIE-CrossDomain-Schema-v1.md](APIE-CrossDomain-Schema-v1.md) | `cross-domain` |
| 5 | APIE Skill Specification v1 | `skills/*.md` | [APIE-Skill-Specification-v1.md](APIE-Skill-Specification-v1.md) | `skill` |

UX flows (`ux-flows/`) and business models (`business-models/`) use lightweight frontmatter defined in their directory READMEs; they are compiled into datasets by `scripts/build_dataset.py`.

## Common Frontmatter Rules

Every content file begins with YAML frontmatter:

```yaml
---
id: kebab-case-unique-id
type: product | pattern | feature | flow | business-model | cross-domain | skill
name: Human Readable Name
tags: [tag1, tag2]
last_updated: YYYY-MM-DD
---
```

Rules:

- `id` is permanent. Once published, an ID never changes; fixes update the file, not the ID.
- `tags` are lowercase, kebab-case, and come from the pattern areas list where applicable.
- `last_updated` changes on every edit of the file.
- Type-specific required fields are defined in each schema below.

## Validation

`python3 scripts/build_dataset.py --validate` checks every content file against its schema and reports missing required fields. CI will enforce this in Phase 2 (see [ROADMAP.md](../ROADMAP.md)).

## Versioning

Schemas are semver'd. v1 is the initial release. Any breaking change requires an RFC (see [CONTRIBUTING.md](../CONTRIBUTING.md)) and a new major version; released schemas are never silently mutated.

