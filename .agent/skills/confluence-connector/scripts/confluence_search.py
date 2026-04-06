#!/usr/bin/env python3
"""Search Confluence content using CQL with formatted output."""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from confluence_client import ConfluenceClient


def format_result(item: dict) -> str:
    title = item.get("title", "Untitled")
    content_type = item.get("type", "?")
    space = item.get("space", {}).get("key", "?")
    page_id = item.get("id", "?")
    status = item.get("status", "?")
    version = item.get("version", {}).get("number", "?")
    return f"[{space}/{page_id}] {title}\n  Type: {content_type} | Status: {status} | Version: {version}"


def main():
    parser = argparse.ArgumentParser(description="Search Confluence with CQL")
    parser.add_argument("cql", help="CQL query string")
    parser.add_argument("--limit", type=int, default=25, help="Max results per page")
    parser.add_argument("--all", action="store_true", help="Fetch all results (auto-paginate)")
    parser.add_argument("--expand", default="space,version",
                        help="Comma-separated expand parameters")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    parser.add_argument("--base-url", help="Confluence base URL")
    parser.add_argument("--pat", help="Personal Access Token")
    args = parser.parse_args()

    client = ConfluenceClient(base_url=args.base_url, pat=args.pat)
    expand_list = [e.strip() for e in args.expand.split(",")]

    if args.all:
        results = client.search_all(args.cql, expand=expand_list, page_size=args.limit)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(f"Found {len(results)} results:\n")
            for item in results:
                print(format_result(item))
                print()
    else:
        result = client.search(args.cql, limit=args.limit, expand=expand_list)
        if "statusCode" in result and result["statusCode"] != 200:
            print(f"Error: {json.dumps(result, indent=2)}", file=sys.stderr)
            sys.exit(1)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            items = result.get("results", [])
            total = result.get("totalSize", len(items))
            print(f"Showing {len(items)} of {total} results:\n")
            for item in items:
                print(format_result(item))
                print()


if __name__ == "__main__":
    main()
