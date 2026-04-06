#!/usr/bin/env python3
"""
Jira Data Center REST API Client Library.
Handles authentication, pagination, error handling, and common operations.

Usage:
    from jira_client import JiraClient
    client = JiraClient()  # reads from env vars
    client = JiraClient(base_url="https://jira.example.com", pat="your-token")
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import urllib.error
import ssl
import time
from typing import Optional, Dict, List, Any, Union


class JiraClient:
    """Jira Data Center REST API client using PAT authentication."""

    def __init__(self, base_url: Optional[str] = None, pat: Optional[str] = None,
                 verify_ssl: bool = True, max_retries: int = 3):
        self.base_url = (base_url or os.environ.get("JIRA_BASE_URL", "")).rstrip("/")
        self.pat = pat or os.environ.get("JIRA_PAT", "")

        if not self.base_url:
            raise ValueError("JIRA_BASE_URL not set. Provide base_url or set JIRA_BASE_URL env var.")
        if not self.pat:
            raise ValueError("JIRA_PAT not set. Provide pat or set JIRA_PAT env var.")

        self.api_url = f"{self.base_url}/rest/api/2"
        self.agile_url = f"{self.base_url}/rest/agile/1.0"
        self.max_retries = max_retries
        self.verify_ssl = verify_ssl

        if not verify_ssl:
            self._ssl_context = ssl.create_default_context()
            self._ssl_context.check_hostname = False
            self._ssl_context.verify_mode = ssl.CERT_NONE
        else:
            self._ssl_context = ssl.create_default_context()

    def _headers(self, extra: Optional[Dict] = None) -> Dict[str, str]:
        headers = {
            "Authorization": f"Bearer {self.pat}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if extra:
            headers.update(extra)
        return headers

    def _request(self, method: str, url: str, data: Optional[Dict] = None,
                 headers: Optional[Dict] = None, raw_data: Optional[bytes] = None) -> Dict:
        """Execute HTTP request with retry and error handling."""
        hdrs = headers or self._headers()

        body = None
        if data is not None:
            body = json.dumps(data).encode("utf-8")
        elif raw_data is not None:
            body = raw_data

        for attempt in range(self.max_retries):
            try:
                req = urllib.request.Request(url, data=body, headers=hdrs, method=method)
                response = urllib.request.urlopen(req, context=self._ssl_context, timeout=30)
                response_body = response.read().decode("utf-8")
                if response_body:
                    return json.loads(response_body)
                return {"status": response.status, "message": "Success"}
            except urllib.error.HTTPError as e:
                error_body = e.read().decode("utf-8", errors="replace")
                if e.code == 429:
                    wait = min(2 ** attempt * 2, 30)
                    print(f"Rate limited. Waiting {wait}s before retry {attempt + 1}/{self.max_retries}...", file=sys.stderr)
                    time.sleep(wait)
                    continue
                error_info = {"status": e.code, "error": error_body}
                try:
                    error_info = json.loads(error_body)
                    error_info["status"] = e.code
                except json.JSONDecodeError:
                    pass
                if attempt < self.max_retries - 1 and e.code >= 500:
                    time.sleep(2 ** attempt)
                    continue
                return error_info
            except urllib.error.URLError as e:
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return {"status": 0, "error": str(e.reason)}
        return {"status": 0, "error": "Max retries exceeded"}

    # ── Search ──

    def search(self, jql: str, fields: Optional[List[str]] = None,
               max_results: int = 50, start_at: int = 0,
               expand: Optional[List[str]] = None) -> Dict:
        """Search issues using JQL."""
        payload = {
            "jql": jql,
            "startAt": start_at,
            "maxResults": max_results,
        }
        if fields:
            payload["fields"] = fields
        if expand:
            payload["expand"] = expand
        return self._request("POST", f"{self.api_url}/search", data=payload)

    def search_all(self, jql: str, fields: Optional[List[str]] = None,
                   page_size: int = 50) -> List[Dict]:
        """Search all issues matching JQL (auto-paginate)."""
        all_issues = []
        start_at = 0
        while True:
            result = self.search(jql, fields=fields, max_results=page_size, start_at=start_at)
            if "issues" not in result:
                break
            all_issues.extend(result["issues"])
            if start_at + page_size >= result.get("total", 0):
                break
            start_at += page_size
        return all_issues

    # ── Issue CRUD ──

    def get_issue(self, issue_key: str, fields: Optional[str] = None,
                  expand: Optional[str] = None) -> Dict:
        """Get issue details."""
        params = []
        if fields:
            params.append(f"fields={urllib.parse.quote(fields)}")
        if expand:
            params.append(f"expand={urllib.parse.quote(expand)}")
        qs = f"?{'&'.join(params)}" if params else ""
        return self._request("GET", f"{self.api_url}/issue/{issue_key}{qs}")

    def create_issue(self, project_key: str, summary: str, issue_type: str = "Task",
                     description: str = "", assignee: Optional[str] = None,
                     priority: Optional[str] = None, labels: Optional[List[str]] = None,
                     custom_fields: Optional[Dict] = None) -> Dict:
        """Create a new issue."""
        fields: Dict[str, Any] = {
            "project": {"key": project_key},
            "summary": summary,
            "issuetype": {"name": issue_type},
        }
        if description:
            fields["description"] = description
        if assignee:
            fields["assignee"] = {"name": assignee}
        if priority:
            fields["priority"] = {"name": priority}
        if labels:
            fields["labels"] = labels
        if custom_fields:
            fields.update(custom_fields)
        return self._request("POST", f"{self.api_url}/issue", data={"fields": fields})

    def update_issue(self, issue_key: str, fields: Optional[Dict] = None,
                     update: Optional[Dict] = None) -> Dict:
        """Update an existing issue."""
        payload: Dict[str, Any] = {}
        if fields:
            payload["fields"] = fields
        if update:
            payload["update"] = update
        return self._request("PUT", f"{self.api_url}/issue/{issue_key}", data=payload)

    def delete_issue(self, issue_key: str, delete_subtasks: bool = True) -> Dict:
        """Delete an issue."""
        qs = f"?deleteSubtasks={'true' if delete_subtasks else 'false'}"
        return self._request("DELETE", f"{self.api_url}/issue/{issue_key}{qs}")

    # ── Transitions ──

    def get_transitions(self, issue_key: str) -> Dict:
        """Get available transitions for an issue."""
        return self._request("GET", f"{self.api_url}/issue/{issue_key}/transitions")

    def transition_issue(self, issue_key: str, transition_id: str,
                         fields: Optional[Dict] = None) -> Dict:
        """Execute a transition on an issue."""
        payload: Dict[str, Any] = {"transition": {"id": str(transition_id)}}
        if fields:
            payload["fields"] = fields
        return self._request("POST", f"{self.api_url}/issue/{issue_key}/transitions", data=payload)

    # ── Comments ──

    def add_comment(self, issue_key: str, body: str,
                    visibility: Optional[Dict] = None) -> Dict:
        """Add a comment to an issue."""
        payload: Dict[str, Any] = {"body": body}
        if visibility:
            payload["visibility"] = visibility
        return self._request("POST", f"{self.api_url}/issue/{issue_key}/comment", data=payload)

    def get_comments(self, issue_key: str) -> Dict:
        """Get all comments on an issue."""
        return self._request("GET", f"{self.api_url}/issue/{issue_key}/comment")

    # ── Attachments ──

    def add_attachment(self, issue_key: str, file_path: str) -> Dict:
        """Upload a file attachment to an issue."""
        import mimetypes
        filename = os.path.basename(file_path)
        content_type = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
        boundary = "----JiraAttachmentBoundary"

        with open(file_path, "rb") as f:
            file_data = f.read()

        body = (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
            f"Content-Type: {content_type}\r\n\r\n"
        ).encode("utf-8") + file_data + f"\r\n--{boundary}--\r\n".encode("utf-8")

        headers = {
            "Authorization": f"Bearer {self.pat}",
            "X-Atlassian-Token": "no-check",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        }
        return self._request("POST", f"{self.api_url}/issue/{issue_key}/attachments",
                             headers=headers, raw_data=body)

    # ── Projects ──

    def get_projects(self) -> List[Dict]:
        """Get all projects visible to the user."""
        result = self._request("GET", f"{self.api_url}/project")
        return result if isinstance(result, list) else []

    def get_project(self, project_key: str) -> Dict:
        """Get a specific project."""
        return self._request("GET", f"{self.api_url}/project/{project_key}")

    # ── Sprints (Agile API) ──

    def get_boards(self, project_key: Optional[str] = None) -> Dict:
        """Get all boards, optionally filtered by project."""
        qs = f"?projectKeyOrId={project_key}" if project_key else ""
        return self._request("GET", f"{self.agile_url}/board{qs}")

    def get_sprints(self, board_id: int, state: Optional[str] = None) -> Dict:
        """Get sprints for a board. State: future, active, closed."""
        qs = f"?state={state}" if state else ""
        return self._request("GET", f"{self.agile_url}/board/{board_id}/sprint{qs}")

    def create_sprint(self, name: str, board_id: int,
                      start_date: Optional[str] = None,
                      end_date: Optional[str] = None,
                      goal: Optional[str] = None) -> Dict:
        """Create a new sprint."""
        payload: Dict[str, Any] = {"name": name, "originBoardId": board_id}
        if start_date:
            payload["startDate"] = start_date
        if end_date:
            payload["endDate"] = end_date
        if goal:
            payload["goal"] = goal
        return self._request("POST", f"{self.agile_url}/sprint", data=payload)

    def move_issues_to_sprint(self, sprint_id: int, issue_keys: List[str]) -> Dict:
        """Move issues to a sprint."""
        return self._request("POST", f"{self.agile_url}/sprint/{sprint_id}/issue",
                             data={"issues": issue_keys})

    def get_sprint_issues(self, sprint_id: int, fields: Optional[List[str]] = None) -> Dict:
        """Get all issues in a sprint."""
        params = []
        if fields:
            params.append(f"fields={','.join(fields)}")
        qs = f"?{'&'.join(params)}" if params else ""
        return self._request("GET", f"{self.agile_url}/sprint/{sprint_id}/issue{qs}")

    # ── Bulk Operations ──

    def bulk_create_issues(self, issues: List[Dict]) -> Dict:
        """Bulk create issues."""
        return self._request("POST", f"{self.api_url}/issue/bulk",
                             data={"issueUpdates": [{"fields": i} for i in issues]})

    def bulk_transition(self, issue_keys: List[str], transition_id: str,
                        fields: Optional[Dict] = None) -> List[Dict]:
        """Transition multiple issues."""
        results = []
        for key in issue_keys:
            result = self.transition_issue(key, transition_id, fields)
            results.append({"key": key, "result": result})
        return results

    # ── Utility ──

    def get_issue_types(self, project_key: Optional[str] = None) -> List[Dict]:
        """Get available issue types."""
        if project_key:
            project = self.get_project(project_key)
            return project.get("issueTypes", [])
        return self._request("GET", f"{self.api_url}/issuetype")

    def get_priorities(self) -> List[Dict]:
        """Get available priorities."""
        result = self._request("GET", f"{self.api_url}/priority")
        return result if isinstance(result, list) else []

    def get_statuses(self) -> List[Dict]:
        """Get available statuses."""
        result = self._request("GET", f"{self.api_url}/status")
        return result if isinstance(result, list) else []

    def get_users(self, query: str = "", max_results: int = 50) -> List[Dict]:
        """Search for users."""
        qs = f"?username={urllib.parse.quote(query)}&maxResults={max_results}"
        result = self._request("GET", f"{self.api_url}/user/search{qs}")
        return result if isinstance(result, list) else []

    def test_connection(self) -> Dict:
        """Test the API connection and authentication."""
        return self._request("GET", f"{self.api_url}/myself")


def main():
    """CLI entry point for quick testing."""
    import argparse
    parser = argparse.ArgumentParser(description="Jira Data Center API Client")
    parser.add_argument("action", choices=["test", "projects", "search", "issue"],
                        help="Action to perform")
    parser.add_argument("--jql", help="JQL query for search")
    parser.add_argument("--key", help="Issue key for issue action")
    parser.add_argument("--base-url", help="Jira base URL (or JIRA_BASE_URL env)")
    parser.add_argument("--pat", help="PAT token (or JIRA_PAT env)")
    args = parser.parse_args()

    client = JiraClient(base_url=args.base_url, pat=args.pat)

    if args.action == "test":
        result = client.test_connection()
    elif args.action == "projects":
        result = client.get_projects()
    elif args.action == "search":
        if not args.jql:
            parser.error("--jql required for search")
        result = client.search(args.jql)
    elif args.action == "issue":
        if not args.key:
            parser.error("--key required for issue")
        result = client.get_issue(args.key)
    else:
        result = {"error": "Unknown action"}

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
