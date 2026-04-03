# 📜 Business Rules — Quy Tắc Kinh Doanh Chi Tiết
## Nguồn: The Software Requirements Memory Jogger (Gottesdiener) + BA Techniques (99 Tools)

---

## 📌 MỤC ĐÍCH

Tài liệu này cung cấp **hướng dẫn chuyên sâu về Business Rules** — từ phân loại, phát hiện, đặc tả đến quản lý. Business Rules là yếu tố thường bị bỏ sót nhất trong phân tích yêu cầu, dẫn đến logic hệ thống không chính xác.

---

## 🧠 TẠI SAO BUSINESS RULES QUAN TRỌNG?

> "Business rules constrain the business — not just the software. They represent the encoded knowledge of how the business operates."
> — Ellen Gottesdiener

**Vấn đề**: Business rules thường bị chôn vùi trong:
- Email chains giữa stakeholders
- Trong đầu của SMEs ("ai cũng biết mà")
- Embedded trong code cũ mà không được document
- Scattered across use cases mà không được tập trung

**Giải pháp**: Tách riêng Business Rules thành một artifact độc lập, được quản lý riêng biệt.

---

## 📋 4 LOẠI BUSINESS RULES

### Type 1: Terms (Thuật ngữ)

**Định nghĩa**: Từ ngữ và khái niệm kinh doanh với ý nghĩa chính xác.

| Sub-type | Ý nghĩa | Example |
|----------|---------|---------|
| **Basic Term** | Định nghĩa khái niệm | "A **Job** is a set of services performed at a customer's location" |
| **Derivation** | Giá trị được tính toán | "**Total Cost** = Sum(Service Costs) + Tax + Surcharge" |
| **Inference** | Kết luận từ điều kiện | "If customer has 10+ jobs this year, customer is a **Repeat Customer**" |

**Template cho Derivation**:
```
<derived term> = <formula/algorithm>

Example: 
  Late Fee = Outstanding Balance × 0.015 × Days Overdue
  Customer Tier = CASE
    WHEN annual_spend > 50000 THEN 'Platinum'
    WHEN annual_spend > 20000 THEN 'Gold'
    ELSE 'Standard'
  END
```

**Template cho Inference**:
```
If <condition> then <term classification>

Example:
  If a customer's total annual spending exceeds $50,000,
  then the customer is classified as a Platinum Customer.
```

---

### Type 2: Facts (Sự kiện)

**Định nghĩa**: Kết nối giữa các terms — mô tả quan hệ giữa các khái niệm kinh doanh.

**Template**:
```
<term A> <verb phrase> <term B>

Examples:
  Each Customer may place one or more Orders.
  Each Order contains one or more Line Items.
  Each Contractor is assigned to one Region.
  Each Region may have zero or more Contractors.
```

**Connection**: Facts map directly to relationships in the Data Model (ERD).

---

### Type 3: Constraints (Ràng buộc)

**Định nghĩa**: Ngăn cấm hoặc hạn chế hành vi — things the system MUST NOT allow.

**Templates**:
```
<subject> must [not] <verb phrase>

If <condition> then <subject> must [not] <verb phrase>

On <event> then <subject> must [not] <verb phrase>

Examples:
  A Customer with overdue payments must not schedule new Jobs.
  The system must not allow deletion of a Job that has been dispatched.
  An Order must not exceed the Customer's credit limit.
  If a Contractor's license has expired, the Contractor must not be assigned to Jobs.
```

**5 sub-categories**:
| Sub-type | Meaning | Example |
|----------|---------|---------|
| **State Constraint** | Entity must be in certain state | "Job must be 'Approved' before dispatch" |
| **Attribute Constraint** | Limits on data values | "Quantity must be between 1 and 999" |
| **Set Constraint** | Limits on collection membership | "Max 5 services per job" |
| **Uniqueness Constraint** | No duplicates | "Customer email must be unique" |
| **Relationship Constraint** | Limits on associations | "Contractor can have max 3 active jobs" |

---

### Type 4: Action Enablers (Kích hoạt Hành động)

**Định nghĩa**: Khi điều kiện thỏa mãn, hệ thống tự động thực hiện hành động.

**Template**:
```
If <condition> then <action>
On <event> if <condition> then <action>
When <trigger> and <condition>, <system action>

Examples:
  If a Repeat Customer's total Jobs for the year exceed $5,000, 
  offer a 15% discount on future services.
  
  On Job Completion, if final cost differs from estimate by > 10%,
  notify the Customer and request approval.
  
  When payment is received and account balance reaches zero,
  update Customer status to "Good Standing".
```

---

## 🔍 BUSINESS RULE DISCOVERY TECHNIQUES

### Discovery Questions (Ask these during elicitation)

**From Use Cases**:
- "What must be true before [actor] can perform [action]?"
- "What prevents [action] from happening?"
- "What happens when [condition X] and [condition Y] are both true?"
- "Are there any exceptions to this step?"
- "What determines which path the user takes?"

**From Data Model**:
- "What are valid values for [attribute]?"
- "Can [entity] exist without [related entity]?"
- "How many [related entities] can one [entity] have?"
- "When is [attribute] required vs optional?"
- "How is [derived attribute] calculated?"

**From State Diagram**:
- "What conditions must be met to move from [state A] to [state B]?"
- "Can the entity go back to a previous state?"
- "What happens if the entity is in [state] when [event] occurs?"

**From Business Policies**:
- "What regulations govern [business area]?"
- "What internal policies affect [process]?"
- "What happens when [policy] conflicts with [user request]?"

### Discovery Sources

```
┌─────────────────────────────────────────────────────────────────┐
│                 BUSINESS RULE SOURCES                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  EXTERNAL:                                                      │
│  ═════════                                                     │
│  • Government regulations                                      │
│  • Industry standards (ISO, PCI-DSS, HIPAA)                   │
│  • Contractual obligations                                     │
│  • Tax laws and financial regulations                          │
│                                                                 │
│  INTERNAL:                                                      │
│  ═════════                                                     │
│  • Company policies & handbooks                                │
│  • Standard operating procedures (SOPs)                        │
│  • Management decisions & memos                                │
│  • Institutional knowledge (SME interviews)                    │
│  • Legacy system logic (reverse engineering)                   │
│                                                                 │
│  DERIVED:                                                       │
│  ════════                                                      │
│  • Use case decision points                                    │
│  • Data validation requirements                                │
│  • State transition conditions                                 │
│  • Workflow routing logic                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📝 BUSINESS RULES CATALOG FORMAT

| Field | Description |
|-------|-------------|
| **BR-ID** | Unique identifier (BR-001, BR-002, etc.) |
| **Rule Name** | Descriptive short name |
| **Statement** | Atomic declarative statement |
| **Category** | Term / Fact / Constraint / Action Enabler |
| **Source** | Where the rule came from (regulation, policy, SME) |
| **Owner** | Person responsible for the rule |
| **Enforcement** | Software / Business Process / Both |
| **Related Use Cases** | UC-IDs that reference this rule |
| **Related Entities** | Data entities governed by this rule |
| **Effective Date** | When the rule takes effect |
| **Expiration Date** | If applicable |
| **Priority** | Must / Should / Could |
| **Status** | Draft / Reviewed / Approved / Deprecated |
| **Notes** | Additional context, exceptions, edge cases |

### Example Catalog Entry

```
BR-ID:             BR-042
Rule Name:         Overdue Customer Job Restriction
Statement:         A Customer with payments overdue by more than 30 days
                   must not be allowed to schedule new Jobs.
Category:          Constraint (State)
Source:            Finance Department Policy FP-2024-07
Owner:             CFO Office
Enforcement:       Software (automated check at job creation)
Related Use Cases: UC-001 (Schedule Job), UC-015 (Create Customer)
Related Entities:  Customer, Job, Payment
Effective Date:    2024-01-01
Priority:          Must
Status:            Approved
Notes:             Exception: Customers with approved credit extension
                   (see BR-043) are exempt from this rule.
```

---

## 📊 DECISION TABLE — Detailed Guide

### When to Use Decision Tables

- Multiple conditions combine to determine different outcomes
- Business users think in terms of "if X and Y then Z"
- Rules have ≤ 6 conditions (otherwise becomes unwieldy)
- Testing coverage needs to be comprehensive

### Construction Steps

```
Step 1  List all CONDITIONS (inputs that affect the decision)
Step 2  List all ACTIONS (outputs/results of the decision)
Step 3  Create all possible condition combinations:
        - For Boolean conditions: 2^n combinations
        - For enumerated conditions: product of all values
Step 4  For each combination, mark which actions apply
Step 5  Simplify:
        a. If changing one condition doesn't affect actions → use "-"
        b. Merge duplicate action columns
Step 6  Verify: are any combinations impossible? Remove them.
Step 7  Verify: are any combinations missing? Add them.
Step 8  Walk through with SME using real scenarios
```

### Completeness Check

```
For n Boolean conditions: should have 2^n rules (before simplification)

Example: 3 conditions = 2^3 = 8 possible rules
If you have only 5 rules → 3 combinations are missing or merged

After simplification: verify every real input maps to exactly one rule
```

### Testing from Decision Tables

Each column (rule) becomes a test case:
- Set up conditions as specified in the column
- Execute the business process
- Verify that ONLY the specified actions occur
- Verify that non-specified actions do NOT occur

---

## 📊 DECISION TREE — Detailed Guide

### When to Use Decision Trees

- Rules are evaluated sequentially (order matters)
- Stakeholders prefer visual over tabular
- Some conditions are only relevant based on prior conditions
- Fewer than 4 levels of nesting (otherwise hard to read)

### Construction Steps

```
Step 1  Identify the first/most important condition
Step 2  Draw branches for each possible value
Step 3  At each branch, identify the next relevant condition
Step 4  Continue until all paths reach an action (leaf node)
Step 5  Label each leaf with the resulting action(s)
Step 6  Verify: every path reaches a leaf (no dead ends)
Step 7  Verify: no two paths lead to conflicting actions
Step 8  Walk through each path with SME
```

### Converting Between Tables and Trees

```
Decision Table → Decision Tree:
  Pick the condition with fewest values → root node
  Branch for each value
  At each branch, repeat with remaining conditions

Decision Tree → Decision Table:
  Each path from root to leaf = one column in the table
  Conditions on the path → condition row values
  Leaf action → action row values
```

---

## ⚠️ COMMON BUSINESS RULE MISTAKES

| Mistake | Example | Fix |
|---------|---------|-----|
| **Procedural** (describes sequence) | "First check credit, then check inventory" | "Order must not be placed if credit limit exceeded OR inventory insufficient" |
| **Ambiguous** | "Large orders get a discount" | "Orders exceeding $10,000 receive a 5% discount" |
| **Compound** (multiple rules in one) | "Members get free shipping and 10% off" | Split into BR-001 (free shipping) + BR-002 (10% discount) |
| **Missing boundary** | "Recent customers get priority" | "Customers registered within the last 90 days receive priority scheduling" |
| **Missing exception** | "All orders require approval" | "Orders over $500 require manager approval. Exception: Auto-approved for VIP customers." |
| **Circular reference** | "A is true if B, B is true if A" | Identify which is the root condition and restructure |
| **Technology-specific** | "Field must match regex ^[a-z]+$" | "Username must contain only lowercase letters" |

---

## 🔗 BUSINESS RULES vs OTHER ARTIFACTS

```
┌─────────────────────────────────────────────────────────────────┐
│         BUSINESS RULES CONNECTION MAP                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Business          ──derive──►  Business Rules                  │
│  Policies                           │                           │
│                                     │                           │
│                         ┌───────────┼───────────┐               │
│                         │           │           │               │
│                         ▼           ▼           ▼               │
│                    Use Cases   Data Model   State Diagram        │
│                    (decision   (validation  (transition          │
│                     points)    rules)       guards)             │
│                         │           │           │               │
│                         └───────────┼───────────┘               │
│                                     ▼                           │
│                              Test Cases                         │
│                         (each rule → tests)                     │
│                                                                 │
│  Traceability Chain:                                            │
│  Policy → Rule → Use Case Step → Functional Req → Test Case    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✅ BUSINESS RULES CHECKLIST

- [ ] Mỗi rule có BR-ID duy nhất?
- [ ] Mỗi rule là declarative (không procedural)?
- [ ] Mỗi rule là atomic (một rule = một statement)?
- [ ] Mỗi rule trace về ít nhất một business policy hoặc need?
- [ ] Mỗi rule được đánh dấu enforcement: Software vs Business Process?
- [ ] Mỗi rule được liên kết với Use Cases liên quan?
- [ ] Đã kiểm tra consistency — không rule nào mâu thuẫn?
- [ ] Complex rules đã được thể hiện bằng Decision Table/Tree?
- [ ] Mỗi rule có Owner rõ ràng?
- [ ] Đã xác định exceptions cho mỗi constraint?
- [ ] Đã review với SME và được approve?
