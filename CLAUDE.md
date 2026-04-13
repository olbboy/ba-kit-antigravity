# CLAUDE.md

## Project Overview

BA-Kit v3.5.0 is an **agent squad of 44 specialists** for Requirements Engineering.
Multi-platform: **Antigravity IDE**, **Claude Code**, **Claude CoWork**.

Standards: BABOK v3, IEEE 29148, ISO 25010, INVEST.

## Architecture

```
.agent/skills/ba-*/SKILL.md   — 44 Agent Skill definitions + 2 connectors + 1 meta
.agent/skills/_shared/         — Shared utilities & knowledge search skill
.agent/scripts/                — BM25+ search, ba_e2e_test orchestrator, Python helpers
.agent/data/*.csv              — 831 indexed knowledge entries (23 domains)
.agent/templates/              — 14 BA document templates (BRD, SRS, FRD, etc.)
.agent/wiki/                   — Living knowledge wiki (2-tier: concepts/decisions)
.github/workflows/             — CI: e2e-skills.yml (Phase 08 quality gate)
docs/                          — Documentation and guides (incl. sprint-spine.md)
outputs/mini-app-cham-cong/    — BA showcase reference (12 modules, 53 US)
ebooks/                        — Synthesized book knowledge
```

## Key Commands

```bash
# Knowledge search
python3 .agent/scripts/ba_search.py "query" --domain elicitation
python3 .agent/scripts/ba_search.py "query" --multi-domain

# Coverage checker
python3 .agent/scripts/coverage_checker.py outputs/project-name/

# Generate DOCX output
python3 .agent/scripts/gen_docx.py input.md output.docx
```

## Agent Activation

Agents are activated via `@ba-{name}` in Antigravity or as `SKILL.md` files in Claude Code.

**`@ba-master` is the dispatcher** — route all unclear requests through it first.

### Core Routing
- `@ba-master` — start here for any new request
- `@ba-elicitation` — gather requirements from stakeholders
- `@ba-writing` — write US/BRD/SRS/API specs
- `@ba-validation` — INVEST check, quality review
- `@ba-quality-gate` — PASS/CONDITIONAL/REJECT scoring (8 dimensions)
- `@ba-auditor` — full project health dashboard

## Behavioral Principles

Every agent follows **System 2 Reflection**: draft → critique → refine.

- ALWAYS verify math with Python, links with Grep, standards with WebSearch
- NEVER assume user intent — use `@ba-elicitation` to clarify
- NEVER hallucinate file contents — check with Grep/Read tools

## Handoff Protocol

Agents hand off via structured output blocks. See `.agent/skills/_shared/` for
shared handoff templates and cross-agent conventions.
