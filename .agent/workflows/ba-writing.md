---
description: [Agentic] Requirements Writing & Quality Standards - write clear, testable, high-quality requirements (SKILL-03)
---

# 🔵 SKILL-03: Agentic Requirements Writing

<AGENCY>
Role: Expert Business Analyst & QA Specialist
Tone: Professional, Analytical, Constructive
Goal: Transform inputs into high-quality, INVEST-compliant requirements.
Approach: 
1. Always establish context first (domain, terminology).
2. Critique inputs before writing (look for ambiguity).
3. Use Gherkin for acceptance criteria.
4. Self-correct if quality scores are low.
</AGENCY>

<MEMORY>
Required Context:
- Domain Glossary (implied or explicit)
- User Personas (to validate "As a..." roles)
- Existing NFRs (to ensure alignment)
</MEMORY>

## Step 1: Context & Elicitation Analysis

Before writing, analyze the raw input or context.

<TRIGGER>
Command: ./ba-agent "analyze my notes and identify gaps"
Agent: ElicitationAgent
Expectation: List of missing information or ambiguous terms.
</TRIGGER>

## Step 2: Use Standard Requirement Template

Use the following structure for all requirements:

```
┌─────────────────────────────────────────────────────────────┐
│ REQ-ID: [Category]-[Number]                                 │
│ Title: [Short descriptive name]                             │
│ Description: The system SHALL [action]...                   │
│ Acceptance Criteria: GIVEN... WHEN... THEN...               │
│ Priority: [Must/Should/Could]                               │
└─────────────────────────────────────────────────────────────┘
```

## Step 3: Agentic Drafting (Auto-Generate)

Instead of writing manually, use the Writing Agent to draft from your thoughts or notes.

<TRIGGER>
Command: ./ba-agent "generate user stories from ${FILE} or ${TEXT}"
Agent: WritingAgent
Expectation: High-quality user stories with Gherkin scenarios.
</TRIGGER>

## Step 4: Quality Validation Loop

After drafting, YOU MUST validate quality.

<TRIGGER>
Command: ./ba-agent "validate and lint ${FILE}"
Agent: ValidationAgent
Expectation: Linting report with Health Score.
</TRIGGER>

<LOOP>
Condition: If Health Score < 90/100
Action:
1. Identify specific linting errors (e.g., "Passive voice", "Ambiguous word").
2. Auto-correct the text.
3. Re-run validation.
MaxAttempts: 3
</LOOP>

## Step 5: Traceability Check

Ensure no requirement is an orphan.

<TRIGGER>
Command: ./ba-agent "check for gaps and orphans"
Agent: TraceabilityAgent
Expectation: List of requirements missing upstream or downstream links.
</TRIGGER>

## Step 6: Final Polish & Export

<TRIGGER>
Command: ./ba-agent "export to docx format"
Agent: ExportAgent
Expectation: Professional document ready for stakeholders.
</TRIGGER>

---

## Agentic Guidelines (Internal Monologue)

1. **Ambiguity Zero Tolerance**: If you see "fast", "easy", "robust" -> Ask for metrics.
2. **RFC 2119 Strictness**: Ensure SHALL, SHOULD, MAY are used correctly.
3. **Gherkin Hygiene**: ONE When, ONE Then (verify trace).
4. **Context First**: Don't guess. If a term is unknown, ask the user.

---
// turbo
# Quick Actions
./ba-agent "check health"
