---
description: Traceability & Change Management - manage requirements lifecycle and changes (SKILL-07)
---

# 🟡 SKILL-07: Traceability & Change Management Workflow

## Purpose
Track requirements throughout their lifecycle and manage changes effectively using the Requirements Traceability Matrix (RTM).

## Step 1: Understand Traceability Concepts

### Types of Traceability

```
┌─────────────────────────────────────────────────────────────┐
│                   TRACEABILITY TYPES                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BACKWARD ←──────────────────────────────── FORWARD         │
│  (To Source)                              (To Implementation)│
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌────────┐│
│  │ Business │ →  │ Stakeholder│ → │ Solution │ →  │ Test   ││
│  │ Need     │    │ Requirement│   │ Requirement│   │ Case   ││
│  └──────────┘    └──────────┘    └──────────┘    └────────┘│
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  VERTICAL (Abstraction Levels):                             │
│  Strategy → Business → Stakeholder → Solution → Component   │
│                                                             │
│  HORIZONTAL (Same Level):                                   │
│  Requirement A ←→ Requirement B (dependency)                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Benefits of Traceability
- **Impact Analysis** - Know what's affected by changes
- **Coverage** - Ensure all requirements are tested
- **Accountability** - Track who requested what
- **Compliance** - Audit trail for regulations
- **Scope Management** - Prevent gold plating

## Step 2: Create Requirements Traceability Matrix (RTM)

### RTM Template

```
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ BR-ID    │ SR-ID    │ FR-ID    │ Design   │ Test     │ Status   │ Notes    │
│          │          │          │ Ref      │ Case     │          │          │
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ BR-001   │ SR-001   │ FR-001   │ DES-001  │ TC-001   │ Approved │          │
│          │          │ FR-002   │ DES-002  │ TC-002   │ Approved │          │
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ BR-002   │ SR-002   │ FR-003   │ DES-003  │ TC-003   │ Dev      │ Sprint 3 │
│          │          │ FR-004   │ DES-004  │ TC-004   │ Dev      │ Sprint 3 │
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ BR-003   │ SR-003   │ FR-005   │ -        │ -        │ Draft    │ Pending  │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

### Column Definitions

| Column | Description |
|--------|-------------|
| **BR-ID** | Business Requirement (WHY) |
| **SR-ID** | Stakeholder Requirement (WHO needs WHAT) |
| **FR-ID** | Functional Requirement (WHAT system does) |
| **Design Ref** | Link to design/architecture document |
| **Test Case** | Link to test case(s) verifying requirement |
| **Status** | Current status (see below) |
| **Notes** | Additional context |

### Requirement Status Definitions

| Status | Description | Next Step |
|--------|-------------|-----------|
| **Draft** | Initial capture, not verified | Validate with stakeholder |
| **Proposed** | Verified, awaiting approval | Review & approve |
| **Approved** | Signed-off, ready for design | Begin design/dev |
| **Designed** | Design complete | Implement |
| **Implemented** | Code complete | Test |
| **Verified** | Testing passed | Deploy |
| **Deferred** | Postponed to later phase | Track in backlog |
| **Rejected** | Will not be implemented | Document reason |

## Step 3: Perform RTM Health Checks

Run these checks regularly to ensure RTM integrity:

### ⚠️ Orphan Requirements
```
FIND: Requirements with NO backward trace to business need
ISSUE: Why does this requirement exist?
ACTION: Validate with stakeholder or remove
```

### ⚠️ Untested Requirements
```
FIND: Requirements with NO test case
ISSUE: How will we verify this works?
ACTION: Create test case or mark as untestable
```

### ⚠️ Gold Plating
```
FIND: Design/Code with NO requirement trace
ISSUE: Who asked for this? Is it in scope?
ACTION: Create requirement or remove feature
```

### ⚠️ Broken Links
```
FIND: References to deleted/invalid IDs
ISSUE: Traceability chain is broken
ACTION: Update or remove invalid references
```

## Step 4: Apply Change Control Process

```
┌─────────────────────────────────────────────────────────────┐
│                 CHANGE CONTROL PROCESS                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. REQUEST    Stakeholder submits change request           │
│       │                                                     │
│       ▼                                                     │
│  2. LOG        BA logs CR in tracking system                │
│       │                                                     │
│       ▼                                                     │
│  3. ANALYZE    Impact analysis performed                    │
│       │        (scope, timeline, budget, risk)              │
│       ▼                                                     │
│  4. REVIEW     CCB reviews CR and recommendation            │
│       │                                                     │
│       ▼                                                     │
│  5. DECISION   Approve / Reject / Defer                     │
│       │                                                     │
│       ▼                                                     │
│  6. IMPLEMENT  If approved, update requirements/RTM         │
│       │                                                     │
│       ▼                                                     │
│  7. VERIFY     Validate change implemented correctly        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Step 5: Use Change Request Template

```
┌─────────────────────────────────────────────────────────────┐
│                    CHANGE REQUEST                           │
├─────────────────────────────────────────────────────────────┤
│ CR-ID: [CR-XXX]                                             │
│ Date: [YYYY-MM-DD]                                          │
│ Requestor: [Name, Role]                                     │
│ Status: [Submitted/Analyzing/Review/Approved/Rejected]      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ CHANGE DESCRIPTION:                                         │
│ [Detailed description of requested change]                  │
│                                                             │
│ BUSINESS JUSTIFICATION:                                     │
│ [Why is this change needed? What value does it add?]        │
│                                                             │
│ AFFECTED REQUIREMENTS:                                      │
│ • [REQ-ID]: [Impact description]                            │
│ • [REQ-ID]: [Impact description]                            │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ IMPACT ANALYSIS:                                            │
│                                                             │
│ Scope Impact:      [Low/Medium/High] - [Description]        │
│ Timeline Impact:   [+X days/weeks] - [Description]          │
│ Budget Impact:     [$X] - [Description]                     │
│ Risk Impact:       [Low/Medium/High] - [New risks]          │
│ Technical Impact:  [Description of technical changes]       │
│ Testing Impact:    [Tests affected/new tests needed]        │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ RECOMMENDATION:                                             │
│ [Approve/Reject/Defer] with rationale                       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ DECISION:                                                   │
│ Decision: [Approved/Rejected/Deferred]                      │
│ Decided by: [CCB/Sponsor name]                              │
│ Date: [YYYY-MM-DD]                                          │
│ Conditions: [Any conditions for approval]                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Step 6: Perform Impact Analysis

### Impact Analysis Framework

```
For each change, assess impact on:

┌─────────────────────────────────────────────────────────────┐
│ DIRECT IMPACTS (Immediately affected)                       │
├─────────────────────────────────────────────────────────────┤
│ • Requirements: Which REQs change?                          │
│ • Design: Which components change?                          │
│ • Code: Which modules change?                               │
│ • Tests: Which tests need updates?                          │
│ • Documentation: What docs need updates?                    │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ RIPPLE IMPACTS (Indirectly affected)                        │
├─────────────────────────────────────────────────────────────┤
│ • Dependent requirements (trace forward)                    │
│ • Integrations with other systems                           │
│ • Training materials                                        │
│ • Deployment procedures                                     │
│ • Operational procedures                                    │
└─────────────────────────────────────────────────────────────┘
```

### Impact Sizing Guide

| Size | Scope | Timeline | Resources |
|------|-------|----------|-----------|
| **Small** | 1-2 requirements | < 1 day effort | Same team |
| **Medium** | 3-10 requirements | 1-5 days effort | Same team |
| **Large** | > 10 requirements | > 1 week effort | Multiple teams |

## Step 7: Apply Version Control

### Versioning Convention
```
Version: X.Y.Z

X = Major version (baseline, significant changes)
Y = Minor version (new features, enhancements)
Z = Patch version (corrections, clarifications)

Example progression:
0.1 → Initial draft
0.2 → Stakeholder feedback incorporated
1.0 → Approved baseline ⭐
1.1 → Minor enhancements
1.2 → Additional features
2.0 → Major revision ⭐
```

### Baseline Management
- **Baseline** = Approved, frozen set of requirements at a point in time
- Changes to baseline require formal change control
- Always compare changes against current baseline
- Track which baseline is in production

## Step 8: Track Change Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **Change Volume** | # CRs per month | Trend ↓ over time |
| **Approval Rate** | Approved / Total | Track pattern |
| **Cycle Time** | Days from submit to decision | < 5 days |
| **Implementation Rate** | Implemented / Approved | > 90% |
| **Churn Rate** | Changed REQs / Total REQs | < 20% |

## Next Steps
After traceability work, proceed to:
- `/ba-validation` for requirements review
- `/ba-writing` to update requirements
- Template workflows for updated documentation
