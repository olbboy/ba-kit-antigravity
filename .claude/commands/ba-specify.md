---
description: Write formal specifications — User Stories, BRD, SRS, API contracts
---

Start specification phase. Activate the writing pipeline:

1. `@ba-writing` — Draft the core spec (User Stories with Gherkin AC, BRD, SRS, API spec)
2. `@ba-nfr` — Add Non-Functional Requirements (ISO 25010 quality attributes)
3. `@ba-traceability` — Link requirements to business objectives (RTM)
4. `@ba-diagram` — Generate diagrams (ERD, sequence, flowchart) for the spec

Ask the user:
- What to specify? (Feature, module, full system)
- Target template? (User Story / BRD / SRS / PRD / FRD)
- Any mockups to extract from? (Visual Scan)

Output: Complete specification with AC, NFRs, diagrams, and traceability.

Boundary rules:
- Every User Story MUST have ≥3 Acceptance Criteria (Happy + Edge + Error)
- Every requirement MUST trace to a business objective
- No ambiguous terms ("fast", "user-friendly", "scalable")

Handoff: `/ba-validate` to quality-check before shipping.
