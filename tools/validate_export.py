#!/usr/bin/env python3
"""
BA-Kit Export Validator (SKILL-21)
Pre-flight checks before exporting documents to DOCX.
"""

import argparse
import re
import sys
from pathlib import Path

# ANSI colors
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

def validate_heading_structure(lines):
    """Check heading hierarchy (no gaps like H1 → H3)."""
    issues = []
    prev_level = 0
    
    for i, line in enumerate(lines, 1):
        if line.startswith('#'):
            level = len(line.split()[0]) if line.split() else 0
            if level > prev_level + 1 and prev_level > 0:
                issues.append(f"Line {i}: Heading gap (H{prev_level} → H{level})")
            prev_level = level
    
    return issues

def validate_placeholders(content):
    """Check for unfilled placeholders like {{...}} or [TBD]."""
    issues = []
    
    # Check {{placeholder}}
    placeholders = re.findall(r'\{\{[^}]+\}\}', content)
    for p in placeholders:
        issues.append(f"Unfilled placeholder: {p}")
    
    # Check [TBD], [TODO], [FIXME]
    tbds = re.findall(r'\[(TBD|TODO|FIXME)[^\]]*\]', content, re.IGNORECASE)
    for t in tbds:
        issues.append(f"Unresolved marker: [{t}]")
    
    return issues

def validate_tables(content):
    """Check table structure validity."""
    issues = []
    lines = content.split('\n')
    
    in_table = False
    header_cols = 0
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|'):
            if not in_table:
                in_table = True
                header_cols = stripped.count('|') - 1
            else:
                current_cols = stripped.count('|') - 1
                if current_cols != header_cols and not re.match(r'^\|[\s\-:]+\|$', stripped):
                    issues.append(f"Line {i}: Table column mismatch ({header_cols} vs {current_cols})")
        else:
            in_table = False
    
    return issues

def validate_special_chars(content):
    """Check for problematic characters that may break DOCX."""
    issues = []
    
    # Check for null bytes or other control chars
    if '\x00' in content:
        issues.append("Contains null bytes (may corrupt DOCX)")
    
    # Check for excessive Unicode that may not render
    if re.search(r'[\U00010000-\U0010FFFF]', content):
        issues.append("Contains exotic Unicode (verify font support)")
    
    return issues

def validate_heading_depth(lines):
    """Check max heading depth (recommend ≤ 4 for DOCX)."""
    issues = []
    
    for i, line in enumerate(lines, 1):
        if line.startswith('#####'):  # H5 or deeper
            issues.append(f"Line {i}: Heading too deep (H5+). Recommend max H4.")
    
    return issues

def validate_file(file_path):
    """Run all validations on a file."""
    print(f"{CYAN}🔍 Validating: {file_path}{RESET}\n")
    
    content = Path(file_path).read_text(encoding='utf-8')
    lines = content.split('\n')
    
    all_issues = []
    
    # Run checks
    checks = [
        ("Heading Structure", validate_heading_structure(lines)),
        ("Unfilled Placeholders", validate_placeholders(content)),
        ("Table Structure", validate_tables(content)),
        ("Special Characters", validate_special_chars(content)),
        ("Heading Depth", validate_heading_depth(lines)),
    ]
    
    for check_name, issues in checks:
        if issues:
            print(f"{YELLOW}⚠ {check_name}:{RESET}")
            for issue in issues:
                print(f"   • {issue}")
            all_issues.extend(issues)
        else:
            print(f"{GREEN}✓ {check_name}: OK{RESET}")
    
    print()
    
    if all_issues:
        print(f"{RED}❌ VALIDATION FAILED: {len(all_issues)} issues found.{RESET}")
        print(f"   Fix these before exporting to DOCX.")
        return False
    else:
        print(f"{GREEN}✅ VALIDATION PASSED: Ready for export.{RESET}")
        return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Export Validator')
    parser.add_argument('input', help='Input Markdown file to validate')
    
    args = parser.parse_args()
    
    if not Path(args.input).exists():
        print(f"{RED}✗ File not found: {args.input}{RESET}")
        sys.exit(1)
    
    success = validate_file(args.input)
    sys.exit(0 if success else 1)
