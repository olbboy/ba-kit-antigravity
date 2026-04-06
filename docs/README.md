# BA-Kit Documentation

> Navigation index for all BA-Kit documentation, guides, and templates.

---

## Getting Started

| Document | Description |
|----------|-------------|
| [Quick Start](../QUICK-START.md) | 2-minute setup guide |
| [Junior BA Start](junior-start.md) | 4-week onboarding path for new BAs |
| [Usage Guide](../USAGE-GUIDE.md) | How the agent squad works |
| [Usage Guide (Vi)](../USAGE-GUIDE.vi.md) | Hướng dẫn sử dụng (tiếng Việt) |

## Core References

| Document | Description |
|----------|-------------|
| [Agent Cheat Sheet](agent-cheat-sheet.md) | All 21 agents at a glance |
| [Prompt Library](prompt-library.md) | 28 copy-paste prompts organized by BA workflow phase |
| [Workflow Cookbook](../WORKFLOW-COOKBOOK.md) | 23 real-world scenario recipes |

## Guides

| Document | Description |
|----------|-------------|
| [AI Foundation](ai-foundation-for-ba.md) | LLM, Tokens, MCP, Agents — bilingual primer |
| [AI Tools Guide](ai-tools-guide.md) | Tool selection matrix for 9+ AI tools |
| [Design & Prototype](design-prototype-guide.md) | Stitch MCP, Figma MCP, vibe coding pipelines |

## Architecture

| Document | Description |
|----------|-------------|
| [Architecture Decisions](architecture-decisions.md) | Naming, identity, CMMI positioning |
| [Antigravity Protocol](antigravity-protocol.md) | Runtime specification for Antigravity IDE |

## Templates

All templates are in the [`templates/`](../templates/) folder:

| Template | Use Case |
|----------|----------|
| [PRD](../templates/prd-template.md) | Product Requirements Document |
| [BRD](../templates/brd-template.md) | Business Requirements Document |
| [SRS](../templates/srs-template.md) | Software Requirements Specification (IEEE 29148) |
| [FRD](../templates/frd-template.md) | Functional Requirements Document |
| [Use Case](../templates/use-case-template.md) | Use Case Specification |
| [API Contract](../templates/api-contract-template.md) | API Contract Definition |
| [Data Dictionary](../templates/data-dictionary-template.md) | Data Dictionary |
| [Communication Plan](../templates/communication-plan-template.md) | Stakeholder Communication Plan |
| [Agile Artifacts](../templates/agile-artifacts.md) | User Stories, Epics, Sprint artifacts |
| [Continuity](../templates/continuity-template.md) | Project context handoff |

## Knowledge Base

Indexed BA knowledge across 23 domains — search via BM25+ engine:
```
python3 .agent/skills/ba-kit-search/scripts/ba_search.py "<query>"
```

See [`knowledge_base/`](knowledge_base/) for raw content:
- `core/` — 3 foundational files
- `specialized/` — 12 domain-specific files
- `advanced/` — 3 advanced methodology files

## eBooks

Synthesized knowledge from BA reference books:
- See [`ebooks/`](../ebooks/) folder and its [README](../ebooks/README.md)
