# 📐 Requirements Modeling — Chi tiết về 15 Mô hình Phân tích
## Nguồn: The Software Requirements Memory Jogger (Gottesdiener) + BA Techniques (99 Tools) + UML Distilled (Fowler)

---

## 📌 MỤC ĐÍCH

Tài liệu này cung cấp **hướng dẫn chi tiết từng bước** cho việc tạo và sử dụng 15 mô hình phân tích yêu cầu. Trọng tâm là **cách các mô hình liên kết với nhau** (model threading) để đảm bảo tính đầy đủ.

---

## 🗂️ MODEL INTERCONNECTION MAP

```
                        ┌──────────────┐
                        │    Vision    │
                        │  Statement   │
                        └──────┬───────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌──────────┐    ┌──────────┐    ┌──────────┐
        │ Glossary │    │ Context  │    │ Business │
        │          │    │ Diagram  │    │ Policies │
        └────┬─────┘    └────┬─────┘    └────┬─────┘
             │               │               │
             │    ┌──────────┼──────────┐     │
             │    │          │          │     │
             │    ▼          ▼          ▼     │
             │  ┌─────┐  ┌──────┐  ┌──────┐  │
             │  │Actor│  │Event │  │Biz   │◄─┘
             │  │Table│  │Resp. │  │Rules │
             │  └──┬──┘  └──┬───┘  └──┬───┘
             │     │        │         │
             │     ▼        ▼         │
             │  ┌───────────────┐     │
             └─►│   USE CASES   │◄────┘
                └──────┬────────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │  Data    │ │  State   │ │ Dialog   │
    │  Model   │ │ Diagram  │ │   Map    │
    └──────────┘ └──────────┘ └──────────┘
          │            │            │
          └────────────┼────────────┘
                       ▼
              ┌────────────────┐
              │   Scenarios    │
              │   & Stories    │
              └────────┬───────┘
                       ▼
              ┌────────────────┐
              │  Prioritized   │
              │  Requirements  │
              └────────────────┘
```

---

## 🔁 CRUD MATRIX (Completeness Verification)

CRUD Matrix kiểm tra tính đầy đủ bằng cách ánh xạ **Use Cases × Data Entities**:

| Entity → | Customer | Job | Service | Contractor |
|----------|----------|-----|---------|-----------|
| **UC: Schedule Job** | R | C | R | R |
| **UC: Update Customer** | U | — | — | — |
| **UC: Assign Contractor** | R | U | R | R/U |
| **UC: Complete Job** | R | U | R | R |
| **UC: Delete Service** | — | — | D | — |

**Verification rules**:
- Every entity must have at least one **C** (Create) → Who creates it?
- Every entity must have at least one **R** (Read) → Who uses it?
- Every entity must have at least one **U** (Update) → Who modifies it?
- Every entity should have a **D** (Delete) or archive policy
- An empty row → a use case that doesn't touch data → suspicious
- An empty column → an entity no one uses → suspicious or external

---

## 📋 STEP-BY-STEP MODEL CREATION PROCEDURES

### Procedure 01: Create a Context Diagram

**Inputs**: Vision Statement, Stakeholder List
**Outputs**: Context Diagram with named data flows

```
Step 1  Draw the system as a single shape in the center
Step 2  Label it with the product name from vision statement
Step 3  Review stakeholder list — identify external entities:
        - Users who interact directly
        - External systems that exchange data
        - Organizations/regulators who govern behavior
Step 4  Draw each external entity around the system
Step 5  Draw arrows for data flows:
        - Arrow INTO system = data the system receives
        - Arrow OUT OF system = data the system produces
Step 6  Name each data flow using business terminology (from Glossary)
Step 7  Verify: Each external entity has at least one flow
Step 8  Verify: Each flow maps to at least one Event-Response
Step 9  Walk through with stakeholders for completeness
```

**Common mistakes**:
- Including internal components (this is NOT data flow diagram)
- Missing temporal events (system-initiated flows)
- Using technical names instead of business terms

---

### Procedure 02: Create an Event-Response Table

**Inputs**: Context Diagram, Vision Statement
**Outputs**: Complete event list with system responses

```
Step 1  List all data flows coming INTO the system from Context Diagram
Step 2  For each inflow, ask: "What event triggers this data?"
Step 3  Add temporal events: "What happens at end of day/month/quarter?"
Step 4  Add signal events: "What data arrives from other systems?"
Step 5  For each event, define:
        - Event Name (business language)
        - Event Type (Business / Temporal / Signal)
        - Stimulus (what triggers it)
        - Response (what the system must do)
        - Source actor (who/what triggers it)
Step 6  Number events: EVT-001, EVT-002, etc.
Step 7  Map each event to potential Use Cases
Step 8  Verify: Every context diagram flow has at least one event
Step 9  Verify: Events are external — not internal system operations
```

---

### Procedure 03: Create a Data Model (ERD)

**Inputs**: Glossary, Use Cases, Event-Response Table
**Outputs**: Entity-Relationship Diagram + Data Dictionary

```
Step 1  Scan Glossary for nouns → candidate entities
Step 2  Scan Use Cases for data referenced → candidate entities
Step 3  Filter: Is this a group of related data we need to store? → Entity
Step 4  For each entity:
        a. List all attributes (data elements)
        b. Identify the primary identifier (unique key)
        c. Define data type and constraints for each attribute
Step 5  Identify relationships between entities:
        a. Use active verbs (not "has" or "uses")
        b. Determine cardinality: 1:1, 1:M, M:M
        c. Determine optionality: Required or Optional
Step 6  Resolve M:M relationships with junction entities
Step 7  Normalize: Remove redundant attributes
Step 8  Create Data Dictionary:
        | Attribute | Type | Size | Required | Constraints | Source |
Step 9  Verify with CRUD Matrix: every entity appears in at least one UC
Step 10 Walk through sample data with stakeholders
```

---

### Procedure 04: Create a State Diagram

**Inputs**: Data Model, Event-Response Table
**Outputs**: State Diagram for critical entities

```
Step 1  Select entities with complex lifecycles from data model
        (Tip: entities with status/state attributes are candidates)
Step 2  List all possible states for the entity
Step 3  Determine initial state ("created" state)
Step 4  Determine final state(s) ("deleted", "archived", "completed")
Step 5  Arrange states in approximate time order
Step 6  For each transition:
        a. Identify triggering event (from Event-Response Table)
        b. Identify guard condition (business rule that must be true)
        c. Identify action (what happens during transition)
Step 7  Draw as: state --[event / guard / action]--> new state
Step 8  Create State-Data Matrix:
        | State | Attr1 Changes? | Attr2 Changes? | Rules Active |
Step 9  Verify: Every state is reachable from the initial state
Step 10 Verify: Every state has at least one exit (except final states)
Step 11 Verify: Every event maps to Event-Response Table
Step 12 Walk through state sequences with stakeholders
```

---

### Procedure 05: Create Use Cases

**Inputs**: Actor Table, Event-Response Table, Business Rules
**Outputs**: Use Case Specifications

```
Step 1  Review Event-Response Table
Step 2  Group related events → candidate Use Cases
Step 3  Name each UC: <strong action verb> + <noun>
        ✅ "Schedule Job"  ❌ "Job Scheduling Stuff"
Step 4  Assign Primary Actor (from Actor Table)
Step 5  Define trigger (event that initiates the UC)
Step 6  Define preconditions (what must be true before)
Step 7  Write Basic Flow (happy path):
        a. Number each step
        b. Actor step: "The [actor] does [action]"
        c. System step: "The system [response]"
Step 8  Identify Alternative Flows:
        a. At step N, ask: "What could go wrong?"
        b. At step N, ask: "What other paths exist?"
        c. Document as: "Na. If [condition], then..."
Step 9  Define postconditions (what is true after success)
Step 10 Reference business rules: "Subject to BR-nn"
Step 11 Verify with scenarios (walk through with concrete data)
Step 12 Create Use Case Diagram for overview
```

---

### Procedure 06: Create Business Rules

**Inputs**: Business Policies, Use Cases, Data Model, State Diagram
**Outputs**: Business Rules Catalog

```
Step 1  Scan Business Policies → extract individual rules
Step 2  Scan Use Cases → identify decision points and constraints
Step 3  Scan Data Model → identify validation rules for attributes
Step 4  Scan State Diagram → identify transition guard conditions
Step 5  Ask discovery questions:
        - "What decisions does the system make?"
        - "What must be true before X can happen?"
        - "What prevents X from happening?"
        - "What happens when conditions Y and Z are both true?"
Step 6  For each rule:
        a. Write as declarative atomic statement
        b. Categorize: Term / Fact / Constraint / Action Enabler
        c. Determine enforcement: Software vs. Business Process
        d. Assign: BR-ID, Owner, Effective Date, Source
Step 7  For complex rules with multiple conditions:
        a. Consider Decision Table (tabular format)
        b. Consider Decision Tree (graphical format)
Step 8  Verify: No rule contradicts another
Step 9  Verify: Rules are necessary — trace to business policy or need
Step 10 Verify: Rules are implementable — developers can build them
```

---

## 📊 DECISION TABLE CONSTRUCTION

**When to use**: A business rule with multiple conditions combined in complex ways.

**Structure**:
```
┌─────────────────────────────────────────────────────────┐
│                    DECISION TABLE                        │
├────────────────────┬──────┬──────┬──────┬──────┬────────┤
│ CONDITIONS         │ R1   │ R2   │ R3   │ R4   │ R5     │
├────────────────────┼──────┼──────┼──────┼──────┼────────┤
│ Customer type?     │ New  │ New  │ Rep  │ Rep  │ Rep    │
│ Order > $5,000?    │ Y    │ N    │ Y    │ Y    │ N      │
│ Credit score > 700?│ -    │ -    │ Y    │ N    │ -      │
├────────────────────┼──────┼──────┼──────┼──────┼────────┤
│ ACTIONS            │      │      │      │      │        │
├────────────────────┼──────┼──────┼──────┼──────┼────────┤
│ Require deposit?   │ Y    │ Y    │ N    │ Y    │ N      │
│ Apply discount?    │ N    │ N    │ Y    │ N    │ N      │
│ Require approval?  │ Y    │ N    │ N    │ Y    │ N      │
└────────────────────┴──────┴──────┴──────┴──────┴────────┘
```

**Steps**:
1. Identify all conditions (Boolean or enumerated values)
2. Identify all possible actions
3. Create all possible condition combinations
4. For each combination, determine which actions apply
5. Simplify: combine rules where a condition doesn't matter (use "-")
6. Verify: total combinations = product of condition values
7. Test with real scenarios to validate

---

## 📊 DECISION TREE CONSTRUCTION

**When to use**: Same as decision table, but stakeholders prefer visual sequential logic.

```
                     Customer Type?
                    /              \
                  New            Repeat
                  /                 \
           Order > $5K?        Order > $5K?
           /       \            /        \
         Yes       No         Yes        No
          |         |          |          |
   [Deposit +   [Deposit   Credit>700?  [No special
    Approval]    only]     /       \     treatment]
                         Yes       No
                          |         |
                    [Discount,  [Deposit +
                     No deposit] Approval]
```

---

## 🧪 MODEL VALIDATION TECHNIQUES

### Cross-Model Validation

| Check | How |
|-------|-----|
| **Context ↔ Events** | Every context flow has at least one event |
| **Events ↔ Use Cases** | Every event maps to at least one UC |
| **Actors ↔ Use Cases** | Every actor participates in at least one UC |
| **Use Cases ↔ Data** | CRUD Matrix — every UC touches data |
| **Data ↔ States** | Every entity with status attribute has a state diagram |
| **States ↔ Events** | Every state transition maps to an event |
| **Rules ↔ Use Cases** | Every rule is referenced by at least one UC |
| **Rules ↔ Policies** | Every rule traces to a business policy or need |

### Thread Testing (Scenario Walk-Through)

```
Step 1  Select a scenario (specific path through a use case)
Step 2  Walk through the scenario step by step:
        a. Does the actor exist in Actor Table?
        b. Does the trigger match an event in Event-Response Table?
        c. Does the data referenced exist in Data Model?
        d. Do decision points match Business Rules?
        e. Do state changes match State Diagram?
        f. Does the dialog navigation match Dialog Map?
Step 3  Mark any model element NOT covered by any scenario → gap
Step 4  Repeat for:
        - Happy path scenarios
        - Edge case scenarios
        - Error/exception scenarios
```

---

## 🎯 MODEL SELECTION GUIDE BY PROJECT TYPE

### New Development
```
Essential:   Vision → Context → Events → Actors → Use Cases → Data → Rules → Quality
Recommended: State Diagrams, Dialog Map, Activity Diagrams
Optional:    DFD, Class Model (if OOP)
```

### Enhancement / Version 2
```
Essential:   As-Is Context → Delta Analysis → Modified UCs → Modified Data → Rules
Recommended: State Diagram (for entities with changed lifecycle)
Optional:    Full re-modeling if major restructuring
```

### COTS Selection
```
Essential:   Process Map → Actors → Use Cases → Rules → Data → UAT → Quality
Key Focus:   Gap Analysis between COTS features and business needs
```

### Bug Fix / Correction
```
Essential:   Affected Rules → Affected Use Cases → Regression UAT → Quality
Key Focus:   Impact Analysis through Trace Matrix
```
