#!/usr/bin/env python3
"""
Push Phase-01 documentation tree to Confluence.
Creates hierarchy under the existing "Mini App Chấm công (New)" parent page.
"""

import os, sys, re, time, requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

BASE_URL = os.environ.get('CONFLUENCE_BASE_URL', '').rstrip('/')
PAT = os.environ.get('CONFLUENCE_PAT', '')
SPACE_KEY = 'CVH'
API = f"{BASE_URL}/rest/api/content"
HEADERS = {'Authorization': f'Bearer {PAT}', 'Content-Type': 'application/json'}
SRC_DIR = Path(__file__).parent / 'mini-app-cham-cong'

# Parent: "Mini App Chấm công (New)" root page
ROOT_PARENT_ID = '196786905'


def _esc(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    t = re.sub(r'[^\x00-\x7F\u00C0-\u024F\u1E00-\u1EFF\u0300-\u036F]', '', t)
    return t


def _inline(t):
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    t = re.sub(r'\*\*\*\*', '', t)
    parts = []
    last = 0
    for m in re.finditer(r'\*\*(.+?)\*\*', t):
        parts.append(_esc(t[last:m.start()]))
        parts.append(f'<strong>{_esc(m.group(1))}</strong>')
        last = m.end()
    parts.append(_esc(t[last:]))
    t = ''.join(parts)
    t = re.sub(r'`([^`]+)`', lambda m: f'<code>{_esc(m.group(1))}</code>', t)
    return t.strip()


def _table(rows):
    if not rows:
        return ''
    h = '<table><colgroup>'
    for _ in rows[0]:
        h += '<col />'
    h += '</colgroup><tbody>'
    for i, row in enumerate(rows):
        h += '<tr>'
        tag = 'th' if i == 0 else 'td'
        for cell in row:
            h += f'<{tag}>{_inline(cell)}</{tag}>'
        h += '</tr>'
    h += '</tbody></table>'
    return h


def md_to_xhtml(md):
    lines = md.split('\n')
    out = []
    in_tbl = in_code = in_list = False
    c_lang = ''
    c_lines = []
    lt = None
    trows = []
    for line in lines:
        if line.startswith('```'):
            if in_code:
                out.append(
                    f'<ac:structured-macro ac:name="code">'
                    f'<ac:parameter ac:name="language">{c_lang}</ac:parameter>'
                    f'<ac:plain-text-body><![CDATA[{chr(10).join(c_lines)}]]></ac:plain-text-body>'
                    f'</ac:structured-macro>')
                in_code = False
                c_lines = []
            else:
                if in_list:
                    out.append(f'</{lt}>')
                    in_list = False
                in_code = True
                c_lang = line[3:].strip() or 'text'
                # Don't use 'mermaid' as language — Confluence doesn't support it
                if c_lang == 'mermaid':
                    c_lang = 'text'
            continue
        if in_code:
            c_lines.append(line)
            continue
        if '|' in line and line.strip().startswith('|'):
            if in_list:
                out.append(f'</{lt}>')
                in_list = False
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            if all(set(c) <= {'-', ':', '+', ' '} for c in cells):
                continue
            if not in_tbl:
                in_tbl = True
                trows = []
            trows.append(cells)
            continue
        elif in_tbl:
            out.append(_table(trows))
            in_tbl = False
            trows = []
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            if in_list:
                out.append(f'</{lt}>')
                in_list = False
            out.append(f'<h{len(m.group(1))}>{_inline(m.group(2))}</h{len(m.group(1))}>')
            continue
        if line.strip() in ('---', '***', '___'):
            if in_list:
                out.append(f'</{lt}>')
                in_list = False
            out.append('<hr />')
            continue
        ul = re.match(r'^(\s*)[-*]\s+(.*)', line)
        if ul:
            if not in_list or lt != 'ul':
                if in_list:
                    out.append(f'</{lt}>')
                out.append('<ul>')
                in_list = True
                lt = 'ul'
            out.append(f'<li>{_inline(ul.group(2))}</li>')
            continue
        ol = re.match(r'^(\s*)\d+\.\s+(.*)', line)
        if ol:
            if not in_list or lt != 'ol':
                if in_list:
                    out.append(f'</{lt}>')
                out.append('<ol>')
                in_list = True
                lt = 'ol'
            out.append(f'<li>{_inline(ol.group(2))}</li>')
            continue
        if not line.strip():
            if in_list:
                out.append(f'</{lt}>')
                in_list = False
            continue
        if in_list:
            out.append(f'</{lt}>')
            in_list = False
        t = _inline(line)
        if t:
            out.append(f'<p>{t}</p>')
    if in_tbl:
        out.append(_table(trows))
    if in_list:
        out.append(f'</{lt}>')
    if in_code:
        out.append(
            f'<ac:structured-macro ac:name="code">'
            f'<ac:parameter ac:name="language">{c_lang}</ac:parameter>'
            f'<ac:plain-text-body><![CDATA[{chr(10).join(c_lines)}]]></ac:plain-text-body>'
            f'</ac:structured-macro>')
    return '\n'.join(out)


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
        return resp.json()['id']
    print(f"    ❌ Create failed: {resp.status_code}: {resp.text[:200]}")
    return None


def get_page_by_title(title):
    resp = requests.get(f"{API}?spaceKey={SPACE_KEY}&title={requests.utils.quote(title)}", headers=HEADERS)
    if resp.status_code == 200:
        results = resp.json().get('results', [])
        if results:
            return results[0]['id']
    return None


def main():
    print("=" * 60)
    print("Push Phase-01 (Thiet Lap) to Confluence")
    print("=" * 60)

    # Phase-01 structure
    phase_dir = SRC_DIR / 'phase-01-thiet-lap'
    if not phase_dir.exists():
        print("ERROR: phase-01-thiet-lap directory not found")
        sys.exit(1)

    # Step 1: Create phase root page
    plan_file = phase_dir / 'plan.md'
    if plan_file.exists():
        with open(plan_file, 'r', encoding='utf-8') as f:
            plan_md = f.read()
        plan_body = md_to_xhtml(plan_md)
    else:
        plan_body = '<p>Phase 01: Thiet Lap - Sprint Implementation Plan</p>'

    phase_title = 'Phase 01: Thiet Lap (M05 + M06 + M07 + M09)'
    phase_id = get_page_by_title(phase_title)
    if not phase_id:
        phase_id = create_page(phase_title, plan_body, ROOT_PARENT_ID)
        print(f"✅ Created Phase root: {phase_title} (ID: {phase_id})")
    else:
        print(f"⏩ Phase root exists: {phase_title} (ID: {phase_id})")
    time.sleep(0.3)

    if not phase_id:
        print("FATAL: Could not create phase root page")
        sys.exit(1)

    # Step 2: Create module pages
    modules = [
        ('m05-quan-ly-nhan-su', 'M05 - Quan ly Nhan su'),
        ('m06-ca-lam-viec', 'M06 - Ca lam viec va Phan ca'),
        ('m07-lich-nghi', 'M07 - Cau hinh Lich nghi'),
        ('m09-thong-bao', 'M09 - Cau hinh Thong bao'),
    ]

    total_created = 0

    for module_dir_name, module_title in modules:
        module_dir = phase_dir / module_dir_name
        if not module_dir.exists():
            print(f"  ⚠️ Module dir not found: {module_dir_name}")
            continue

        # Create module parent (from README.md)
        readme_path = module_dir / 'README.md'
        if readme_path.exists():
            with open(readme_path, 'r', encoding='utf-8') as f:
                readme_md = f.read()
            readme_body = md_to_xhtml(readme_md)
        else:
            readme_body = f'<p>{module_title}</p>'

        mod_page_id = get_page_by_title(module_title)
        if not mod_page_id:
            mod_page_id = create_page(module_title, readme_body, phase_id)
            if mod_page_id:
                print(f"  ✅ Created module: {module_title} (ID: {mod_page_id})")
                total_created += 1
        else:
            print(f"  ⏩ Module exists: {module_title} (ID: {mod_page_id})")
        time.sleep(0.3)

        if not mod_page_id:
            continue

        # Create child pages (US files, api-spec, db-schema)
        for child_file in sorted(module_dir.glob('*.md')):
            if child_file.name == 'README.md':
                continue

            with open(child_file, 'r', encoding='utf-8') as f:
                child_md = f.read()
            child_body = md_to_xhtml(child_md)

            # Generate title
            if child_file.name == 'api-spec.md':
                child_title = f'{module_title} - API Specification'
            elif child_file.name == 'db-schema.md':
                child_title = f'{module_title} - DB Schema'
            else:
                # Extract title from markdown
                first_line = child_md.split('\n')[0].replace('# ', '').strip()
                child_title = first_line if first_line else child_file.stem

            existing = get_page_by_title(child_title)
            if not existing:
                page_id = create_page(child_title, child_body, mod_page_id)
                if page_id:
                    print(f"    ✅ Created: {child_title} (ID: {page_id})")
                    total_created += 1
            else:
                print(f"    ⏩ Exists: {child_title} (ID: {existing})")
            time.sleep(0.3)

    print(f"\n{'=' * 60}")
    print(f"Phase-01 DONE! Created: {total_created} new pages")
    print("=" * 60)

    # Now also sync existing 2.11-Mini-app pages
    print(f"\n{'=' * 60}")
    print("Now syncing existing 2.11-Mini-app pages...")
    print("=" * 60)
    os.system(f"cd {os.path.dirname(__file__)} && cd .. && python3 outputs/sync_to_confluence.py")
    print("\nRunning diagram fix...")
    os.system(f"cd {os.path.dirname(__file__)} && cd .. && python3 outputs/fix_mermaid_diagrams.py")


if __name__ == '__main__':
    main()
