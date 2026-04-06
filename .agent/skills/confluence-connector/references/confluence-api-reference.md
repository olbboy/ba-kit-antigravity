# Confluence Data Center REST API Reference

## Table of Contents
1. [Authentication](#authentication)
2. [Content Endpoints](#content-endpoints)
3. [Search (CQL)](#search-cql)
4. [Space Endpoints](#space-endpoints)
5. [Storage Format](#storage-format)
6. [Macros in Storage Format](#macros-in-storage-format)
7. [Content Properties](#content-properties)
8. [Blueprints and Templates](#blueprints-and-templates)
9. [Common CQL Patterns](#common-cql-patterns)
10. [Error Reference](#error-reference)

## Authentication

### Personal Access Token (PAT)
Available in Confluence Data Center 7.9+.

```
Authorization: Bearer <token>
```

PATs inherit full permissions of the creating user. Managed under user settings > Personal Access Tokens.

## Content Endpoints

### Content Types
| Type | Description |
|------|-------------|
| `page` | Standard page |
| `blogpost` | Blog post |
| `comment` | Comment on content |
| `attachment` | File attachment |

### Full Create Schema

```json
POST /rest/api/content
{
  "type": "page",
  "title": "Page Title",
  "space": {"key": "SPACEKEY"},
  "ancestors": [{"id": "parentPageId"}],
  "status": "current",
  "body": {
    "storage": {
      "value": "<p>Content</p>",
      "representation": "storage"
    }
  },
  "metadata": {
    "properties": {
      "editor": {"value": "v2", "key": "editor"}
    }
  }
}
```

### Blog Posts
```json
POST /rest/api/content
{
  "type": "blogpost",
  "title": "Blog Post Title",
  "space": {"key": "SPACEKEY"},
  "body": {
    "storage": {
      "value": "<p>Blog content</p>",
      "representation": "storage"
    }
  }
}
```

### Get Content Tree (Children)
```
GET /rest/api/content/{id}/child/page?limit=25&start=0&expand=version
```

### Get Content Descendants
```
GET /rest/api/content/{id}/descendant/page
```

### Move Page
```
PUT /rest/api/content/{id}/move/{position}/{targetId}
```
Positions: `before`, `after`, `append` (as child).

### Copy Page
```
POST /rest/api/content/{id}/copy
{
  "destination": {
    "type": "parent_page",
    "value": "targetPageId"
  },
  "copyAttachments": true,
  "copyLabels": true
}
```

## Search (CQL)

### CQL Operators
| Operator | Example |
|----------|---------|
| `=` | `type = page` |
| `!=` | `space != "ARCHIVE"` |
| `~` | `title ~ "keyword"` (contains) |
| `!~` | `title !~ "draft"` |
| `IN` | `space IN ("DEV", "OPS")` |
| `NOT IN` | `type NOT IN ("comment", "attachment")` |
| `>`, `<`, `>=`, `<=` | `created >= "2026-01-01"` |

### CQL Fields
| Field | Description |
|-------|-------------|
| `type` | Content type (page, blogpost, comment, attachment) |
| `space` | Space key |
| `title` | Page title |
| `text` | Full-text content search |
| `label` | Content label |
| `creator` | Content creator |
| `contributor` | Content contributor |
| `created` | Creation date |
| `lastModified` | Last modification date |
| `ancestor` | Ancestor page ID |
| `parent` | Direct parent page ID |

### CQL Functions
```
currentUser()     -- Logged-in user
now()             -- Current time
startOfDay()      -- Start of today
endOfWeek()       -- End of this week
startOfMonth(-1)  -- Start of last month
```

## Space Endpoints

### Space Types
- `global`: Visible to all users
- `personal`: User-specific space

### Space Permissions
```
GET /rest/api/space/{key}/permission
```

### Space Settings
```
GET /rest/api/space/{key}/settings
```

## Storage Format

### Basic Elements
```html
<p>Paragraph</p>
<h1>Heading 1</h1> through <h6>Heading 6</h6>
<strong>Bold</strong> <em>Italic</em> <u>Underline</u> <del>Strikethrough</del>
<br /> <hr />
<ol><li>Ordered item</li></ol>
<ul><li>Unordered item</li></ul>
<table><thead><tr><th>Header</th></tr></thead><tbody><tr><td>Cell</td></tr></tbody></table>
<a href="https://example.com">Link</a>
<ac:link><ri:page ri:content-title="Page Title" ri:space-key="SPACE"/></ac:link>
<ac:image><ri:attachment ri:filename="image.png"/></ac:image>
```

## Macros in Storage Format

### Code Block
```xml
<ac:structured-macro ac:name="code">
  <ac:parameter ac:name="language">python</ac:parameter>
  <ac:parameter ac:name="title">Example</ac:parameter>
  <ac:parameter ac:name="linenumbers">true</ac:parameter>
  <ac:plain-text-body><![CDATA[
def hello():
    print("Hello, World!")
  ]]></ac:plain-text-body>
</ac:structured-macro>
```

### Info/Warning/Note Panels
```xml
<ac:structured-macro ac:name="info">  <!-- also: warning, note -->
  <ac:rich-text-body><p>Panel text</p></ac:rich-text-body>
</ac:structured-macro>
```

### Table of Contents
```xml
<ac:structured-macro ac:name="toc">
  <ac:parameter ac:name="maxLevel">3</ac:parameter>
</ac:structured-macro>
```

### Expand/Collapse
```xml
<ac:structured-macro ac:name="expand">
  <ac:parameter ac:name="title">Click to expand</ac:parameter>
  <ac:rich-text-body><p>Hidden content</p></ac:rich-text-body>
</ac:structured-macro>
```

### Status Macro
```xml
<ac:structured-macro ac:name="status">
  <ac:parameter ac:name="colour">Green</ac:parameter>
  <ac:parameter ac:name="title">DONE</ac:parameter>
</ac:structured-macro>
```

### Jira Issue Macro
```xml
<ac:structured-macro ac:name="jira">
  <ac:parameter ac:name="key">PROJ-123</ac:parameter>
</ac:structured-macro>
```

## Content Properties

Content properties are key-value pairs attached to content:

```
GET /rest/api/content/{id}/property
GET /rest/api/content/{id}/property/{key}
POST /rest/api/content/{id}/property
PUT /rest/api/content/{id}/property/{key}
DELETE /rest/api/content/{id}/property/{key}

{
  "key": "my-property",
  "value": {
    "any": "json structure",
    "nested": {"data": true}
  }
}
```

## Blueprints and Templates

### List Templates
```
GET /rest/api/template/page?spaceKey=SPACE
GET /rest/api/template/blueprint
```

### Create from Template
```
POST /rest/api/content/blueprint/instance/{draftId}
{
  "space": {"key": "SPACE"},
  "status": "current",
  "title": "New Page",
  "ancestors": [{"id": "parentId"}]
}
```

## Common CQL Patterns

```sql
type = page AND space = "MYSPACE"                                    -- all pages in space
text ~ "search term" AND type = page                                 -- full-text search
label = "important" AND type = page AND space = "DEV"                -- by label
type = page AND lastModified >= now("-7d") ORDER BY lastModified DESC -- recent changes
creator = currentUser() AND type = page                              -- my pages
type = blogpost AND created >= startOfMonth()                        -- blog posts this month
ancestor = 12345 AND type = page                                     -- child pages
type = page AND space = "DOCS" AND label IS NULL                     -- unlabeled pages
```

## Error Reference

| Code | Meaning | Common Cause |
|------|---------|--------------|
| 400 | Bad Request | Malformed JSON or invalid storage format |
| 401 | Unauthorized | Invalid/expired PAT |
| 403 | Forbidden | No space or page permissions |
| 404 | Not Found | Wrong page ID or space key |
| 409 | Conflict | Version number mismatch (stale update) |
| 429 | Rate Limited | Too many API requests |
| 500 | Server Error | Confluence internal error |

### Version Conflict Resolution
When you get a 409, re-fetch the page to get the current version number, then retry with `version.number = current + 1`.
