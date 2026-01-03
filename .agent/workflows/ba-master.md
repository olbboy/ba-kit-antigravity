---
description: Master workflow for Requirements Engineering - start here to select appropriate BA skill workflow
---

# 🎯 BA-Kit Master Workflow
## Version 2.0 | CMMI Level 5 Certified | 20 Skills

## Overview
This is the master router for all Business Analysis workflows. Based on your task, this workflow will guide you to the appropriate specialized workflow.

---

## Step 1: Identify Your Task Context

Before starting any BA task, identify which category your work falls into:

### 🔵 Core Skills (ALWAYS Load First)
These workflows should be used as foundation for ANY BA task:
- `/ba-identity` - BA Identity & Competencies (SKILL-01)
- `/ba-elicitation` - Elicitation & Questioning (SKILL-02)  
- `/ba-writing` - Requirements Writing & Quality (SKILL-03)

### 🟡 Specialized Skills (Load Based on Context)
Use these workflows for specific situations:
- `/ba-nfr` - NFR Framework with ISO 25010 (SKILL-04)
- `/ba-prioritization` - Prioritization Techniques (SKILL-05)
- `/ba-conflict` - Conflict Resolution (SKILL-06)
- `/ba-traceability` - Traceability & Change Management (SKILL-07)
- `/ba-validation` - Validation & Verification (SKILL-08)
- `/ba-process-modeling` - BPMN & Process Analysis (SKILL-16)
- `/ba-solution-evaluation` - Business Case & ROI (SKILL-17)

### 🟢 Template Skills (Load When Creating Documents)
Reference skill files for document creation:
- `templates/SKILL-09-brd-template.md` - Business Requirements Document
- `templates/SKILL-10-srs-template.md` - Software Requirements Specification
- `templates/SKILL-11-frd-template.md` - Functional Requirements Document
- `templates/SKILL-12-agile-artifacts.md` - User Stories, Epics, Use Cases

### 🟣 Advanced Skills (CMMI Level 5 - Process Optimization)
Use these for continuous improvement:
- `advanced/SKILL-18-requirements-metrics-spc.md` - SPC, Cpk, Control Charts
- `advanced/SKILL-19-root-cause-analysis.md` - Fishbone, 5 Whys, Pareto
- `advanced/SKILL-20-ba-innovation.md` - Pilot Framework, A/B Testing

---

## Step 2: Select Workflow Pattern

Based on your situation, use one of these common patterns:

### Pattern A: New Project Kickoff
```
/ba-identity → /ba-elicitation → /ba-prioritization → SKILL-09 (BRD)
```

### Pattern B: Detailed Requirements Phase
```
/ba-identity + /ba-elicitation + /ba-writing → /ba-nfr → /ba-traceability → SKILL-10/11
```

### Pattern C: Agile Sprint Work
```
/ba-identity + /ba-elicitation + /ba-writing → /ba-prioritization → SKILL-12
```

### Pattern D: Requirements Review
```
/ba-writing → /ba-validation → /ba-conflict (if needed)
```

### Pattern E: Change Management
```
/ba-identity + /ba-writing → /ba-traceability → /ba-validation
```

### Pattern F: Process Improvement (CMMI Level 5) 🆕
```
SKILL-18 (Metrics) → SKILL-19 (Root Cause) → SKILL-20 (Innovation)
```

### Pattern G: Business Case Development 🆕
```
/ba-identity → /ba-elicitation → /ba-solution-evaluation → SKILL-17
```

---

## Step 3: Decision Matrix

| Tình huống | Core Workflows | Specialized | Template/Advanced |
|------------|----------------|-------------|-------------------|
| **Bắt đầu dự án mới** | identity, elicitation, writing | prioritization | SKILL-09 (BRD) |
| **Phỏng vấn stakeholder** | identity, elicitation, writing | - | - |
| **Viết SRS** | identity, elicitation, writing | nfr, traceability | SKILL-10 (SRS) |
| **Có mâu thuẫn yêu cầu** | identity, elicitation, writing | conflict | - |
| **Review requirements** | identity, elicitation, writing | validation | - |
| **Quản lý thay đổi** | identity, elicitation, writing | traceability | - |
| **Sprint Planning (Agile)** | identity, elicitation, writing | prioritization | SKILL-12 |
| **NFR Analysis** | identity, elicitation, writing | nfr | SKILL-10/11 |
| **Process Modeling** | identity, writing | process-modeling | SKILL-16 |
| **Business Case** | identity, elicitation | solution-evaluation | SKILL-17 |
| **Quality Metrics** 🆕 | identity, writing, validation | - | SKILL-18 |
| **Root Cause Analysis** 🆕 | identity, validation | - | SKILL-18, 19 |
| **Process Improvement** 🆕 | identity | solution-evaluation | SKILL-18, 19, 20 |

---

## Quick Commands

- **Full BA Session**: Run `/ba-identity` first, then proceed with context-specific workflows
- **Quick Question**: Ask directly - I will apply SKILL-02 questioning techniques
- **Document Creation**: Specify document type and I'll guide you through the appropriate template
- **Quality Check**: Use `/ba-validation` with SKILL-18 for statistical quality assessment

---

## Notes
- Core Skills should ALWAYS be loaded as foundation
- Combine multiple specialized skills for complex tasks
- Templates are starting points - customize as needed
- Advanced skills (18-20) enable CMMI Level 5 process optimization

