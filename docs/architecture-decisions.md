# Architecture Decisions & Strategic Analysis

> Internal analysis of BA-Kit positioning, naming conventions, and maturity claims.
> Consolidated from architecture review, strategic analysis, and maturity model assessments.

---

## 1. The "ba-" Prefix Decision

### Analysis

| Factor | Keep `ba-` | Remove `ba-` |
| :--- | :--- | :--- |
| **Namespace Collision** | Safe. `@ba-master` is unique. | Risk. `@master` may conflict with other kits. |
| **Brand Identity** | Clear. "BA" = Business Analysis. | Generic. "Writing" could be any agent. |
| **Discoverability** | All agents sort together alphabetically. | Agents scatter across the list. |
| **Mental Model** | User knows all `@ba-*` = This Kit. | User must memorize arbitrary names. |
| **Migration Cost** | Zero. Status quo. | High. Update all files, docs, guides. |

### Decision: **Keep the `ba-` prefix**

The prefix acts as a namespace (like `@org/package` in npm). The 3-char overhead is negligible compared to clarity benefits.

If a pivot is needed in the future, `@req-*` (Requirements) is the preferred alternative.

---

## 2. Identity: "Swarm" → "Squad"

### Problem

| Language | "Swarm" Interpretation |
| :--- | :--- |
| **English** | Collective intelligence, synchronized movement |
| **Vietnamese** | "Bầy đàn" = instinct, insects, chaos, herd mentality (negative) |

This conflicts with BA-Kit's core value: **System 2 thinking** (deliberate, critical). "Bầy đàn" implies System 1 (reactive, instinctive).

### Decision: Use "Squad" (Biệt Đội)

| Concept | Old Term (Vi) | New Term (Vi) |
| :--- | :--- | :--- |
| **System Name** | Bầy Đàn (Swarm) | **Biệt Đội (Squad)** |
| **The Agents** | Con bot / Cá thể | **Chuyên Gia (Specialist)** |
| **Orchestrator** | Con đầu đàn | **Chỉ Huy (Commander)** |
| **Interaction** | Handoffs | **Phối Hợp (Collaboration)** |
| **Memory** | Sổ cái | **Hồ Sơ Dự Án (Project Dossier)** |

---

## 3. CMMI Level 5 Positioning

### The Dilemma

- **CMMI Level 5 ("Optimizing")** implies an *organization* that continuously changes its processes based on statistical data.
- **BA-Kit** provides the *tools* to do this (SPC Charts, Root Cause Analysis), but cannot force organizational change.
- Claiming "We are CMMI Level 5" risks sounding like marketing to seasoned Enterprise Architects.

### The "Exoskeleton" Theory

BA-Kit wraps around a human user and mechanically guides them to perform Level 5 behaviors:

| Level | Characteristic | Without BA-Kit | With BA-Kit |
| :--- | :--- | :--- | :--- |
| **1. Initial** | Chaotic, hero-based | User guesses requirements | Agents force structure |
| **2. Managed** | Planned, tracked | User makes a checklist | `@ba-master` enforces routing |
| **3. Defined** | Standard processes | User reads a PDF guide | `.agent/skills` *are* the process |
| **4. Quantitative** | Statistical control | User needs a spreadsheet | `@ba-metrics` & `@ba-solution` do the math |
| **5. Optimizing** | Continuous improvement | User holds a retrospective | `@ba-root-cause` & `@ba-innovation` |

### The Gap

A true Level 5 system involves **recursive self-optimization** — agents rewriting their own skill files based on defect patterns. BA-Kit does not allow this (safety guardrail). The user must choose to improve.

### Decision: Use "CMMI Level 5 Enabler"

- ❌ "We are a CMMI Level 5 System" — implies the AI is the organization
- ✅ "We are a CMMI Level 5 Enabler" — the AI empowers the user

**Maturity Score**: 4.8 / 5.0 — The final 0.2 gap is human agency.

---

## 4. Production Readiness Score

| Category | Score | Notes |
| :--- | :--- | :--- |
| **Core Logic** | 10/10 | System 2, Tool Mandates, 21 Agents |
| **Documentation** | 9/10 | Comprehensive with bilingual support |
| **Terminology** | 10/10 | "Squad" is professional and consistent |
| **Extensibility** | 8/10 | MCP integration, skill-based architecture |
| **Localization** | 8/10 | Vietnamese guides and bilingual docs |

**Overall**: **9.0 / 10** — Production ready.

---

## 5. Improvement Roadmap

### Tier 1: Quick Wins

| # | Improvement | Effort |
| :--- | :--- | :--- |
| 1 | Version badges sync | 10 min |
| 2 | WORKFLOW-COOKBOOK terminology audit | 1 hr |

### Tier 2: Medium Wins

| # | Improvement | Effort |
| :--- | :--- | :--- |
| 3 | Interactive demo flow (Mermaid lifecycle diagram) | 1 hr |
| 4 | Error handling protocol for ambiguity | 2 hrs |

### Tier 3: Strategic Upgrades

| # | Improvement | Effort |
| :--- | :--- | :--- |
| 5 | Recursive optimization (agent self-improvement) | Very High |
| 6 | Project templates for common scenarios | 4 hrs |
| 7 | Auto-artifact generation to `/outputs` | 6 hrs |
