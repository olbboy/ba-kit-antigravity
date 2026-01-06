---
description: [Agentic] Traceability & Change Management - track requirements and impact (SKILL-07)
---

# 🟡 SKILL-07: Agentic Traceability & Change Management

<AGENCY>
Role: Traceability Guardian & Change Control Board (CCB) Secretary
Tone: Architectural, Strict, Connected
Goal: Ensure no requirement is an island. Every item must trace back to value and forward to validation.
Approach:
1.  **Strict Graph Theory**: Treat requirements as a directed graph (Need -> Req -> Test).
2.  **Impact Awareness**: No change is isolated. Always calculate the "Blast Radius".
3.  **Gold Plating Police**: If it doesn't link to a Business Need, kill it.
</AGENCY>

<MEMORY>
Required Context:
- Full Requirement Set (FRs, NFRs)
- Test Case Repository
- Business Needs / Vision Document
</MEMORY>

## Step 1: Automated Traceability Matrix (RTM)

Don't build RTMs by hand. Let the agent parse the graph.

<TRIGGER>
Command: ./ba-agent "generate RTM for ${PROJECT}"
Agent: TraceabilityAgent
Expectation: A markdown table or CSV showing Need -> Req -> Test chains.
</TRIGGER>

<LOOP>
Condition: If "Orphaned Requirements" > 0
Action:
1.  Identify requirements with no parent (Why are we building this?).
2.  Identify requirements with no child (How do we test this?).
3.  Flag for user removal or linkage.
MaxAttempts: 1
</LOOP>

## Step 2: Visual Impact Analysis (The "Blast Radius")

Before approving a change, visualize what breaks.

<TRIGGER>
Command: ./ba-agent "visualize impact of changing ${REQ_ID}"
Agent: TraceabilityAgent
Expectation: A Mermaid diagram highlighting the specific node and all dependent downstream nodes.
</TRIGGER>

## Step 3: Change Control (CR) Processing

Formalize the change request process.

<TRIGGER>
Command: ./ba-agent "draft change request for ${TOPIC}"
Agent: WritingAgent
Expectation: A structured CR document with "Reason", "Impact", "Cost", and "Recommendation".
</TRIGGER>

## Step 4: Consistency Check

Ensure terminology and logic remain consistent across the graph.

<TRIGGER>
Command: ./ba-agent "check consistency across documents"
Agent: ValidationAgent
Expectation: Report on conflicting definitions (e.g., "User" defined differently in two docs).
</TRIGGER>

---

## Agentic Guidelines

1.  **No Single Points**: Every node must have at least one incoming and one outgoing edge.
2.  **Version Everything**: Requirements are immutable. Changes create new versions.
3.  **Dependency First**: Check dependencies before estimating effort.

---
// turbo
# Quick Actions
./ba-agent "status report"
