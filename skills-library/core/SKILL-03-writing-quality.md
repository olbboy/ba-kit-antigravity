# 🔵 SKILL-03: REQUIREMENTS WRITING & QUALITY
## Core Skill - Writing Standards & Quality Assurance

---

## 📌 SKILL METADATA

| Attribute | Value |
|-----------|-------|
| **Skill ID** | SKILL-03 |
| **Category** | 🔵 Core |
| **Load Priority** | 3 |
| **Dependencies** | SKILL-01, SKILL-02 |
| **Output** | High-quality, verifiable requirements |

---

## 🎯 MỤC ĐÍCH

Skill này cung cấp **tiêu chuẩn viết requirements** và **quality checklist** để đảm bảo mọi yêu cầu đều clear, testable, và complete.

---

## 📐 REQUIREMENT STRUCTURE

### Standard Requirement Template

```
┌─────────────────────────────────────────────────────────────┐
│ REQ-ID: [Category]-[Number]                                 │
│ Example: FR-001, NFR-SEC-003                                │
├─────────────────────────────────────────────────────────────┤
│ Title: [Short descriptive name]                             │
├─────────────────────────────────────────────────────────────┤
│ Description:                                                │
│ The system SHALL [action] WHEN [condition/trigger]          │
│ SO THAT [purpose/value].                                    │
├─────────────────────────────────────────────────────────────┤
│ Acceptance Criteria:                                        │
│ • Given [context], When [action], Then [result]             │
│ • Given [context], When [action], Then [result]             │
├─────────────────────────────────────────────────────────────┤
│ Priority: [Must | Should | Could | Won't]                   │
│ Source: [Stakeholder/Document name]                         │
│ Status: [Draft | Review | Approved | Implemented]           │
│ Version: [X.Y]                                              │
│ Dependencies: [Related REQ-IDs]                             │
│ Traceability: [BR-ID → FR-ID → TC-ID]                       │
└─────────────────────────────────────────────────────────────┘
```

### Requirement ID Conventions

| Prefix | Category | Example |
|--------|----------|---------|
| **BR** | Business Requirement | BR-001 |
| **SR** | Stakeholder Requirement | SR-001 |
| **FR** | Functional Requirement | FR-001 |
| **NFR** | Non-Functional Requirement | NFR-001 |
| **NFR-PERF** | Performance | NFR-PERF-001 |
| **NFR-SEC** | Security | NFR-SEC-001 |
| **NFR-USA** | Usability | NFR-USA-001 |
| **NFR-REL** | Reliability | NFR-REL-001 |
| **UC** | Use Case | UC-001 |
| **US** | User Story | US-001 |

---

## 📝 WRITING GUIDELINES

### RFC 2119 Keywords

| Keyword | Meaning | Usage |
|---------|---------|-------|
| **SHALL** | Mandatory, must be implemented | Core requirements |
| **SHALL NOT** | Prohibited | Constraints, security |
| **SHOULD** | Recommended, implement if possible | Important but not critical |
| **SHOULD NOT** | Not recommended | Discouraged behavior |
| **MAY** | Optional | Nice-to-have features |

### Sentence Patterns

#### Pattern 1: Basic Functional
```
The system SHALL [verb] [object] [qualifier].

Example:
The system SHALL display customer orders sorted by date.
```

#### Pattern 2: Conditional
```
WHEN [condition], the system SHALL [action].

Example:
WHEN payment fails, the system SHALL display an error message 
and log the transaction details.
```

#### Pattern 3: User-focused
```
The system SHALL allow [user role] to [action] [object] [constraint].

Example:
The system SHALL allow administrators to export user data 
in CSV format.
```

#### Pattern 4: With Purpose (Recommended)
```
The system SHALL [action] WHEN [condition] SO THAT [value/purpose].

Example:
The system SHALL send email notifications WHEN order status changes 
SO THAT customers are informed of their order progress.
```

---

## ✅ QUALITY ATTRIBUTES (INVEST + More)

### Individual Requirement Quality

| Attribute | Question | ✓ |
|-----------|----------|---|
| **Atomic** | Does it express ONE single need? | ☐ |
| **Complete** | Is all info needed to implement present? | ☐ |
| **Consistent** | Does it conflict with other requirements? | ☐ |
| **Correct** | Does it accurately represent stakeholder need? | ☐ |
| **Feasible** | Can it be implemented within constraints? | ☐ |
| **Necessary** | Does it trace to a business need? | ☐ |
| **Unambiguous** | Is there only ONE interpretation? | ☐ |
| **Verifiable** | Can it be tested/measured? | ☐ |
| **Prioritized** | Is priority clearly assigned? | ☐ |
| **Traceable** | Can origin and links be identified? | ☐ |

### Requirements Set Quality

| Attribute | Check |
|-----------|-------|
| **Complete Set** | All requirements for scope captured? |
| **No Contradictions** | No conflicts between requirements? |
| **Modifiable** | Easy to update and maintain? |
| **Organized** | Logically structured and grouped? |
| **Ranked** | Clear prioritization across all? |

---

## 🚫 AMBIGUOUS WORDS TO AVOID

| ❌ Avoid | Problem | ✅ Replace With |
|----------|---------|-----------------|
| Fast, Quick | Not measurable | "Within 2 seconds" |
| User-friendly | Subjective | "WCAG 2.1 AA compliant" |
| Easy | Subjective | "In 3 clicks or less" |
| Appropriate | No criteria | Specify exact criteria |
| Flexible | Too broad | Define specific adaptations |
| Robust | Vague | Define failure handling |
| Seamless | Not measurable | Define integration specifics |
| Intuitive | Subjective | Define learnability metrics |
| State-of-the-art | Changes over time | Specify technology/version |
| As much as possible | No target | Define specific limit |
| Support | Unclear scope | Define specific capability |
| Handle | Unclear action | Define specific processing |
| Etc., And so on | Incomplete | List ALL items explicitly |
| Usually, Generally | Ambiguous exceptions | Define ALL scenarios |
| Efficient | Vague | Define specific metrics |
| Quickly | Not measurable | Define exact time |
| Large/Small | Relative | Define exact quantities |

---

## 📊 SMART CRITERIA

| Criteria | Description | ❌ Bad Example | ✅ Good Example |
|----------|-------------|----------------|-----------------|
| **S**pecific | Clear, precise | "Show many products" | "Display 20 products per page" |
| **M**easurable | Quantifiable | "Fast response" | "Response time < 2 seconds" |
| **A**chievable | Realistic | "Support infinite users" | "Support 10,000 concurrent users" |
| **R**elevant | Business aligned | "Add pretty colors" | "Reduce checkout time by 30%" |
| **T**ime-bound | Has deadline | "Implement soon" | "Deploy in Sprint 5" |

---

## 📋 ACCEPTANCE CRITERIA FORMAT

### Gherkin/BDD Format

```gherkin
GIVEN [precondition/context]
WHEN [action/trigger]
THEN [expected result]
AND [additional result] (optional)
```

### Examples

```gherkin
# Login Success
GIVEN user is on login page
AND user has valid credentials
WHEN user enters email and password
AND clicks "Login" button
THEN user is redirected to dashboard
AND welcome message displays user's name

# Login Failure
GIVEN user is on login page
WHEN user enters invalid credentials
AND clicks "Login" button
THEN error message "Invalid email or password" displays
AND login attempt is logged
AND user remains on login page
```

### Checklist Format (Alternative)

```
Acceptance Criteria for FR-001:
☐ User can enter email in valid format
☐ User can enter password (min 8 characters)
☐ System validates credentials against database
☐ Successful login redirects to dashboard
☐ Failed login shows error message
☐ Account locks after 5 failed attempts
```

---

## 🔍 REQUIREMENT REVIEW CHECKLIST

### Before Submitting for Review

```
┌─────────────────────────────────────────────────────────────┐
│              PRE-REVIEW SELF-CHECK                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CONTENT:                                                   │
│  ☐ Uses SHALL/SHOULD/MAY correctly                          │
│  ☐ No ambiguous words                                       │
│  ☐ Has acceptance criteria                                  │
│  ☐ Specifies error handling                                 │
│  ☐ Covers edge cases                                        │
│                                                             │
│  STRUCTURE:                                                 │
│  ☐ Has unique ID                                            │
│  ☐ Has clear title                                          │
│  ☐ Priority assigned                                        │
│  ☐ Source documented                                        │
│  ☐ Dependencies identified                                  │
│                                                             │
│  QUALITY:                                                   │
│  ☐ One requirement per statement                            │
│  ☐ Verifiable/Testable                                      │
│  ☐ No contradictions with others                            │
│  ☐ Traced to business need                                  │
│  ☐ Feasible within constraints                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📈 REQUIREMENTS METRICS

| Metric | Formula | Target |
|--------|---------|--------|
| **Volatility** | Changed Reqs / Total × 100% | < 15% |
| **Completeness** | Approved / Total Identified × 100% | > 95% |
| **Testability** | Verifiable / Total × 100% | 100% |
| **Traceability** | Traced / Total × 100% | 100% |
| **Defect Rate** | Defects Found / Total Reqs | < 0.5 |
| **Change Rate** | Changes per Week | Trend ↓ |
| **Approval Time** | Days from Draft to Approved | < 5 days |

---

## ✍️ WRITING DO's AND DON'Ts

### ✅ DO:

```
✓ Use active voice
  "The system shall display..." 
  NOT "The report will be generated..."

✓ One requirement per statement
  Split compound requirements

✓ Be specific with numbers
  "Maximum 100 characters"
  NOT "Not too long"

✓ Include acceptance criteria
  Always define how to test

✓ Reference standards
  "Compliant with WCAG 2.1 Level AA"

✓ Provide examples
  For complex requirements

✓ Define all terms
  In glossary or inline
```

### ❌ DON'T:

```
✗ Use passive voice
  Makes responsibility unclear

✗ Combine multiple requirements
  Hard to trace and test

✗ Use vague terms
  "Fast", "user-friendly", "easy"

✗ Describe implementation
  Focus on WHAT, not HOW

✗ Use negative requirements
  When positive is clearer

✗ Assume reader knowledge
  Define context explicitly

✗ Leave TBDs unresolved
  Follow up before baseline
```

---

## 🎯 COMMON PATTERNS

### Data Validation Pattern
```
The system SHALL validate [field name] to ensure:
• [Validation rule 1]
• [Validation rule 2]
• [Validation rule 3]
WHEN validation fails, the system SHALL display 
[specific error message] and prevent form submission.
```

### CRUD Pattern
```
The system SHALL allow [user role] to:
• CREATE new [entity] with [required fields]
• READ [entity] details and list view
• UPDATE [entity] [specific fields]
• DELETE [entity] with confirmation prompt
```

### Notification Pattern
```
The system SHALL send [notification type] to [recipient]
WHEN [trigger event] occurs
containing [specific information]
via [channel: email/SMS/push/in-app].
```

### Integration Pattern
```
The system SHALL integrate with [external system]
to [action/purpose]
using [protocol/method]
with [frequency/trigger]
handling [error scenarios].
```

---

## 🔗 RELATED SKILLS

| For... | Load |
|--------|------|
| NFR specifications | → SKILL-04 |
| Prioritization | → SKILL-05 |
| Traceability | → SKILL-07 |
| Reviews | → SKILL-08 |
| Document templates | → SKILL-09, 10, 11, 12 |

---

*This skill ensures every requirement you write is professional, clear, and verifiable.*
