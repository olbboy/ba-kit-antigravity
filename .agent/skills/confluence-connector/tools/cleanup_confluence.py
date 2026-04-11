#!/usr/bin/env python3
"""
Clean up Confluence: remove orphan pages from old 2.11-Mini-app structure
that no longer map to local files. Ensures 1:1 mapping with local structure.

Phase 1: Audit (dry run) — list what would be deleted
Phase 2: Delete (with confirmation)
"""
import os, sys, json, requests, time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

BASE_URL = os.environ.get('CONFLUENCE_BASE_URL', '').rstrip('/')
PAT = os.environ.get('CONFLUENCE_PAT', '')
SPACE_KEY = 'CVH'
API = f"{BASE_URL}/rest/api/content"
HEADERS = {'Authorization': f'Bearer {PAT}', 'Content-Type': 'application/json'}

# Root parent page
ROOT_ID = '196786905'

# Known good pages (created by push_all_v2.py) — these are the NEW structure pages
# We'll collect ALL pages under root, then check which ones map to NEW structure


def get_all_descendants(page_id, depth=0):
    """Recursively get all child pages under a page."""
    pages = []
    start = 0
    limit = 50
    while True:
        url = f"{API}/{page_id}/child/page?start={start}&limit={limit}&expand=version"
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code != 200:
            print(f"  Error fetching children of {page_id}: {resp.status_code}")
            break
        data = resp.json()
        results = data.get('results', [])
        if not results:
            break
        for page in results:
            pid = page['id']
            title = page['title']
            pages.append({
                'id': pid,
                'title': title,
                'depth': depth,
                'version': page['version']['number'],
                'parent_id': page_id,
            })
            # Recurse into children
            children = get_all_descendants(pid, depth + 1)
            pages.extend(children)
        start += limit
        if len(results) < limit:
            break
        time.sleep(0.2)
    return pages


def get_local_titles():
    """Get all titles that should exist (from local markdown files)."""
    SRC = Path(os.path.dirname(__file__)) / 'mini-app-cham-cong'
    titles = set()

    # Read first H1 from each .md file
    for md_file in SRC.rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    titles.add(line[2:].strip())
                    break

    # Also add known structural titles
    structural = [
        'Mini App Cham cong - README',
        'Mini App Cham cong - INDEX',
        'Mini App Chấm công (New)',  # root
        'Phase 01: Thiet Lap (M05 + M06 + M07 + M09)',  # old phase root
        'Cross-Cutting Concerns',
    ]
    titles.update(structural)

    return titles


def delete_page(page_id, title):
    """Delete a Confluence page."""
    resp = requests.delete(f"{API}/{page_id}", headers=HEADERS)
    if resp.status_code in (200, 204):
        return True
    else:
        print(f"  ❌ Failed to delete '{title}' (ID: {page_id}): {resp.status_code}")
        return False


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'audit'

    print("=" * 60)
    print(f"Confluence Cleanup — Mode: {mode.upper()}")
    print("=" * 60)

    # Step 1: Get all pages under root
    print(f"\n📡 Fetching all pages under root (ID: {ROOT_ID})...")
    all_pages = get_all_descendants(ROOT_ID)
    print(f"  Found {len(all_pages)} total pages on Confluence")

    # Step 2: Get local titles
    local_titles = get_local_titles()
    print(f"  Found {len(local_titles)} local titles")

    # Step 3: Identify OLD pages (from 2.11-Mini-app structure)
    # Old pages have titles like "2.11.X..." or "US-..." that are children of the OLD structure
    # New pages are children of Phase/Cross-cutting parents

    # Known OLD parent page IDs (from the old sync_to_confluence.py)
    OLD_PAGE_IDS = {
        '196786907',  # 2.11 Mini app (old root module page)
        '196786908',  # 2.11.1 Cham cong (old)
        '196786921',  # 2.11.2 Ca lam viec (old)
        '196786927',  # 2.11.3 Giai trinh (old)
        '196786929',  # 2.11.4 Trung tam dang ky (old)
        '196786935',  # 2.11.5 Bao cao ca nhan (old)
        '196786937',  # 2.11.6 Quan ly nhan su (old)
        '196786944',  # 2.11.7 Lich nghi (old)
        '196786949',  # 2.11.8 Camera AI (old)
        '196786953',  # 2.11.9 Thong bao (old)
        '196786956',  # 2.11.10 Phe duyet (old)
        '196786917',  # 2.11.11 Bao cao tong (old)
        '196786958',  # BRD-HR (old)
        '196786959',  # BRD-NV (old)
        '196786960',  # Demo Plan (old)
        '196786961',  # UAT (old)
        '196786957',  # Tai lieu du an (old)
        '196787048',  # 2.11.12 Quan tri (old)
        '196786906',  # EAMS doc (old)
        '196789739',  # US-CAM-04 (old location)
    }

    # Also collect ALL page IDs from old sync mapping
    OLD_SYNC_IDS = set()
    sync_path = os.path.join(os.path.dirname(__file__), 'sync_to_confluence.py')
    if os.path.exists(sync_path):
        with open(sync_path, 'r') as f:
            for line in f:
                # Extract page IDs from the mapping
                import re
                m = re.search(r"'(\d{9})'", line)
                if m:
                    OLD_SYNC_IDS.add(m.group(1))

    # Also include Phase-01 old root created by push_phase01.py
    OLD_ADDITIONAL = {
        '196789806',  # Phase 01: Thiet Lap (old)
        '196789807',  # M05 - Quan ly Nhan su (old)
        '196789810',  # M06 - Ca lam viec (old)
    }

    # Identify orphans: pages on Confluence whose titles don't match any local title
    # AND are from the old structure
    orphans = []
    keep = []

    for page in all_pages:
        pid = page['id']
        title = page['title']

        # Check if this is an old-structure page by ID
        is_old_by_id = pid in OLD_PAGE_IDS or pid in OLD_SYNC_IDS or pid in OLD_ADDITIONAL

        # Check if title exists in local
        title_matches_local = title in local_titles

        # A page is an orphan if:
        # 1. Its ID is in the old mapping, OR
        # 2. Its title doesn't match any local file
        # But we should KEEP pages that have matching content in the new structure

        # Simple approach: collect all pages, mark as OLD or NEW
        if is_old_by_id and not title_matches_local:
            orphans.append(page)
        elif not title_matches_local:
            # Check if it's a structural page from old structure
            old_indicators = [
                '2.11 Mini app',
                'M05 - Quan ly',
                'M06 - Ca lam viec',
                'M07 - Cau hinh',
                'M09 - Cau hinh',
                'Phase 01: Thiet Lap',
            ]
            if any(ind in title for ind in old_indicators):
                orphans.append(page)
            else:
                keep.append(page)
        else:
            keep.append(page)

    # Sort orphans by depth (deepest first — must delete children before parents)
    orphans.sort(key=lambda p: -p['depth'])

    print(f"\n{'=' * 60}")
    print(f"  Pages to KEEP: {len(keep)}")
    print(f"  Pages to DELETE (orphans): {len(orphans)}")
    print(f"{'=' * 60}")

    if orphans:
        print("\n🗑️  Pages to DELETE:")
        for p in orphans:
            indent = "  " * (p['depth'] + 1)
            print(f"{indent}❌ [{p['id']}] {p['title']} (v{p['version']})")

    if mode == 'audit':
        print(f"\n⚠️  DRY RUN — No pages deleted. Run with 'delete' to execute.")
        print(f"   python3 {sys.argv[0]} delete")
    elif mode == 'delete':
        print(f"\n🔥 DELETING {len(orphans)} orphan pages...")
        deleted = 0
        failed = 0
        for p in orphans:
            ok = delete_page(p['id'], p['title'])
            if ok:
                print(f"  ✅ Deleted: {p['title']} (ID: {p['id']})")
                deleted += 1
            else:
                failed += 1
            time.sleep(0.3)
        print(f"\n{'=' * 60}")
        print(f"DONE! Deleted: {deleted} | Failed: {failed}")
        print("=" * 60)

    # Show what's kept
    print(f"\n✅ Pages KEPT ({len(keep)}):")
    for p in sorted(keep, key=lambda x: x['title']):
        indent = "  " * (p['depth'] + 1)
        print(f"{indent}✅ {p['title']}")


if __name__ == '__main__':
    main()
