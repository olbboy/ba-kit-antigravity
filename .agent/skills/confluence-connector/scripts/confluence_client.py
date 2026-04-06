#!/usr/bin/env python3
"""
Confluence Data Center REST API Client Library.
Handles authentication, pagination, error handling, and common operations.

Usage:
    from confluence_client import ConfluenceClient
    client = ConfluenceClient()  # reads from env vars
    client = ConfluenceClient(base_url="https://confluence.example.com", pat="your-token")
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


class ConfluenceClient:
    """Confluence Data Center REST API client using PAT authentication."""

    def __init__(self, base_url: Optional[str] = None, pat: Optional[str] = None,
                 verify_ssl: bool = True, max_retries: int = 3):
        self.base_url = (base_url or os.environ.get("CONFLUENCE_BASE_URL", "")).rstrip("/")
        self.pat = pat or os.environ.get("CONFLUENCE_PAT", "")

        if not self.base_url:
            raise ValueError("CONFLUENCE_BASE_URL not set. Provide base_url or set CONFLUENCE_BASE_URL env var.")
        if not self.pat:
            raise ValueError("CONFLUENCE_PAT not set. Provide pat or set CONFLUENCE_PAT env var.")

        self.api_url = f"{self.base_url}/rest/api"
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

    def search(self, cql: str, limit: int = 25, start: int = 0,
               expand: Optional[List[str]] = None) -> Dict:
        """Search content using CQL."""
        params = [
            f"cql={urllib.parse.quote(cql)}",
            f"limit={limit}",
            f"start={start}",
        ]
        if expand:
            params.append(f"expand={','.join(expand)}")
        return self._request("GET", f"{self.api_url}/content/search?{'&'.join(params)}")

    def search_all(self, cql: str, expand: Optional[List[str]] = None,
                   page_size: int = 25) -> List[Dict]:
        """Search all content matching CQL (auto-paginate)."""
        all_results = []
        start = 0
        while True:
            result = self.search(cql, limit=page_size, start=start, expand=expand)
            results = result.get("results", [])
            if not results:
                break
            all_results.extend(results)
            if result.get("size", 0) < page_size:
                break
            start += page_size
        return all_results

    # ── Page CRUD ──

    def get_page(self, page_id: str, expand: Optional[List[str]] = None) -> Dict:
        """Get page by ID."""
        exp = f"?expand={','.join(expand)}" if expand else ""
        return self._request("GET", f"{self.api_url}/content/{page_id}{exp}")

    def get_page_by_title(self, space_key: str, title: str,
                          expand: Optional[List[str]] = None) -> Dict:
        """Get page by space key and title."""
        params = [
            f"spaceKey={urllib.parse.quote(space_key)}",
            f"title={urllib.parse.quote(title)}",
        ]
        if expand:
            params.append(f"expand={','.join(expand)}")
        return self._request("GET", f"{self.api_url}/content?{'&'.join(params)}")

    def create_page(self, space_key: str, title: str, body: str,
                    parent_id: Optional[str] = None,
                    content_type: str = "page") -> Dict:
        """Create a new page."""
        payload: Dict[str, Any] = {
            "type": content_type,
            "title": title,
            "space": {"key": space_key},
            "body": {
                "storage": {
                    "value": body,
                    "representation": "storage"
                }
            }
        }
        if parent_id:
            payload["ancestors"] = [{"id": str(parent_id)}]
        return self._request("POST", f"{self.api_url}/content", data=payload)

    def update_page(self, page_id: str, title: str, body: str,
                    version_number: int, content_type: str = "page",
                    version_message: Optional[str] = None) -> Dict:
        """Update an existing page. version_number must be current version + 1."""
        version: Dict[str, Any] = {"number": version_number}
        if version_message:
            version["message"] = version_message
        payload = {
            "type": content_type,
            "title": title,
            "version": version,
            "body": {
                "storage": {
                    "value": body,
                    "representation": "storage"
                }
            }
        }
        return self._request("PUT", f"{self.api_url}/content/{page_id}", data=payload)

    def delete_page(self, page_id: str) -> Dict:
        """Delete a page."""
        return self._request("DELETE", f"{self.api_url}/content/{page_id}?status=current")

    def get_page_version(self, page_id: str) -> int:
        """Get the current version number of a page."""
        result = self.get_page(page_id, expand=["version"])
        return result.get("version", {}).get("number", 0)

    # ── Spaces ──

    def get_spaces(self, limit: int = 25, start: int = 0,
                   space_type: Optional[str] = None) -> Dict:
        """Get all spaces."""
        params = [f"limit={limit}", f"start={start}"]
        if space_type:
            params.append(f"type={space_type}")
        return self._request("GET", f"{self.api_url}/space?{'&'.join(params)}")

    def get_space(self, space_key: str, expand: Optional[List[str]] = None) -> Dict:
        """Get space by key."""
        exp = f"?expand={','.join(expand)}" if expand else ""
        return self._request("GET", f"{self.api_url}/space/{space_key}{exp}")

    def create_space(self, key: str, name: str, description: str = "",
                     space_type: str = "global") -> Dict:
        """Create a new space."""
        payload: Dict[str, Any] = {
            "key": key,
            "name": name,
            "type": space_type,
        }
        if description:
            payload["description"] = {
                "plain": {"value": description, "representation": "plain"}
            }
        return self._request("POST", f"{self.api_url}/space", data=payload)

    def get_space_content(self, space_key: str, content_type: str = "page",
                          limit: int = 25, start: int = 0) -> Dict:
        """Get content in a space."""
        return self._request(
            "GET",
            f"{self.api_url}/space/{space_key}/content/{content_type}?limit={limit}&start={start}"
        )

    # ── Comments ──

    def get_comments(self, page_id: str, expand: Optional[List[str]] = None) -> Dict:
        """Get comments on a page."""
        exp = f"?expand={','.join(expand)}" if expand else ""
        return self._request("GET", f"{self.api_url}/content/{page_id}/child/comment{exp}")

    def add_comment(self, page_id: str, body: str) -> Dict:
        """Add a comment to a page."""
        payload = {
            "type": "comment",
            "container": {"id": str(page_id), "type": "page"},
            "body": {
                "storage": {
                    "value": body,
                    "representation": "storage"
                }
            }
        }
        return self._request("POST", f"{self.api_url}/content", data=payload)

    # ── Attachments ──

    def get_attachments(self, page_id: str) -> Dict:
        """Get attachments on a page."""
        return self._request("GET", f"{self.api_url}/content/{page_id}/child/attachment")

    def add_attachment(self, page_id: str, file_path: str) -> Dict:
        """Upload a file attachment to a page."""
        import mimetypes
        filename = os.path.basename(file_path)
        content_type = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
        boundary = "----ConfluenceAttachmentBoundary"

        with open(file_path, "rb") as f:
            file_data = f.read()

        body = (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
            f"Content-Type: {content_type}\r\n\r\n"
        ).encode("utf-8") + file_data + f"\r\n--{boundary}--\r\n".encode("utf-8")

        headers = {
            "Authorization": f"Bearer {self.pat}",
            "X-Atlassian-Token": "nocheck",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        }
        return self._request("POST", f"{self.api_url}/content/{page_id}/child/attachment",
                             headers=headers, raw_data=body)

    # ── Labels ──

    def get_labels(self, page_id: str) -> Dict:
        """Get labels on a page."""
        return self._request("GET", f"{self.api_url}/content/{page_id}/label")

    def add_labels(self, page_id: str, labels: List[str]) -> Dict:
        """Add labels to a page."""
        payload = [{"prefix": "global", "name": label} for label in labels]
        return self._request("POST", f"{self.api_url}/content/{page_id}/label", data=payload)

    def remove_label(self, page_id: str, label: str) -> Dict:
        """Remove a label from a page."""
        return self._request("DELETE", f"{self.api_url}/content/{page_id}/label/{label}")

    # ── Page Restrictions ──

    def get_restrictions(self, page_id: str) -> Dict:
        """Get page restrictions."""
        return self._request("GET", f"{self.api_url}/content/{page_id}/restriction")

    # ── Content Properties ──

    def get_property(self, page_id: str, key: str) -> Dict:
        """Get a content property."""
        return self._request("GET", f"{self.api_url}/content/{page_id}/property/{key}")

    def set_property(self, page_id: str, key: str, value: Any) -> Dict:
        """Set a content property."""
        return self._request("POST", f"{self.api_url}/content/{page_id}/property/{key}",
                             data={"value": value})

    # ── History ──

    def get_history(self, page_id: str) -> Dict:
        """Get page history."""
        return self._request("GET", f"{self.api_url}/content/{page_id}/history")

    # ── Children ──

    def get_children(self, page_id: str, child_type: str = "page",
                     limit: int = 25, start: int = 0) -> Dict:
        """Get child pages."""
        return self._request(
            "GET",
            f"{self.api_url}/content/{page_id}/child/{child_type}?limit={limit}&start={start}"
        )

    # ── Bulk Operations ──

    def bulk_create_pages(self, space_key: str, pages: List[Dict[str, str]],
                          parent_id: Optional[str] = None) -> List[Dict]:
        """Create multiple pages. Each dict needs 'title' and 'body'."""
        results = []
        for page in pages:
            result = self.create_page(
                space_key=space_key,
                title=page["title"],
                body=page["body"],
                parent_id=parent_id
            )
            results.append(result)
        return results

    def bulk_add_labels(self, page_ids: List[str], labels: List[str]) -> List[Dict]:
        """Add labels to multiple pages."""
        results = []
        for page_id in page_ids:
            result = self.add_labels(page_id, labels)
            results.append({"page_id": page_id, "result": result})
        return results

    # ── Utility ──

    def test_connection(self) -> Dict:
        """Test the API connection and authentication."""
        return self._request("GET", f"{self.api_url}/space?limit=1")

    def convert_to_storage(self, content: str, representation: str = "wiki") -> Dict:
        """Convert content to storage format."""
        return self._request("POST", f"{self.api_url}/contentbody/convert/storage",
                             data={"value": content, "representation": representation})


def main():
    """CLI entry point for quick testing."""
    import argparse
    parser = argparse.ArgumentParser(description="Confluence Data Center API Client")
    parser.add_argument("action", choices=["test", "spaces", "search", "page"],
                        help="Action to perform")
    parser.add_argument("--cql", help="CQL query for search")
    parser.add_argument("--id", help="Page ID for page action")
    parser.add_argument("--base-url", help="Confluence base URL (or CONFLUENCE_BASE_URL env)")
    parser.add_argument("--pat", help="PAT token (or CONFLUENCE_PAT env)")
    args = parser.parse_args()

    client = ConfluenceClient(base_url=args.base_url, pat=args.pat)

    if args.action == "test":
        result = client.test_connection()
    elif args.action == "spaces":
        result = client.get_spaces()
    elif args.action == "search":
        if not args.cql:
            parser.error("--cql required for search")
        result = client.search(args.cql)
    elif args.action == "page":
        if not args.id:
            parser.error("--id required for page")
        result = client.get_page(args.id, expand=["body.storage", "version", "space"])
    else:
        result = {"error": "Unknown action"}

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
