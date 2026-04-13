---
description: Validate specs — INVEST check, quality gates, consistency, test generation
---

Start validation phase. Run the quality pipeline:

1. `@ba-validation` — INVEST check, ambiguity scan, defect detection (Health Score 0-100)
2. `@ba-quality-gate` — 8-dimensional scoring (PASS / CONDITIONAL / REJECT)
3. `@ba-consistency` — Cross-artifact alignment (US ↔ API ↔ DB ↔ BRD)
4. `@ba-test-gen` — Generate test cases from ACs (7 categories: Happy/Edge/Error/Security/Concurrency/Data/Perf)
5. `@ba-traceability` — Verify RTM coverage
6. `@ba-auditor` — Executive health dashboard

Ask the user:
- What to validate? (paste spec or provide file path)
- Target quality gate threshold? (default: 80%)

Output: Health Score, defect list by severity, test suite, consistency report, audit dashboard.

Exit criteria (all must be TRUE):
- [ ] INVEST: all stories pass
- [ ] AC coverage: ≥3 scenarios per story (happy/edge/error)
- [ ] Ambiguous terms: 0 detected
- [ ] Quality gate: ≥80% (PASS)
- [ ] Consistency: no mismatches US/API/DB/BRD
- [ ] Test coverage: ≥90% of ACs have test cases

Handoff: `/ba-deliver` if PASS. Back to `/ba-specify` if REJECT.
