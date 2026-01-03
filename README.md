<p align="center">
  <img src="assets/logo.png" alt="BA-Kit Logo" width="200">
</p>

<div align="center">

[**🇬🇧 English**](README.md) | [**🇻🇳 Tiếng Việt**](README.vi.md)

</div>

<p align="center">
  <img src="https://img.shields.io/badge/Skills-12-blue?style=for-the-badge" alt="12 Skills">
  <img src="https://img.shields.io/badge/Workflows-9-green?style=for-the-badge" alt="9 Workflows">
  <img src="https://img.shields.io/badge/Templates-4-orange?style=for-the-badge" alt="4 Templates">
  <img src="https://img.shields.io/badge/Standards-ISO%2029148%20%7C%20ISO%2025010%20%7C%20BABOK-purple?style=for-the-badge" alt="Standards">
</p>

<h1 align="center">🏆 BA-Kit</h1>
<h3 align="center">The Definitive Business Analysis Framework</h3>

<p align="center">
  <strong>Master the Art of Requirements Engineering</strong><br>
  12 connected competencies • 9 strategic workflows • World-class documentation standards
</p>

---

## 🎯 The Gold Standard in Business Analysis

BA-Kit is not just a library; it is a **comprehensive cognitive framework** designed to elevate requirements engineering to an art form. It bridges the gap between abstract business strategy and precise technical execution.

Whether used by **Human Experts** or **Agentic AI**, BA-Kit delivers a structured, ISO-compliant methodology to:

- **Elicit** hidden value and unspoken needs
- **Architect** robust, conflict-free requirements
- **Validate** specifications with surgical precision
- **Orchestrate** the entire product definition lifecycle

This is the toolkit for those who refuse to compromise on clarity.

---

## 📊 Skill Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         BA-KIT SKILL PYRAMID                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  🟢 TEMPLATES (Output Layer)                                                │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐                   │
│  │ SKILL-09  │ │ SKILL-10  │ │ SKILL-11  │ │ SKILL-12  │                   │
│  │    BRD    │ │    SRS    │ │    FRD    │ │   Agile   │                   │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘                   │
│                              │                                              │
│  🟡 SPECIALIZED (Context Layer)                                             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐               │
│  │SKILL-04 │ │SKILL-05 │ │SKILL-06 │ │SKILL-07 │ │SKILL-08 │               │
│  │   NFR   │ │Priority │ │Conflict │ │ Trace   │ │Validate │               │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘               │
│                              │                                              │
│  🔵 CORE (Foundation Layer) ─ ALWAYS ACTIVE                                 │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐               │
│  │    SKILL-01     │ │    SKILL-02     │ │    SKILL-03     │               │
│  │    Identity     │ │   Elicitation   │ │  Writing Quality│               │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### For AI Agent Integration

1. **Copy the workflows** from `.agent/workflows/` to your AI agent's workflow directory
2. **Reference AGENT.MD** as the system prompt or persona
3. **Use slash commands** to activate specific skills:

```
/ba-master        → See complete workflow map
/ba-identity      → Activate BA persona
/ba-elicitation   → Start requirements gathering
/ba-writing       → Quality documentation mode
/ba-nfr           → NFR specification (ISO 25010)
/ba-prioritization → MoSCoW, Kano, WSJF
/ba-conflict      → Stakeholder conflict resolution
/ba-traceability  → RTM and change management
/ba-validation    → Requirements review mode
```

### For Human BAs

1. **Read USAGE-GUIDE.md** for comprehensive usage documentation
2. **Reference the skill files** in `core/`, `specialized/`, `templates/`
3. **Use the templates** as starting points for your deliverables

---

## 📁 Repository Structure

```
ba-kit/
│
├── AGENT.MD                    # 🏆 Master orchestrator - AI agent persona
├── USAGE-GUIDE.md              # 📘 Comprehensive usage documentation
├── 00-MASTER-INDEX.md          # 📋 Original skill library index
├── QUICK-START.md              # ⚡ Quick reference guide
├── README.md                   # 📄 This file
│
├── .agent/workflows/           # 🤖 Antigravity/AI Agent Workflows
│   ├── ba-master.md            #    Router workflow
│   ├── ba-identity.md          #    SKILL-01 workflow
│   ├── ba-elicitation.md       #    SKILL-02 workflow
│   ├── ba-writing.md           #    SKILL-03 workflow
│   ├── ba-nfr.md               #    SKILL-04 workflow
│   ├── ba-prioritization.md    #    SKILL-05 workflow
│   ├── ba-conflict.md          #    SKILL-06 workflow
│   ├── ba-traceability.md      #    SKILL-07 workflow
│   └── ba-validation.md        #    SKILL-08 workflow
│
├── core/                       # 🔵 Core Skills (Always Load)
│   ├── SKILL-01-identity.md    #    BA persona & stakeholder framework
│   ├── SKILL-02-elicitation.md #    Questioning & interviewing
│   └── SKILL-03-writing-quality.md # Requirements writing standards
│
├── specialized/                # 🟡 Specialized Skills (Context-Based)
│   ├── SKILL-04-nfr-framework.md    # ISO 25010 NFR templates
│   ├── SKILL-05-prioritization.md   # MoSCoW, Kano, WSJF, etc.
│   ├── SKILL-06-conflict-resolution.md # Harvard negotiation method
│   ├── SKILL-07-traceability-change.md # RTM & change control
│   └── SKILL-08-validation-verification.md # V&V checklists
│
└── templates/                  # 🟢 Document Templates
    ├── SKILL-09-brd-template.md     # Business Requirements Document
    ├── SKILL-10-srs-template.md     # SRS (IEEE 29148)
    ├── SKILL-11-frd-template.md     # Functional Requirements Document
    └── SKILL-12-agile-artifacts.md  # User Stories, Epics, Use Cases
```

---

## 🎓 The 12 Skills

### 🔵 Core Skills (Always Active)

| Skill | Name | Purpose |
|-------|------|---------|
| **01** | Identity & Competencies | BA persona, stakeholder mapping, RACI |
| **02** | Elicitation & Questioning | Funnel technique, 5W1H, interview structure |
| **03** | Writing & Quality | RFC 2119 keywords, INVEST criteria, acceptance criteria |

### 🟡 Specialized Skills (Context-Based)

| Skill | Name | Purpose |
|-------|------|---------|
| **04** | NFR Framework | ISO 25010 templates for Performance, Security, Reliability |
| **05** | Prioritization | MoSCoW, Kano Model, WSJF, Value vs Effort |
| **06** | Conflict Resolution | Harvard Method, principled negotiation, escalation |
| **07** | Traceability & Change | RTM, change control process, impact analysis |
| **08** | Validation & Verification | Inspections, walkthroughs, sign-off process |

### 🟢 Template Skills (Document Creation)

| Skill | Name | Purpose |
|-------|------|---------|
| **09** | BRD Template | Business Requirements for executive approval |
| **10** | SRS Template | IEEE 29148 Software Requirements Specification |
| **11** | FRD Template | Detailed Functional Requirements |
| **12** | Agile Artifacts | User Stories, Epics, Use Cases, Story Mapping |

---

## 📜 Standards Compliance

BA-Kit incorporates best practices from:

| Standard | Coverage |
|----------|----------|
| **ISO/IEC/IEEE 29148:2018** | Requirements engineering processes |
| **ISO/IEC 25010:2011** | System quality model (SQuaRE) |
| **BABOK v3** | Business Analysis Body of Knowledge |
| **RFC 2119** | Requirement keywords (SHALL/SHOULD/MAY) |
| **IREB CPRE** | Requirements engineering syllabus |
| **SAFe/Agile** | User stories, WSJF prioritization |

---

## 🤖 AI Agent Integration

### Antigravity (Google DeepMind)

Copy workflows to `.agent/workflows/` in your project:

```bash
cp -r ba-kit/.agent/workflows/ your-project/.agent/workflows/
```

### Claude / ChatGPT / Other

Use `AGENT.MD` as system prompt or reference the skill files directly in your prompts.

### Custom Integration

The skill files are pure Markdown—parse and integrate into any AI system.

---

## 📖 Usage Examples

### Example 1: New Project Discovery

```
User: I need to gather requirements for a new e-commerce platform.

AI (with BA-Kit): 
/ba-identity → Maps stakeholders (Product, IT, Marketing, Customers)
/ba-elicitation → Applies Funnel Questioning:
  - Exploratory: "What are the primary business goals?"
  - Clarifying: "When you say 'fast checkout', what's the target time?"
  - Probing: "What happens if payment fails mid-transaction?"
```

### Example 2: Conflict Resolution

```
User: Sales wants real-time reporting but IT says it's not feasible.

AI (with BA-Kit):
/ba-conflict → Applies Harvard Method:
  - Sales POSITION: "Real-time reports"
  - Sales INTEREST: Need current data for quick decisions
  - IT POSITION: "Batch processing"
  - IT INTEREST: System performance concerns
  
  OPTIONS: Near-real-time (5-min), cache strategy, priority tiering
```

### Example 3: Requirements Review

```
User: Review this SRS for quality issues.

AI (with BA-Kit):
/ba-validation → Applies verification checklist:
  ☐ Uses SHALL/SHOULD/MAY correctly
  ☐ No ambiguous terms ("fast", "user-friendly")
  ☐ Has acceptance criteria
  ☐ Traces to business need
  
  DEFECTS FOUND:
  - FR-003: "fast response" → AMBIGUOUS
  - FR-007: Missing acceptance criteria → INCOMPLETE
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:

1. **Report issues** - Found a gap in the skills? Let us know.
2. **Suggest improvements** - Better techniques or templates to add?
3. **Add translations** - Help make BA-Kit multilingual.
4. **Share use cases** - How are you using BA-Kit?

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **IIBA** - For BABOK v3 framework
- **IREB** - For CPRE syllabus
- **ISO** - For 29148 and 25010 standards
- **Harvard Negotiation Project** - For principled negotiation method
- **SAFe** - For WSJF and Agile frameworks

---

<p align="center">
  <strong>Built with 💜 for the Requirements Engineering Community</strong><br>
  <em>Transform your AI into a Legendary Business Analyst</em>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-the-12-skills">Skills</a> •
  <a href="#-ai-agent-integration">Integration</a> •
  <a href="#-usage-examples">Examples</a>
</p>
