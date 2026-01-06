#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from datetime import datetime

# ANSI colors
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

LOG_FILE = "decisions.json"

def load_log():
    log_path = Path(LOG_FILE)
    if log_path.exists():
        return json.loads(log_path.read_text(encoding='utf-8'))
    return []

def save_log(data):
    Path(LOG_FILE).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

def add_decision(req_id, rationale, author="BA Agent"):
    log = load_log()
    entry = {
        "timestamp": datetime.now().isoformat(),
        "id": req_id.upper(),
        "rationale": rationale,
        "author": author
    }
    log.append(entry)
    save_log(log)
    print(f"{GREEN}✅ Decision logged for {req_id}.{RESET}")

def query_decisions(req_id):
    log = load_log()
    results = [e for e in log if e['id'] == req_id.upper()]
    
    if not results:
        print(f"{YELLOW}No decisions logged for {req_id}.{RESET}")
        return
    
    print(f"{CYAN}📜 Decision History for {req_id}:{RESET}\n")
    for e in results:
        print(f"  [{e['timestamp'][:10]}] {e['rationale']}")
        print(f"            - by {e['author']}\n")

def list_all():
    log = load_log()
    if not log:
        print(f"{YELLOW}No decisions logged yet.{RESET}")
        return
    
    print(f"{CYAN}📜 All Logged Decisions ({len(log)} total):{RESET}\n")
    for e in log[-10:]:  # Last 10
        print(f"  [{e['timestamp'][:10]}] {e['id']}: {e['rationale'][:50]}...")
    if len(log) > 10:
        print(f"\n  ... and {len(log) - 10} more.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Decision Log')
    parser.add_argument('action', choices=['log', 'why', 'list'], help='Action to perform')
    parser.add_argument('--id', help='Requirement ID (for log/why)')
    parser.add_argument('--reason', help='Reason for decision (for log)')
    parser.add_argument('--author', help='Author name', default='BA Agent')
    
    args = parser.parse_args()
    
    if args.action == 'log':
        if not args.id or not args.reason:
            print(f"{YELLOW}Usage: decision_log.py log --id FR-001 --reason \"Deprioritized due to budget\"{RESET}")
            exit(1)
        add_decision(args.id, args.reason, args.author)
    elif args.action == 'why':
        if not args.id:
            print(f"{YELLOW}Usage: decision_log.py why --id FR-001{RESET}")
            exit(1)
        query_decisions(args.id)
    elif args.action == 'list':
        list_all()
