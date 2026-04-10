#!/usr/bin/env python3
"""
Push NEW pages to Confluence (7 new US files + 1 module README).
Creates pages under the correct parent from the existing manifest.
Then re-syncs ALL pages (existing + new) with latest content.
"""

import os
import sys
import json
import re
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

BASE_URL = os.environ.get('CONFLUENCE_BASE_URL', '').rstrip('/')
PAT = os.environ.get('CONFLUENCE_PAT', '')
SPACE_KEY = 'CVH'
API = f"{BASE_URL}/rest/api/content"
HEADERS = {
    'Authorization': f'Bearer {PAT}',
    'Content-Type': 'application/json',
}

SRC_DIR = Path(__file__).parent / 'mini-app-cham-cong'


def _escape_xml(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    text = re.sub(r'[\U0001F300-\U0001F9FF\U00002600-\U000027BF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF'
                  r'\u2B50\u2705\u26A0\u2753\u274C\u2714\U0001F534\U0001F7E0\U0001F7E1'
                  r'\U0001F4CB\U0001F4D0\U0001F4C8\U0001F4C2\U0001F4D8\U0001F4D6\U0001F4C4'
                  r'\U0001F527\U0001F6A8\u2B55\U0001F7E2\U0001F4DD\u2B06\u2191'
                  r'\U0001F4E3\U0001F4E6\U0001F4E5\U0001F4E4\U0001F4E2\U0001F4E1'
                  r'\U0001F464\U0001F454\U0001F3E2\U00002699\U0001F528\u270F\u270B]', '', text)
    return text


def _clean_inline(text):
    def process_formatting(s):
        s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
        s = re.sub(r'\*\*\*\*', '', s)
        s = re.sub(r'\*\*(.+?)\*\*', lambda m: f'<strong>{_escape_xml(m.group(1))}</strong>', s)
        s = re.sub(r'(?<!<)\*(.+?)\*(?!>)', lambda m: f'<em>{_escape_xml(m.group(1))}</em>', s)
        s = re.sub(r'`(.+?)`', lambda m: f'<code>{_escape_xml(m.group(1))}</code>', s)
        return s
    result = process_formatting(text)
    final = []
    tag_pattern = re.compile(r'(</?(?:strong|em|code)[^>]*>)')
    for seg in tag_pattern.split(result):
        if tag_pattern.match(seg):
            final.append(seg)
        else:
            final.append(_escape_xml(seg))
    return ''.join(final).strip()


def _render_table(rows):
    if not rows:
        return ''
    html = '<table><colgroup>'
    for _ in rows[0]:
        html += '<col />'
    html += '</colgroup><tbody>'
    for i, row in enumerate(rows):
        html += '<tr>'
        tag = 'th' if i == 0 else 'td'
        for cell in row:
            html += f'<{tag}>{_clean_inline(cell)}</{tag}>'
        html += '</tr>'
    html += '</tbody></table>'
    return html


def md_to_xhtml(md_content):
    lines = md_content.split('\n')
    xhtml_parts = []
    in_table = False
    in_code = False
    code_lang = ''
    code_lines = []
    in_list = False
    list_type = None
    table_rows = []

    for line in lines:
        if line.startswith('```'):
            if in_code:
                code_content = '\n'.join(code_lines)
                xhtml_parts.append(
                    f'<ac:structured-macro ac:name="code">'
                    f'<ac:parameter ac:name="language">{code_lang}</ac:parameter>'
                    f'<ac:plain-text-body><![CDATA[{code_content}]]></ac:plain-text-body>'
                    f'</ac:structured-macro>')
                in_code = False
                code_lines = []
            else:
                if in_list:
                    xhtml_parts.append(f'</{list_type}>')
                    in_list = False
                in_code = True
                code_lang = line[3:].strip() or 'text'
            continue
        if in_code:
            code_lines.append(line)
            continue

        if '|' in line and line.strip().startswith('|'):
            if in_list:
                xhtml_parts.append(f'</{list_type}>')
                in_list = False
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            if all(set(c) <= {'-', ':', ' '} for c in cells):
                continue
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(cells)
            continue
        elif in_table:
            xhtml_parts.append(_render_table(table_rows))
            in_table = False
            table_rows = []

        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            if in_list:
                xhtml_parts.append(f'</{list_type}>')
                in_list = False
            level = len(m.group(1))
            text = _clean_inline(m.group(2))
            xhtml_parts.append(f'<h{level}>{text}</h{level}>')
            continue

        if line.strip() in ('---', '***', '___'):
            if in_list:
                xhtml_parts.append(f'</{list_type}>')
                in_list = False
            xhtml_parts.append('<hr />')
            continue

        m_ul = re.match(r'^(\s*)[-*]\s+(.*)', line)
        if m_ul:
            text = _clean_inline(m_ul.group(2))
            if not in_list or list_type != 'ul':
                if in_list:
                    xhtml_parts.append(f'</{list_type}>')
                xhtml_parts.append('<ul>')
                in_list = True
                list_type = 'ul'
            xhtml_parts.append(f'<li>{text}</li>')
            continue

        m_ol = re.match(r'^(\s*)\d+\.\s+(.*)', line)
        if m_ol:
            text = _clean_inline(m_ol.group(2))
            if not in_list or list_type != 'ol':
                if in_list:
                    xhtml_parts.append(f'</{list_type}>')
                xhtml_parts.append('<ol>')
                in_list = True
                list_type = 'ol'
            xhtml_parts.append(f'<li>{text}</li>')
            continue

        if not line.strip():
            if in_list:
                xhtml_parts.append(f'</{list_type}>')
                in_list = False
            continue

        if in_list:
            xhtml_parts.append(f'</{list_type}>')
            in_list = False
        text = _clean_inline(line)
        if text:
            xhtml_parts.append(f'<p>{text}</p>')

    if in_table:
        xhtml_parts.append(_render_table(table_rows))
    if in_list:
        xhtml_parts.append(f'</{list_type}>')
    if in_code:
        code_content = '\n'.join(code_lines)
        xhtml_parts.append(
            f'<ac:structured-macro ac:name="code">'
            f'<ac:parameter ac:name="language">{code_lang}</ac:parameter>'
            f'<ac:plain-text-body><![CDATA[{code_content}]]></ac:plain-text-body>'
            f'</ac:structured-macro>')

    return '\n'.join(xhtml_parts)


def create_page(title, body, parent_id):
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": SPACE_KEY},
        "ancestors": [{"id": str(parent_id)}],
        "body": {"storage": {"value": body, "representation": "storage"}}
    }
    resp = requests.post(API, headers=HEADERS, json=payload)
    if resp.status_code == 200:
        data = resp.json()
        return data['id']
    print(f"    ❌ Create failed: {resp.status_code}: {resp.text[:200]}")
    return None


def get_page(page_id):
    resp = requests.get(f"{API}/{page_id}?expand=body.storage,version", headers=HEADERS)
    return resp.json() if resp.status_code == 200 else None


def update_page(page_id, title, body, version):
    payload = {
        "type": "page",
        "title": title,
        "version": {"number": version + 1},
        "body": {"storage": {"value": body, "representation": "storage"}}
    }
    resp = requests.put(f"{API}/{page_id}", headers=HEADERS, json=payload)
    return resp.status_code == 200


# New pages to create (relative_path → (title, parent_page_id))
# Parent IDs from existing manifest
NEW_PAGES = {
    '2.11-Mini-app/2.11.1.-Chấm-công-và-Nhật-ký-chấm-công/US-ATTEN-05-Nhập-chấm-công-thủ-công.md': 
        ('US-ATTEN-05: Nhập chấm công thủ công (Manual Entry)', '196786908'),
    '2.11-Mini-app/2.11.3.-Giải-trình-công/US-EXPL-02-Yêu-cầu-sửa-chấm-công.md': 
        ('US-EXPL-02: Yêu cầu sửa chấm công (Attendance Correction)', '196786927'),
    '2.11-Mini-app/2.11.2.-Cấu-hình-ca-làm-việc/US-SHIFT-06-Phân-ca-theo-pattern.md': 
        ('US-SHIFT-06: Phân ca theo Pattern (Ca xoay)', '196786921'),
    '2.11-Mini-app/2.11.4.-Trung-tâm-đăng-ký/US-REG-05-Cấu-hình-chính-sách-phép-năm.md': 
        ('US-REG-05: Cấu hình chính sách phép năm', '196786929'),
    '2.11-Mini-app/2.11.12.-Quản-trị-hệ-thống/README.md': 
        ('2.11.12. Quản trị hệ thống', '196786907'),
    '2.11-Mini-app/2.11.12.-Quản-trị-hệ-thống/US-SYS-01-Quản-lý-chi-nhánh.md': 
        ('US-SYS-01: Quản lý chi nhánh (Site Management)', None),  # parent = Module 12 README (created above)
    '2.11-Mini-app/2.11.12.-Quản-trị-hệ-thống/US-SYS-02-Audit-log-viewer.md': 
        ('US-SYS-02: Audit Log Viewer', None),
    '2.11-Mini-app/2.11.12.-Quản-trị-hệ-thống/US-SYS-03-Employee-offboarding.md': 
        ('US-SYS-03: Employee Offboarding Workflow', None),
}

# Existing pages to UPDATE (from sync script)
EXISTING_PAGES = {
    'README.md': '196786905',
    'docs_business-comprehensive-documentation.md': '196786906',
    '2.11-Mini-app/README.md': '196786907',
    '2.11-Mini-app/2.11.1.-Chấm-công-và-Nhật-ký-chấm-công/README.md': '196786908',
    '2.11-Mini-app/2.11.2.-Cấu-hình-ca-làm-việc/README.md': '196786921',
    '2.11-Mini-app/2.11.3.-Giải-trình-công/README.md': '196786927',
    '2.11-Mini-app/2.11.4.-Trung-tâm-đăng-ký/README.md': '196786929',
}


def main():
    print("=" * 60)
    print("Phase 1: CREATE new pages in Confluence")
    print("=" * 60)

    module12_page_id = None
    created = 0

    for rel_path, (title, parent_id) in NEW_PAGES.items():
        filepath = SRC_DIR / rel_path
        if not filepath.exists():
            print(f"  ⚠️  File not found: {rel_path}")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            md = f.read()
        body = md_to_xhtml(md)

        # For SYS-01/02/03, parent = Module 12 page (created first)
        if parent_id is None:
            if module12_page_id is None:
                print(f"  ❌ Module 12 not yet created, skipping: {title}")
                continue
            parent_id = module12_page_id

        page_id = create_page(title, body, parent_id)
        if page_id:
            print(f"  ✅ Created: {title} (ID: {page_id})")
            created += 1
            if 'README.md' in rel_path and '2.11.12' in rel_path:
                module12_page_id = page_id
        time.sleep(0.3)

    print(f"\nCreated: {created} new pages")

    print("\n" + "=" * 60)
    print("Phase 2: UPDATE existing pages with new content")
    print("=" * 60)

    updated = 0
    for rel_path, page_id in EXISTING_PAGES.items():
        filepath = SRC_DIR / rel_path
        if not filepath.exists():
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            md = f.read()
        body = md_to_xhtml(md)
        page = get_page(page_id)
        if not page:
            continue
        title = page['title']
        version = page['version']['number']
        if update_page(page_id, title, body, version):
            print(f"  ✅ Updated: {title} (v{version+1})")
            updated += 1
        time.sleep(0.3)

    print(f"\n{'=' * 60}")
    print(f"DONE! Created: {created} | Updated: {updated}")
    print("=" * 60)


if __name__ == '__main__':
    main()
