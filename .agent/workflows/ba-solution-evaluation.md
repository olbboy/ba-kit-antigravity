---
description: Solution Evaluation - Business Case, ROI analysis, and Post-Implementation Review (SKILL-17)
---

# Solution Evaluation Workflow

Use this workflow when you need to evaluate solutions, build business cases, calculate ROI, or conduct post-implementation reviews.

## Prerequisites
Load SKILL-17 from `specialized/SKILL-17-solution-evaluation.md`

## Workflow Steps

### 1. Define Value Framework
- Identify business objectives and success criteria
- Define stakeholder value expectations
- Establish baseline metrics for comparison
- Determine measurement timeline

### 2. Build Business Case
Complete the business case framework:
- **Executive Summary**: One-page overview
- **Problem Statement**: Current pain and impact
- **Proposed Solution**: What we're recommending
- **Cost Analysis**: Development, implementation, ongoing costs
- **Benefit Analysis**: Tangible and intangible benefits
- **Financial Analysis**: ROI, NPV, IRR, Payback Period
- **Risk Assessment**: Key risks and mitigation
- **Recommendation**: Clear go/no-go recommendation

### 3. Quantify Benefits
Use standard quantification techniques:
- **Labor Cost Savings**: (Hours saved × Hourly rate × Volume)
- **Error Reduction**: (Error rate reduction × Cost per error × Volume)
- **Revenue Increase**: (Additional transactions × Revenue per transaction)
- **Cost Avoidance**: (Future costs prevented)

### 4. Calculate Financial Metrics
- **Simple ROI**: (Benefits - Costs) / Costs × 100%
- **Payback Period**: Initial Investment / Annual Net Benefit
- **NPV**: Present value of future cash flows minus investment
- **IRR**: Discount rate where NPV = 0
- **Benefit-Cost Ratio (BCR)**: Total Benefits / Total Costs

### 5. Define KPI Framework
For each key outcome:
- Define the metric and calculation
- Set baseline and target values
- Assign owner and measurement frequency
- Document data source

### 6. Conduct Post-Implementation Review (PIR)
After implementation:
- Assess objectives achievement (Met/Partially/Not Met)
- Measure actual benefits vs projected
- Compare budget actuals vs planned
- Evaluate schedule performance
- Document lessons learned
- Capture recommendations for future

## Output Artifacts
- Business Case Document
- ROI Analysis Spreadsheet
- KPI Framework/Dashboard
- Post-Implementation Review Report

## Step 7: Generate Quality Report (Auto-Run)
// turbo
Generate comprehensive metrics and quality report:

```bash
./ba doctor
```

## Step 8: AI Business Case Review (Auto-Run)
// turbo
Get expert AI review of your business case:

```bash
python3 tools/gen_prompt.py [business_case.md]
```

Copy the generated prompt for ROI and value proposition review.

## Related Skills
- SKILL-05: Prioritization (for benefit ranking)
- SKILL-07: Traceability (for linking to requirements)
- SKILL-09: BRD Template (for business requirements context)
- SKILL-15: Workshop Facilitation (for stakeholder alignment)
