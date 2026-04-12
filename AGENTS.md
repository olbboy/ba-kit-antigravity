# BA-Kit Antigravity — Agent Rules

## Project Overview

BA-Kit is a squad of **33 BA Specialists** for Requirements Engineering.
Knowledge engine: BM25+ over 831 entries across 23 domains.
Templates: 14 BA document templates in `.agent/templates/`.

## Agent Squad (invoke via /ba-*)

| Agent | Role |
| :--- | :--- |
| `/ba-master` | Dispatcher — routing & squad planning |
| `/ba-identity` | Chief of Staff — persona & stakeholder mapping |
| `/ba-elicitation` | Journalist — funnel questioning |
| `/ba-writing` | Architect — user stories, Gherkin |
| `/ba-validation` | QA Lead — visual QA, edge cases |
| `/ba-traceability` | CCB Secretary — RTM, impact analysis |
| `/ba-nfr` | SRE Architect — ISO-validated NFRs |
| `/ba-process` | Lean Master — process mapping, waste analysis |
| `/ba-prioritization` | Product Manager — MoSCoW, RICE, WSJF |
| `/ba-solution` | Investor — ROI/NPV analysis |
| `/ba-conflict` | Mediator — Harvard negotiation, ADR |
| `/ba-export` | Publisher — compliance, formatting |
| `/ba-metrics` | Data Scientist — SPC charts, Cpk stats |
| `/ba-root-cause` | Investigator — 5 Whys, Fishbone, Pareto |
| `/ba-innovation` | R&D Scientist — A/B testing, hypothesis design |
| `/ba-strategy` | Strategist — PESTLE, SWOT, BMC |
| `/ba-facilitation` | Facilitator — workshop design, ODEC |
| `/ba-systems` | Systems Analyst — stocks & flows, leverage points |
| `/ba-agile` | Agile Analyst — story mapping, MVP, estimation |
| `/ba-jira` | Jira Bridge — story→ticket transport |
| `/ba-confluence` | Confluence Bridge — markdown→XHTML publishing |
| `/ba-test-gen` | QA Architect — AC → 7-category test cases |
| `/ba-quality-gate` | Quality Officer — 8-dimension quality scoring |
| `/ba-consistency` | Integration Auditor — cross-artifact alignment |
| `/ba-auditor` | Chief Auditor — project health dashboard |
| `/ba-questioning` | Critical Thinker — Paul-Elder framework, assumption surfacing |
| `/ba-communication` | Communicator — status reports, executive summaries |
| `/ba-ux` | UX Analyst — persona, journey mapping, usability testing |
| `/ba-data` | Data Analyst — ERD, data dictionary, DFD, migration |
| `/ba-change` | Change Manager — ADKAR, training needs, go-live |
| `/ba-business-rules` | Rules Engineer — decision tables, rule catalog |
| `/ba-diagram` | Visual Architect — Mermaid v11 (24+ types) |
| `/ba-wiki` | Knowledge Curator — wiki query, living documentation |

## Key Commands

```bash
# Search knowledge base (831 entries, 23 domains)
python3 .agent/skills/ba-kit-search/scripts/ba_search.py "<query>"

# Check US/AC coverage
python3 .agent/skills/ba-kit-search/scripts/coverage_checker.py <file>
```

## Development Principles

- YAGNI / KISS / DRY
- System 2 reflection before every output
- Verify math with Python, verify links with Grep, verify standards with WebSearch
- Never hallucinate file contents — check with Grep/Read

## Documentation Structure

```
.agent/skills/ba-*/SKILL.md   — 33 agent skill files
.agent/templates/              — 14 BA document templates
docs/                          — guides, cheat sheet, prompt library
ebooks/                        — 7 synthesized BA ebooks
```
