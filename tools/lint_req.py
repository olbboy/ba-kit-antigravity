#!/usr/bin/env python3
import re
import sys
import argparse
from pathlib import Path

# ANSI colors for terminal output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Expert Rules Definition
AMBIGUOUS_TERMS = [
    "fast", "slow", "easy", "clean", "robust", "sufficient", 
    "user-friendly", "intuitive", "flexible", "modern", 
    "immediately", "later", "efficient", "seamless"
]

REQUIRED_SECTIONS = [
    "Acceptance Criteria",
    "Priority",
    "Description"
]

def check_file(file_path):
    print(f"🔍 Analyzing {file_path} for Quality Standards...\n")
    
    try:
        content = Path(file_path).read_text(encoding='utf-8')
    except Exception as e:
        print(f"{RED}Error reading file: {e}{RESET}")
        return False

    issues = []
    
    # 1. Ambiguity Check
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        for term in AMBIGUOUS_TERMS:
            # Check for whole words, case insensitive
            if re.search(r'\b' + re.escape(term) + r'\b', line, re.IGNORECASE):
                issues.append({
                    "line": i,
                    "type": "AMBIGUITY",
                    "msg": f"Found ambiguous term '{term}' - Must quantify (e.g., 'fast' -> '< 200ms')",
                    "content": line.strip()
                })

    # 2. Structure/Completeness Check (Heuristic)
    # Check if 'Acceptance Criteria' exists if it looks like a requirement block
    # This is a simple heuristic; can be made smarter
    req_blocks = re.split(r'^#+\s+', content, flags=re.MULTILINE)
    
    # 3. ID Validation
    # Find all [REQ-xxx] tags
    req_ids = re.findall(r'\[(REQ-\d+|US-\d+)\]', content)
    unique_ids = set(req_ids)
    if len(req_ids) != len(unique_ids):
        issues.append({
            "line": 0,
            "type": "DUPLICATE_ID",
            "msg": f"Found duplicate Requirement IDs. Total found: {len(req_ids)}, Unique: {len(unique_ids)}",
            "content": ""
        })

    # Report Results
    if not issues:
        print(f"{GREEN}✅ QUALITY CHECK PASSED: No critical issues found.{RESET}")
        return True
    else:
        print(f"{RED}❌ QUALITY CHECK FAILED: Found {len(issues)} issues.{RESET}")
        print("-" * 60)
        for issue in issues:
            loc = f"Line {issue['line']}" if issue['line'] > 0 else "File-level"
            print(f"{YELLOW}[{issue['type']}] {loc}:{RESET} {issue['msg']}")
            if issue['content']:
                print(f"   Context: \"{issue['content'][:80]}...\"")
        print("-" * 60)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Requirements Linter')
    parser.add_argument('file', help='Markdown file to check')
    args = parser.parse_args()
    
    if not check_file(args.file):
        sys.exit(1)
