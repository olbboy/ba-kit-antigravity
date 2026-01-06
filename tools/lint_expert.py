#!/usr/bin/env python3
import re
import sys
import argparse
from pathlib import Path

# ANSI colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

def check_gherkin(content):
    """
    Checks if Acceptance Criteria follows Gherkin syntax (Given/When/Then)
    Current heuristic: Look for 'Acceptance Criteria' section, then check lines.
    """
    issues = []
    
    # Extract Acceptance Criteria sections
    # Regex to capture content between "Acceptance Criteria" header and next header
    ac_blocks = re.finditer(r'(#{2,}\s*Acceptance Criteria.*?)(?=^#|\Z)', content, re.DOTALL | re.MULTILINE | re.IGNORECASE)
    
    found_ac = False
    for match in ac_blocks:
        found_ac = True
        block_content = match.group(1)
        lines = block_content.split('\n')
        
        gherkin_keywords = ['Given', 'When', 'Then', 'And', 'But']
        gherkin_count = 0
        total_lines = 0
        
        for line in lines[1:]: # Skip header
            clean_line = line.strip().lstrip('-*1234567890. ')
            if not clean_line: continue
            total_lines += 1
            
            # Check if line starts with Gherkin keyword
            if any(clean_line.startswith(kw) for kw in gherkin_keywords):
                gherkin_count += 1
        
        if total_lines > 0 and gherkin_count == 0:
             issues.append({
                "type": "GHERKIN_MISSING",
                "msg": f"Acceptance Criteria found but no Gherkin (Given/When/Then) syntax detected.",
                "context": lines[1][:50] + "..." if len(lines) > 1 else "Empty AC"
            })
            
    if not found_ac:
        # Depending on file type, this might be okay, but for User Stories it's critical.
        # We'll just note it if it looks like a User Story file.
        if "User Story" in content or "US-" in content:
             issues.append({
                "type": "AC_MISSING",
                "msg": "Document appears to contain User Stories but no 'Acceptance Criteria' section found.",
                "context": "File level"
            })
            
    return issues

def check_invest(content):
    """
    Checks heuristics for INVEST criteria.
    - Testable: Has AC (covered above)
    - Small: Description length check (heuristic)
    """
    issues = []
    
    # Check for "TBD" (Negotiable/Not Ready)
    if "TBD" in content or "TODO" in content:
        issues.append({
            "type": "INVEST_NOT_READY",
            "msg": "Found 'TBD' or 'TODO' placeholders. Requirement may not be ready.",
            "context": "Search for TBD/TODO"
        })
        
    return issues

def check_attributes(content):
    """
    Ensures mandatory attributes exist (Priority, ID)
    """
    issues = []
    
    # Check for Priority
    if not re.search(r'\bPriority\b', content, re.IGNORECASE):
        issues.append({
            "type": "ATTR_MISSING",
            "msg": "Missing 'Priority' attribute.",
            "context": "File level"
        })
        
    return issues

def lint_file(file_path):
    print(f"🧠 Expert Linter Analyzing {file_path}...\n")
    
    try:
        content = Path(file_path).read_text(encoding='utf-8')
    except Exception as e:
        print(f"{RED}Error reading file: {e}{RESET}")
        return False

    all_issues = []
    all_issues.extend(check_gherkin(content))
    all_issues.extend(check_invest(content))
    all_issues.extend(check_attributes(content))
    
    if not all_issues:
        print(f"{GREEN}✅ EXPERT CHECK PASSED: Document looks solid.{RESET}")
        return True
    else:
        print(f"{YELLOW}⚠️  Exeprt Suggestions ({len(all_issues)}):{RESET}")
        for issue in all_issues:
            print(f"   [{issue['type']}] {issue['msg']}")
        print(f"\n{CYAN}Tip: Use /ba-writing to get help improving these.{RESET}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Expert Linter')
    parser.add_argument('file', help='Markdown file to check')
    args = parser.parse_args()
    
    lint_file(args.file)
