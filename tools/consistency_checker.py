#!/usr/bin/env python3
import os
import re
import argparse
from pathlib import Path
from collections import defaultdict

# ANSI colors
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

IGNORE_DIRS = ['.git', '.agent', 'tools', 'node_modules', '.gemini']

def get_markdown_files(root_dir):
    files = []
    for root, dirs, filenames in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for filename in filenames:
            if filename.endswith('.md'):
                files.append(Path(root) / filename)
    return files

def extract_attributes(content, file_path):
    """
    Extract ID-Attribute pairs from markdown tables.
    Returns dict: { "ID": {"Priority": "High", "Status": "Draft", ...} }
    """
    attributes = {}
    id_pattern = re.compile(r'\b([A-Z]{2,}-\d+)\b')
    
    lines = content.split('\n')
    header_map = {}
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Detect table header row
        if stripped.startswith('|') and 'ID' in stripped:
            # Parse header columns
            cols = [c.strip() for c in stripped.split('|') if c.strip()]
            header_map = {idx: col for idx, col in enumerate(cols)}
            continue
        
        # Parse data row
        if stripped.startswith('|') and header_map:
            cols = [c.strip() for c in stripped.split('|') if c.strip()]
            if len(cols) >= 2:
                # Find ID column
                for idx, val in enumerate(cols):
                    match = id_pattern.match(val)
                    if match:
                        req_id = match.group(1)
                        attrs = {}
                        for col_idx, col_val in enumerate(cols):
                            if col_idx in header_map and col_idx != idx:
                                attrs[header_map[col_idx]] = col_val
                        attrs['_source'] = str(file_path)
                        attributes[req_id] = attrs
                        break
    
    return attributes

def check_consistency(files):
    """Check for attribute mismatches across documents."""
    all_attrs = {}  # { "ID": [ {attrs1}, {attrs2}, ... ] }
    
    print(f"🔍 Checking consistency across {len(files)} files...\n")
    
    for f in files:
        content = f.read_text(encoding='utf-8')
        attrs = extract_attributes(content, f)
        for req_id, attr_dict in attrs.items():
            if req_id not in all_attrs:
                all_attrs[req_id] = []
            all_attrs[req_id].append(attr_dict)
    
    # Find conflicts
    conflicts = []
    for req_id, attr_list in all_attrs.items():
        if len(attr_list) < 2:
            continue  # Need at least 2 occurrences to have conflict
        
        # Compare Priority, Status across occurrences
        for attr_key in ['Priority', 'Status', 'Type']:
            values = defaultdict(list)
            for attr in attr_list:
                if attr_key in attr:
                    values[attr[attr_key]].append(attr['_source'])
            
            if len(values) > 1:
                conflicts.append({
                    "id": req_id,
                    "attribute": attr_key,
                    "values": dict(values)
                })
    
    return conflicts

def print_report(conflicts):
    if not conflicts:
        print(f"{GREEN}✅ CONSISTENCY CHECK PASSED: No attribute conflicts detected!{RESET}")
        return True
    
    print(f"{RED}❌ CONSISTENCY CHECK FAILED: Found {len(conflicts)} conflicts.{RESET}\n")
    
    for c in conflicts:
        print(f"{YELLOW}⚠️ Conflict: {c['id']} has mismatched '{c['attribute']}'{RESET}")
        for val, sources in c['values'].items():
            for src in sources:
                print(f"   - '{val}' in {Path(src).name}")
        print()
    
    print(f"{CYAN}Action: Align these values across documents before baseline.{RESET}")
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Cross-Document Consistency Checker')
    parser.add_argument('--path', help='Root directory', default='.')
    args = parser.parse_args()
    
    files = get_markdown_files(args.path)
    conflicts = check_consistency(files)
    print_report(conflicts)
