# 🟡 SKILL-08: VALIDATION & VERIFICATION
## Specialized Skill - Requirements Quality Assurance

---

## 📌 SKILL METADATA

| Attribute | Value |
|-----------|-------|
| **Skill ID** | SKILL-08 |
| **Category** | 🟡 Specialized |
| **Load When** | Reviewing requirements, quality checks, sign-off |
| **Dependencies** | SKILL-01, SKILL-03 |
| **Output** | Reviewed requirements, defect reports, approvals |

---

## 🎯 MỤC ĐÍCH

Skill này cung cấp **techniques và checklists** để verify (đúng quy cách) và validate (đúng nhu cầu) requirements.

---

## ⚖️ VALIDATION vs VERIFICATION

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    VALIDATION vs VERIFICATION                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────┐    ┌─────────────────────────────┐        │
│  │       VERIFICATION          │    │        VALIDATION           │        │
│  ├─────────────────────────────┤    ├─────────────────────────────┤        │
│  │                             │    │                             │        │
│  │  "Are we building the       │    │  "Are we building the       │        │
│  │   product RIGHT?"           │    │   RIGHT product?"           │        │
│  │                             │    │                             │        │
│  │  • Checks against specs     │    │  • Checks against needs     │        │
│  │  • Internal process         │    │  • External process         │        │
│  │  • Done by QA/BA team       │    │  • Done with stakeholders   │        │
│  │  • Reviews, inspections     │    │  • Demos, UAT, prototypes   │        │
│  │  • Static testing           │    │  • Dynamic testing          │        │
│  │                             │    │                             │        │
│  │  Questions:                 │    │  Questions:                 │        │
│  │  • Is it well-written?      │    │  • Is this what you need?   │        │
│  │  • Is it complete?          │    │  • Does this solve problem? │        │
│  │  • Is it consistent?        │    │  • Is this valuable?        │        │
│  │                             │    │                             │        │
│  └─────────────────────────────┘    └─────────────────────────────┘        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔍 VERIFICATION TECHNIQUES

### 1️⃣ Inspection (Fagan Method)

```
┌─────────────────────────────────────────────────────────────┐
│                   FORMAL INSPECTION PROCESS                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. PLANNING (Moderator)                                    │
│     ├── Select materials to inspect                         │
│     ├── Identify participants (3-6 people)                  │
│     ├── Schedule meetings                                   │
│     └── Distribute materials                                │
│                                                             │
│  2. OVERVIEW (Author)                                       │
│     ├── Present the document/requirements                   │
│     ├── Explain context and goals                           │
│     └── Answer clarifying questions                         │
│                                                             │
│  3. PREPARATION (Individual, 2hrs max)                      │
│     ├── Each reviewer examines independently                │
│     ├── Note potential issues                               │
│     └── Use checklists                                      │
│                                                             │
│  4. INSPECTION MEETING (Team, 2hrs max)                     │
│     ├── Reader paraphrases requirements                     │
│     ├── Reviewers raise issues                              │
│     ├── Recorder logs defects                               │
│     └── NO solutions discussed (just identification)        │
│                                                             │
│  5. REWORK (Author)                                         │
│     └── Fix identified issues                               │
│                                                             │
│  6. FOLLOW-UP (Moderator)                                   │
│     └── Verify fixes are correct                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Inspection Roles

| Role | Responsibility |
|------|---------------|
| **Moderator** | Plans, facilitates, ensures process followed |
| **Author** | Created the requirements, answers questions |
| **Reader** | Paraphrases requirements during meeting |
| **Recorder** | Documents all defects found |
| **Reviewer** | Examines and identifies issues |

### 2️⃣ Walkthrough

| Aspect | Description |
|--------|-------------|
| **Purpose** | Author explains document to team |
| **Formality** | Less formal than inspection |
| **Focus** | Understanding and education |
| **Output** | Issues identified, suggestions |
| **Duration** | 30-60 minutes |

### 3️⃣ Peer Review

| Aspect | Description |
|--------|-------------|
| **Purpose** | Colleague reviews for quality |
| **Participants** | Author + 1-2 peers |
| **Formality** | Informal |
| **Focus** | Finding defects early |
| **Duration** | Varies |

---

## ✅ VERIFICATION CHECKLIST

### Individual Requirement Quality

```
┌─────────────────────────────────────────────────────────────┐
│           REQUIREMENT VERIFICATION CHECKLIST                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  COMPLETENESS:                                              │
│  ☐ Has unique ID                                            │
│  ☐ Has clear title                                          │
│  ☐ Description is complete                                  │
│  ☐ Has acceptance criteria                                  │
│  ☐ Source documented                                        │
│  ☐ Priority assigned                                        │
│  ☐ Dependencies identified                                  │
│                                                             │
│  CLARITY:                                                   │
│  ☐ Uses SHALL/SHOULD/MAY correctly                          │
│  ☐ No ambiguous words                                       │
│  ☐ Single interpretation possible                           │
│  ☐ Terms defined or in glossary                             │
│  ☐ Examples provided where helpful                          │
│                                                             │
│  CORRECTNESS:                                               │
│  ☐ Accurately represents stakeholder need                   │
│  ☐ Business rules are correct                               │
│  ☐ Data values/ranges are accurate                          │
│  ☐ References are valid                                     │
│                                                             │
│  CONSISTENCY:                                               │
│  ☐ No conflicts with other requirements                     │
│  ☐ Terminology used consistently                            │
│  ☐ Follows document conventions                             │
│  ☐ Aligns with project scope                                │
│                                                             │
│  TESTABILITY:                                               │
│  ☐ Can write specific test cases                            │
│  ☐ Pass/fail criteria clear                                 │
│  ☐ Measurable metrics defined                               │
│                                                             │
│  FEASIBILITY:                                               │
│  ☐ Technically achievable                                   │
│  ☐ Within budget constraints                                │
│  ☐ Within timeline                                          │
│  ☐ Resources available                                      │
│                                                             │
│  TRACEABILITY:                                              │
│  ☐ Traces to business need                                  │
│  ☐ Forward trace defined (design/test)                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Requirements Set Quality

```
┌─────────────────────────────────────────────────────────────┐
│           REQUIREMENTS SET VERIFICATION                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  COMPLETE SET:                                              │
│  ☐ All scope areas covered                                  │
│  ☐ All user roles addressed                                 │
│  ☐ Functional requirements complete                         │
│  ☐ Non-functional requirements defined                      │
│  ☐ Edge cases documented                                    │
│  ☐ Error handling specified                                 │
│                                                             │
│  CONSISTENT SET:                                            │
│  ☐ No contradicting requirements                            │
│  ☐ Prioritization is consistent                             │
│  ☐ Terminology is uniform                                   │
│                                                             │
│  ORGANIZED:                                                 │
│  ☐ Logically grouped                                        │
│  ☐ Easy to navigate                                         │
│  ☐ Cross-references work                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 VALIDATION TECHNIQUES

### 1️⃣ Prototyping

```
Fidelity Levels:
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Sketch  │ → │Wireframe │ → │ Mockup   │ → │Prototype │
│  (Paper) │   │ (Digital)│   │ (Visual) │   │(Clickable│
│  5-10min │   │ 1-2 hrs  │   │ 4-8 hrs  │   │ 1-2 days │
└──────────┘   └──────────┘   └──────────┘   └──────────┘
     │              │              │              │
     ▼              ▼              ▼              ▼
  Concept        Layout         Look &        Feel &
  Validation    Structure       Feel         Function
```

### 2️⃣ Scenario Walkthrough

**Process:**
1. Select key scenarios/use cases
2. Walk through with stakeholders step-by-step
3. Ask "What happens if...?" questions
4. Document gaps and issues

**Template:**
```
SCENARIO WALKTHROUGH RECORD

Scenario: [Name]
Participants: [Names]
Date: [Date]

Step-by-Step Review:
| Step | Requirement | Stakeholder Feedback | Issue? |
|------|-------------|---------------------|--------|
| 1    | [REQ-ID]    | [Feedback]          | ☐      |
| 2    | [REQ-ID]    | [Feedback]          | ☐      |

Issues Identified:
• [Issue 1]
• [Issue 2]

Action Items:
• [Action 1] - Owner: [Name]
```

### 3️⃣ Requirements Workshop

**Validation Workshop Agenda:**
```
1. Present requirements summary (15 min)
2. Walkthrough by module/feature (30-45 min)
3. Q&A and discussion (20 min)
4. Gap identification (15 min)
5. Priority confirmation (10 min)
6. Sign-off discussion (10 min)
```

### 4️⃣ User Acceptance Testing (UAT)

```
UAT for Requirements Validation:

PRE-UAT:
☐ Requirements documented and approved
☐ UAT scenarios prepared
☐ Test environment ready
☐ Users trained on system

DURING UAT:
☐ Users execute scenarios
☐ Compare behavior to requirements
☐ Log discrepancies
☐ Gather feedback

POST-UAT:
☐ Analyze results
☐ Categorize issues
☐ Update requirements if needed
☐ Get sign-off
```

---

## 🐛 DEFECT CLASSIFICATION

### Defect Types

```
┌─────────────────────────────────────────────────────────────┐
│               REQUIREMENTS DEFECT TYPES                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Type              │ Description           │ Example        │
│  ──────────────────┼───────────────────────┼────────────────│
│  MISSING           │ Required info absent  │ No error       │
│                    │                       │ handling       │
│  ──────────────────┼───────────────────────┼────────────────│
│  WRONG             │ Incorrect info        │ Wrong formula  │
│  ──────────────────┼───────────────────────┼────────────────│
│  AMBIGUOUS         │ Multiple meanings     │ "fast response"│
│  ──────────────────┼───────────────────────┼────────────────│
│  INCONSISTENT      │ Conflicts with other  │ Contradicting  │
│                    │ requirements          │ rules          │
│  ──────────────────┼───────────────────────┼────────────────│
│  INFEASIBLE        │ Cannot be implemented │ "100% uptime"  │
│  ──────────────────┼───────────────────────┼────────────────│
│  UNVERIFIABLE      │ Cannot be tested      │ "User-friendly"│
│  ──────────────────┼───────────────────────┼────────────────│
│  DUPLICATE         │ Same as another req   │ Repeated in    │
│                    │                       │ different words│
│  ──────────────────┼───────────────────────┼────────────────│
│  IRRELEVANT        │ Out of scope          │ Feature creep  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Defect Severity

| Severity | Definition | Action |
|----------|------------|--------|
| **Critical** | Blocks understanding or implementation | Must fix immediately |
| **Major** | Significant issue, workaround possible | Fix before baseline |
| **Minor** | Small issue, cosmetic | Fix when convenient |
| **Enhancement** | Suggestion for improvement | Consider for future |

### Defect Log Template

| ID | REQ-ID | Type | Severity | Description | Status | Resolution |
|----|--------|------|----------|-------------|--------|------------|
| D-001 | FR-003 | Ambiguous | Major | "Quick" not defined | Open | Define <2s |
| D-002 | FR-007 | Missing | Critical | No error handling | Fixed | Added AC |
| D-003 | FR-012 | Inconsistent | Major | Conflicts with FR-005 | Open | - |

---

## ✍️ SIGN-OFF PROCESS

### Sign-off Checklist

```
┌─────────────────────────────────────────────────────────────┐
│              REQUIREMENTS SIGN-OFF CHECKLIST                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PRE-REQUISITES:                                            │
│  ☐ All requirements reviewed                                │
│  ☐ All critical/major defects resolved                      │
│  ☐ Stakeholder validation complete                          │
│  ☐ Traceability verified                                    │
│  ☐ Document version finalized                               │
│                                                             │
│  SIGN-OFF MEETING:                                          │
│  ☐ Present final requirements                               │
│  ☐ Confirm understanding                                    │
│  ☐ Address final questions                                  │
│  ☐ Obtain formal approval                                   │
│                                                             │
│  POST SIGN-OFF:                                             │
│  ☐ Document baseline                                        │
│  ☐ Distribute approved version                              │
│  ☐ Archive working documents                                │
│  ☐ Enable change control                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Sign-off Form

```
┌─────────────────────────────────────────────────────────────┐
│              REQUIREMENTS APPROVAL FORM                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Document: [Document Name]                                   │
│ Version: [X.Y.Z]                                            │
│ Date: [YYYY-MM-DD]                                          │
│                                                             │
│ By signing below, I confirm that:                           │
│ • I have reviewed the requirements document                 │
│ • The requirements accurately represent the needs           │
│ • I approve proceeding to the next phase                    │
│                                                             │
│ ┌───────────────┬──────────────┬──────────────┬──────────┐  │
│ │ Name          │ Role         │ Signature    │ Date     │  │
│ ├───────────────┼──────────────┼──────────────┼──────────┤  │
│ │               │ Sponsor      │              │          │  │
│ │               │ Product Owner│              │          │  │
│ │               │ Tech Lead    │              │          │  │
│ │               │ QA Lead      │              │          │  │
│ │               │ User Rep     │              │          │  │
│ └───────────────┴──────────────┴──────────────┴──────────┘  │
│                                                             │
│ Comments/Conditions:                                        │
│ ________________________________________________________    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 V&V METRICS

| Metric | Formula | Target |
|--------|---------|--------|
| **Defect Density** | Defects / # of Requirements | < 0.5 |
| **Review Coverage** | Reviewed Reqs / Total Reqs | 100% |
| **Defect Removal Efficiency** | Defects Found / Total Defects | > 85% |
| **Review Effectiveness** | Critical Defects Found / Total Critical | > 95% |
| **Cycle Time** | Days from Draft to Approved | < 10 days |

---

## 🔗 RELATED SKILLS

| For... | Load |
|--------|------|
| Writing better requirements | SKILL-03 |
| Handling review conflicts | SKILL-06 |
| Managing approved changes | SKILL-07 |
| Document templates | SKILL-09, 10, 11 |

---

*Use this skill to ensure requirements are both correct (verification) and valuable (validation).*
