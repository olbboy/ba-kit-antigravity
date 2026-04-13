---
description: Analyze raw requirements — process modeling, data modeling, systems thinking
---

Start analysis phase. Activate relevant agents based on what's being analyzed:

- Process flow? → `@ba-process` (BPMN swimlanes, waste analysis)
- Data structures? → `@ba-data` (ERD, Data Dictionary, DFD)
- System dynamics? → `@ba-systems` (causal loops, leverage points)
- Root cause? → `@ba-root-cause` (5 Whys, Fishbone, Pareto)
- Business rules? → `@ba-business-rules` (decision tables, rule catalog)
- Conflict? → `@ba-conflict` (Harvard Negotiation, positions vs interests)
- Priority? → `@ba-prioritization` (MoSCoW, RICE, WSJF)

Ask the user:
- What needs analysis? (process / data / rules / conflict / priority)
- Do you have As-Is documentation or starting from scratch?

Output: Analysis artifacts (BPMN diagrams, ERDs, decision tables, root cause reports).

Handoff: `/ba-specify` to write formal specs, `/ba-validate` if analysis reveals gaps.
