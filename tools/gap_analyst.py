#!/usr/bin/env python3
import os
import re
import argparse
from pathlib import Path

# ANSI colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

IGNORE_DIRS = ['.git', '.agent', 'tools', 'node_modules', '.gemini']

def get_files(root_dir):
    files = []
    for root, dirs, filenames in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for filename in filenames:
            if filename.endswith('.md'):
                files.append(Path(root) / filename)
    return files

def find_ids_and_refs(files):
    """
    Returns:
    - definitions: { "ID": "Source_File" }
    - references: { "ID": ["Ref_File_1", "Ref_File_2"] }
    """
    definitions = {}
    references = {}
    
    # Relaxed pattern: digits can be 1 or more
    id_pattern = re.compile(r'\b([A-Z]{2,}-\d+)\b')
    
    print(f"🔍 Scanning {len(files)} files for Traceability Gaps...\n")
    
    for file_path in files:
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        for line in lines:
            matches = id_pattern.findall(line)
            for req_id in matches:
                # Check for Definition Context
                is_def = False
                stripped = line.strip()
                
                # Handle standard markdown tables (|) AND Box Drawing (│)
                if (stripped.startswith('|') or stripped.startswith('│')) and f" {req_id} " in line:
                    # Check columns. Usually ID is in col 1 or 2.
                    # We assume if it's in a table row and it matches the ID pattern, it MIGHT be a def.
                    # But we need to distinguish Def vs Ref.
                    # Heuristic: If the Header contained "ID" in that column? Too complex.
                    # Simple rule: If it's the FIRST ID in the row, it's a Def.
                    is_def = True
                
                # Check Headers
                if stripped.startswith(f"### {req_id}") or stripped.startswith(f"## {req_id}"):
                    is_def = True
                    
                # Store
                if is_def:
                    if req_id not in definitions:
                        definitions[req_id] = str(file_path)
                else:
                    if req_id not in references:
                        references[req_id] = []
                    # Don't add self-reference if possible (or just filter later)
                    references[req_id].append(str(file_path))

    return definitions, references

def analyze_gaps(definitions, references):
    gaps = [] # IDs defined but not referenced
    
    for req_id, source_file in definitions.items():
        # Filter self-references
        refs = references.get(req_id, [])
        external_refs = [r for r in refs if r != source_file]
        
        if not external_refs:
            gaps.append({
                "id": req_id,
                "file": source_file,
                "type": "ORPHAN (No Downstream Trace)"
            })
            
    return gaps

def print_report(gaps, definitions):
    if not gaps:
        print(f"{GREEN}✅ GAP ANALYSIS PASSED: All {len(definitions)} requirements are traced!{RESET}")
        return

    print(f"{RED}❌ GAP ANALYSIS FAILED: Found {len(gaps)} Untraced Requirements.{RESET}")
    print(f"{YELLOW}These requirements exist but are not linked/implemented anywhere else:{RESET}\n")
    
    # Sort by ID
    gaps.sort(key=lambda x: x['id'])
    
    print(f"╔════════════╦═══════════════════════════════════════════════╗")
    print(f"║ ID         ║ LOCATION (Defined In)                         ║")
    print(f"╠════════════╬═══════════════════════════════════════════════╣")
    for gap in gaps:
        filename = Path(gap['file']).name
        print(f"║ {gap['id'].ljust(10)} ║ {filename.ljust(45)} ║")
    print(f"╚════════════╩═══════════════════════════════════════════════╝")
    
    print(f"\n{CYAN}Action: Check these IDs. Are they implemented in code? Tested? Or just forgotten?{RESET}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Gap Analysis Engine')
    parser.add_argument('--path', help='Root directory', default='.')
    args = parser.parse_args()
    
    try:
        files = get_files(args.path)
        defs, refs = find_ids_and_refs(files)
        gaps = analyze_gaps(defs, refs)
        print_report(gaps, definitions=defs)
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
