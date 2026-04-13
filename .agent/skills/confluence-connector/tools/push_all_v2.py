#!/usr/bin/env python3
"""
Push entire restructured mini-app-cham-cong documentation to Confluence.
Handles the new phase-based structure with api-spec and db-schema files.
"""
import os, sys, re, time, json, requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

BASE_URL = os.environ.get('CONFLUENCE_BASE_URL', '').rstrip('/')
PAT = os.environ.get('CONFLUENCE_PAT', '')
SPACE_KEY = 'CVH'
API = f"{BASE_URL}/rest/api/content"
HEADERS = {'Authorization': f'Bearer {PAT}', 'Content-Type': 'application/json'}
SRC = Path(os.path.dirname(__file__)) / 'mini-app-cham-cong'

# Root parent: Mini App Cham cong (New)
ROOT_PARENT_ID = '196786905'

# Cache for page IDs
PAGE_CACHE = {}


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
    if not rows: return ''
    h = '<table><colgroup>'
    for _ in rows[0]: h += '<col />'
    h += '</colgroup><tbody>'
    for i, row in enumerate(rows):
        h += '<tr>'
        tag = 'th' if i == 0 else 'td'
        for cell in row: h += f'<{tag}>{_inline(cell)}</{tag}>'
        h += '</tr>'
    h += '</tbody></table>'
    return h


# Confluence DC language mapping (CRITICAL — DC breaks on unsupported languages)
DC_LANG_MAP = {'json': 'javascript', 'gherkin': 'text', 'typescript': 'javascript', 'go': 'text', 'rust': 'text'}
DC_TITLE_MAP = {'json': 'JSON', 'gherkin': 'Gherkin Scenarios', 'typescript': 'TypeScript', 'go': 'Go', 'rust': 'Rust'}

def md_to_xhtml(md):
    lines = md.split('\n')
    out = []
    in_tbl = in_code = in_list = False
    c_lang = ''; c_orig_lang = ''; c_lines = []; lt = None; trows = []
    for line in lines:
        if line.startswith('```'):
            if in_code:
                code_content = chr(10).join(c_lines)
                if c_orig_lang == 'mermaid':
                    # Use Stratus mermaid-macro plugin
                    out.append(f'<ac:structured-macro ac:name="mermaid-macro"><ac:plain-text-body><![CDATA[{code_content}]]></ac:plain-text-body></ac:structured-macro>')
                else:
                    title_param = f'<ac:parameter ac:name="title">{DC_TITLE_MAP[c_orig_lang]}</ac:parameter>' if c_orig_lang in DC_TITLE_MAP else ''
                    out.append(f'<ac:structured-macro ac:name="code"><ac:parameter ac:name="language">{c_lang}</ac:parameter>{title_param}<ac:plain-text-body><![CDATA[{code_content}]]></ac:plain-text-body></ac:structured-macro>')
                in_code = False; c_lines = []
            else:
                if in_list: out.append(f'</{lt}>'); in_list = False
                in_code = True
                c_orig_lang = line[3:].strip() or 'text'
                c_lang = DC_LANG_MAP.get(c_orig_lang, c_orig_lang)
            continue
        if in_code: c_lines.append(line); continue
        if '|' in line and line.strip().startswith('|'):
            if in_list: out.append(f'</{lt}>'); in_list = False
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            if all(set(c) <= {'-',':','+',' '} for c in cells): continue
            if not in_tbl: in_tbl = True; trows = []
            trows.append(cells); continue
        elif in_tbl: out.append(_table(trows)); in_tbl = False; trows = []
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            if in_list: out.append(f'</{lt}>'); in_list = False
            out.append(f'<h{len(m.group(1))}>{_inline(m.group(2))}</h{len(m.group(1))}>'); continue
        if line.strip() in ('---','***','___'):
            if in_list: out.append(f'</{lt}>'); in_list = False
            out.append('<hr />'); continue
        ul = re.match(r'^(\s*)[-*]\s+(.*)', line)
        if ul:
            if not in_list or lt != 'ul':
                if in_list: out.append(f'</{lt}>')
                out.append('<ul>'); in_list = True; lt = 'ul'
            out.append(f'<li>{_inline(ul.group(2))}</li>'); continue
        ol = re.match(r'^(\s*)\d+\.\s+(.*)', line)
        if ol:
            if not in_list or lt != 'ol':
                if in_list: out.append(f'</{lt}>')
                out.append('<ol>'); in_list = True; lt = 'ol'
            out.append(f'<li>{_inline(ol.group(2))}</li>'); continue
        if not line.strip():
            if in_list: out.append(f'</{lt}>'); in_list = False
            continue
        if in_list: out.append(f'</{lt}>'); in_list = False
        t = _inline(line)
        if t: out.append(f'<p>{t}</p>')
    if in_tbl: out.append(_table(trows))
    if in_list: out.append(f'</{lt}>')
    if in_code:
        code_content = chr(10).join(c_lines)
        if c_orig_lang == 'mermaid':
            out.append(f'<ac:structured-macro ac:name="mermaid-macro"><ac:plain-text-body><![CDATA[{code_content}]]></ac:plain-text-body></ac:structured-macro>')
        else:
            title_param = f'<ac:parameter ac:name="title">{DC_TITLE_MAP[c_orig_lang]}</ac:parameter>' if c_orig_lang in DC_TITLE_MAP else ''
            out.append(f'<ac:structured-macro ac:name="code"><ac:parameter ac:name="language">{c_lang}</ac:parameter>{title_param}<ac:plain-text-body><![CDATA[{code_content}]]></ac:plain-text-body></ac:structured-macro>')
    return '\n'.join(out)


def get_title_from_md(filepath):
    """Extract title from first H1 in markdown."""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
    return filepath.stem


def find_page_under_root(title, parent_id):
    """Find page by title ONLY if it's under ROOT_PARENT_ID hierarchy. Parent-safe."""
    cache_key = f"{parent_id}:{title}"
    if cache_key in PAGE_CACHE:
        return PAGE_CACHE[cache_key]
    resp = requests.get(
        f"{API}?spaceKey={SPACE_KEY}&title={requests.utils.quote(title)}&expand=ancestors",
        headers=HEADERS
    )
    if resp.status_code == 200:
        for page in resp.json().get('results', []):
            # SAFETY CHECK: only match pages that are descendants of ROOT_PARENT_ID
            ancestor_ids = [a['id'] for a in page.get('ancestors', [])]
            if ROOT_PARENT_ID in ancestor_ids or page['id'] == ROOT_PARENT_ID:
                pid = page['id']
                PAGE_CACHE[cache_key] = pid
                return pid
    return None


def create_or_update_page(title, body, parent_id):
    """Create page if not exists under our root, update if exists. PARENT-SAFE."""
    page_id = find_page_under_root(title, parent_id)
    if page_id:
        # Update — only pages confirmed under our root
        resp = requests.get(f"{API}/{page_id}?expand=version", headers=HEADERS)
        if resp.status_code == 200:
            ver = resp.json()['version']['number']
            payload = {
                "version": {"number": ver + 1},
                "title": title,
                "type": "page",
                "body": {"storage": {"value": body, "representation": "storage"}}
            }
            resp2 = requests.put(f"{API}/{page_id}", headers=HEADERS, json=payload)
            if resp2.status_code == 200:
                return page_id, 'updated'
            else:
                return page_id, f'update-fail:{resp2.status_code}'
        return page_id, 'exists'
    else:
        # Create under specified parent
        payload = {
            "type": "page", "title": title, "space": {"key": SPACE_KEY},
            "ancestors": [{"id": str(parent_id)}],
            "body": {"storage": {"value": body, "representation": "storage"}}
        }
        resp = requests.post(API, headers=HEADERS, json=payload)
        if resp.status_code == 200:
            pid = resp.json()['id']
            PAGE_CACHE[f"{parent_id}:{title}"] = pid
            return pid, 'created'
        else:
            return None, f'create-fail:{resp.status_code}:{resp.text[:150]}'


def push_file(filepath, title, parent_id):
    """Push a single markdown file to Confluence."""
    with open(filepath, 'r', encoding='utf-8') as f:
        md = f.read()
    body = md_to_xhtml(md)
    pid, status = create_or_update_page(title, body, parent_id)
    return pid, status


def main():
    print("=" * 60)
    print("Push ALL mini-app-cham-cong to Confluence (new structure)")
    print("=" * 60)

    stats = {'created': 0, 'updated': 0, 'failed': 0, 'skipped': 0}

    # 1. ROOT files (README, INDEX, eams-v2)
    print("\n📁 Root files")
    root_files = [
        ('README.md', 'Mini App Cham cong - README'),
        ('INDEX.md', 'Mini App Cham cong - INDEX'),
        ('eams-v2-comprehensive.md', None),  # use title from markdown
    ]
    for fname, forced_title in root_files:
        fp = SRC / fname
        if not fp.exists():
            continue
        title = forced_title or get_title_from_md(fp)
        pid, status = push_file(fp, title, ROOT_PARENT_ID)
        print(f"  {'✅' if 'fail' not in status else '❌'} {title} ({status})")
        if 'fail' in status: stats['failed'] += 1
        elif status == 'created': stats['created'] += 1
        else: stats['updated'] += 1
        time.sleep(0.3)

    # 2. Overview directory
    overview_dir = SRC / 'overview'
    if overview_dir.exists():
        print("\n📁 Overview")
        ov_title = 'Mini App - Overview'
        readme = overview_dir / 'README.md'
        if readme.exists():
            ov_title = get_title_from_md(readme) or ov_title
        ov_pid, status = push_file(readme, ov_title, ROOT_PARENT_ID) if readme.exists() else (None, 'no-readme')
        print(f"  {'✅' if ov_pid else '⚠️'} {ov_title} ({status})")
        if ov_pid:
            if status == 'created': stats['created'] += 1
            else: stats['updated'] += 1
            for f in sorted(overview_dir.glob('*.md')):
                if f.name == 'README.md': continue
                t = get_title_from_md(f)
                pid2, s2 = push_file(f, t, ov_pid)
                print(f"    {'✅' if pid2 else '❌'} {t} ({s2})")
                if 'fail' in s2: stats['failed'] += 1
                elif s2 == 'created': stats['created'] += 1
                else: stats['updated'] += 1
                time.sleep(0.3)

    # 3. Phase directories
    phases = sorted([d for d in SRC.iterdir() if d.is_dir() and d.name.startswith('phase-')])
    for phase_dir in phases:
        phase_readme = phase_dir / 'plan.md'
        phase_title = f"Phase: {phase_dir.name}"
        if phase_readme.exists():
            phase_title_md = get_title_from_md(phase_readme)
            if phase_title_md and len(phase_title_md) > 5:
                phase_title = phase_title_md

        print(f"\n📁 {phase_dir.name}")
        # Push plan.md as phase root
        if phase_readme.exists():
            phase_pid, ps = push_file(phase_readme, phase_title, ROOT_PARENT_ID)
        else:
            phase_pid, ps = create_or_update_page(phase_title, f'<p>{phase_title}</p>', ROOT_PARENT_ID)
        print(f"  {'✅' if phase_pid else '❌'} {phase_title} ({ps})")
        if 'fail' in str(ps): stats['failed'] += 1
        elif ps == 'created': stats['created'] += 1
        else: stats['updated'] += 1
        time.sleep(0.3)

        if not phase_pid:
            continue

        # Push modules inside phase
        modules = sorted([d for d in phase_dir.iterdir() if d.is_dir()])
        for mod_dir in modules:
            mod_readme = mod_dir / 'README.md'
            mod_title = get_title_from_md(mod_readme) if mod_readme.exists() else mod_dir.name
            if mod_readme.exists():
                mod_pid, ms = push_file(mod_readme, mod_title, phase_pid)
            else:
                mod_pid, ms = create_or_update_page(mod_title, f'<p>{mod_title}</p>', phase_pid)
            print(f"    {'✅' if mod_pid else '❌'} {mod_title} ({ms})")
            if 'fail' in str(ms): stats['failed'] += 1
            elif ms == 'created': stats['created'] += 1
            else: stats['updated'] += 1
            time.sleep(0.3)

            if not mod_pid:
                continue

            # Push child files
            for child in sorted(mod_dir.glob('*.md')):
                if child.name == 'README.md':
                    continue
                if child.name == 'api-spec.md':
                    child_title = f"{mod_title} - API Spec"
                elif child.name == 'db-schema.md':
                    child_title = f"{mod_title} - DB Schema"
                else:
                    child_title = get_title_from_md(child) or child.stem
                pid3, s3 = push_file(child, child_title, mod_pid)
                print(f"      {'✅' if pid3 else '❌'} {child_title} ({s3})")
                if 'fail' in str(s3): stats['failed'] += 1
                elif s3 == 'created': stats['created'] += 1
                else: stats['updated'] += 1
                time.sleep(0.3)

    # 4. Cross-cutting directory
    cc_dir = SRC / 'cross-cutting'
    if cc_dir.exists():
        print(f"\n📁 cross-cutting")
        cc_title = 'Cross-Cutting Concerns'
        cc_pid, cs = create_or_update_page(cc_title, '<p>Cross-cutting modules</p>', ROOT_PARENT_ID)
        print(f"  {'✅' if cc_pid else '❌'} {cc_title} ({cs})")
        if cc_pid:
            if cs == 'created': stats['created'] += 1
            else: stats['updated'] += 1
            for mod_dir in sorted(cc_dir.iterdir()):
                if not mod_dir.is_dir(): continue
                mod_readme = mod_dir / 'README.md'
                mod_title = get_title_from_md(mod_readme) if mod_readme.exists() else mod_dir.name
                if mod_readme.exists():
                    mod_pid, ms = push_file(mod_readme, mod_title, cc_pid)
                else:
                    mod_pid, ms = create_or_update_page(mod_title, f'<p>{mod_title}</p>', cc_pid)
                print(f"    {'✅' if mod_pid else '❌'} {mod_title} ({ms})")
                if 'fail' in str(ms): stats['failed'] += 1
                elif ms == 'created': stats['created'] += 1
                else: stats['updated'] += 1
                time.sleep(0.3)
                if mod_pid:
                    for child in sorted(mod_dir.glob('*.md')):
                        if child.name == 'README.md': continue
                        child_title = get_title_from_md(child) or child.stem
                        pid4, s4 = push_file(child, child_title, mod_pid)
                        print(f"      {'✅' if pid4 else '❌'} {child_title} ({s4})")
                        if 'fail' in str(s4): stats['failed'] += 1
                        elif s4 == 'created': stats['created'] += 1
                        else: stats['updated'] += 1
                        time.sleep(0.3)

    print(f"\n{'=' * 60}")
    print(f"DONE! Created: {stats['created']} | Updated: {stats['updated']} | Failed: {stats['failed']}")
    print("=" * 60)


if __name__ == '__main__':
    main()
