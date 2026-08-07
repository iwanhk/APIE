# APIE Schemas (condensed)

Every APIE content file begins with YAML frontmatter and follows one of five schemas. Full definitions live in the repo under `docs/APIE-*-Schema-v1.md`.

## Common frontmatter rules

```yaml
---
id: kebab-case-unique-id
type: product | pattern | feature | flow | business-model | cross-domain | skill
name: Human Readable Name
tags: [tag1, tag2]
last_updated: YYYY-MM-DD
---
```

- `id` is permanent once published.
- `tags` lowercase, kebab-case.
- `last_updated` changes on every edit.

## 1. Product (type: product)

Required frontmatter: `id, type, name, category, company, founded, status, tags, last_updated, sources`.

Required sections: Overview · History · Target User · Business · Growth · UX · AI · Architecture · Patterns · Lessons · Innovation · Sources.

## 2. Pattern (type: pattern)

Required frontmatter: `id, type, name, status, tags, last_updated`. `status` ∈ established | emerging | hypothesis.

Required sections: Definition · Purpose · Problem · When To Use · When NOT To Use · Examples (≥2) · Engineering · UX · Business · Cross-Domain Transfers · Pitfalls.

## 3. Feature (type: feature)

Required frontmatter: `id, type, name, tags, last_updated`.

Required sections: Definition · Core Loop · UX Flow · AI Integration · Metrics · Examples · Pitfalls.

## 4. Cross-domain (type: cross-domain)

Required frontmatter: `id, type, name, source_domain, target_domain, source_pattern, status, last_updated`.

Required sections: Source · Pattern · Transfer · Example · Future · Risks.

## 5. Skill (type: skill)

Required frontmatter: `id, type, name, skill_type, tags, inputs, outputs, last_updated`. `skill_type` ∈ analysis | generation | evaluation | combination.

Required sections: Purpose · When To Use / When NOT To Use · Workflow · Quality Checks · Provenance · Example Output.

## Validation

In the repo: `python3 scripts/build_dataset.py --validate` (schema + required fields). Every PR is CI-checked.

