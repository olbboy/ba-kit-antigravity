---
description: Master workflow for Requirements Engineering - start here to select appropriate BA skill workflow
---

# 🎯 BA-Kit Master Workflow

## Overview
This is the master router for all Business Analysis workflows. Based on your task, this workflow will guide you to the appropriate specialized workflow.

## Step 1: Identify Your Task Context

Before starting any BA task, identify which category your work falls into:

### 🔵 Core Skills (ALWAYS Load First)
These workflows should be used as foundation for ANY BA task:
- `/ba-identity` - BA Identity & Competencies (SKILL-01)
- `/ba-elicitation` - Elicitation & Questioning (SKILL-02)  
- `/ba-writing` - Requirements Writing & Quality (SKILL-03)

### 🟡 Specialized Skills (Load Based on Context)
Use these workflows for specific situations:
- `/ba-nfr` - NFR Framework with ISO 25010 (SKILL-04) - Use when specifying quality attributes
- `/ba-prioritization` - Prioritization Techniques (SKILL-05) - Use when ranking features
- `/ba-conflict` - Conflict Resolution (SKILL-06) - Use when stakeholders disagree
- `/ba-traceability` - Traceability & Change Management (SKILL-07) - Use when managing RTM/changes
- `/ba-validation` - Validation & Verification (SKILL-08) - Use when reviewing requirements

### 🟢 Template Skills (Load When Creating Documents)
Use these workflows when creating specific deliverables:
- `/ba-brd` - Business Requirements Document (SKILL-09) - For new projects
- `/ba-srs` - Software Requirements Specification (SKILL-10) - For detailed specs
- `/ba-frd` - Functional Requirements Document (SKILL-11) - For functional details
- `/ba-agile` - Agile Artifacts (SKILL-12) - For User Stories, Epics, Use Cases

## Step 2: Select Workflow Pattern

Based on your situation, use one of these common patterns:

### Pattern A: New Project Kickoff
```
/ba-identity → /ba-elicitation → /ba-prioritization → /ba-brd
```

### Pattern B: Detailed Requirements Phase
```
/ba-identity + /ba-elicitation + /ba-writing → /ba-nfr → /ba-traceability → /ba-srs or /ba-frd
```

### Pattern C: Agile Sprint Work
```
/ba-identity + /ba-elicitation + /ba-writing → /ba-prioritization → /ba-agile
```

### Pattern D: Requirements Review
```
/ba-writing → /ba-validation → /ba-conflict (if needed)
```

### Pattern E: Change Management
```
/ba-identity + /ba-writing → /ba-traceability → /ba-validation
```

## Step 3: Decision Matrix

| Tình huống | Core Workflows | Specialized | Template |
|------------|----------------|-------------|----------|
| **Bắt đầu dự án mới** | identity, elicitation, writing | prioritization | brd |
| **Phỏng vấn stakeholder** | identity, elicitation, writing | - | - |
| **Viết SRS** | identity, elicitation, writing | nfr, traceability | srs |
| **Có mâu thuẫn yêu cầu** | identity, elicitation, writing | conflict | - |
| **Review requirements** | identity, elicitation, writing | validation | - |
| **Quản lý thay đổi** | identity, elicitation, writing | traceability | - |
| **Sprint Planning (Agile)** | identity, elicitation, writing | prioritization | agile |
| **NFR Analysis** | identity, elicitation, writing | nfr | srs hoặc frd |

## Quick Commands

- **Full BA Session**: Run `/ba-identity` first, then proceed with context-specific workflows
- **Quick Question**: Ask directly - I will apply SKILL-02 questioning techniques
- **Document Creation**: Specify document type and I'll guide you through the appropriate template

## Notes
- Core Skills should ALWAYS be loaded as foundation
- Combine multiple specialized skills for complex tasks
- Templates are starting points - customize as needed
