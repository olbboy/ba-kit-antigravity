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
RESET = '\033[0m'

IGNORE_DIRS = ['.git', '.agent', 'tools', 'node_modules', '.gemini']

def get_markdown_files(root_dir):
    files = []
    for root, dirs, filenames in os.walk(root_dir):
        # Filter directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for filename in filenames:
            if filename.endswith('.md'):
                files.append(Path(root) / filename)
    return files

def extract_concepts(files):
    """
    Scans files for H1 (#) and H2 (##) headers to define 'Concepts'.
    Returns a dict: { "Concept Name": "File Path" }
    """
    concepts = {}
    for file_path in files:
        try:
            content = file_path.read_text(encoding='utf-8')
            # Look for headers
            headers = re.findall(r'^(#{1,2})\s+(.+)$', content, re.MULTILINE)
            for level, title in headers:
                # Clean title (remove links, formatting)
                clean_title = re.sub(r'[\[\]\(\)*`]', '', title).strip()
                if len(clean_title) > 3: # Avoid noise
                    concepts[clean_title] = str(file_path)
                    
            # Also add filename as a concept (e.g., SKILL-01)
            concepts[file_path.stem] = str(file_path)
            
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    return concepts

def analyze_graph(root_dir, target_files=None):
    root_path = Path(root_dir)
    files = get_markdown_files(root_path) if not target_files else [Path(f) for f in target_files]
    
    print(f"🧠 Building Knowledge Graph for {len(files)} files...\n")
    
    # 1. Define Concepts (Nodes)
    concepts = extract_concepts(files)
    print(f"Found {len(concepts)} Concepts/Topics.")
    
    # 2. Build Edges & Check Semantic Links
    nodes = {} # { filepath: id }
    edges = [] # (from, to)
    missing_links = []
    
    for idx, f in enumerate(files):
        nodes[str(f)] = f"N{idx}"
        
    for file_path in files:
        content = file_path.read_text(encoding='utf-8')
        file_id = nodes[str(file_path)]
        
        # Check for Explicit Links [Title](path) or [[WikiLink]]
        # Heuristic for internal markdown links
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for text, link_path_str in links:
             # Resolve relative path
             # This is tricky without a real resolver, so heuristic: check if basename matches any file
             if link_path_str.startswith('http') or link_path_str.startswith('#'): continue
             
             link_name = Path(link_path_str).name
             for target_file, target_id in nodes.items():
                 if link_name in target_file:
                     edges.append((file_id, target_id))
                     break

        # Check for Semantic Mentions (Implicit Links)
        for concept, concept_file in concepts.items():
            if concept_file == str(file_path): continue # Don't self-reference
            
            # If concept is mentioned in text
            if re.search(r'\b' + re.escape(concept) + r'\b', content, re.IGNORECASE):
                # Check if it was already explicitly linked? (Simplification: Just check if we made an edge)
                # For now, just report it as a potential "Semantic Link"
                
                # We need to check if there is an explicit link to that file nearby? 
                # For the graph, we add valid semantic edges? Or just dashed ones?
                # Let's add dashed edges for semantic matches
                
                target_id = nodes.get(concept_file)
                if target_id:
                     edges.append((file_id, target_id, "semantic"))
                     
                     # Check if ANY explicit link exists to that file?
                     # Heuristic: simplistic check
                     if concept_file not in content and Path(concept_file).name not in content:
                         missing_links.append({
                             "source": file_path.name,
                             "target": concept,
                             "target_file": Path(concept_file).name
                         })

    # 3. Generate Mermaid
    mermaid = ["graph TD"]
    
    # Add Nodes (using Basename)
    reversed_nodes = {v: k for k, v in nodes.items()}
    for nid in reversed_nodes:
        path = reversed_nodes[nid]
        name = Path(path).stem
        mermaid.append(f"    {nid}[\"{name}\"]")
    
    # Add Edges
    unique_edges = set()
    for edge in edges:
        src, dst = edge[0], edge[1]
        style = "-->" if len(edge) == 2 else "-.->" # dashed for semantic
        
        # Avoid duplicates
        edge_key = f"{src}{style}{dst}"
        if edge_key not in unique_edges and src != dst:
            mermaid.append(f"    {src} {style} {dst}")
            unique_edges.add(edge_key)
            
    # Output Mermaid
    out_file = root_path / "project_graph.mermaid"
    out_file.write_text('\n'.join(mermaid), encoding='utf-8')
    
    print(f"{GREEN}✅ Knowledge Graph Generated: {out_file}{RESET}")
    print(f"    - Nodes: {len(nodes)}")
    print(f"    - Edges: {len(unique_edges)}")
    
    if missing_links:
        print(f"\n{YELLOW}⚠️  Missing Semantic Links (Concepts mentioned but not linked):{RESET}")
        for link in missing_links[:10]: # Limit output
            print(f"   - In {CYAN}{link['source']}{RESET}: Mentioned '{link['target']}' -> Link to {link['target_file']}?")
        if len(missing_links) > 10: print(f"   ... and {len(missing_links) - 10} more.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Knowledge Graph Builder')
    parser.add_argument('--path', help='Root directory', default='.')
    args = parser.parse_args()
    
    analyze_graph(args.path)
