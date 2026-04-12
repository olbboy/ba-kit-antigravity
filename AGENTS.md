# BA-Kit Antigravity — Project Rules

> These rules are automatically loaded by the Antigravity agent for every conversation in this workspace.
> Last updated: 2026-04-12

---

## 1. Confluence Data Center Rules

### 1.1 Code Macro Language Whitelist
When generating XHTML for Confluence DC, ONLY use these `language` values in code macros:
```
SAFE:    text, javascript, java, python, sql, xml, html, css, bash, ruby,
         groovy, csharp, c++, diff, php, scala, perl, yaml, powershell, none
```

**Map unsupported languages:**
- `json` → `javascript` (add `title="JSON"`)
- `gherkin` → `text` (add `title="Gherkin Scenarios"`)
- `typescript` → `javascript` (add `title="TypeScript"`)
- `mermaid` → DO NOT use code macro. Use `mermaid-macro` plugin instead.

### 1.2 Mermaid Diagrams
- Plugin: Stratus "Mermaid Diagrams for Confluence"
- Macro name: **`mermaid-macro`** (NOT `mermaid`, NOT `mermaid-cloud`, NOT `html`)
- XHTML: `<ac:structured-macro ac:name="mermaid-macro"><ac:plain-text-body><![CDATA[...]]></ac:plain-text-body></ac:structured-macro>`

### 1.3 Blocked Macros
- `ac:name="html"` is **BLOCKED** on CTS KMS. Never use it.

### 1.4 Validation
- Always validate uploads via `body.view` (NOT `body.storage`)
- Scan for `"Error rendering"` and `"Unknown macro"` in rendered output
- Use `confluence_xhtml.py` module for safe markdown→XHTML conversion

### 1.5 Reusable Module
```python
from confluence_xhtml import md_to_xhtml, validate_rendered_pages
xhtml = md_to_xhtml(markdown_content)  # Auto-applies all rules
```

---

## 2. Documentation Quality Rules

### 2.1 Template Completeness
Every module README must contain:
- [ ] Process Flow diagram (`graph TD`)
- [ ] Use Case diagram (`graph LR`)
- [ ] Metadata table
- [ ] User needs table
- [ ] NFR section

### 2.2 Test Suite Standards
Every test-cases.md must have:
- 7-column format: TC-ID | Category | Precondition | Steps | Input | Expected Result | Priority
- BVA (Boundary Value Analysis) section for numeric fields
- All 7 categories: Happy, Edge, Error, Security, Concurrency, Data, Performance
- Coverage Summary table

### 2.3 Batch Generation Limit
- Generate complex artifacts (test suites, API specs) for **max 3 modules** per session
- Quality degrades with larger batches due to context pressure

---

## 3. Confluence Sync Rules

### 3.1 Environment
- `CONFLUENCE_BASE_URL` and `CONFLUENCE_PAT` must be set in `.env`
- Target space: `CVH` (C-Vision Hub)
- Target instance: CTS Knowledge Hub (kms.cmcts.com.vn) — Data Center

### 3.2 Local vs Confluence Formats
- **Local markdown**: Keep native languages (`json`, `gherkin`, `mermaid`) — VSCode/GitHub renders them
- **Confluence upload**: Use `confluence_xhtml.py` which auto-maps to DC-safe equivalents
- Never manually construct XHTML with `language="json"` or `language="gherkin"`

### 3.3 Post-Upload Checklist
After every bulk upload:
1. Run `validate_rendered_pages()` scan
2. Verify 0 broken pages
3. Spot-check 2-3 pages visually via browser

---

## 4. Agent Skill References

| Skill | Reference Files |
|-------|----------------|
| confluence-connector | `references/confluence-dc-rendering-rules.md`, `scripts/confluence_xhtml.py` |
| ba-diagram | HARD RULES R1-R5 in SKILL.md |
| ba-test-gen | 7-category system, 7-column output format |
