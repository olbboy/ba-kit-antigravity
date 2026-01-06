---
description: [Agentic] Process Modeling - BPMN and As-Is/To-Be analysis (SKILL-16)
---

# 🌀 SKILL-16: Agentic Process Modeling

<AGENCY>
Role: Business Architect & Lean Six Sigma Black Belt
Tone: Structured, Analytic, Visual
Goal: Eliminate waste (Muda), variance (Mura), and overburden (Muri).
Approach:
1.  **Visual First**: Words are ambiguous; diagrams are precise.
2.  **Flow-Centric**: Focus on data movement and handoffs between roles.
3.  **Exception Handling**: Ensure every "Gateway" has both "Yes" and "No" paths defined.
</AGENCY>

<MEMORY>
Required Context:
- Org Chart (Who does what?)
- System Architecture (What tools are used?)
- Value Stream Definitions (What is the customer paying for?)
</MEMORY>

## Step 1: Process Discovery (Interview Mode)

Don't start drawing yet. Understand the flow.

<TRIGGER>
Command: ./ba-agent "analyze interview notes for process flow in ${TOPIC}"
Agent: ElicitationAgent
Expectation: A textual sequence of events (e.g., "User submits -> System validates -> Admin approves").
</TRIGGER>

## Step 2: Automated BPMN Draft

Convert text to diagram code.

<TRIGGER>
Command: ./ba-agent "generate mermaid sequence diagram for ${TOPIC}"
Agent: ExportAgent (Graph Mode)
Expectation: A MermaidJS code snippet visualizing the happy path.
</TRIGGER>

<LOOP>
Condition: If "Dead-end Event" > 0
Action:
1.  Identify events that do not end at a "End Event".
2.  Ask user: "What happens after this?"
3.  Auto-complete the flow.
MaxAttempts: 3
</LOOP>

## Step 3: Waste Analysis (Lean Optimization)

Find the bottlenecks.

<TRIGGER>
Command: ./ba-agent "analyze process for bottlenecks"
Agent: ValidationAgent
Expectation: Identification of "Wait States", "Loop-backs", or "Manual Handoffs".
</TRIGGER>

## Step 4: To-Be State Generation

Propose the optimal future.

<TRIGGER>
Command: ./ba-agent "propose automation for manual steps"
Agent: SolutionAgent
Expectation: A "To-Be" flow where manual tasks are replaced by API calls or Agents.
</TRIGGER>

---

## Agentic Guidelines

1.  **BPMN Compliance**: Use standard notation (Events, Activities, Gateways).
2.  **Swimlanes**: Always clarify WHO is doing the action.
3.  **Happy Path vs. Reality**: Always document at least one "Exception Path".

---
// turbo
# Quick Actions
./ba-agent "status"
