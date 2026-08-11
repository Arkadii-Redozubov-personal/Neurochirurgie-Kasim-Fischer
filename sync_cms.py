#!/usr/bin/env python3
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

def sync_treatments(data):
    treatments = data.get('treatments', [])
    if not treatments:
        return

    print(f"\n📋 Syncing {len(treatments)} treatments to praxis-schwerpunkte.html...")
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'praxis-schwerpunkte.html')
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for treatment in treatments:
            lang_data = treatment.get(lang, {})
            if not lang_data:
                continue

            title = lang_data.get('title', '')
            if title:
                content = re.sub(
                    r'(<h3 class="service-title-new">)' + re.escape(title) + r'(</h3>)',
                    r'\g<1>' + title + r'\g<2>',
                    content
                )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def sync_pages(data):
    pages = data.get('pages', [])
    if not pages:
        print("ℹ️  No pages data to sync.")
        return

    print(f"\n📝 Syncing {len(pages)} pages across all languages...")

    for page in pages:
        page_id = page.get('id')
        sections = page.get('sections', [])
        if not page_id: continue
        
        filename = f"{page_id}.html"
        for lang, directory in DIRS.items():
            filepath = os.path.join(directory, filename)
            if not os.path.exists(filepath):
                continue
                
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            for section in sections:
                if section.get('type') == 'hero':
                    lang_data = section.get('content', {}).get(lang, {})
                    title = lang_data.get('title', '')
                    desc = lang_data.get('desc', '')
                    
                    if title:
                        content = re.sub(
                            r'(<h1[^>]*class="[^"]*hero-title[^"]*"[^>]*>).*?(</h1>)',
                            rf'\g<1>{title}\g<2>',
                            content,
                            flags=re.DOTALL | re.IGNORECASE
                        )
                    if desc:
                        content = re.sub(
                            r'(<p[^>]*class="[^"]*hero-desc[^"]*"[^>]*>).*?(</p>)',
                            rf'\g<1>{desc}\g<2>',
                            content,
                            flags=re.DOTALL | re.IGNORECASE
                        )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"   ✅ Processed {filepath}")

def main():
    print("=" * 55)
    print("  Neurochirurgie Fischer — CMS Sync Script")
    print("=" * 55)
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    data = load_cms_data()
    if not data:
        return

    print(f"✅ Loaded cms_data.json")
    print(f"   - Pages: {len(data.get('pages', []))}")
    print(f"   - Treatments: {len(data.get('treatments', []))}")

    sync_pages(data)
    sync_treatments(data)
    print("\n✅ All synchronization tasks completed successfully!")

if __name__ == '__main__':
    main()
