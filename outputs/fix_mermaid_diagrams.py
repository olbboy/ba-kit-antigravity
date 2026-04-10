#!/usr/bin/env python3
"""
Fix mermaid diagrams on Confluence:
1. Extract mermaid code from local markdown files
2. Render to PNG via Kroki.io
3. Upload as attachments to Confluence pages
4. Update page XHTML to use <ac:image> instead of broken code macro

Root cause: Confluence Code Macro only supports a finite list of languages.
"mermaid" is NOT a valid language → "Error rendering macro 'code': Invalid value"
"""

import os
import sys
import re
import time
import base64
import zlib
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

BASE_URL = os.environ.get('CONFLUENCE_BASE_URL', '').rstrip('/')
PAT = os.environ.get('CONFLUENCE_PAT', '')
API = f"{BASE_URL}/rest/api/content"
HEADERS = {
    'Authorization': f'Bearer {PAT}',
    'Content-Type': 'application/json',
}
SRC_DIR = Path(__file__).parent / 'mini-app-cham-cong'

# File → Page ID mapping (only files with mermaid)
MERMAID_FILES = {
    '2.11-Mini-app/README.md': '196786907',
    '2.11-Mini-app/2.11.1.-Chấm-công-và-Nhật-ký-chấm-công/README.md': '196786908',
    '2.11-Mini-app/2.11.3.-Giải-trình-công/README.md': '196786927',
    '2.11-Mini-app/2.11.7.-Cấu-hình-lịch-nghỉ/README.md': '196786944',
    '2.11-Mini-app/Tài-liệu-dự-án-Mini-App/BRD-HR-(Admin).md': '196786958',
    '2.11-Mini-app/Tài-liệu-dự-án-Mini-App/BRD-Nhân-viên.md': '196786959',
}


def extract_mermaid_blocks(filepath):
    """Extract all mermaid code blocks from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = []
    pattern = re.compile(r'```mermaid\n(.*?)```', re.DOTALL)
    for i, match in enumerate(pattern.finditer(content)):
        blocks.append(match.group(1).strip())
    return blocks


def render_mermaid_png(mermaid_code):
    """Render mermaid diagram to PNG using Kroki.io."""
    # Kroki accepts base64-encoded, deflated mermaid code
    compressed = zlib.compress(mermaid_code.encode('utf-8'), 9)
    encoded = base64.urlsafe_b64encode(compressed).decode('ascii')
    
    url = f"https://kroki.io/mermaid/png/{encoded}"
    resp = requests.get(url, timeout=30)
    
    if resp.status_code == 200:
        return resp.content
    else:
        print(f"    ⚠️  Kroki error {resp.status_code}: {resp.text[:100]}")
        return None


def upload_attachment(page_id, filename, png_data):
    """Upload PNG as attachment to Confluence page."""
    url = f"{API}/{page_id}/child/attachment"
    headers = {
        'Authorization': f'Bearer {PAT}',
        'X-Atlassian-Token': 'nocheck',
    }
    
    # Check if attachment already exists
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 200:
        for att in resp.json().get('results', []):
            if att['title'] == filename:
                # Update existing
                att_id = att['id']
                update_url = f"{API}/{page_id}/child/attachment/{att_id}/data"
                files = {'file': (filename, png_data, 'image/png')}
                r = requests.post(update_url, headers=headers, files=files)
                return r.status_code == 200
    
    # Create new
    files = {'file': (filename, png_data, 'image/png')}
    resp = requests.post(url, headers=headers, files=files)
    return resp.status_code == 200


def get_page(page_id):
    """Get page content and version."""
    resp = requests.get(f"{API}/{page_id}?expand=body.storage,version", headers=HEADERS)
    return resp.json() if resp.status_code == 200 else None


def update_page_body(page_id, title, body, version):
    """Update page body."""
    payload = {
        "type": "page",
        "title": title,
        "version": {"number": version + 1},
        "body": {"storage": {"value": body, "representation": "storage"}}
    }
    resp = requests.put(f"{API}/{page_id}", headers=HEADERS, json=payload)
    if resp.status_code == 200:
        return True
    print(f"    ❌ Update failed: {resp.status_code}: {resp.text[:200]}")
    return False


def replace_mermaid_code_macros(xhtml_body, image_filenames):
    """Replace mermaid code macros with image references in XHTML."""
    # Pattern to match mermaid code blocks in XHTML
    mermaid_pattern = re.compile(
        r'<ac:structured-macro ac:name="code">\s*'
        r'<ac:parameter ac:name="language">mermaid</ac:parameter>\s*'
        r'<ac:plain-text-body><!\[CDATA\[.*?\]\]></ac:plain-text-body>\s*'
        r'</ac:structured-macro>',
        re.DOTALL
    )
    
    matches = list(mermaid_pattern.finditer(xhtml_body))
    
    # Replace in reverse order to preserve positions
    for i, match in enumerate(reversed(matches)):
        img_idx = len(matches) - 1 - i
        if img_idx < len(image_filenames):
            filename = image_filenames[img_idx]
            replacement = f'<p><ac:image ac:width="800"><ri:attachment ri:filename="{filename}" /></ac:image></p>'
            xhtml_body = xhtml_body[:match.start()] + replacement + xhtml_body[match.end():]
    
    return xhtml_body


def main():
    print("=" * 60)
    print("Fix Mermaid Diagrams on Confluence")
    print(f"Files with mermaid: {len(MERMAID_FILES)}")
    print("=" * 60)
    
    if not BASE_URL or not PAT:
        print("ERROR: Missing CONFLUENCE_BASE_URL or CONFLUENCE_PAT")
        sys.exit(1)
    
    total_diagrams = 0
    total_fixed = 0
    
    for rel_path, page_id in MERMAID_FILES.items():
        filepath = SRC_DIR / rel_path
        if not filepath.exists():
            print(f"  ⚠️  File not found: {rel_path}")
            continue
        
        print(f"\n📄 {rel_path} (page: {page_id})")
        
        # Extract mermaid blocks
        blocks = extract_mermaid_blocks(filepath)
        if not blocks:
            print("  ⏩ No mermaid blocks found")
            continue
        
        print(f"  Found {len(blocks)} mermaid diagram(s)")
        
        # Render each block to PNG and upload
        image_filenames = []
        for i, mermaid_code in enumerate(blocks):
            diagram_name = f"diagram_{os.path.basename(rel_path).replace('.md', '')}_{i+1}.png"
            
            # Render via Kroki
            png_data = render_mermaid_png(mermaid_code)
            if not png_data:
                print(f"    ❌ Failed to render diagram {i+1}")
                image_filenames.append(None)
                continue
            
            print(f"    ✅ Rendered diagram {i+1} ({len(png_data)} bytes)")
            
            # Upload to Confluence
            if upload_attachment(page_id, diagram_name, png_data):
                print(f"    ✅ Uploaded: {diagram_name}")
                image_filenames.append(diagram_name)
                total_diagrams += 1
            else:
                print(f"    ❌ Failed to upload: {diagram_name}")
                image_filenames.append(None)
            
            time.sleep(0.5)
        
        # Now update the page body to replace mermaid code macros with image refs
        valid_filenames = [f for f in image_filenames if f is not None]
        if not valid_filenames:
            continue
        
        page = get_page(page_id)
        if not page:
            print(f"  ❌ Cannot get page {page_id}")
            continue
        
        title = page['title']
        version = page['version']['number']
        body = page['body']['storage']['value']
        
        new_body = replace_mermaid_code_macros(body, valid_filenames)
        
        if new_body != body:
            if update_page_body(page_id, title, new_body, version):
                print(f"  ✅ Page updated: replaced {len(valid_filenames)} diagram(s) with images")
                total_fixed += 1
            else:
                print(f"  ❌ Failed to update page body")
        else:
            print(f"  ⏩ No mermaid code macros found in current page body")
        
        time.sleep(0.5)
    
    print(f"\n{'=' * 60}")
    print(f"DONE! Diagrams rendered: {total_diagrams} | Pages fixed: {total_fixed}")
    print("=" * 60)


if __name__ == '__main__':
    main()
