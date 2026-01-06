---
description: Validation & Verification - review requirements for quality and correctness (SKILL-08)
---

# 🟡 SKILL-08: Validation & Verification Workflow

## Purpose
Ensure requirements are correct (building the right product) and complete (building the product right) through structured review techniques.

## Step 1: Understand V&V Difference

| Aspect | Verification | Validation |
|--------|--------------|------------|
| **Question** | Are we building it RIGHT? | Are we building the RIGHT thing? |
| **Focus** | Conformance to specs | Meeting stakeholder needs |
| **Techniques** | Inspections, reviews, walkthroughs | Prototypes, demos, UAT |
| **Performed by** | Internal team | Stakeholders, users |
| **When** | Throughout development | At key milestones |

## Step 2: Automated Quality Check (Active Rules)

Before manual inspection, run the **Requirements Linter** to catch common errors automatically.

**Command (Basic):**
```bash
python3 tools/lint_req.py [file.md]
```

**Command (Expert - Gherkin/INVEST):**
```bash
python3 tools/lint_expert.py [file.md]
```

**What it checks:**
- 🚫 Ambiguous words (fast, easy, robust)
- 🆔 Duplicate Requirement IDs
- 🥒 Gherkin Syntax (Given/When/Then) in Acceptance Criteria
- 💎 INVEST Criteria heuristics

**Fix any errors reported by the tool before proceeding.**

## Step 3: AI-Assisted Deep Review (The Magic Hook)

Don't just rely on human eyes. Generate a specialized "System Prompt" to get a deep architectural audit from AI.

**Command:**
```bash
python3 tools/gen_prompt.py [file.md]
```

## Step 4: Full Project Health Check (Auto-Run)
// turbo
Run the comprehensive doctor command to get metrics, gaps, and quality report:

```bash
./ba doctor
```

## Step 5: Cross-Document Consistency (Auto-Run)
// turbo
Ensure all linked documents have consistent attributes:

```bash
./ba consistency
```

## Step 6: Traceability Gap Analysis (Auto-Run)
// turbo
Identify any orphaned requirements:

```bash
./ba gap
```

## Step 7: Manual Review Techniques

**Action:**
1. Run the command.
2. Copy the generated prompt.
3. Paste it into your AI Chat window.
4. Review the AI's findings (Security, Scalability, Edge Cases).

## Step 4: Apply Verification Techniques

### 🔍 Inspection (Most Formal)

**Process:**
1. **Planning** - Schedule, distribute materials
2. **Overview** - Author presents the document
3. **Preparation** - Reviewers examine individually
4. **Inspection Meeting** - Discuss defects found
5. **Rework** - Author fixes defects
6. **Follow-up** - Verify fixes

**Inspection Checklist:**
```
INDIVIDUAL REQUIREMENT:
☐ Has unique, traceable ID
☐ Uses SHALL/SHOULD/MAY correctly
☐ Is atomic (single requirement)
☐ Is unambiguous (one interpretation)
☐ Is testable/verifiable
☐ Is feasible within constraints
☐ Has acceptance criteria
☐ Has no TBDs or placeholders
☐ Has no prohibited words (fast, easy, user-friendly)
☐ Traces to business need

REQUIREMENT SET:
☐ Complete - all needs captured
☐ Consistent - no contradictions
☐ Feasible - achievable within constraints
☐ Prioritized - all requirements have priority
☐ Traceable - forward and backward links
☐ No duplicates
☐ No gaps in coverage
```

### 📋 Walkthrough (Less Formal)

**Process:**
1. Author leads reviewers through document
2. Reviewers ask questions and note issues
3. Focus on understanding and finding defects
4. Less structured than inspection

**Walkthrough Agenda (60-90 min):**
```
• Opening (5 min): Goals, ground rules
• Walkthrough (45-60 min): Section by section review
• Discussion (15 min): Clarify issues found
• Wrap-up (5 min): Next steps, action items
```

### 👥 Peer Review (Least Formal)

**Process:**
1. One or two reviewers examine document
2. Provide feedback directly to author
3. Quick turnaround
4. Good for smaller documents or changes

## Step 3: Apply Validation Techniques

### 🎨 Prototyping

**Types:**
- **Paper prototype** - Sketches, wireframes
- **Clickable mockup** - Interactive prototype
- **Proof of concept** - Working subset

**Validation Questions:**
- "Does this match what you expected?"
- "Is anything missing?"
- "Would this solve your problem?"

### 🎬 Scenario Walkthrough

Walk stakeholders through realistic scenarios:

```
SCENARIO: [Scenario Name]
─────────────────────────────────────────────────────
Actor: [User role]
Goal: [What user wants to achieve]
Preconditions: [Starting state]

Steps:
1. User does [action]
   System responds [response]
   ✓ Stakeholder confirms correct
   
2. User does [action]
   System responds [response]
   ⚠️ Stakeholder notes: [feedback]
   
3. [Continue...]

Result: [Final outcome]
Stakeholder Feedback: [Summary of feedback]
─────────────────────────────────────────────────────
```

### 🏛️ Requirements Workshop

**Structure:**
```
VALIDATION WORKSHOP (2-4 hours)
─────────────────────────────────────────────────────
1. INTRODUCTION (15 min)
   • Goals and agenda
   • Participant introductions
   
2. REQUIREMENTS REVIEW (60-120 min)
   • Walk through each requirement
   • Stakeholders confirm or correct
   • Note all feedback
   
3. PRIORITY VALIDATION (30 min)
   • Confirm priorities are correct
   • Adjust if needed
   
4. GAP ANALYSIS (30 min)
   • "Is anything missing?"
   • "What haven't we covered?"
   
5. WRAP-UP (15 min)
   • Summarize decisions
   • Confirm next steps
─────────────────────────────────────────────────────
```

### ✅ User Acceptance Testing (UAT)

**UAT Checklist:**
```
BEFORE UAT:
☐ Requirements baselined
☐ Test environment ready
☐ Test data prepared
☐ UAT test cases written
☐ UAT testers identified and trained
☐ Defect tracking process in place

DURING UAT:
☐ Execute test cases
☐ Log all defects found
☐ Track test progress
☐ Escalate blockers

AFTER UAT:
☐ All critical defects resolved
☐ UAT sign-off obtained
☐ Go/No-go decision documented
```

## Step 4: Use Defect Classification

### Defect Types

| Type | Description | Example |
|------|-------------|---------|
| **Missing** | Requirement not specified | No error handling specified |
| **Wrong** | Incorrect requirement | Wrong calculation formula |
| **Ambiguous** | Multiple interpretations | "Fast response time" |
| **Inconsistent** | Contradicts another requirement | FR-001 conflicts with FR-005 |
| **Incomplete** | Partially specified | Missing edge cases |
| **Infeasible** | Cannot be implemented | "100% uptime" |

### Defect Severity

| Severity | Description | Action |
|----------|-------------|--------|
| **Critical** | Requirements unusable, project blocker | Fix immediately |
| **Major** | Significant impact, workaround difficult | Fix before baseline |
| **Minor** | Small impact, workaround exists | Fix if time permits |
| **Cosmetic** | Formatting, typos | Fix in next revision |

### Defect Log Template

```
┌────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ ID     │ REQ-ID   │ Type     │ Severity │ Description│ Status │
├────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ DEF-001│ FR-003   │ Ambiguous│ Major    │ "Fast" not │ Open   │
│        │          │          │          │ defined    │        │
├────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ DEF-002│ FR-007   │ Missing  │ Critical │ No error   │ Fixed  │
│        │          │          │          │ handling   │        │
└────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

## Step 5: Conduct Sign-off Process

### Sign-off Checklist
```
BEFORE SIGN-OFF:
☐ All sections complete (no TBDs)
☐ All critical defects resolved
☐ All major defects resolved or accepted
☐ Traceability complete
☐ Stakeholder walkthrough complete
☐ Final document distributed

SIGN-OFF CRITERIA:
☐ Stakeholders have reviewed
☐ Questions have been answered
☐ Conflicts have been resolved
☐ Priorities have been confirmed
```

### Sign-off Form Template

```
┌─────────────────────────────────────────────────────────────┐
│              REQUIREMENTS SIGN-OFF FORM                     │
├─────────────────────────────────────────────────────────────┤
│ Document: [Document Name]                                   │
│ Version: [X.Y]                                              │
│ Date: [YYYY-MM-DD]                                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ I confirm that I have reviewed the requirements document    │
│ and agree that it accurately represents the requirements    │
│ for the [Project Name] project.                             │
│                                                             │
│ Any known issues or reservations:                           │
│ [List any documented exceptions]                            │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ APPROVALS:                                                  │
│                                                             │
│ ┌──────────────────┬────────────┬─────────────┬───────────┐│
│ │ Name             │ Role       │ Signature   │ Date      ││
│ ├──────────────────┼────────────┼─────────────┼───────────┤│
│ │                  │ Sponsor    │             │           ││
│ │                  │ Product    │             │           ││
│ │                  │ Tech Lead  │             │           ││
│ │                  │ QA Lead    │             │           ││
│ │                  │ BA         │             │           ││
│ └──────────────────┴────────────┴─────────────┴───────────┘│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Step 6: Track V&V Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| **Defect Density** | Defects / Page or Defects / Requirement | Quality indicator |
| **Review Coverage** | Reviewed REQs / Total REQs | Completeness |
| **Defect Removal Efficiency** | Defects found before dev / Total defects | Process effectiveness |
| **Inspection Rate** | Pages / Hour | Efficiency |
| **Rework Rate** | Reworked REQs / Total REQs | Quality indicator |

## Best Practices

### ✅ DO:
- Schedule reviews early and often
- Use checklists consistently
- Document all defects found
- Track defects to closure
- Get formal sign-off

### ❌ DON'T:
- Skip reviews due to time pressure
- Combine verification with other meetings
- Rely only on informal reviews
- Allow undocumented sign-off
- Baseline with open critical defects

## Next Steps
After validation, proceed to:
- `/ba-traceability` to update RTM
- `/ba-writing` to fix defects
- Template workflows for final documentation
