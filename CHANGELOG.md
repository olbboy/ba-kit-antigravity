# Changelog

All notable changes to BA-Kit will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.4.0] - 2026-01-07

### 🧠 The Antigravity Native Update (System 2 Swarm)

This major architectural release transitions BA-Kit from a collection of scripts/prompts to a full **Antigravity Native Swarm** of 15 self-correcting agents.

#### 🆕 System 2 Intelligence
*   **Reflective Loops**: All 15 agents now use a "Stop & Think" cognitive model. They critique their own drafts before answering.
*   **Tool Mandates**: Implemented strict rules to prevent LLM Hallucinations:
    *   **Math**: Agents MUST use `python` for ROI/NPV/SPC calculations.
    *   **Search**: Agents MUST use `grep` to verify file existence (Traceability).
    *   **Standards**: Agents MUST use `search_web` to verify ISO clauses.

#### 🤖 New Agents (CMMI Level 5)
*   **`@ba-metrics`**: The Data Scientist Agent. Uses Python to calculate Control Charts, Sigma Levels, and Defect Density.
*   **`@ba-root-cause`**: The Investigator Agent. Uses Fishbone and 5 Whys to find systemic issues.
*   **`@ba-innovation`**: The R&D Scientist Agent. Designs A/B tests and calculates Pilot ROI.

#### 📚 Documentation Overhaul
*   **README.md**: Completely rewritten to feature the "15 Agent Swarm".
*   **QUICK-START.md**: Simplified to "Install & Summon" (Antigravity Syntax).
*   **USAGE-GUIDE.md**: Deep dive into the "Cognitive Loop" and best practices.
*   **AGENT.MD**: Updated to be the "Single Source of Truth" for the Swarm Configuration.

#### 🛠️ Deprecation
*   **Legacy Python Scripts**: The old CLI wrappers (`python ba-agent.py`) are now secondary to the direct `@agent` syntax.

---

## [2.3.0] - 2026-01-07
### 🛡️ The Tool Hardening Update
*   Enforced "Mandatory Tool Use" for `@ba-solution` (Math) and `@ba-traceability` (Grep).
*   Completed "Deep Gap Analysis" of Antigravity potential.

## [2.2.0] - 2026-01-04

### 💎 The Professional Branding Update
*   New "Knowledge Block" Logo.
*   Context-Aware Template Organization.

---
(Previous versions preserved below...)
