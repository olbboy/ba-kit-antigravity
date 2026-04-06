#!/usr/bin/env python3
"""Bulk operations for Jira issues."""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from jira_client import JiraClient


def bulk_create(client, args):
    """Create issues from a JSON file."""
    with open(args.file) as f:
        issues = json.load(f)
    result = client.bulk_create_issues(issues)
    print(json.dumps(result, indent=2))


def bulk_update(client, args):
    """Update multiple issues from JQL with given fields."""
    fields = json.loads(args.fields)
    issues = client.search_all(args.jql, fields=["key"], page_size=50)
    results = []
    for issue in issues:
        key = issue["key"]
        result = client.update_issue(key, fields=fields)
        success = result.get("status") in (200, 204) or result.get("message") == "Success"
        results.append({"key": key, "success": success})
        print(f"  {'OK' if success else 'FAIL'}: {key}")
    print(f"\nUpdated {sum(1 for r in results if r['success'])}/{len(results)} issues")


def bulk_transition(client, args):
    """Transition all issues matching JQL."""
    issues = client.search_all(args.jql, fields=["key"], page_size=50)
    keys = [i["key"] for i in issues]
    fields = json.loads(args.fields) if args.fields else None
    results = client.bulk_transition(keys, args.transition_id, fields=fields)
    for r in results:
        success = r["result"].get("status") in (200, 204) or r["result"].get("message") == "Success"
        print(f"  {'OK' if success else 'FAIL'}: {r['key']}")
    successes = sum(1 for r in results
                    if r["result"].get("status") in (200, 204) or r["result"].get("message") == "Success")
    print(f"\nTransitioned {successes}/{len(results)} issues")


def bulk_comment(client, args):
    """Add same comment to all issues matching JQL."""
    issues = client.search_all(args.jql, fields=["key"], page_size=50)
    for issue in issues:
        key = issue["key"]
        result = client.add_comment(key, args.body)
        success = "id" in result
        print(f"  {'OK' if success else 'FAIL'}: {key}")
    print(f"\nCommented on {len(issues)} issues")


def main():
    parser = argparse.ArgumentParser(description="Jira Bulk Operations")
    parser.add_argument("--base-url", help="Jira base URL")
    parser.add_argument("--pat", help="Personal Access Token")
    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser("create", help="Bulk create from JSON file")
    p_create.add_argument("--file", required=True, help="JSON file with issues array")

    p_update = sub.add_parser("update", help="Bulk update issues matching JQL")
    p_update.add_argument("--jql", required=True, help="JQL to find issues")
    p_update.add_argument("--fields", required=True, help="JSON fields to update")

    p_trans = sub.add_parser("transition", help="Bulk transition issues matching JQL")
    p_trans.add_argument("--jql", required=True, help="JQL to find issues")
    p_trans.add_argument("--transition-id", required=True, help="Transition ID")
    p_trans.add_argument("--fields", help="JSON fields for transition")

    p_comment = sub.add_parser("comment", help="Bulk add comment to issues matching JQL")
    p_comment.add_argument("--jql", required=True, help="JQL to find issues")
    p_comment.add_argument("--body", required=True, help="Comment text")

    args = parser.parse_args()
    client = JiraClient(base_url=args.base_url, pat=args.pat)

    commands = {
        "create": bulk_create, "update": bulk_update,
        "transition": bulk_transition, "comment": bulk_comment,
    }
    commands[args.command](client, args)


if __name__ == "__main__":
    main()
