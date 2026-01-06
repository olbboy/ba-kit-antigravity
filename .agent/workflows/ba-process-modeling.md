---
description: Process Modeling - BPMN and As-Is/To-Be analysis (SKILL-16)
---

# Process Modeling Workflow

Use this workflow when you need to model business processes, create BPMN diagrams, or conduct As-Is/To-Be analysis.

## Prerequisites
Load SKILL-16 from `specialized/SKILL-16-process-modeling.md`

## Workflow Steps

### 1. Identify Process Scope
- Define the process name and purpose
- Identify the process owner and stakeholders
- Determine the process boundaries (start/end events)
- Classify the process level (Value Chain, Process, Activity)

### 2. Document Current State (As-Is)
- Map current process flow using BPMN 2.0 notation
- Identify all roles/swimlanes involved
- Document decision points (gateways)
- Capture pain points and inefficiencies
- Measure key metrics:
  - Cycle time
  - Wait time
  - % Complete & Accurate

### 3. Analyze Process Issues
- Identify bottlenecks and delays
- Document handoff problems
- Find redundant or manual steps
- Calculate process efficiency ratio

### 4. Design Future State (To-Be)
- Propose improvements addressing identified issues
- Create To-Be process diagram
- Define new roles or automation opportunities
- Estimate improvement in metrics

### 5. Create Value Stream Map (Optional)
- Map the complete value stream
- Identify value-add vs non-value-add activities
- Calculate takt time and lead time
- Highlight waste (7 wastes of Lean)

### 6. Document Process Specification
- Write detailed process description
- Define inputs, outputs, and controls
- Specify business rules
- Link to related requirements (FRD/SRS)

## Output Artifacts
- BPMN 2.0 Process Diagram
- As-Is/To-Be Comparison
- Process Specification Document
- Value Stream Map (if applicable)

## Step 7: Visualize Process Connections (Auto-Run)
// turbo
Generate knowledge graph to visualize process relationships:

```bash
./ba graph
```

## Related Skills
- SKILL-02: Elicitation (for process discovery)
- SKILL-13: Data Modeling (for data flows)
- SKILL-14: UX Research (for user experience in processes)
- SKILL-15: Workshop Facilitation (for process mapping sessions)
