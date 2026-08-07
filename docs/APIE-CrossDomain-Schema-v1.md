# APIE Cross-Domain Schema v1

**Status:** ratified (initial release)
**Applies to:** `cross-domain/<Source>-to-<Target>.md`
**Frontmatter `type`:** `cross-domain`

## Purpose

Cross-domain transfers are the part of APIE no one else builds: they take a mechanism proven in one industry and map it into another. This is where innovation is generated, not just documented.

## Required Frontmatter

```yaml
---
id: netflix-recommendation-to-investment
type: cross-domain
name: Netflix Recommendation → Investment
source_domain: Consumer Media
target_domain: FinTech / Investment
source_pattern: patterns/Recommendation.md
status: hypothesis
last_updated: 2026-08-07
---
```

| Field | Notes |
| --- | --- |
| `source_domain` | where the pattern was proven |
| `target_domain` | where the pattern could land |
| `source_pattern` | relative link to the source pattern file |
| `status` | `hypothesis` (proposed) / `in-practice` (a product does it) / `validated` (strong evidence) |

## Required Sections

### Source
The origin domain and the pattern as proven there. One or two canonical examples with the mechanism.

### Pattern
The abstract mechanism — stated without domain vocabulary so it can be re-planted.

### Transfer
The mapping: which elements transfer directly, which need adaptation, which fail.

### Example
At least one concrete worked example: a product concept in the target domain, built from the pattern. The more specific the better.

### Future
Where this transfer could go next, and which products might already be doing it.

### Risks
What breaks in the new domain: regulation, trust, data availability, user agency.

## Example

[cross-domain/Netflix-Recommendation-to-Investment.md](../cross-domain/Netflix-Recommendation-to-Investment.md)

