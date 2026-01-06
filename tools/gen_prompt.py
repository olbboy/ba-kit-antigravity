#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path

# ANSI colors
CYAN = '\033[96m'
GREEN = '\033[92m'
RESET = '\033[0m'

PROMPTS = {
    "REVIEW_BRD": """
Act as a Senior Business Analyst and Strategic Consultant. Review the following Business Requirements Document (BRD).
Focus on:
1. **Strategic Alignment**: Do the objectives align with the problem statement?
2. **ROI Logic**: Is the business value clear and quantified?
3. **Completeness**: Are there missing stakeholders or scope gaps?
4. **Risks**: Identify hidden risks not mentioned in the document.

Output your review in a structured format with "Critical Issues", "Suggestions", and "Questions for Stakeholders".
""",
    "REVIEW_SRS": """
Act as a Solutions Architect and Security Expert. Audit the following Software Requirements Specification (SRS).
Focus on:
1. **Feasibility**: Are these requirements technically implementable?
2. **Security**: Identify potential vulnerabilities (OWASP Top 10) in the described features.
3. **Scalability**: Will this design handle high load?
4. **Edge Cases**: What failure scenarios are missing?

Provide a technical risk assessment.
""",
    "REVIEW_USER_STORIES": """
Act as a Lead QA Engineer and Product Owner. Critique the following User Stories.
Verify if they meet the INVEST criteria:
- **Independent**: Dependencies minimal?
- **Negotiable**: Too prescriptive?
- **Valuable**: Clear user value?
- **Estimable**: Clear scope?
- **Small**: Fit in a sprint?
- **Testable**: Clear Acceptance Criteria (Given/When/Then)?

For each story, reject it if it fails criteria or suggest a rewrite.
"""
}

def generate_prompt(file_path, prompt_type=None):
    try:
        content = Path(file_path).read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Auto-detect type if not specified
    if not prompt_type:
        filename = file_path.lower()
        if "brd" in filename:
            prompt_type = "REVIEW_BRD"
        elif "srs" in filename:
            prompt_type = "REVIEW_SRS"
        elif "story" in filename or "agile" in filename:
            prompt_type = "REVIEW_USER_STORIES"
        else:
            # Default fallback
            prompt_type = "REVIEW_BRD" 

    selected_prompt = PROMPTS.get(prompt_type, PROMPTS["REVIEW_BRD"])
    
    final_output = f"""
{selected_prompt}

---
CONTEXT DOCUMENT ({file_path}):

{content}
"""
    
    print(f"{GREEN}✅ Generated AI Review Prompt for {prompt_type}{RESET}")
    print(f"{CYAN}Copy the text below and paste it into your AI assistant:{RESET}\n")
    print("-" * 60)
    print(final_output)
    print("-" * 60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Prompt Generator')
    parser.add_argument('file', help='Markdown file to analyze')
    parser.add_argument('--type', help='Prompt type (REVIEW_BRD, REVIEW_SRS, REVIEW_USER_STORIES)', default=None)
    args = parser.parse_args()
    
    generate_prompt(args.file, args.type)
