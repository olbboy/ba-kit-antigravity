#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path

# Add tools directory to path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

try:
    import knowledge_graph
except ImportError:
    print("Error: Could not import knowledge_graph.py.")
    sys.exit(1)

# ANSI colors
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

def simulate_impact(req_id, root_path='.'):
    """Simulate the impact of removing a requirement using the knowledge graph."""
    print(f"🔮 Simulating impact of removing {CYAN}{req_id}{RESET}...\n")
    
    root = Path(root_path)
    files = knowledge_graph.get_markdown_files(root)
    concepts = knowledge_graph.extract_concepts(files)
    
    # Find files that mention this ID
    affected_files = []
    for f in files:
        content = f.read_text(encoding='utf-8')
        if req_id.upper() in content.upper():
            affected_files.append(f.name)
    
    if not affected_files:
        print(f"{YELLOW}No references to {req_id} found in the project.{RESET}")
        return
    
    print(f"{RED}⚠️ Impact Analysis for {req_id}:{RESET}")
    print(f"   This ID is referenced in {len(affected_files)} files:\n")
    for af in affected_files[:10]:
        print(f"   📄 {af}")
    if len(affected_files) > 10:
        print(f"   ... and {len(affected_files) - 10} more.")
    
    print(f"\n{YELLOW}Recommendation:{RESET}")
    print(f"   Review these files before removing {req_id}.")
    print(f"   Consider updating linked items (User Stories, Test Cases) to prevent orphans.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Impact Simulator')
    parser.add_argument('req_id', help='Requirement ID to simulate removal (e.g., FR-001)')
    parser.add_argument('--path', help='Root directory', default='.')
    
    args = parser.parse_args()
    simulate_impact(args.req_id, args.path)
