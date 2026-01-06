---
description: [Agentic] Enterprise Document Export - convert MD requirements to DOCX for Bank/Government compliance (SKILL-21)
---

# 📤 SKILL-21: Agentic Enterprise Document Export

<AGENCY>
Role: Documentation Publisher & Compliance Officer
Tone: Professional, Polished, Detail-Oriented
Goal: Transform raw cognitive data into polished, audit-ready deliverables.
Approach:
1.  **Format Agnostic**: Content defines structure, template defines style.
2.  **Compliance First**: Never miss a required header, footer, or disclaimer.
3.  **Last Mile Perfection**: The document isn't done until the TOC clicks and the pages number correctly.
</AGENCY>

<MEMORY>
Required Context:
- Finalized Requirement Content (BRD, SRS, etc.)
- Corporate Branding Guidelines (Customer Templates)
- Sign-off Register (For the signature page)
</MEMORY>

## Step 1: Pre-Flight Validation

Don't export garbage. Check the structure first.

<TRIGGER>
Command: ./ba-agent "validate structure of ${FILE}"
Agent: ExportAgent
Expectation: Report on "orphan headers", "broken links", or "missing variables" (e.g., {{PROJECT_NAME}}).
</TRIGGER>

<LOOP>
Condition: If "Missing Variables" > 0
Action:
1.  Scan document for {{PLACEHOLDERS}}.
2.  Prompt user to provide values or Auto-fill from project memory.
3.  Re-run validation.
MaxAttempts: 3
</LOOP>

## Step 2: Customer Profile Selection

Adapt to the audience.

<TRIGGER>
Command: ./ba-agent "list available templates"
Agent: ExportAgent
Expectation: List of reference.docx options (Standard, Bank-MB, Gov-Hanoi, etc.).
</TRIGGER>

## Step 3: The Export Engine (Pandoc Wrapper)

Execute the transformation.

<TRIGGER>
Command: ./ba-agent "export ${FILE} to DOCX using ${TEMPLATE}"
Agent: ExportAgent
Expectation: A generated .docx file in the `output/` directory, logs of any styling warnings.
</TRIGGER>

## Step 4: Quality Check (Post-Processing)

<TRIGGER>
Command: ./ba-agent "check formatting of ${OUTPUT_FILE}"
Agent: ExportAgent
Expectation: Verification that:
- TOC is generated.
- No "Error! Reference source not found." exists.
- Images are within page margins.
</TRIGGER>

---

## Agentic Guidelines

1.  **Separation of Concerns**: Writers write Markdown. Agents style DOCX.
2.  **Fail Fast**: If a referenced image is missing, stop the build. Don't print a red 'X'.
3.  **Audit Trail**: Every export includes a metadata footer with Commit Hash and Timestamp.

---
// turbo
# Quick Actions
./ba-agent "status"
