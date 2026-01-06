#!/usr/bin/env python3
import re
import sys
import argparse
from pathlib import Path

# ANSI colors
CYAN = '\033[96m'
GREEN = '\033[92m'
RESET = '\033[0m'

def parse_step(step_line):
    """
    Heuristic parser to map English Gherkin steps to Playwright code (TypeScript).
    """
    line = step_line.strip()
    # Remove Given/When/Then/And/But prefixes
    clean_line = re.sub(r'^(Given|When|Then|And|But)\s+', '', line, flags=re.IGNORECASE).strip()
    
    # Heuristics
    
    # 1. Navigation: "I go to /login" or "I visit https://google.com"
    match = re.search(r'(?:go to|visit|navigate to)\s+(.+)', clean_line, re.IGNORECASE)
    if match:
        url = match.group(1).strip()
        if not url.startswith('http'):
            # assume relative path or placeholder
            return f"    await page.goto('{url}');"
        return f"    await page.goto('{url}');"

    # 2. Clicking: "I click 'Submit'" or "I click on [Login Button]"
    match = re.search(r'click(?:ing| on)?\s+[\'"]?([^\'"]+)[\'"]?', clean_line, re.IGNORECASE)
    if match:
        target = match.group(1).strip()
        # Default to finding by text, which is very common in Playwright
        return f"    await page.getByText('{target}').click();"

    # 3. Filling fields: "I fill 'User' with 'admin'" or "I type 'admin' into 'User'"
    # Pattern A: fill [Field] with [Value]
    match = re.search(r'fill\s+[\'"]?([^\'"]+)[\'"]?\s+with\s+[\'"]?([^\'"]+)[\'"]?', clean_line, re.IGNORECASE)
    if match:
        field, value = match.group(1), match.group(2)
        return f"    await page.getByLabel('{field}').fill('{value}');"
    
    # Pattern B: type [Value] into [Field]
    match = re.search(r'type\s+[\'"]?([^\'"]+)[\'"]?\s+into\s+[\'"]?([^\'"]+)[\'"]?', clean_line, re.IGNORECASE)
    if match:
        value, field = match.group(1), match.group(2)
        return f"    await page.getByLabel('{field}').fill('{value}');"

    # 4. Assertions (Visibility/Text): "I see 'Welcome'" or "I should see 'Error'"
    match = re.search(r'(?:see|should see|verify)\s+[\'"]?([^\'"]+)[\'"]?', clean_line, re.IGNORECASE)
    if match:
        text = match.group(1).strip()
        return f"    await expect(page.locator('body')).toContainText('{text}');"

    # 5. URL Assertion: "I should be on '/dashboard'"
    match = re.search(r'(?:be on|redirected to)\s+[\'"]?([^\'"]+)[\'"]?', clean_line, re.IGNORECASE)
    if match:
        url_part = match.group(1).strip()
        return f"    await expect(page).toHaveURL(/{re.escape(url_part)}/);"

    # Fallback: Comment out unrecognized steps
    return f"    // TODO: Implement step: {clean_line}"

def generate_test(file_path):
    try:
        content = Path(file_path).read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    filename = Path(file_path).stem
    output_lines = []
    
    # Header
    output_lines.append("import { test, expect } from '@playwright/test';")
    output_lines.append("")
    output_lines.append(f"test.describe('Generated Tests for {filename}', () => {{")
    
    # Scan for Scenarios
    # Regex for "Scenario: [Title]"
    scenario_matches = list(re.finditer(r'^\s*(?:###\s*)?Scenario:\s*(.+)$', content, re.MULTILINE))
    
    if not scenario_matches:
        print(f"No 'Scenario:' blocks found in {file_path}")
        return

    for i, match in enumerate(scenario_matches):
        scenario_title = match.group(1).strip()
        output_lines.append(f"  test('{scenario_title}', async ({{ page }}) => {{")
        
        # Get content between this scenario and the next (or EOF)
        start_idx = match.end()
        end_idx = scenario_matches[i+1].start() if i + 1 < len(scenario_matches) else len(content)
        block = content[start_idx:end_idx]
        
        # Parse lines in the block
        test_steps = []
        for line in block.split('\n'):
            line = line.strip()
            # Look for Gherkin keywords
            if re.match(r'^(Given|When|Then|And|But)', line, re.IGNORECASE):
                code = parse_step(line)
                test_steps.append(code)
        
        if not test_steps:
             output_lines.append("    // No steps found for this scenario")
        else:
             output_lines.extend(test_steps)
             
        output_lines.append("  });")
        output_lines.append("")

    output_lines.append("});")
    
    # Output file
    out_file = Path(file_path).with_suffix('.spec.ts')
    out_file.write_text('\n'.join(output_lines), encoding='utf-8')
    
    print(f"{GREEN}✅ Generated Playwright Test: {out_file}{RESET}")
    print(f"{CYAN}To run (if Playwright installed):{RESET}")
    print(f"npx playwright test {out_file.name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Gherkin to Playwright Converter')
    parser.add_argument('file', help='Markdown file containing Gherkin scenarios')
    args = parser.parse_args()
    
    generate_test(args.file)
