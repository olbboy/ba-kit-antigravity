#!/usr/bin/env python3
"""Bulk operations for Confluence pages."""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from confluence_client import ConfluenceClient


def bulk_create(client, args):
    """Create pages from a JSON file."""
    with open(args.file) as f:
        pages = json.load(f)
    results = client.bulk_create_pages(args.space, pages, parent_id=args.parent_id)
    for r in results:
        if "id" in r:
            print(f"  OK: {r.get('title')} (ID: {r['id']})")
        else:
            print(f"  FAIL: {json.dumps(r)}")
    successes = sum(1 for r in results if "id" in r)
    print(f"\nCreated {successes}/{len(results)} pages")


def bulk_label(client, args):
    """Add labels to pages matching CQL."""
    results_data = client.search_all(args.cql, page_size=25)
    page_ids = [r["id"] for r in results_data]
    labels = [l.strip() for l in args.labels.split(",")]
    results = client.bulk_add_labels(page_ids, labels)
    for r in results:
        print(f"  Page {r['page_id']}: labeled")
    print(f"\nLabeled {len(results)} pages with: {', '.join(labels)}")


def bulk_delete(client, args):
    """Delete pages matching CQL."""
    results_data = client.search_all(args.cql, page_size=25)
    count = 0
    for page in results_data:
        result = client.delete_page(page["id"])
        success = result.get("status") in (200, 204) or result.get("message") == "Success"
        print(f"  {'OK' if success else 'FAIL'}: {page.get('title', page['id'])}")
        if success:
            count += 1
    print(f"\nDeleted {count}/{len(results_data)} pages")


def bulk_export(client, args):
    """Export pages matching CQL to JSON."""
    expand = ["body.storage", "version", "space", "metadata.labels"]
    results_data = client.search_all(args.cql, expand=expand, page_size=25)
    export_data = []
    for page in results_data:
        export_data.append({
            "id": page.get("id"),
            "title": page.get("title"),
            "space": page.get("space", {}).get("key"),
            "version": page.get("version", {}).get("number"),
            "body": page.get("body", {}).get("storage", {}).get("value", ""),
            "labels": [l["name"] for l in page.get("metadata", {}).get("labels", {}).get("results", [])],
        })

    output_file = args.output or "confluence_export.json"
    with open(output_file, "w") as f:
        json.dump(export_data, f, indent=2)
    print(f"Exported {len(export_data)} pages to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Confluence Bulk Operations")
    parser.add_argument("--base-url", help="Confluence base URL")
    parser.add_argument("--pat", help="Personal Access Token")
    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser("create", help="Bulk create from JSON file")
    p_create.add_argument("--space", required=True, help="Space key")
    p_create.add_argument("--file", required=True, help="JSON file with pages array")
    p_create.add_argument("--parent-id", help="Parent page ID")

    p_label = sub.add_parser("label", help="Bulk add labels to pages matching CQL")
    p_label.add_argument("--cql", required=True, help="CQL query")
    p_label.add_argument("--labels", required=True, help="Comma-separated labels")

    p_delete = sub.add_parser("delete", help="Bulk delete pages matching CQL")
    p_delete.add_argument("--cql", required=True, help="CQL query")

    p_export = sub.add_parser("export", help="Export pages matching CQL to JSON")
    p_export.add_argument("--cql", required=True, help="CQL query")
    p_export.add_argument("--output", help="Output file path")

    args = parser.parse_args()
    client = ConfluenceClient(base_url=args.base_url, pat=args.pat)

    commands = {
        "create": bulk_create, "label": bulk_label,
        "delete": bulk_delete, "export": bulk_export,
    }
    commands[args.command](client, args)


if __name__ == "__main__":
    main()
