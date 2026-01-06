#!/usr/bin/env python3
import re
import sys
import argparse
from pathlib import Path

# ANSI colors
CYAN = '\033[96m'
GREEN = '\033[92m'
RESET = '\033[0m'

def generate_traceability(file_path):
    print(f"🕸️  Generating Traceability Graph for {file_path}...\n")
    
    try:
        content = Path(file_path).read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        return False

    # Regex to find IDs like [REQ-001] or [US-1] or BR-01 inside table cells
    # We look for patterns that look like IDs.
    # Pattern: Uppercase letters, hyphen, digits.
    id_pattern = re.compile(r'\b([A-Z]{2,}-\d+)\b')
    
    lines = content.split('\n')
    nodes = set()
    edges = []
    
    current_node = None
    
    # Simple parser: 
    # 1. If we find an ID in a "definition" position (start of line or first col of table), it's a Node.
    # 2. If we find an ID in the "description" text of a Node, it's an Edge (Dependency).
    
    print(f"DEBUG: Scanning {len(lines)} lines...")
    for line in lines:
        matches = id_pattern.findall(line)
        if not matches:
            continue
            
        # Debug
        # print(f"DEBUG: Line matches: {matches}")

        # Check for table definition: starts with pipe OR is just the ID
        stripped = line.strip()
        is_definition = False
        
        if stripped.startswith('|'):
            parts = stripped.split('|')
            if len(parts) > 1:
                # Check if the first match is inside the first content column (index 1)
                # We relax this: check if match matches the START of the 1st col
                first_col = parts[1].strip()
                if first_col.startswith(matches[0]):
                    is_definition = True
        elif stripped.startswith(matches[0]):
            is_definition = True
            
        if is_definition:
            current_node = matches[0]
            nodes.add(current_node)
            # Link to other IDs in the same line
            for other_id in matches[1:]:
                edges.append((current_node, other_id))
                nodes.add(other_id)
        else:
            # Usage reference
            if current_node:
                for other_id in matches:
                    if other_id != current_node:
                        edges.append((current_node, other_id))
                        nodes.add(other_id)

    # Generate Mermaid Content
    mermaid = ["graph LR"]
    
    # Style definitions
    mermaid.append("    classDef req fill:#f9f,stroke:#333,stroke-width:2px;")
    mermaid.append("    classDef obj fill:#aaf,stroke:#333,stroke-width:2px;")
    mermaid.append("    classDef other fill:#efe,stroke:#333,stroke-width:1px;")
    
    sorted_nodes = sorted(list(nodes))
    if not sorted_nodes:
        print("No IDs found to trace.")
        return True

    for node in sorted_nodes:
        # Assign style based on prefix
        style = "other"
        if "REQ" in node or "BR" in node: style = "req"
        elif "OBJ" in node: style = "obj"
        mermaid.append(f"    {node}:::{style}")

    for src, dst in edges:
        mermaid.append(f"    {src} --> {dst}")

    mermaid_str = "\n".join(mermaid)
    
    # Output to file
    out_file = Path(file_path).parent / "traceability_matrix.mermaid"
    out_file.write_text(mermaid_str, encoding='utf-8')
    
    print(f"{GREEN}✅ Traceability Graph Generated: {out_file}{RESET}")
    print(f"    Nodes: {len(nodes)}")
    print(f"    Edges: {len(edges)}")
    
    # Preview
    print("\nPreview:")
    print(mermaid_str[:200] + "...")
    
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Traceability Generator')
    parser.add_argument('file', help='Markdown file to analyze')
    args = parser.parse_args()
    
    generate_traceability(args.file)
