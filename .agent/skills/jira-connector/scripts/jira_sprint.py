#!/usr/bin/env python3
"""Jira Sprint and Board management CLI."""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from jira_client import JiraClient


def cmd_boards(client, args):
    result = client.get_boards(project_key=args.project)
    boards = result.get("values", [])
    if args.json:
        print(json.dumps(boards, indent=2))
    else:
        for b in boards:
            print(f"  ID: {b['id']} | Name: {b['name']} | Type: {b.get('type', '?')}")


def cmd_sprints(client, args):
    result = client.get_sprints(args.board_id, state=args.state)
    sprints = result.get("values", [])
    if args.json:
        print(json.dumps(sprints, indent=2))
    else:
        for s in sprints:
            state = s.get("state", "?")
            goal = s.get("goal", "")
            print(f"  ID: {s['id']} | {s['name']} | State: {state}")
            if goal:
                print(f"    Goal: {goal}")


def cmd_create_sprint(client, args):
    result = client.create_sprint(
        name=args.name, board_id=args.board_id,
        start_date=args.start, end_date=args.end, goal=args.goal
    )
    if "id" in result:
        print(f"Created sprint: {result['name']} (ID: {result['id']})")
    else:
        print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)


def cmd_move(client, args):
    keys = [k.strip() for k in args.issues.split(",")]
    result = client.move_issues_to_sprint(args.sprint_id, keys)
    if result.get("status") in (200, 204) or result.get("message") == "Success":
        print(f"Moved {len(keys)} issues to sprint {args.sprint_id}")
    else:
        print(f"Result: {json.dumps(result, indent=2)}")


def cmd_issues(client, args):
    result = client.get_sprint_issues(args.sprint_id, fields=["key", "summary", "status", "assignee"])
    issues = result.get("issues", [])
    if args.json:
        print(json.dumps(issues, indent=2))
    else:
        print(f"Sprint {args.sprint_id} - {len(issues)} issues:\n")
        for issue in issues:
            fields = issue.get("fields", {})
            status = fields.get("status", {}).get("name", "?")
            assignee = fields.get("assignee", {})
            name = assignee.get("displayName", "Unassigned") if assignee else "Unassigned"
            print(f"  [{issue['key']}] {fields.get('summary', '?')} | {status} | {name}")


def main():
    parser = argparse.ArgumentParser(description="Jira Sprint Management")
    parser.add_argument("--base-url", help="Jira base URL")
    parser.add_argument("--pat", help="Personal Access Token")
    sub = parser.add_subparsers(dest="command", required=True)

    p_boards = sub.add_parser("boards", help="List boards")
    p_boards.add_argument("--project", help="Filter by project key")
    p_boards.add_argument("--json", action="store_true")

    p_sprints = sub.add_parser("sprints", help="List sprints for a board")
    p_sprints.add_argument("board_id", type=int, help="Board ID")
    p_sprints.add_argument("--state", choices=["active", "future", "closed"])
    p_sprints.add_argument("--json", action="store_true")

    p_create = sub.add_parser("create", help="Create a sprint")
    p_create.add_argument("--name", required=True, help="Sprint name")
    p_create.add_argument("--board-id", required=True, type=int, help="Board ID")
    p_create.add_argument("--start", help="Start date (ISO 8601)")
    p_create.add_argument("--end", help="End date (ISO 8601)")
    p_create.add_argument("--goal", help="Sprint goal")

    p_move = sub.add_parser("move", help="Move issues to a sprint")
    p_move.add_argument("--sprint-id", required=True, type=int, help="Sprint ID")
    p_move.add_argument("--issues", required=True, help="Comma-separated issue keys")

    p_issues = sub.add_parser("issues", help="List issues in a sprint")
    p_issues.add_argument("sprint_id", type=int, help="Sprint ID")
    p_issues.add_argument("--json", action="store_true")

    args = parser.parse_args()
    client = JiraClient(base_url=args.base_url, pat=args.pat)

    commands = {
        "boards": cmd_boards, "sprints": cmd_sprints,
        "create": cmd_create_sprint, "move": cmd_move, "issues": cmd_issues,
    }
    commands[args.command](client, args)


if __name__ == "__main__":
    main()
