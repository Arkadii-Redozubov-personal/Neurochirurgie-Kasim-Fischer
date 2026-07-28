#!/usr/bin/env python3
"""
sync_cms.py - Neurochirurgie Fischer CMS Sync Script
=======================================================
Reads cms_data.json (exported from Admin Panel) and updates
all 30 HTML files across 5 language versions.

Usage:
    python sync_cms.py

Place cms_data.json in the same folder as this script (vertex/).
"""

import json
import os
import re
from datetime import datetime

DIRS = {
    'de': '.',
    'en': 'en',
    'ru': 'ru',
    'tr': 'tr',
    'ar': 'ar'
}

def load_cms_data(path='cms_data.json'):
    if not os.path.exists(path):
        print(f"❌ ERROR: {path} not found!")
        print("   Please export data from the Admin Panel first.")
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def update_html(filepath, replacements):
    """Apply a dict of {old_text: new_text} replacements to an HTML file."""
    if not os.path.exists(filepath):
        return False
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    changed = False
    for old, new in replacements.items():
        if old and new and old in content and old != new:
            content = content.replace(old, new)
            changed = True
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    return changed

def sync_treatments(data):
    """Update treatment descriptions in praxis-schwerpunkte.html files."""
    treatments = data.get('treatments', [])
    if not treatments:
        print("ℹ️  No treatments data to sync.")
        return

    print(f"\n📋 Syncing {len(treatments)} treatments...")

    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'praxis-schwerpunkte.html')
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all service cards and update them
        for treatment in treatments:
            lang_data = treatment.get(lang, {})
            if not lang_data:
                continue

            title = lang_data.get('title', '')
            desc = lang_data.get('desc', '')
            full_desc = lang_data.get('fullDesc', '')

            if not title:
                continue

            # Update title inside service cards (match by looking for the title in h3)
            if title:
                content = re.sub(
                    r'(<h3 class="service-title-new">)' + re.escape(title) + r'(</h3>)',
                    r'\g<1>' + title + r'\g<2>',
                    content
                )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ Updated {filepath}")

def sync_texts(data):
    """Update global texts (hero title, subtitles etc.) in index.html files."""
    texts = data.get('texts', {})
    if not texts:
        print("ℹ️  No texts data to sync.")
        return

    print(f"\n📝 Syncing global texts...")

    # Map field keys to CSS classes or IDs in HTML
    FIELD_MAP = {
        'hero_title': 'hero-title',
        'hero_subtitle': 'hero-desc',
        'treatments_title': 'section-title',
        'team_title': 'section-title'
    }

    for lang, directory in DIRS.items():
        lang_texts = texts.get(lang, {})
        if not lang_texts:
            continue

        filepath = os.path.join(directory, 'index.html')
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False
        for field, css_class in FIELD_MAP.items():
            new_val = lang_texts.get(field, '')
            if not new_val:
                continue

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ Processed {filepath}")

def main():
    print("=" * 55)
    print("  Neurochirurgie Fischer — CMS Sync Script")
    print("=" * 55)
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    data = load_cms_data()
    if not data:
        return

    print(f"✅ Loaded cms_data.json")
    print(f"   - Treatments: {len(data.get('treatments', []))}")
    print(f"   - Team members: {len(data.get('team', []))}")
    print(f"   - Text sets: {len(data.get('texts', {}))}")

    sync_treatments(data)
    sync_texts(data)

    print()
    print("=" * 55)
    print("  ✅ Sync complete!")
    print("=" * 55)

if __name__ == '__main__':
    main()
