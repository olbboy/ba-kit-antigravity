#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

# ANSI colors
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'

def structurize_notes(input_path):
    print(f"📝 Structuring notes from {input_path}...\n")
    
    try:
        content = Path(input_path).read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    lines = [l.strip() for l in content.split('\n') if l.strip()]
    
    # Heuristic 1: Colon Separation (Key: Value)
    structured_data = []
    
    for line in lines:
        if ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            val = parts[1].strip()
            # Clean up list bullets
            if key.startswith('- ') or key.startswith('* '): key = key[2:]
            structured_data.append((key, val))
    
    if not structured_data:
        print("Could not find structured patterns (Key: Value).")
        return

    # Generate Table
    # Determine headers (Generic)
    headers = ["Item", "Detail"]
    
    # Calculate widths
    col1_w = max(len(headers[0]), max(len(r[0]) for r in structured_data))
    col2_w = max(len(headers[1]), max(len(r[1]) for r in structured_data))
    
    # Draw
    table = []
    table.append(f"| {headers[0].ljust(col1_w)} | {headers[1].ljust(col2_w)} |")
    table.append(f"| {'-' * col1_w} | {'-' * col2_w} |")
    
    for row in structured_data:
        table.append(f"| {row[0].ljust(col1_w)} | {row[1].ljust(col2_w)} |")
        
    result = '\n'.join(table)
    
    print(f"{GREEN}✅ Structured Output:{RESET}")
    print(result)
    
    # Suggest Copy
    print(f"\n{CYAN}Tip: Copy the above table into your markdown file.{RESET}")
    
    # Optional: Write to file
    out_path = Path(input_path).with_suffix('.structured.md')
    out_path.write_text(result, encoding='utf-8')
    print(f"Saved to: {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Note Structurizer')
    parser.add_argument('file', help='Input text file to structurize')
    
    args = parser.parse_args()
    structurize_notes(args.file)
