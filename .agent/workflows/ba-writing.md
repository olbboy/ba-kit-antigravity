---
description: Requirements Writing & Quality Standards - write clear, testable, high-quality requirements (SKILL-03)
---

# 🔵 SKILL-03: Requirements Writing & Quality Workflow

## Purpose
Ensure all requirements are written to professional standards - clear, testable, complete, and verifiable.

## Step 1: Use Standard Requirement Template

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
├─────────────────────────────────────────────────────────────┤
│ Priority: [Must | Should | Could | Won't]                   │
│ Source: [Stakeholder/Document name]                         │
│ Status: [Draft | Review | Approved | Implemented]           │
│ Dependencies: [Related REQ-IDs]                             │
│ Traceability: [BR-ID → FR-ID → TC-ID]                       │
└─────────────────────────────────────────────────────────────┘
```

## Step 2: Apply RFC 2119 Keywords

| Keyword | Meaning | Usage |
|---------|---------|-------|
| **SHALL** | Mandatory, must be implemented | Core requirements |
| **SHALL NOT** | Prohibited | Constraints, security |
| **SHOULD** | Recommended, implement if possible | Important but not critical |
| **SHOULD NOT** | Not recommended | Discouraged behavior |
| **MAY** | Optional | Nice-to-have features |

## Step 3: Use Correct Sentence Patterns

### Pattern 1: Basic Functional
```
The system SHALL [verb] [object] [qualifier].

Example:
The system SHALL display customer orders sorted by date.
```

### Pattern 2: Conditional
```
WHEN [condition], the system SHALL [action].

Example:
WHEN payment fails, the system SHALL display an error message 
and log the transaction details.
```

### Pattern 3: User-focused
```
The system SHALL allow [user role] to [action] [object] [constraint].

Example:
The system SHALL allow administrators to export user data 
in CSV format.
```

### Pattern 4: With Purpose (Recommended)
```
The system SHALL [action] WHEN [condition] SO THAT [value/purpose].

Example:
The system SHALL send email notifications WHEN order status changes 
SO THAT customers are informed of their order progress.
```

## Step 4: Check Quality Attributes (INVEST+)

### Individual Requirement Quality Checklist

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

## Step 5: Avoid Ambiguous Words

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
| Large/Small | Relative | Define exact quantities |

## Step 6: Apply SMART Criteria

| Criteria | Description | ❌ Bad | ✅ Good |
|----------|-------------|--------|---------|
| **S**pecific | Clear, precise | "Show many products" | "Display 20 products per page" |
| **M**easurable | Quantifiable | "Fast response" | "Response time < 2 seconds" |
| **A**chievable | Realistic | "Support infinite users" | "Support 10,000 concurrent users" |
| **R**elevant | Business aligned | "Add pretty colors" | "Reduce checkout time by 30%" |
| **T**ime-bound | Has deadline | "Implement soon" | "Deploy in Sprint 5" |

## Step 7: Write Acceptance Criteria (Gherkin/BDD)

### Format
```gherkin
GIVEN [precondition/context]
WHEN [action/trigger]
THEN [expected result]
AND [additional result] (optional)
```

### Example
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

## Step 8: Use Common Requirement Patterns

### Data Validation Pattern
```
The system SHALL validate [field name] to ensure:
• [Validation rule 1]
• [Validation rule 2]
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

## Step 9: Pre-Review Self-Check

### Before Submitting for Review
```
CONTENT:
☐ Uses SHALL/SHOULD/MAY correctly
☐ No ambiguous words
☐ Has acceptance criteria
☐ Specifies error handling
☐ Covers edge cases

STRUCTURE:
☐ Has unique ID
☐ Has clear title
☐ Priority assigned
☐ Source documented
☐ Dependencies identified

QUALITY:
☐ One requirement per statement
☐ Verifiable/Testable
☐ No contradictions with others
☐ Traced to business need
☐ Feasible within constraints
```

## Writing DO's and DON'Ts

### ✅ DO:
- Use active voice: "The system shall display..." NOT "The report will be generated..."
- One requirement per statement - Split compound requirements
- Be specific with numbers: "Maximum 100 characters" NOT "Not too long"
- Include acceptance criteria - Always define how to test
- Reference standards: "Compliant with WCAG 2.1 Level AA"
- Provide examples for complex requirements
- Define all terms in glossary or inline

### ❌ DON'T:
- Use passive voice - Makes responsibility unclear
- Combine multiple requirements - Hard to trace and test
- Use vague terms - "Fast", "user-friendly", "easy"
- Describe implementation - Focus on WHAT, not HOW
- Use negative requirements when positive is clearer
- Assume reader knowledge - Define context explicitly
- Leave TBDs unresolved - Follow up before baseline

## Step 10: Auto-Generate Draft Story (Optional, Auto-Run)
// turbo
If you have BRD text and want a quick User Story draft:

```bash
./ba story --text "Your BRD requirement text here"
```

## Step 11: Final Quality Check (Auto-Run)
// turbo
Before submitting, run the expert linter:

```bash
./ba check [your_file.md]
```

## Step 12: Auto-Generate Test Code (Auto-Run)
// turbo
If your document has Gherkin Acceptance Criteria, instantly generate Playwright tests:

```bash
./ba gen [your_file.md]
```

This creates `[filename].spec.ts` with executable test stubs.

## Step 13: AI Deep Review (Auto-Run)
// turbo
Generate a specialized prompt for AI architectural review:

```bash
python3 tools/gen_prompt.py [your_file.md]
```

Copy the output and send to AI for expert-level review.

## Next Steps
After writing requirements, proceed to:
- `/ba-validation` for quality review
- `/ba-traceability` for managing RTM
- Template workflows for document creation
