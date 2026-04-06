# Jira Data Center REST API Reference

## Table of Contents
1. [Authentication](#authentication)
2. [Issue Endpoints](#issue-endpoints)
3. [Search (JQL)](#search-jql)
4. [Agile/Sprint Endpoints](#agilesprint-endpoints)
5. [Project Endpoints](#project-endpoints)
6. [User Endpoints](#user-endpoints)
7. [Custom Fields](#custom-fields)
8. [Webhooks](#webhooks)
9. [Common JQL Patterns](#common-jql-patterns)
10. [Error Reference](#error-reference)

## Authentication

### Personal Access Token (PAT)
Available in Jira Data Center 8.14.0+.

```
Authorization: Bearer <token>
```

PATs inherit the creating user's full permission set. Tokens can have configurable expiration via `expirationDuration` (in days).

### Creating PATs programmatically
```
POST /rest/pat/latest/tokens
Content-Type: application/json

{"expirationDuration": 90}
```

## Issue Endpoints

### Full Issue Schema

```
POST /rest/api/2/issue
{
  "fields": {
    "project": {"key": "PROJ"},
    "summary": "string (required)",
    "description": "string",
    "issuetype": {"name": "Bug|Task|Story|Epic|Sub-task"},
    "assignee": {"name": "username"},
    "reporter": {"name": "username"},
    "priority": {"name": "Highest|High|Medium|Low|Lowest"},
    "labels": ["label1", "label2"],
    "components": [{"name": "component1"}],
    "fixVersions": [{"name": "1.0"}],
    "affectsVersions": [{"name": "0.9"}],
    "environment": "string",
    "duedate": "2026-12-31",
    "timetracking": {
      "originalEstimate": "2h 30m",
      "remainingEstimate": "1h"
    },
    "security": {"name": "Security Level Name"},
    "customfield_XXXXX": "value"
  }
}
```

### Issue Link Types
```
GET /rest/api/2/issueLinkType
```

### Create Issue Link
```
POST /rest/api/2/issueLink
{
  "type": {"name": "Blocks"},
  "inwardIssue": {"key": "PROJ-1"},
  "outwardIssue": {"key": "PROJ-2"},
  "comment": {"body": "Linked issues"}
}
```

### Watchers
```
GET /rest/api/2/issue/{key}/watchers
POST /rest/api/2/issue/{key}/watchers  (body: "username")
DELETE /rest/api/2/issue/{key}/watchers?username=user
```

### Work Logs
```
GET /rest/api/2/issue/{key}/worklog
POST /rest/api/2/issue/{key}/worklog
{
  "timeSpent": "2h",
  "started": "2026-03-01T09:00:00.000+0000",
  "comment": "Work log entry"
}
```

## Search (JQL)

### JQL Operators
| Operator | Example |
|----------|---------|
| `=` | `status = "In Progress"` |
| `!=` | `status != Done` |
| `IN` | `status IN ("Open", "In Progress")` |
| `NOT IN` | `status NOT IN (Done, Closed)` |
| `~` | `summary ~ "search text"` (contains) |
| `!~` | `summary !~ "excluded"` |
| `IS` | `assignee IS EMPTY` |
| `IS NOT` | `assignee IS NOT EMPTY` |
| `>`, `<`, `>=`, `<=` | `created >= -7d` |
| `WAS` | `status WAS "In Progress"` |
| `CHANGED` | `status CHANGED FROM "Open" TO "In Progress"` |

### JQL Functions
| Function | Description |
|----------|-------------|
| `currentUser()` | Logged-in user |
| `membersOf("group")` | Members of a group |
| `now()` | Current datetime |
| `startOfDay()` | Start of today |
| `endOfWeek()` | End of this week |
| `startOfMonth(-1)` | Start of last month |
| `releasedVersions(PROJECT)` | Released versions |
| `unreleasedVersions(PROJECT)` | Unreleased versions |

### ORDER BY
```
ORDER BY created DESC, priority ASC
```

## Agile/Sprint Endpoints

### Base Path: `/rest/agile/1.0/`

### Board Types
- **Scrum**: Sprint-based workflow
- **Kanban**: Continuous flow

### Backlog
```
GET /rest/agile/1.0/board/{boardId}/backlog
```

### Epic
```
GET /rest/agile/1.0/board/{boardId}/epic
GET /rest/agile/1.0/epic/{epicId}/issue
POST /rest/agile/1.0/epic/{epicId}/issue  (move issues to epic)
```

### Board Configuration
```
GET /rest/agile/1.0/board/{boardId}/configuration
```

## Project Endpoints

### Project Roles
```
GET /rest/api/2/project/{key}/role
GET /rest/api/2/project/{key}/role/{roleId}
```

### Project Versions
```
GET /rest/api/2/project/{key}/versions
POST /rest/api/2/version
{
  "name": "1.0",
  "description": "First release",
  "project": "PROJ",
  "released": false,
  "releaseDate": "2026-06-01"
}
```

### Project Components
```
GET /rest/api/2/project/{key}/components
POST /rest/api/2/component
{
  "name": "Backend",
  "project": "PROJ",
  "leadUserName": "username"
}
```

## User Endpoints

```
GET /rest/api/2/myself
GET /rest/api/2/user?username=username
GET /rest/api/2/user/search?username=query&maxResults=50
GET /rest/api/2/group/member?groupname=group&maxResults=50
```

## Custom Fields

### Getting Custom Field IDs
```
GET /rest/api/2/field
```

Filter the response for `custom: true` to see custom fields with their IDs (e.g., `customfield_10001`).

### Setting Custom Fields
```json
{
  "fields": {
    "customfield_10001": "text value",
    "customfield_10002": {"value": "dropdown option"},
    "customfield_10003": [{"value": "multi-select 1"}, {"value": "multi-select 2"}],
    "customfield_10004": {"name": "username"},
    "customfield_10005": "2026-12-31"
  }
}
```

## Webhooks

### Register Webhook
```
POST /rest/webhooks/1.0/webhook
{
  "name": "My Webhook",
  "url": "https://example.com/webhook",
  "events": [
    "jira:issue_created",
    "jira:issue_updated",
    "jira:issue_deleted",
    "comment_created",
    "sprint_started",
    "sprint_closed"
  ],
  "filters": {
    "issue-related-events-section": "project = PROJ"
  }
}
```

## Common JQL Patterns

```sql
-- My open issues
assignee = currentUser() AND status != Done ORDER BY priority DESC

-- Sprint issues
sprint = "Sprint 1" AND status != Done

-- Recently updated in project
project = PROJ AND updated >= -24h ORDER BY updated DESC

-- Overdue issues
duedate < now() AND status != Done AND assignee IS NOT EMPTY

-- Unassigned bugs
project = PROJ AND issuetype = Bug AND assignee IS EMPTY

-- Created this week
project = PROJ AND created >= startOfWeek()

-- Blocked issues
status = Blocked OR statusCategory = "In Progress" AND priority IN (Highest, High)
```

## Error Reference

| Code | Meaning | Common Cause |
|------|---------|--------------|
| 400 | Bad Request | Malformed JSON, invalid field |
| 401 | Unauthorized | Invalid/expired PAT |
| 403 | Forbidden | Insufficient project permissions |
| 404 | Not Found | Wrong issue key or project |
| 409 | Conflict | Concurrent modification |
| 429 | Rate Limited | Too many requests |
| 500 | Server Error | Jira internal error |
