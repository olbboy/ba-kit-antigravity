# 📘 BA-Kit Antigravity Workflows - Comprehensive Usage Guide

<p align="center">
  <img src="assets/logo.png" alt="BA-Kit Logo" width="150">
</p>

## 🧠 Philosophy & Deep Understanding

### The Core Principle: Layered Competency

The BA-Kit is built on a **layered competency model** where skills build upon each other:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     BA-KIT COMPETENCY PYRAMID                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                           ┌───────────────┐                             │
│                           │   TEMPLATES   │  ← OUTPUT LAYER             │
│                           │   (09-12)     │    Deliverables             │
│                           └───────┬───────┘                             │
│                                   │                                     │
│                    ┌──────────────┴──────────────┐                      │
│                    │     SPECIALIZED SKILLS      │  ← CONTEXT LAYER     │
│                    │         (04-08)             │    Apply as needed   │
│                    └──────────────┬──────────────┘                      │
│                                   │                                     │
│         ┌─────────────────────────┴─────────────────────────┐          │
│         │              CORE SKILLS (01-03)                   │  ← BASE  │
│         │   Identity → Elicitation → Writing Quality         │    LAYER │
│         └───────────────────────────────────────────────────┘          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Key Insight**: You cannot effectively use specialized skills without first establishing core skills. Think of it like a house:
- **Foundation** (SKILL-01 Identity): WHO you are, HOW you think
- **Walls** (SKILL-02 Elicitation): HOW you gather information
- **Roof** (SKILL-03 Writing): HOW you express requirements
- **Interior** (SKILL 04-08): WHAT specific techniques you apply
- **Furniture** (SKILL 09-12): WHAT documents you produce

---

## 🎯 Usage Scenarios & Decision Trees

### Scenario 1: Starting a New Project from Scratch

```
USER: "I need to analyze requirements for a new mobile banking app"

WORKFLOW PATH:
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 1: /ba-identity                                                    │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Activate BA Expert persona                                            │
│ • Map stakeholders (Bank executives, Product team, End users, IT)       │
│ • Determine power/interest grid                                         │
│ • Set communication style per stakeholder type                          │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 2: /ba-elicitation                                                 │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Start with EXPLORATORY questions:                                     │
│   - "Mục tiêu kinh doanh chính của ứng dụng mobile banking?"            │
│   - "Ai là đối tượng khách hàng mục tiêu?"                              │
│   - "Pain points lớn nhất của quy trình hiện tại?"                      │
│                                                                         │
│ • Progress to CLARIFYING questions:                                     │
│   - "Khi nói 'giao dịch nhanh', bạn đề cập đến bao nhiêu giây?"        │
│   - "'Khách hàng VIP' được định nghĩa như thế nào?"                    │
│                                                                         │
│ • Drill down with PROBING questions:                                    │
│   - "Điều gì xảy ra nếu mất kết nối giữa giao dịch?"                   │
│   - "Có ngoại lệ nào cho quy tắc xác thực 2 bước không?"               │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 3: /ba-prioritization (Apply when you have gathered requirements)  │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Use MoSCoW for quick categorization:                                  │
│   MUST: Login, Transfer, Balance check                                  │
│   SHOULD: Bill payment, Transaction history                             │
│   COULD: Investment products, Chatbot                                   │
│   WON'T: Crypto trading (Phase 2)                                       │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 4: /ba-writing + /ba-nfr                                           │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Write FR using standard template:                                     │
│   "The system SHALL allow authenticated users to transfer funds         │
│    WHEN they provide recipient account and amount                       │
│    SO THAT they can complete financial transactions remotely."          │
│                                                                         │
│ • Define NFRs using ISO 25010:                                          │
│   NFR-PERF-001: Response time < 2 seconds for transfers                 │
│   NFR-SEC-001: TLS 1.3 encryption, biometric authentication             │
│   NFR-REL-001: 99.99% availability                                      │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 5: Create deliverable using template                               │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Reference: templates/SKILL-09-brd-template.md (for business case)     │
│ • Reference: templates/SKILL-10-srs-template.md (for detailed specs)    │
│ • Reference: templates/SKILL-12-agile-artifacts.md (for user stories)   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### Scenario 2: Stakeholders Are in Conflict

```
USER: "The Sales team wants real-time reporting but IT says batch is more feasible"

WORKFLOW PATH:
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 1: /ba-identity (Quick refresh)                                    │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Remember: Stay NEUTRAL - you are facilitator, not decision maker      │
│ • Map both stakeholders:                                                │
│   Sales = High Interest, Medium Power                                   │
│   IT = Medium Interest, High Power (technical authority)                │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 2: /ba-conflict (PRIMARY WORKFLOW)                                 │
│ ─────────────────────────────────────────────────────────────────────── │
│ Apply Harvard Method - Focus on INTERESTS, not POSITIONS:               │
│                                                                         │
│ SALES POSITION: "We need real-time reports"                             │
│ SALES INTEREST: Need CURRENT data to make quick decisions               │
│                                                                         │
│ IT POSITION: "Batch processing is sufficient"                           │
│ IT INTEREST: Worried about system PERFORMANCE and COMPLEXITY            │
│                                                                         │
│ GENERATE OPTIONS:                                                       │
│ 1. Real-time for critical KPIs only, batch for detailed reports         │
│ 2. Near-real-time (5-minute refresh) as compromise                      │
│ 3. Real-time with IT-approved caching strategy                          │
│                                                                         │
│ USE OBJECTIVE CRITERIA:                                                 │
│ • What latency do competitors offer?                                    │
│ • What is the actual business impact of 5-min delay?                    │
│ • What is the infrastructure cost difference?                           │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 3: /ba-traceability                                                │
│ ─────────────────────────────────────────────────────────────────────── │
│ Document the decision:                                                  │
│ • Original conflict                                                     │
│ • Options considered                                                    │
│ • Final decision + rationale                                            │
│ • Who approved                                                          │
│ • Update RTM with resolved requirement                                  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### Scenario 3: Reviewing Existing Requirements Document

```
USER: "Please review this SRS for quality issues"

WORKFLOW PATH:
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 1: /ba-writing (Use as checklist reference)                        │
│ ─────────────────────────────────────────────────────────────────────── │
│ Check each requirement against quality criteria:                        │
│                                                                         │
│ ☐ Uses SHALL/SHOULD/MAY correctly?                                      │
│ ☐ Is atomic (one requirement per statement)?                            │
│ ☐ Is unambiguous (no "fast", "user-friendly", "etc.")?                 │
│ ☐ Is testable (has measurable acceptance criteria)?                     │
│ ☐ Is complete (no TBDs)?                                                │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 2: /ba-validation (PRIMARY WORKFLOW)                               │
│ ─────────────────────────────────────────────────────────────────────── │
│ Apply verification checklist:                                           │
│                                                                         │
│ INDIVIDUAL REQUIREMENT CHECK:                                           │
│ ☐ Has unique ID                                                         │
│ ☐ Has clear title                                                       │
│ ☐ Uses correct keywords                                                 │
│ ☐ Has acceptance criteria                                               │
│ ☐ Is feasible                                                           │
│ ☐ Traces to business need                                               │
│                                                                         │
│ REQUIREMENT SET CHECK:                                                  │
│ ☐ Complete - all needs captured                                         │
│ ☐ Consistent - no contradictions                                        │
│ ☐ No duplicates                                                         │
│ ☐ No gaps                                                               │
│                                                                         │
│ Log defects found:                                                      │
│ DEF-001: FR-003 uses "fast" - AMBIGUOUS - Major                         │
│ DEF-002: FR-007 has no acceptance criteria - INCOMPLETE - Major         │
│ DEF-003: FR-012 and FR-015 contradict - INCONSISTENT - Critical         │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 3: /ba-traceability                                                │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Run RTM health checks                                                 │
│ • Identify orphan requirements                                          │
│ • Identify untested requirements                                        │
│ • Update RTM with review findings                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### Scenario 4: Agile Sprint Planning

```
USER: "Help me create user stories for the checkout feature"

WORKFLOW PATH:
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 1: /ba-elicitation (Quick discovery)                               │
│ ─────────────────────────────────────────────────────────────────────── │
│ Ask 5W1H questions:                                                     │
│ • WHO: Which user roles check out? (Guest, Member, VIP)                 │
│ • WHAT: What actions? (Add to cart, Apply coupon, Pay, Confirm)         │
│ • WHEN: Any time constraints? (Session timeout, Flash sale)             │
│ • WHERE: Web only or mobile too?                                        │
│ • WHY: Business goal? (Increase conversion, Reduce abandonment)         │
│ • HOW: Payment methods? (Credit, Debit, Mobile wallet)                  │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 2: /ba-writing (Structure user stories)                            │
│ ─────────────────────────────────────────────────────────────────────── │
│ Use standard format + INVEST criteria:                                  │
│                                                                         │
│ ✅ GOOD USER STORY:                                                     │
│ "As a returning customer,                                               │
│  I want to save my payment method,                                      │
│  So that I can checkout faster on future purchases."                    │
│                                                                         │
│ Acceptance Criteria (Gherkin):                                          │
│ Given I am logged in and on checkout page                               │
│ When I check "Save this card for future purchases"                      │
│ Then my card is securely stored                                         │
│ And I see it pre-selected on next checkout                              │
│                                                                         │
│ INVEST Check:                                                           │
│ ☑ Independent - Can develop without other stories                       │
│ ☑ Negotiable - Details can be discussed                                 │
│ ☑ Valuable - Clear user benefit                                         │
│ ☑ Estimable - Team can estimate                                         │
│ ☑ Small - Fits in one sprint                                            │
│ ☑ Testable - Clear acceptance criteria                                  │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Step 3: /ba-prioritization                                              │
│ ─────────────────────────────────────────────────────────────────────── │
│ Apply WSJF for backlog ordering:                                        │
│                                                                         │
│ ┌────────────────────┬───────┬───────┬───────┬───────┬────────┐        │
│ │ Story              │ Value │ Time  │ Risk  │ Size  │ WSJF   │        │
│ ├────────────────────┼───────┼───────┼───────┼───────┼────────┤        │
│ │ Basic checkout     │   13  │   8   │   5   │   5   │  5.2   │        │
│ │ Save payment       │    5  │   3   │   2   │   2   │  5.0   │        │
│ │ Apply coupon       │    8  │   5   │   1   │   3   │  4.7   │        │
│ │ Guest checkout     │    8  │   8   │   3   │   5   │  3.8   │        │
│ └────────────────────┴───────┴───────┴───────┴───────┴────────┘        │
│                                                                         │
│ Sprint 1: Basic checkout (highest WSJF)                                 │
│ Sprint 2: Save payment, Apply coupon                                    │
│ Sprint 3: Guest checkout                                                │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Quick Command Reference

### When to Use Each Workflow

| You Want To... | Use This Command | What It Does |
|----------------|------------------|--------------|
| **Start any BA task** | `/ba-identity` | Activate expert persona, map stakeholders |
| **Interview stakeholders** | `/ba-elicitation` | Get question frameworks, funnel technique |
| **Write quality requirements** | `/ba-writing` | Get templates, quality checklists |
| **Specify NFRs** | `/ba-nfr` | Get ISO 25010 templates (Performance, Security, etc.) |
| **Prioritize features** | `/ba-prioritization` | Get MoSCoW, Kano, WSJF techniques |
| **Resolve conflicts** | `/ba-conflict` | Get Harvard Method, escalation matrix |
| **Track requirements** | `/ba-traceability` | Get RTM templates, change control |
| **Review requirements** | `/ba-validation` | Get V&V checklists, sign-off process |

---

## 🎓 Mastery Tips

### Tip 1: Chain Workflows Naturally
Don't think of workflows as isolated tools. They flow naturally:

```
/ba-identity → /ba-elicitation → /ba-writing → /ba-validation
     ↓              ↓                ↓               ↓
   WHO?         GATHER           DOCUMENT         VERIFY
```

### Tip 2: Always Start with Core Skills
Even for "quick" tasks, mentally activate:
1. **Identity** - Am I staying neutral? Who are my stakeholders?
2. **Elicitation** - Am I asking the right questions?
3. **Writing** - Am I documenting clearly?

### Tip 3: Use Templates as Starting Points
The templates (SKILL-09 to SKILL-12) are meant to be customized. Don't fill every field if not applicable.

### Tip 4: Document Decisions, Not Just Requirements
Use `/ba-traceability` and `/ba-conflict` to capture WHY decisions were made, not just WHAT was decided.

### Tip 5: Iterate, Don't Perfect
Requirements evolve. Use iterative approach:
- Draft → Review → Refine → Baseline
- Baseline → Change Request → Impact Analysis → Update

---

## 📋 Quick Start Commands for Common Tasks

```
┌─────────────────────────────────────────────────────────────────────────┐
│ TASK                              │ COMMAND SEQUENCE                    │
├───────────────────────────────────┼─────────────────────────────────────┤
│ New project kickoff               │ /ba-identity → /ba-elicitation      │
│                                   │ → /ba-prioritization                │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Write SRS                         │ /ba-writing → /ba-nfr               │
│                                   │ + templates/SKILL-10                │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Create user stories               │ /ba-elicitation → /ba-writing       │
│                                   │ + templates/SKILL-12                │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Resolve stakeholder disagreement  │ /ba-conflict                        │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Review requirements quality       │ /ba-validation → /ba-writing        │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Handle change request             │ /ba-traceability                    │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Define performance requirements   │ /ba-nfr                             │
└───────────────────────────────────┴─────────────────────────────────────┘
```

---

## 🚀 Getting Started Right Now

**Step 1**: Open any BA-related conversation

**Step 2**: Type `/ba-master` to see the complete workflow map

**Step 3**: Select the appropriate workflow based on your task

**Step 4**: Follow the step-by-step guidance in that workflow

**Example Prompt**:
```
I need to gather requirements for a new VIP customer recognition system 
at bank branches. Start with /ba-identity and /ba-elicitation workflows.
```

The AI will then:
1. Activate the BA Expert persona
2. Help you map stakeholders
3. Guide you through structured questioning
4. Document requirements in proper format
