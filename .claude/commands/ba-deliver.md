---
description: Deliver artifacts — export, publish to Jira/Confluence, change management
---

Start delivery phase. Package and distribute:

1. `@ba-export` — Compile to DOCX/PDF (Pandoc, compliance-checked)
2. `@ba-diagram` — Final diagrams (Confluence-ready Mermaid)
3. `@ba-jira` — Create/update tickets from validated User Stories
4. `@ba-confluence` — Publish BRD/SRS/FRD to Confluence space (with Mermaid support)
5. `@ba-communication` — Draft status report + executive summary
6. `@ba-change` — Go-live readiness (ADKAR, training plan, go-live checklist)

Ask the user:
- Target systems? (Jira project key, Confluence space key)
- Delivery format? (DOCX / Confluence page / Jira tickets / all)
- Audience? (Dev team / Stakeholders / Executives)

Output: Published artifacts, Jira tickets, Confluence pages, status report.

Pre-delivery checklist:
- [ ] Validation passed (Health Score ≥ 80%)
- [ ] Stakeholder approval (if required)
- [ ] No sensitive data in exports
- [ ] Version tagged in RTM

Handoff: `/ba-audit` for post-delivery health check.
