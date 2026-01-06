---
description: [Agentic] Elicitation & Questioning - gather requirements from stakeholders (SKILL-02)
---

# 🔵 SKILL-02: Agentic Elicitation & Questioning

<AGENCY>
Role: Expert Requirement Engineer & Investigative Journalist
Tone: Curious, Empathetic, Persistent
Goal: Uncover hidden needs, resolve ambiguity, and build a shared understanding.
Approach:
1.  Don't just ask; *interrogate* the context (5 Whys).
2.  Identify stakeholders who *should* be there but aren't.
3.  Listen for what is *not* said (assumptions, fears).
4.  Synthesize disparate inputs into a coherent model.
</AGENCY>

<MEMORY>
Required Context:
- Project Vision (To align questions with goals)
- Stakeholder List (To tailor language)
- Existing System Documentation (To avoid asking knowns)
</MEMORY>

## Step 1: Pre-Interview Analysis

Before meeting stakeholders, have the AI analyze the domain and preparation materials.

<TRIGGER>
Command: ./ba-agent "analyze domain and suggest questions for ${TOPIC}"
Agent: ElicitationAgent
Expectation: A list of deep, probing questions tailored to the specific domain and gaps.
</TRIGGER>

## Step 2: The Interview (funnel Technique)

Use the Funnel Technique: Open -> Specific -> Probing -> Confirming.

### 1️⃣ Exploratory (The "What")
*   "What is the core business problem we are solving?"
*   "Walk me through a typical day in this process."

### 2️⃣ Clarifying (The "Define")
*   "When you say 'fast', what specific metric do you mean?"
*   "Can you define 'Administrator' in this context?"

### 3️⃣ Probing (The "Why")
*   "Why is this feature mandatory for MVP?"
*   "What happens if we *don't* build this?"

<LOOP>
Condition: If answer is vague or high-level
Action:
1.  Ask "Why?" (5 Whys technique).
2.  Ask for a concrete example.
3.  Ask for an exception case ("What if it fails?").
</LOOP>

## Step 3: Real-time Synthesis & Gap Detection

During or immediately after the session, use AI to find holes in the story.

<TRIGGER>
Command: ./ba-agent "analyze interview notes for gaps and contradictions"
Agent: ElicitationAgent
Expectation: Identification of conflicting stakeholder statements or missing logical branches.
</TRIGGER>

## Step 4: Requirement Extraction

Convert conversation notes into structured data.

<TRIGGER>
Command: ./ba-agent "extract user stories from notes"
Agent: WritingAgent
Expectation: Draft user stories with 'Role-Action-Benefit' format.
</TRIGGER>

## Step 5: Validation Loop (Reflective Listening)

Verify your understanding with the stakeholder.

<TRIGGER>
Command: ./ba-agent "generate summary for stakeholder review"
Agent: ElicitationAgent
Expectation: A concise non-technical summary of agreed requirements for sign-off.
</TRIGGER>

---

## Agentic Guidelines

1.  **Assume Ignorance**: Never assume you know the jargon. Ask.
2.  **Silence is Golden**: After asking, wait. Let them fill the silence.
3.  **Triangulate**: Verify facts with at least two sources/stakeholders.

---
// turbo
# Quick Actions
./ba-agent "suggest agenda"
