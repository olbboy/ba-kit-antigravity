# BA-Kit Reference Templates

This directory contains customer-specific DOCX reference templates for the Enterprise Document Export (SKILL-21).

## How It Works

When you run `./ba export file.md --customer bank_a`, the exporter looks for:
1. `references/bank_a_reference.docx` - Customer-specific template
2. `references/default_reference.docx` - Fallback if customer template not found

## Creating a Reference Template

1. Open Microsoft Word
2. Define styles for:
   - Heading 1-6 (font, size, spacing)
   - Body Text / Normal
   - List Bullet
   - List Number
   - Table Grid
3. Set page margins (typically 2.5cm for A4)
4. Save as `[customer_name]_reference.docx`

## Available Templates

| Template | Description |
|----------|-------------|
| `default_reference.docx` | Standard formatting |
| `bank_standard_reference.docx` | Bank brand guidelines |
| `gov_standard_reference.docx` | Government compliance |

## Usage

```bash
# Use default template
./ba export requirements.md

# Use customer-specific template
./ba export brd.md --customer bank_standard
```

Note: Create actual .docx files with your organization's styling requirements.
