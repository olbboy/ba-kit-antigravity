#!/usr/bin/env python3
"""Confluence page CRUD operations CLI."""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from confluence_client import ConfluenceClient


def cmd_create(client, args):
    body = args.body
    if args.body_file:
        with open(args.body_file) as f:
            body = f.read()
    result = client.create_page(
        space_key=args.space,
        title=args.title,
        body=body or "<p></p>",
        parent_id=args.parent_id
    )
    if "id" in result:
        page_id = result["id"]
        title = result.get("title", args.title)
        print(f"Created: {title} (ID: {page_id})")
        print(f"URL: {client.base_url}/pages/viewpage.action?pageId={page_id}")
    else:
        print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)
        sys.exit(1)


def cmd_get(client, args):
    expand = ["body.storage", "version", "space", "metadata.labels", "history"]
    result = client.get_page(args.id, expand=expand)
    if "statusCode" in result and result["statusCode"] != 200:
        print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)
        sys.exit(1)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"ID: {result.get('id')}")
        print(f"Title: {result.get('title')}")
        print(f"Space: {result.get('space', {}).get('key')}")
        print(f"Version: {result.get('version', {}).get('number')}")
        print(f"Status: {result.get('status')}")
        labels = result.get("metadata", {}).get("labels", {}).get("results", [])
        if labels:
            print(f"Labels: {', '.join(l['name'] for l in labels)}")
        body = result.get("body", {}).get("storage", {}).get("value", "")
        if body and args.content:
            print(f"\nContent:\n{body}")


def cmd_update(client, args):
    current_version = client.get_page_version(args.id)
    if current_version == 0:
        print("Error: Could not get current page version", file=sys.stderr)
        sys.exit(1)

    body = args.body
    if args.body_file:
        with open(args.body_file) as f:
            body = f.read()

    title = args.title
    if not title:
        page = client.get_page(args.id)
        title = page.get("title", "Untitled")

    result = client.update_page(
        page_id=args.id,
        title=title,
        body=body,
        version_number=current_version + 1,
        version_message=args.message
    )
    if "id" in result:
        print(f"Updated: {result.get('title')} (Version: {current_version + 1})")
    else:
        print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)
        sys.exit(1)


def cmd_delete(client, args):
    result = client.delete_page(args.id)
    if result.get("status") in (200, 204) or result.get("message") == "Success":
        print(f"Deleted page: {args.id}")
    else:
        print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)
        sys.exit(1)


def cmd_comment(client, args):
    if args.list:
        result = client.get_comments(args.id, expand=["body.storage"])
        comments = result.get("results", [])
        for c in comments:
            body_val = c.get("body", {}).get("storage", {}).get("value", "")[:200]
            version = c.get("version", {})
            who = version.get("by", {}).get("displayName", "?")
            when = version.get("when", "?")
            print(f"  [{who} @ {when}]: {body_val}")
        return
    if not args.body:
        print("--body required to add a comment", file=sys.stderr)
        sys.exit(1)
    result = client.add_comment(args.id, f"<p>{args.body}</p>")
    if "id" in result:
        print(f"Comment added to page {args.id}")
    else:
        print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)


def cmd_labels(client, args):
    if args.list:
        result = client.get_labels(args.id)
        labels = result.get("results", [])
        for l in labels:
            print(f"  {l.get('prefix', 'global')}:{l['name']}")
        return
    if args.add:
        label_list = [l.strip() for l in args.add.split(",")]
        result = client.add_labels(args.id, label_list)
        print(f"Added labels: {', '.join(label_list)}")
        return
    if args.remove:
        result = client.remove_label(args.id, args.remove)
        print(f"Removed label: {args.remove}")


def main():
    parser = argparse.ArgumentParser(description="Confluence Page CRUD Operations")
    parser.add_argument("--base-url", help="Confluence base URL")
    parser.add_argument("--pat", help="Personal Access Token")
    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser("create", help="Create a page")
    p_create.add_argument("--space", required=True, help="Space key")
    p_create.add_argument("--title", required=True, help="Page title")
    p_create.add_argument("--body", help="Page body (storage format HTML)")
    p_create.add_argument("--body-file", help="File with page body content")
    p_create.add_argument("--parent-id", help="Parent page ID")

    p_get = sub.add_parser("get", help="Get page details")
    p_get.add_argument("id", help="Page ID")
    p_get.add_argument("--json", action="store_true", help="Raw JSON output")
    p_get.add_argument("--content", action="store_true", help="Show page content")

    p_update = sub.add_parser("update", help="Update a page")
    p_update.add_argument("id", help="Page ID")
    p_update.add_argument("--title", help="New title")
    p_update.add_argument("--body", help="New body (storage format)")
    p_update.add_argument("--body-file", help="File with new body content")
    p_update.add_argument("--message", help="Version message")

    p_delete = sub.add_parser("delete", help="Delete a page")
    p_delete.add_argument("id", help="Page ID")

    p_comment = sub.add_parser("comment", help="Manage comments")
    p_comment.add_argument("id", help="Page ID")
    p_comment.add_argument("--list", action="store_true", help="List comments")
    p_comment.add_argument("--body", help="Comment body text")

    p_labels = sub.add_parser("labels", help="Manage labels")
    p_labels.add_argument("id", help="Page ID")
    p_labels.add_argument("--list", action="store_true", help="List labels")
    p_labels.add_argument("--add", help="Comma-separated labels to add")
    p_labels.add_argument("--remove", help="Label to remove")

    args = parser.parse_args()
    client = ConfluenceClient(base_url=args.base_url, pat=args.pat)

    commands = {
        "create": cmd_create, "get": cmd_get, "update": cmd_update,
        "delete": cmd_delete, "comment": cmd_comment, "labels": cmd_labels,
    }
    commands[args.command](client, args)


if __name__ == "__main__":
    main()
