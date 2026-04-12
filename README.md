<p align="center">
  <img src="docs/assets/logo.png?v=3.1.0" alt="BA-Kit Logo" width="200">
</p>

<div align="center">

[**🇬🇧 English**](README.md) | [**🇻🇳 Tiếng Việt**](README.vi.md)

</div>

<p align="center">
  <img src="https://img.shields.io/badge/Version-3.1.0-blue?style=for-the-badge" alt="Version 3.1.0">
  <img src="https://img.shields.io/badge/Agents-33-green?style=for-the-badge" alt="33 Agents">
  <img src="https://img.shields.io/badge/Platforms-Antigravity%20%7C%20Claude%20Code%20%7C%20CoWork-orange?style=for-the-badge" alt="3 Platforms">
  <img src="https://img.shields.io/badge/Capability-CMMI%20Level%205%20Enabler-purple?style=for-the-badge" alt="CMMI Level 5 Enabler">
  <img src="https://img.shields.io/badge/Knowledge-831%20Entries%20%7C%2023%20Domains-teal?style=for-the-badge" alt="831 Knowledge Entries">
  <img src="https://img.shields.io/badge/Integration-Jira%20%2B%20Confluence-blue?style=for-the-badge" alt="Jira + Confluence">
  <img src="https://img.shields.io/badge/Templates-14-gray?style=for-the-badge" alt="14 Templates">
  <img src="https://img.shields.io/badge/Prompts-48-yellow?style=for-the-badge" alt="48 Prompts">
</p>

<h1 align="center">BA-Kit</h1>
<h3 align="center">Agent Squad for Requirements Engineering</h3>

---

## What is BA-Kit?

BA-Kit is **not a prompt library**. It is an **agent squad** for agentic AI platforms.

It replaces the single-chatbot approach with **33 specialists** — each with a defined role, toolset, and System 2 Reflective Loop — running across three platforms:

| Platform | Runtime | Best For |
| :--- | :--- | :--- |
| **Antigravity IDE** (Google DeepMind) | Agent Skills + MCP | Power users, full toolchain |
| **Claude Code** (Anthropic) | CLI, Git, CI/CD | Engineers, project-level reasoning |
| **Claude CoWork** (Anthropic) | Desktop | Non-technical BAs, document synthesis |

---

## How It Works

```
User Request
     │
     ▼
@ba-master ──── Triage + Route ──────────────────────────────┐
     │                                                         │
     ▼                                                         ▼
Specialist Agent                                      Context Handoff
  (e.g. @ba-writing)                               (shared continuity)
     │
     ├── System 1: Draft Output
     │
     ├── System 2: STOP & REFLECT
     │     ├── Did I hallucinate?
     │     └── Verify via grep / python / web
     │
     └── Verified Output → Handoff to Next Agent
```

---

## The Agent Squad (33 Agents)

<details>
<summary><strong>Orchestrator (1)</strong></summary>

| Agent | Role | Capability |
| :--- | :--- | :--- |
| **`@ba-master`** | Dispatcher | Strategy, Routing, Context Management |

</details>

<details>
<summary><strong>Core (3) — The Foundation</strong></summary>

| Agent | Role | Capability |
| :--- | :--- | :--- |
| **`@ba-identity`** | Chief of Staff | Stakeholder Mapping, RACI, Competency Grid |
| **`@ba-elicitation`** | Journalist | Funnel Questioning, Colombo Method |
| **`@ba-writing`** | Architect | Visual UI Scan, Gherkin Drafting (BDD) |

</details>

<details>
<summary><strong>Specialized (8) — The Experts</strong></summary>

| Agent | Role | Capability |
| :--- | :--- | :--- |
| **`@ba-validation`** | QA Lead | Visual QA, Edge Case Detection |
| **`@ba-traceability`** | CCB Secretary | Grep Verification, No Hallucinations |
| **`@ba-nfr`** | SRE Architect | Web-Validated ISO 25010 Standards |
| **`@ba-process`** | Lean Master | Whiteboard Vision, BPMN Waste Analysis |
| **`@ba-prioritization`** | Product Manager | MoSCoW, RICE, WSJF Frameworks |
| **`@ba-solution`** | Investor | Python-Verified ROI & NPV Math |
| **`@ba-conflict`** | Mediator | Harvard Negotiation, ADR Drafting |
| **`@ba-export`** | Publisher | Compliance Check, Pandoc Formatting |

</details>

<details>
<summary><strong>Advanced (3)</strong></summary>

| Agent | Role | Capability |
| :--- | :--- | :--- |
| **`@ba-metrics`** | Data Scientist | SPC Charts, Defect Density, Cpk Stats |
| **`@ba-root-cause`** | Investigator | 5 Whys, Fishbone, Pareto Analysis |
| **`@ba-innovation`** | R&D Scientist | A/B Testing, Hypothesis Designs |

</details>

<details>
<summary><strong>Strategic (4)</strong></summary>

| Agent | Role | Capability |
| :--- | :--- | :--- |
| **`@ba-strategy`** | Strategist | PESTLE, SWOT, Business Model Canvas, Porter's 5 Forces |
| **`@ba-facilitation`** | Facilitator | Workshop Design, ODEC Framework, Group Dynamics |
| **`@ba-systems`** | Systems Analyst | Stocks & Flows, Leverage Points, System Archetypes |
| **`@ba-agile`** | Agile Analyst | User Story Mapping, MVP Definition, Hypothesis-Driven |

</details>

<details>
<summary><strong>Quality & Audit (4)</strong></summary>

| Agent | Role | Capability |
| :--- | :--- | :--- |
| **`@ba-test-gen`** | QA Architect | AC → 7-category Test Cases (BVA, Decision Tables, State Transitions) |
| **`@ba-quality-gate`** | Quality Officer | 8-dimension scoring, 5 gates: PASS / CONDITIONAL / REJECT |
| **`@ba-consistency`** | Integration Auditor | Cross-artifact alignment: US ↔ API ↔ DB ↔ BRD |
| **`@ba-auditor`** | Chief Auditor | Full project health dashboard + action plan |

</details>

<details>
<summary><strong>Lifecycle (7)</strong></summary>

| Agent | Role | Capability |
| :--- | :--- | :--- |
| **`@ba-questioning`** | Master Interviewer | Context-Free Questions, Interview Prep, Assumption Surfacing |
| **`@ba-communication`** | Communicator | Audience Adaptation, Status Reports, Executive Summaries |
| **`@ba-ux`** | UX Researcher | Persona, Journey Map, Empathy Map, JTBD, Usability Testing |
| **`@ba-data`** | Data Architect | ERD, Data Dictionary, DFD, Data Mapping, Migration Planning |
| **`@ba-change`** | Change Agent | ADKAR, Readiness Assessment, Training Plans, Go-Live |
| **`@ba-business-rules`** | Rules Engine | Decision Tables, Decision Trees, Rule Catalog, Conflict Detection |
| **`@ba-diagram`** | Visualizer | Mermaid v11 (24+ types), BA artifact→diagram, Confluence export |

</details>

<details>
<summary><strong>Integration (2) + Knowledge (1)</strong></summary>

| Agent | Role | Capability |
| :--- | :--- | :--- |
| **`@ba-jira`** | Jira Bridge | Story→Ticket Transport, Sprint Planning, Transport Gate Reflection |
| **`@ba-confluence`** | Confluence Bridge | Markdown→XHTML Publishing, Document Import, Version Tracking |
| **`@ba-wiki`** | Knowledge Curator | 2-tier knowledge ingest, wiki query, living docs, glossary management |

</details>

---

## Quick Start

**Antigravity IDE**
```bash
cp -r ba-kit/.agent/skills/* ~/.gemini/antigravity/skills/
```

**Claude Code**
```bash
cp -r ba-kit/.agent/skills/* ~/.claude/skills/
```

**Claude CoWork**
```bash
cp -r ba-kit/.agent/skills/* ~/Library/Application\ Support/Claude/skills/
```

Then summon any specialist:
```
@ba-writing I need a login feature spec.
@ba-solution check the ROI for this initiative.
@ba-master route this request to the right specialist.
```

---

## System 2 Intelligence

Every agent runs a **Reflective Cognitive Loop** before responding:

1. **Analyze (System 1)** — fast pattern matching
2. **Draft (System 1)** — generate initial output
3. **Reflect (System 2)** — STOP. Did I hallucinate? Verify with `grep` / `python` / web
4. **Output** — verified, high-precision answer

This loop reduces hallucinations and surfaces hidden assumptions automatically.

---

## Knowledge Search Engine

**831 indexed entries** across **23 domains**, powered by BM25+.

```bash
python3 .agent/scripts/ba_search.py "acceptance criteria gherkin"
python3 .agent/scripts/ba_search.py "GDPR compliance" --domain compliance
python3 .agent/scripts/ba_search.py "stakeholder analysis" --multi-domain
python3 .agent/scripts/ba_search.py --stats
```

Domains: `writing` `elicitation` `validation` `nfr` `process` `prioritization` `traceability` `conflict` `solution` `systems` `agile` `identity` `workshop` `innovation` `metrics` `modeling` `ux-research` `business-rules` `integration` `compliance` `communication` `testing` `data-analytics`

---

## Repository Structure

```
ba-kit/
├── .agent/skills/          # 33 Agent Skills + 2 Connectors
├── .agent/scripts/         # BM25+ Knowledge Search Engine
├── .agent/data/            # 831 Indexed Knowledge Entries (23 domains)
├── .agent/templates/       # 14 Document Templates (BRD, SRS, FRD, PRD, ...)
├── .agent/wiki/            # Living Knowledge Wiki
├── docs/                   # Documentation & Guides
│   ├── agent-cheat-sheet.md
│   ├── prompt-library.md   # 48 copy-paste prompts by phase
│   └── knowledge_base/
├── ebooks/                 # Synthesized Book Knowledge (9 files)
├── README.md
└── README.vi.md
```

---

## License

MIT License. Free to use for personal and enterprise projects.

---

<p align="center">
  <strong>Antigravity • Claude Code • Claude CoWork</strong><br>
  <em>Code Less. Think More.</em>
</p>
