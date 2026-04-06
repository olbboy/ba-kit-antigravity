#!/usr/bin/env python3
"""Search Jira issues using JQL with formatted output."""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from jira_client import JiraClient


def format_issue(issue: dict) -> str:
    fields = issue.get("fields", {})
    key = issue.get("key", "?")
    summary = fields.get("summary", "No summary")
    status = fields.get("status", {}).get("name", "?")
    assignee = fields.get("assignee", {})
    assignee_name = assignee.get("displayName", "Unassigned") if assignee else "Unassigned"
    priority = fields.get("priority", {})
    priority_name = priority.get("name", "?") if priority else "?"
    return f"[{key}] {summary}\n  Status: {status} | Assignee: {assignee_name} | Priority: {priority_name}"


def main():
    parser = argparse.ArgumentParser(description="Search Jira issues with JQL")
    parser.add_argument("jql", help="JQL query string")
    parser.add_argument("--max-results", type=int, default=50, help="Max results per page")
    parser.add_argument("--all", action="store_true", help="Fetch all results (auto-paginate)")
    parser.add_argument("--fields", default="key,summary,status,assignee,priority",
                        help="Comma-separated fields to return")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    parser.add_argument("--base-url", help="Jira base URL")
    parser.add_argument("--pat", help="Personal Access Token")
    args = parser.parse_args()

    client = JiraClient(base_url=args.base_url, pat=args.pat)
    fields_list = [f.strip() for f in args.fields.split(",")]

    if args.all:
        issues = client.search_all(args.jql, fields=fields_list, page_size=args.max_results)
        if args.json:
            print(json.dumps(issues, indent=2))
        else:
            print(f"Found {len(issues)} issues:\n")
            for issue in issues:
                print(format_issue(issue))
                print()
    else:
        result = client.search(args.jql, fields=fields_list, max_results=args.max_results)
        if "error" in result or "errorMessages" in result:
            print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)
            sys.exit(1)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            issues = result.get("issues", [])
            total = result.get("total", 0)
            print(f"Showing {len(issues)} of {total} issues:\n")
            for issue in issues:
                print(format_issue(issue))
                print()


if __name__ == "__main__":
    main()
