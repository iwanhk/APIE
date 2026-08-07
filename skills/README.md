# Skills

Structured, executable workflows for AI agents — not just prompts. Two layers:

1. **Knowledge-library skills** (`skills/*.md`) — schema-based workflow documents following [APIE Skill Specification v1](../docs/APIE-Skill-Specification-v1.md).
2. **Installable skill packages** (`skills/<name>/`) — standard skill format (SKILL.md + references), installable into Codex, Claude Code, or Cursor. Tool-agnostic by design.

## Installable Skills

| Skill | What it does | Package |
| --- | --- | --- |
| APIE Brain | The product innovation engine (Retrieve → Reason → Compose → Evaluate → Innovate) | [skills/apie-brain/](apie-brain/) |

### Install

```bash
# One command, choose your tool
python3 scripts/install_skill.py --list
python3 scripts/install_skill.py --tool codex      # ~/.codex/skills/apie-brain
python3 scripts/install_skill.py --tool claude     # ~/.claude/skills/apie-brain
python3 scripts/install_skill.py --tool cursor     # ~/.cursor/rules/apie.mdc
```

Or install directly from this GitHub repo without cloning (via the Codex skill installer):

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo iwanhk/APIE --path skills/apie-brain
```

## Knowledge-Library Skills

| Skill | Type | File |
| --- | --- | --- |
| Product Reverse Engineer | analysis | [Product-Reverse-Engineer.md](Product-Reverse-Engineer.md) |
| Cross-Innovation | combination | [Cross-Innovation.md](Cross-Innovation.md) |

Planned: Pattern Finder · Idea Generator · Product Critic · Architecture Expert · Growth Expert · AI-Native Product Designer · Business Designer.
