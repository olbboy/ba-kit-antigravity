---
description: Enterprise Document Export - convert MD requirements to DOCX for Bank/Government compliance (SKILL-21)
---

# 📤 SKILL-21: Enterprise Document Export Workflow

## Purpose
Export BA documents (BRD, SRS, FRD) from Markdown to enterprise-compliant DOCX format using Pandoc and customer-specific reference templates.

## Prerequisites
- **Pandoc** must be installed: `brew install pandoc` (macOS) or `apt install pandoc` (Linux)
- Reference template in `references/` directory (optional but recommended)

## Step 1: Select Document Type

| Document Type | Template | Typical Audience |
|---------------|----------|------------------|
| BRD | SKILL-09 template | Business stakeholders |
| SRS | SKILL-10 template | Technical team |
| FRD | SKILL-11 template | Development team |
| User Stories | SKILL-12 template | Agile team |

## Step 2: Pre-Flight Validation (Auto-Run)
// turbo
Before exporting, validate the document for common issues:

```bash
./ba validate-export [your_file.md]
```

**What it checks:**
- ✓ Heading structure (no gaps like H1→H3)
- ✓ Unfilled placeholders ({{...}})
- ✓ Unresolved TBD/TODO markers
- ✓ Table column consistency
- ✓ Problematic characters

**Fix any issues before proceeding.**

## Step 3: Select Customer Profile

Available reference templates in `references/`:

| Profile | File | Description |
|---------|------|-------------|
| Default | `default_reference.docx` | Standard formatting |
| Bank Standard | `bank_standard.docx` | Bank brand guidelines |
| Government | `gov_standard.docx` | Government compliance |

To add a new customer:
1. Create a DOCX file with desired styles (Heading 1-6, Body Text, List Bullet, etc.)
2. Save as `references/[customer_name]_reference.docx`

## Step 4: Export to DOCX (Auto-Run)
// turbo
Generate the DOCX file:

```bash
./ba export [your_file.md] --customer [profile_name]
```

**Options:**
- `--customer bank_a` - Use specific customer reference
- `--no-toc` - Disable table of contents
- `--no-number` - Disable section numbering
- `-o output.docx` - Specify output filename

## Step 5: Post-Export Verification

After export, verify in Microsoft Word or LibreOffice:
- [ ] TOC generates correctly (right-click → Update Field)
- [ ] Headings have correct styles
- [ ] Tables render properly
- [ ] Page breaks are appropriate
- [ ] Headers/footers display correctly (if using DOCX shell)

## Complex Layout Requirements

If customer requires:
- Custom cover page
- Different first page header
- Section-specific headers/footers
- Landscape pages for wide tables

**Use DOCX Shell approach:**
1. Create pre-formatted DOCX shell with layout elements
2. Save in `shells/` directory
3. Use python-docx to merge content (advanced)

## Quick Reference

```bash
# Validate before export
./ba validate-export requirements.md

# Export with default styling
./ba export requirements.md

# Export with customer profile
./ba export brd.md --customer bank_a

# Export without TOC
./ba export srs.md --no-toc
```

## Next Steps
After exporting, proceed to:
- `/ba-validation` for final quality review
- Manual review in Word for layout polish
- Stakeholder distribution

## Related Skills
- SKILL-09: BRD Template
- SKILL-10: SRS Template
- SKILL-11: FRD Template
- SKILL-08: Validation & Verification
