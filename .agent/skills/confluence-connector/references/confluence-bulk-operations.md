# Confluence Bulk Operations Reference

## Overview

Use `scripts/confluence_bulk.py` to perform batch operations on multiple Confluence pages. All commands accept `--base-url` and `--pat` flags, or read from `CONFLUENCE_BASE_URL` and `CONFLUENCE_PAT` environment variables.

## Commands

### Bulk Create

Create multiple pages in a space from a JSON file:

```bash
python3 scripts/confluence_bulk.py create --space SPACEKEY --file pages.json
```

Optionally specify a parent page:

```bash
python3 scripts/confluence_bulk.py create --space SPACEKEY --file pages.json --parent-id 12345
```

Prepare the JSON file as an array of page objects:

```json
[
  {
    "title": "First Page",
    "body": "<p>Page content in storage format</p>"
  },
  {
    "title": "Second Page",
    "body": "<h1>Heading</h1><p>More content</p>"
  }
]
```

### Bulk Label

Add labels to all pages matching a CQL query:

```bash
python3 scripts/confluence_bulk.py label --cql "space = MYSPACE AND type = page" --labels "reviewed,archived"
```

Pass `--labels` as comma-separated label names. Each matching page receives all specified labels.

### Bulk Delete

Delete all pages matching a CQL query:

```bash
python3 scripts/confluence_bulk.py delete --cql "space = ARCHIVE AND type = page AND label = deprecated"
```

Use with caution — deletion is irreversible. Test the CQL query first with a search to verify matched pages.

### Bulk Export

Export pages matching a CQL query to JSON:

```bash
python3 scripts/confluence_bulk.py export --cql "space = DOCS AND type = page" --output export.json
```

Exports page ID, title, space key, version, body (storage format), and labels. Default output file: `confluence_export.json`.

## Error Handling

Each operation prints per-page success/failure status and a final summary count. Common failure causes:

- **403**: Insufficient permissions on specific pages or space
- **404**: Page deleted during batch operation
- **409**: Version conflict during concurrent edits
- **429**: Rate limited — client handles with exponential backoff
