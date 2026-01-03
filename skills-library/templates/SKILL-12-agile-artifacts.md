# 🟢 SKILL-12: AGILE ARTIFACTS
## Template Skill - User Stories, Use Cases, Epics

---

## 📌 SKILL METADATA

| Attribute | Value |
|-----------|-------|
| **Skill ID** | SKILL-12 |
| **Category** | 🟢 Template |
| **Load When** | Working in Agile/Scrum environment |
| **Dependencies** | SKILL-01, 02, 03 |
| **Output** | User Stories, Epics, Use Cases |

---

## 🎯 WHEN TO USE AGILE ARTIFACTS

| Use Agile Artifacts When | Don't Use When |
|--------------------------|----------------|
| ✓ Scrum/Kanban environment | ✗ Waterfall/formal documentation required |
| ✓ Iterative development | ✗ Fixed-price contract with detailed specs |
| ✓ Continuous delivery | ✗ Regulatory requires formal SRS |
| ✓ Close collaboration with PO | ✗ Offshore team needs complete specs |
| ✓ Flexible scope | ✗ Complex integrations (supplement with specs) |

---

## 📊 AGILE REQUIREMENTS HIERARCHY

```
┌─────────────────────────────────────────────────────────────┐
│              AGILE REQUIREMENTS HIERARCHY                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                      THEME                           │   │
│  │        Strategic goal or large initiative            │   │
│  │        Example: "Improve Customer Experience"        │   │
│  └───────────────────────┬─────────────────────────────┘   │
│                          │                                  │
│          ┌───────────────┼───────────────┐                  │
│          ▼               ▼               ▼                  │
│  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐     │
│  │     EPIC      │ │     EPIC      │ │     EPIC      │     │
│  │  Large body   │ │  Large body   │ │  Large body   │     │
│  │  of work      │ │  of work      │ │  of work      │     │
│  └───────┬───────┘ └───────────────┘ └───────────────┘     │
│          │                                                  │
│    ┌─────┼─────┬─────────┐                                  │
│    ▼     ▼     ▼         ▼                                  │
│  ┌────┐┌────┐┌────┐   ┌────┐                               │
│  │ US ││ US ││ US │   │ US │  User Stories                 │
│  │ 01 ││ 02 ││ 03 │   │ 04 │  (Fits in 1 sprint)          │
│  └──┬─┘└────┘└────┘   └────┘                               │
│     │                                                       │
│  ┌──┴───────────┐                                          │
│  │    TASKS     │  Technical tasks                         │
│  │  (Dev work)  │  (Hours, not story points)               │
│  └──────────────┘                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 USER STORY TEMPLATE

### Standard Format

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                      USER STORY                             ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ ID: US-[XXX]                     Epic: [Epic Name]          ┃
┃ Sprint: [Number]                 Points: [X]                ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                             ┃
┃ STORY:                                                      ┃
┃ ┌─────────────────────────────────────────────────────────┐ ┃
┃ │                                                         │ ┃
┃ │  As a [type of user],                                   │ ┃
┃ │  I want [goal/desire],                                  │ ┃
┃ │  So that [benefit/value].                               │ ┃
┃ │                                                         │ ┃
┃ └─────────────────────────────────────────────────────────┘ ┃
┃                                                             ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ ACCEPTANCE CRITERIA:                                        ┃
┃                                                             ┃
┃ Scenario 1: [Happy path title]                              ┃
┃   Given [precondition/context]                              ┃
┃   When [action/trigger]                                     ┃
┃   Then [expected outcome]                                   ┃
┃   And [additional outcome]                                  ┃
┃                                                             ┃
┃ Scenario 2: [Alternative path title]                        ┃
┃   Given [precondition/context]                              ┃
┃   When [action/trigger]                                     ┃
┃   Then [expected outcome]                                   ┃
┃                                                             ┃
┃ Scenario 3: [Error handling title]                          ┃
┃   Given [error condition]                                   ┃
┃   When [action/trigger]                                     ┃
┃   Then [error handling behavior]                            ┃
┃                                                             ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ DEFINITION OF DONE:                                         ┃
┃ ☐ Code complete and peer-reviewed                           ┃
┃ ☐ Unit tests written and passing (>80% coverage)            ┃
┃ ☐ All acceptance criteria verified                          ┃
┃ ☐ Integration tests passing                                 ┃
┃ ☐ Documentation updated                                     ┃
┃ ☐ No critical/major bugs                                    ┃
┃ ☐ Deployed to staging                                       ┃
┃ ☐ PO sign-off obtained                                      ┃
┃                                                             ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ ADDITIONAL INFO:                                            ┃
┃ Priority: [High/Medium/Low]                                 ┃
┃ Dependencies: [US-IDs or external]                          ┃
┃ Blocked by: [US-IDs or issues]                              ┃
┃ UI Mockup: [Link]                                           ┃
┃ Notes: [Additional context]                                 ┃
┃                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

### INVEST Criteria

| Criteria | Description | Check |
|----------|-------------|-------|
| **I**ndependent | Can be developed without depending on other stories | ☐ |
| **N**egotiable | Details can be discussed, not a contract | ☐ |
| **V**aluable | Delivers value to user/business | ☐ |
| **E**stimable | Team can estimate effort | ☐ |
| **S**mall | Fits in one sprint | ☐ |
| **T**estable | Clear criteria to verify | ☐ |

### User Story Examples

```
EXAMPLE 1: E-commerce
─────────────────────────────────────────────────────────────
As a returning customer,
I want to save items to a wishlist,
So that I can easily find and purchase them later.

Acceptance Criteria:
• Given I am logged in, When I click "Add to Wishlist" on a 
  product, Then the item appears in my wishlist
• Given I have items in wishlist, When I view my wishlist, 
  Then I see product image, name, price, and availability
• Given item is out of stock, When it becomes available, 
  Then I receive an email notification
─────────────────────────────────────────────────────────────

EXAMPLE 2: Internal Tool
─────────────────────────────────────────────────────────────
As a sales manager,
I want to export my team's monthly report to PDF,
So that I can share it in our monthly review meeting.

Acceptance Criteria:
• Given I am on the reports page, When I select date range 
  and click "Export PDF", Then a PDF downloads within 10 seconds
• Given the report has charts, When exported, Then charts 
  render clearly at print resolution
• Given the report exceeds 50 pages, When exported, Then 
  it includes a table of contents
─────────────────────────────────────────────────────────────
```

---

## 📚 EPIC TEMPLATE

```
╔═════════════════════════════════════════════════════════════╗
║                         EPIC                                ║
╠═════════════════════════════════════════════════════════════╣
║ ID: EPIC-[XXX]                                              ║
║ Name: [Epic Name]                                           ║
║ Theme: [Parent Theme if applicable]                         ║
║ Owner: [Product Owner / Business Owner]                     ║
╠═════════════════════════════════════════════════════════════╣
║                                                             ║
║ DESCRIPTION:                                                ║
║ [2-3 paragraph description of the epic, including           ║
║  business context, goals, and high-level scope]             ║
║                                                             ║
╠═════════════════════════════════════════════════════════════╣
║ BUSINESS VALUE:                                             ║
║ • [Value statement 1]                                       ║
║ • [Value statement 2]                                       ║
║ • [Measurable outcome/KPI]                                  ║
║                                                             ║
╠═════════════════════════════════════════════════════════════╣
║ SUCCESS CRITERIA:                                           ║
║ • [Measurable criterion 1]                                  ║
║ • [Measurable criterion 2]                                  ║
║ • [Measurable criterion 3]                                  ║
║                                                             ║
╠═════════════════════════════════════════════════════════════╣
║ SCOPE:                                                      ║
║                                                             ║
║ In Scope:                                                   ║
║ • [Feature/capability 1]                                    ║
║ • [Feature/capability 2]                                    ║
║                                                             ║
║ Out of Scope:                                               ║
║ • [Excluded item 1]                                         ║
║ • [Excluded item 2]                                         ║
║                                                             ║
╠═════════════════════════════════════════════════════════════╣
║ USER STORIES:                                               ║
║ ┌──────────┬────────────────────────────────┬─────────────┐ ║
║ │ Story ID │ Title                          │ Status      │ ║
║ ├──────────┼────────────────────────────────┼─────────────┤ ║
║ │ US-001   │ [Story title]                  │ Done        │ ║
║ │ US-002   │ [Story title]                  │ In Progress │ ║
║ │ US-003   │ [Story title]                  │ To Do       │ ║
║ │ US-004   │ [Story title]                  │ To Do       │ ║
║ └──────────┴────────────────────────────────┴─────────────┘ ║
║                                                             ║
║ Progress: [2/4 stories complete = 50%]                      ║
║                                                             ║
╠═════════════════════════════════════════════════════════════╣
║ DEPENDENCIES:                                               ║
║ • [EPIC-YYY]: [Dependency description]                      ║
║ • [External]: [External dependency]                         ║
║                                                             ║
╠═════════════════════════════════════════════════════════════╣
║ RISKS & ASSUMPTIONS:                                        ║
║                                                             ║
║ Risks:                                                      ║
║ • [Risk 1] - Mitigation: [Strategy]                         ║
║                                                             ║
║ Assumptions:                                                ║
║ • [Assumption 1]                                            ║
║                                                             ║
╠═════════════════════════════════════════════════════════════╣
║ TIMELINE:                                                   ║
║ Target Start: [Sprint X / Date]                             ║
║ Target End: [Sprint Y / Date]                               ║
║ Estimated Effort: [X story points / Y sprints]              ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝
```

---

## 🎭 USE CASE TEMPLATE

```
┌─────────────────────────────────────────────────────────────┐
│                    USE CASE SPECIFICATION                   │
├─────────────────────────────────────────────────────────────┤
│ Use Case ID: UC-[XXX]                                       │
│ Use Case Name: [Verb + Noun phrase]                         │
│ Version: [X.Y]                                              │
│ Last Updated: [Date]                                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ BRIEF DESCRIPTION:                                          │
│ [1-2 sentences describing the use case]                     │
│                                                             │
│ ACTORS:                                                     │
│ • Primary: [Main actor who initiates]                       │
│ • Secondary: [Supporting actors, if any]                    │
│ • System: [External systems involved]                       │
│                                                             │
│ TRIGGER:                                                    │
│ [What initiates this use case]                              │
│                                                             │
│ PRECONDITIONS:                                              │
│ • [Condition that must be true before UC starts]            │
│ • [Another precondition]                                    │
│                                                             │
│ POSTCONDITIONS (Success):                                   │
│ • [State of system after successful completion]             │
│                                                             │
│ POSTCONDITIONS (Failure):                                   │
│ • [State of system if use case fails]                       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ BASIC FLOW (Main Success Scenario):                         │
│                                                             │
│ 1. [Actor] [action - present tense]                         │
│ 2. [System] [response - present tense]                      │
│ 3. [Actor] [action]                                         │
│ 4. [System] [response]                                      │
│ 5. [System] [final action]                                  │
│ 6. Use case ends successfully                               │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ ALTERNATIVE FLOWS:                                          │
│                                                             │
│ 3a. [Condition for alternative]:                            │
│     3a.1. [System] [alternative action]                     │
│     3a.2. [Actor] [response]                                │
│     3a.3. Return to step 4                                  │
│                                                             │
│ 4a. [Another condition]:                                    │
│     4a.1. [Action]                                          │
│     4a.2. Use case continues from step 5                    │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ EXCEPTION FLOWS:                                            │
│                                                             │
│ 2a. [Error condition]:                                      │
│     2a.1. [System] displays error message "[message]"       │
│     2a.2. [System] logs the error                           │
│     2a.3. Use case ends unsuccessfully                      │
│                                                             │
│ *a. [At any time] User cancels:                             │
│     *a.1. [System] discards any unsaved changes             │
│     *a.2. [System] returns to previous screen               │
│     *a.3. Use case ends                                     │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ BUSINESS RULES:                                             │
│ • BR-001: [Rule description]                                │
│ • BR-002: [Rule description]                                │
│                                                             │
│ SPECIAL REQUIREMENTS:                                       │
│ • [Performance: Response < 2 seconds]                       │
│ • [Security: Requires authentication]                       │
│ • [Usability: Must work on mobile]                          │
│                                                             │
│ FREQUENCY: [How often this UC is executed]                  │
│ Example: ~500 times/day, peak during business hours         │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ RELATED USE CASES:                                          │
│ • <<includes>>: UC-YYY (always included)                    │
│ • <<extends>>: UC-ZZZ (optional extension)                  │
│ • <<precedes>>: UC-WWW (must happen first)                  │
│                                                             │
│ UI REFERENCE: [Link to mockup/wireframe]                    │
│                                                             │
│ RELATED USER STORIES: US-001, US-002, US-003                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Use Case Example

```
┌─────────────────────────────────────────────────────────────┐
│ UC-001: Process Customer Order                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Brief: Customer completes purchase of items in cart         │
│                                                             │
│ Primary Actor: Customer                                     │
│ Secondary: Payment Gateway, Inventory System                │
│                                                             │
│ Trigger: Customer clicks "Checkout" button                  │
│                                                             │
│ Preconditions:                                              │
│ • Customer is logged in                                     │
│ • Cart contains at least one item                           │
│ • Items in cart are in stock                                │
│                                                             │
│ Basic Flow:                                                 │
│ 1. Customer clicks "Checkout"                               │
│ 2. System displays order summary with items and total       │
│ 3. Customer confirms/updates shipping address               │
│ 4. System calculates shipping cost                          │
│ 5. Customer selects payment method                          │
│ 6. Customer enters payment details                          │
│ 7. System validates payment with Payment Gateway            │
│ 8. System reserves inventory                                │
│ 9. System creates order record                              │
│ 10. System sends confirmation email                         │
│ 11. System displays order confirmation page                 │
│                                                             │
│ Alternative Flow:                                           │
│ 5a. Customer selects saved payment method:                  │
│     5a.1. System retrieves saved payment info               │
│     5a.2. Continue from step 7                              │
│                                                             │
│ Exception Flow:                                             │
│ 7a. Payment declined:                                       │
│     7a.1. System displays "Payment declined" message        │
│     7a.2. System suggests alternative payment               │
│     7a.3. Return to step 5                                  │
│                                                             │
│ 8a. Item out of stock:                                      │
│     8a.1. System displays "Item unavailable" message        │
│     8a.2. System offers alternatives or removal             │
│     8a.3. Return to step 2                                  │
│                                                             │
│ Postcondition (Success): Order created, payment captured,   │
│ inventory reduced, confirmation sent                        │
│                                                             │
│ Postcondition (Failure): No order created, no payment,      │
│ cart preserved                                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📐 STORY MAPPING

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           USER STORY MAP                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  USER JOURNEY (Left to Right)                                               │
│  ═══════════════════════════════════════════════════════════════════════    │
│                                                                             │
│  ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐             │
│  │  Browse   │   │   Shop    │   │ Checkout  │   │  Receive  │  ACTIVITIES │
│  │ Products  │   │           │   │           │   │  Order    │  (Backbone) │
│  └─────┬─────┘   └─────┬─────┘   └─────┬─────┘   └─────┬─────┘             │
│        │               │               │               │                    │
│  ──────┼───────────────┼───────────────┼───────────────┼──────────────────  │
│        │               │               │               │                    │
│        ▼               ▼               ▼               ▼                    │
│  ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐             │
│  │  Search   │   │ Add to    │   │  Enter    │   │  Track    │  USER       │
│  │ Products  │   │ Cart      │   │ Address   │   │  Order    │  TASKS      │
│  ├───────────┤   ├───────────┤   ├───────────┤   ├───────────┤             │
│  │  Filter   │   │  View     │   │  Select   │   │  Receive  │             │
│  │  Results  │   │  Cart     │   │ Payment   │   │  Package  │             │
│  ├───────────┤   ├───────────┤   ├───────────┤   ├───────────┤             │
│  │   View    │   │  Update   │   │  Review   │   │  Return   │             │
│  │  Details  │   │  Qty      │   │  Order    │   │  Item     │             │
│  └───────────┘   └───────────┘   └───────────┘   └───────────┘             │
│                                                                             │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ MVP Line     │
│                                                                             │
│  ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐             │
│  │ Save to   │   │  Wishlist │   │  Apply    │   │  Leave    │  RELEASE 2  │
│  │ Wishlist  │   │  Mgmt     │   │  Coupon   │   │  Review   │             │
│  └───────────┘   └───────────┘   └───────────┘   └───────────┘             │
│                                                                             │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ Release 2    │
│                                                                             │
│  ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐             │
│  │  Product  │   │   Share   │   │  Multiple │   │ Subscribe │  FUTURE     │
│  │  Compare  │   │   Cart    │   │ Addresses │   │  Orders   │             │
│  └───────────┘   └───────────┘   └───────────┘   └───────────┘             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 STORY POINT ESTIMATION

### Fibonacci Scale

```
┌──────┬─────────────────────────────────────────────────────┐
│Points│ Guidance                                            │
├──────┼─────────────────────────────────────────────────────┤
│  1   │ Trivial - Simple config change, text update         │
│  2   │ Small - Single, well-understood change              │
│  3   │ Medium-Small - A few components, clear path         │
│  5   │ Medium - Multiple components, some complexity       │
│  8   │ Medium-Large - Significant work, some unknowns      │
│ 13   │ Large - Complex, consider splitting                 │
│ 21   │ Very Large - Too big, must split                    │
│  ?   │ Unknown - Need spike/research first                 │
└──────┴─────────────────────────────────────────────────────┘
```

### T-Shirt Sizing (Alternative)

| Size | Relative Effort | Example |
|------|-----------------|---------|
| **XS** | < 1 day | Config change |
| **S** | 1-2 days | Simple feature |
| **M** | 3-5 days | Standard feature |
| **L** | 1-2 weeks | Complex feature |
| **XL** | > 2 weeks | Epic - split it! |

---

## ✅ AGILE ARTIFACTS CHECKLIST

### User Story Checklist
```
☐ Follows "As a... I want... So that..." format
☐ Passes INVEST criteria
☐ Has clear acceptance criteria (Gherkin format)
☐ Small enough for one sprint
☐ Has story points estimated
☐ Definition of Done defined
☐ Dependencies identified
```

### Epic Checklist
```
☐ Has clear business value statement
☐ Success criteria defined and measurable
☐ Broken down into user stories
☐ Scope clearly defined (in/out)
☐ Timeline estimated
☐ Dependencies identified
☐ Risks documented
```

### Use Case Checklist
```
☐ Clear trigger and actors
☐ Preconditions stated
☐ Basic flow complete
☐ Alternative flows documented
☐ Exception flows for errors
☐ Postconditions defined
☐ Business rules referenced
```

---

## 🔄 REFINEMENT PROCESS

### Backlog Refinement Meeting

```
BEFORE REFINEMENT:
• PO prepares stories 2-3 sprints ahead
• Team reviews stories before meeting
• Questions identified

DURING REFINEMENT (1-2 hours):
1. PO presents each story (5 min)
2. Team asks clarifying questions (5 min)
3. Discuss acceptance criteria (5 min)
4. Estimate (planning poker) (5 min)
5. Identify dependencies/blockers (2 min)

AFTER REFINEMENT:
• Stories updated with details
• Large stories split if needed
• Ready stories marked "Refined"
```

### Definition of Ready (DoR)

```
A story is READY for sprint when:
☐ User story follows standard format
☐ Acceptance criteria are clear
☐ Story is estimated
☐ Dependencies are identified and resolved
☐ No blockers
☐ Small enough for sprint
☐ Team understands the story
☐ UI mockups available (if needed)
```

---

## 🔗 RELATED SKILLS

| For... | Load |
|--------|------|
| Elicitation for stories | SKILL-02 |
| Writing quality criteria | SKILL-03 |
| Prioritization (WSJF) | SKILL-05 |
| Formal documentation | SKILL-10 or SKILL-11 |

---

*Use this skill to work effectively in Agile environments with proper story structure and estimation.*
