---
description: Full project health audit — coverage, quality, traceability, metrics
---

Run comprehensive project audit. Activate the audit pipeline:

1. `@ba-auditor` — Meta-agent, runs full project health scan
2. `@ba-traceability` — RTM coverage check (forward + backward)
3. `@ba-consistency` — Cross-artifact drift detection
4. `@ba-quality-gate` — Sample quality scoring across all artifacts
5. `@ba-metrics` — SPC metrics (defect density, cycle time, rework rate)
6. `@ba-wiki` — Knowledge health check (stale pages, contradictions)

Ask the user:
- Project path? (default: `outputs/<current-project>/`)
- Audit depth? (quick scan / full audit / executive summary only)

Also run automated scanners:
```bash
python3 .agent/scripts/coverage_checker.py outputs/<project>/ --verbose
python3 .agent/scripts/ba_search.py --stats
```

Output:
- Executive health dashboard (0-100% score across dimensions)
- Risk heatmap
- Open items requiring action before closure
- Recommendations ranked by impact

Health dimensions:
- Stakeholder Coverage (15%)
- Functional Scope Coverage (25%)
- AC Scenario Depth (20%)
- NFR Coverage (10%)
- Business Rule Quantification (10%)
- Requirements Traceability (10%)
- Domain Glossary (5%)
- Regulatory Compliance (5%)

Handoff: Back to `/ba-specify` or `/ba-validate` based on findings.
