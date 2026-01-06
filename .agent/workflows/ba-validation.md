---
description: [Agentic] Validation & Verification - ensure quality and correctness (SKILL-08)
---

# 🟡 SKILL-08: Agentic Validation & Verification

<AGENCY>
Role: Quality Assurance Lead & Requirements Validator
Tone: Critical, Precise, Uncompromising
Goal: Detect defects early, ensure 100% testability, and verify alignment with user needs.
Approach:
1.  Assume nothing is perfect; look for hidden ambiguity.
2.  Validate against INVEST criteria and Gherkin standards.
3.  Cross-reference with upstream documents (Business Case, Vision).
4.  If a requirement is untestable, flag it immediately.
</AGENCY>

<MEMORY>
Required Context:
- Requirement Documents (Target for validation)
- Domain Glossary (To check terminology consistency)
- NFR List (To ensure non-functional coverage)
</MEMORY>

## Step 1: Automated Quality Gates

Before manual review, run automated checks to catch syntax and structure errors.

<TRIGGER>
Command: ./ba-agent "validate quality of ${FILE}"
Agent: ValidationAgent
Expectation: Linting report identifying ambiguity, passive voice, and weak words.
</TRIGGER>

<LOOP>
Condition: If Critical Errors > 0 or Health Score < 85
Action:
1.  Auto-fix standard linting errors (e.g., replace "user-friendly" with specific metrics).
2.  Rewrite passive sentences to active voice.
3.  Re-run validation.
MaxAttempts: 3
</LOOP>

## Step 2: Gherkin & Testability Check

Ensure every requirement has clear acceptance criteria.

<TRIGGER>
Command: ./ba-agent "check gherkin syntax in ${FILE}"
Agent: ValidationAgent
Expectation: List of user stories missing scenarios or invalid Given/When/Then structures.
</TRIGGER>

## Step 3: Deep Reasoning & Edge Case Analysis

Use AI responsibility to find what humans missed.

<TRIGGER>
Command: ./ba-agent "analyze edge cases and security risks for ${FILE}"
Agent: ValidationAgent
Expectation: Report on missing error handling, security gaps, or logical contradictions.
</TRIGGER>

## Step 4: Traceability & Gap Analysis

<TRIGGER>
Command: ./ba-agent "check traceability gaps"
Agent: TraceabilityAgent
Expectation: List of orphaned requirements (no parent) or leaf requirements (no test cases).
</TRIGGER>

## Step 5: Final Review & Sign-off

Once automated checks pass, prepare for stakeholder sign-off.

<TRIGGER>
Command: ./ba-agent "generate defect report"
Agent: ExportAgent
Expectation: Summary of open defects and health status for sign-off meeting.
</TRIGGER>

---

## Agentic Guidelines

1.  **Zero Tolerence for "Fast"**: Any subjective adjective must be replaced with a number.
2.  **No Orphans**: Every requirement must have a parent (Need) and a child (Test).
3.  **INVEST Always**: Stories must be Independent, Negotiable, Valuable, Estimable, Small, Testable.

---
// turbo
# Quick Actions
./ba-agent "validate current directory"
