#!/usr/bin/env python3
"""Jira issue CRUD operations CLI."""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from jira_client import JiraClient


def cmd_create(client, args):
    custom_fields = {}
    if args.custom_fields:
        custom_fields = json.loads(args.custom_fields)
    labels = args.labels.split(",") if args.labels else None
    result = client.create_issue(
        project_key=args.project,
        summary=args.summary,
        issue_type=args.type,
        description=args.description or "",
        assignee=args.assignee,
        priority=args.priority,
        labels=labels,
        custom_fields=custom_fields
    )
    if "key" in result:
        print(f"Created: {result['key']}")
        print(f"URL: {client.base_url}/browse/{result['key']}")
    else:
        print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)
        sys.exit(1)


def cmd_get(client, args):
    result = client.get_issue(args.key, expand="names,renderedFields")
    if "error" in result or "errorMessages" in result:
        print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)
        sys.exit(1)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        fields = result.get("fields", {})
        print(f"Key: {result.get('key')}")
        print(f"Summary: {fields.get('summary')}")
        print(f"Status: {fields.get('status', {}).get('name')}")
        print(f"Type: {fields.get('issuetype', {}).get('name')}")
        assignee = fields.get('assignee')
        print(f"Assignee: {assignee.get('displayName') if assignee else 'Unassigned'}")
        print(f"Priority: {fields.get('priority', {}).get('name')}")
        print(f"Created: {fields.get('created')}")
        print(f"Updated: {fields.get('updated')}")
        if fields.get("description"):
            print(f"\nDescription:\n{fields['description']}")


def cmd_update(client, args):
    fields = {}
    if args.summary:
        fields["summary"] = args.summary
    if args.assignee:
        fields["assignee"] = {"name": args.assignee}
    if args.priority:
        fields["priority"] = {"name": args.priority}
    if args.description:
        fields["description"] = args.description
    if args.labels:
        fields["labels"] = args.labels.split(",")
    if args.custom_fields:
        fields.update(json.loads(args.custom_fields))
    if not fields:
        print("No fields to update. Use --summary, --assignee, --priority, etc.", file=sys.stderr)
        sys.exit(1)
    result = client.update_issue(args.key, fields=fields)
    if result.get("status") in (200, 204) or result.get("message") == "Success":
        print(f"Updated: {args.key}")
    else:
        print(f"Result: {json.dumps(result, indent=2)}")


def cmd_delete(client, args):
    result = client.delete_issue(args.key, delete_subtasks=args.subtasks)
    if result.get("status") in (200, 204) or result.get("message") == "Success":
        print(f"Deleted: {args.key}")
    else:
        print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)
        sys.exit(1)


def cmd_transition(client, args):
    if args.list:
        result = client.get_transitions(args.key)
        transitions = result.get("transitions", [])
        for t in transitions:
            print(f"  ID: {t['id']} -> {t['name']}")
        return
    if not args.transition_id:
        print("--transition-id required (use --list to see available transitions)", file=sys.stderr)
        sys.exit(1)
    fields = json.loads(args.fields) if args.fields else None
    result = client.transition_issue(args.key, args.transition_id, fields=fields)
    if result.get("status") in (200, 204) or result.get("message") == "Success":
        print(f"Transitioned: {args.key}")
    else:
        print(f"Result: {json.dumps(result, indent=2)}")


def cmd_comment(client, args):
    if args.list:
        result = client.get_comments(args.key)
        for c in result.get("comments", []):
            author = c.get("author", {}).get("displayName", "?")
            created = c.get("created", "?")
            body = c.get("body", "")[:200]
            print(f"  [{author} @ {created}]: {body}")
        return
    if not args.body:
        print("--body required to add a comment", file=sys.stderr)
        sys.exit(1)
    result = client.add_comment(args.key, args.body)
    if "id" in result:
        print(f"Comment added to {args.key}")
    else:
        print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Jira Issue CRUD Operations")
    parser.add_argument("--base-url", help="Jira base URL")
    parser.add_argument("--pat", help="Personal Access Token")
    sub = parser.add_subparsers(dest="command", required=True)

    # Create
    p_create = sub.add_parser("create", help="Create an issue")
    p_create.add_argument("--project", required=True, help="Project key")
    p_create.add_argument("--summary", required=True, help="Issue summary")
    p_create.add_argument("--type", default="Task", help="Issue type")
    p_create.add_argument("--description", help="Description")
    p_create.add_argument("--assignee", help="Assignee username")
    p_create.add_argument("--priority", help="Priority name")
    p_create.add_argument("--labels", help="Comma-separated labels")
    p_create.add_argument("--custom-fields", help="JSON custom fields")

    # Get
    p_get = sub.add_parser("get", help="Get issue details")
    p_get.add_argument("key", help="Issue key (e.g., PROJ-123)")
    p_get.add_argument("--json", action="store_true", help="Output raw JSON")

    # Update
    p_update = sub.add_parser("update", help="Update an issue")
    p_update.add_argument("key", help="Issue key")
    p_update.add_argument("--summary", help="New summary")
    p_update.add_argument("--assignee", help="New assignee")
    p_update.add_argument("--priority", help="New priority")
    p_update.add_argument("--description", help="New description")
    p_update.add_argument("--labels", help="Comma-separated labels")
    p_update.add_argument("--custom-fields", help="JSON custom fields")

    # Delete
    p_delete = sub.add_parser("delete", help="Delete an issue")
    p_delete.add_argument("key", help="Issue key")
    p_delete.add_argument("--subtasks", action="store_true", default=True,
                          help="Also delete subtasks")

    # Transition
    p_trans = sub.add_parser("transition", help="Transition an issue")
    p_trans.add_argument("key", help="Issue key")
    p_trans.add_argument("--list", action="store_true", help="List available transitions")
    p_trans.add_argument("--transition-id", help="Transition ID")
    p_trans.add_argument("--fields", help="JSON fields for transition")

    # Comment
    p_comment = sub.add_parser("comment", help="Manage comments")
    p_comment.add_argument("key", help="Issue key")
    p_comment.add_argument("--list", action="store_true", help="List comments")
    p_comment.add_argument("--body", help="Comment body text")

    args = parser.parse_args()
    client = JiraClient(base_url=args.base_url, pat=args.pat)

    commands = {
        "create": cmd_create, "get": cmd_get, "update": cmd_update,
        "delete": cmd_delete, "transition": cmd_transition, "comment": cmd_comment,
    }
    commands[args.command](client, args)


if __name__ == "__main__":
    main()
