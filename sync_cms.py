#!/usr/bin/env python3
import json
import sys
sys.stdout.reconfigure(encoding="utf-8")
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
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def sync_schwerpunkte(data):
    schwerpunkte = data.get('schwerpunkte', [])
    if not schwerpunkte: return
    print(f"\n📋 Syncing {len(schwerpunkte)} schwerpunkte to praxis-schwerpunkte.html...")
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'praxis-schwerpunkte.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # we try to replace all <h3 class="service-title-new">...</h3> and <p class="service-desc-new">...</p>
        # but regex replacing by index is safer.
        titles = re.split(r'(<h3 class="service-title-new">)(.*?)(</h3>)', content, flags=re.DOTALL)
        descs = re.split(r'(<p class="service-desc-new">)(.*?)(</p>)', content, flags=re.DOTALL)
        
        # For simplicity, if lengths roughly match, we replace.
        for i, sp in enumerate(schwerpunkte):
            lang_data = sp.get(lang, {})
            title = lang_data.get('title', '')
            desc = lang_data.get('desc', '')
            
            if title and (i*4 + 2) < len(titles):
                titles[i*4 + 2] = title
            if desc and (i*4 + 2) < len(descs):
                descs[i*4 + 2] = desc
        
        content = "".join(titles)
        # re-split for descs since content string changed
        descs = re.split(r'(<p class="service-desc-new">)(.*?)(</p>)', content, flags=re.DOTALL)
        for i, sp in enumerate(schwerpunkte):
            lang_data = sp.get(lang, {})
            desc = lang_data.get('desc', '')
            if desc and (i*4 + 2) < len(descs):
                descs[i*4 + 2] = desc
                
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("".join(descs))

def sync_treatments(data):
    treatments = data.get('treatments', [])
    if not treatments: return
    print(f"\n📋 Syncing {len(treatments)} treatments to behandlungen.html...")
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'behandlungen.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        titles = re.split(r'(<h3 class="treatment-title">)(.*?)(</h3>)', content, flags=re.DOTALL)
        for i, tr in enumerate(treatments):
            lang_data = tr.get(lang, {})
            title = lang_data.get('title', '')
            if title and (i*4 + 2) < len(titles):
                titles[i*4 + 2] = title
        content = "".join(titles)

        descs = re.split(r'(<p class="treatment-desc">)(.*?)(</p>)', content, flags=re.DOTALL)
        for i, tr in enumerate(treatments):
            lang_data = tr.get(lang, {})
            desc = lang_data.get('desc', '')
            if desc and (i*4 + 2) < len(descs):
                descs[i*4 + 2] = desc
                
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("".join(descs))

def sync_team(data): # DISABLED because CMS order differs from HTML order
    team = data.get('team', [])
    if not team: return
    print(f"\n📋 Syncing {len(team)} team members to unser-team.html...")
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'unser-team.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace names
        names = re.split(r'(class="team-name-new"[^>]*>)(.*?)(</div>)', content, flags=re.DOTALL)
        for i, t in enumerate(team):
            lang_data = t.get(lang, {})
            name = lang_data.get('name', '')
            if name and (i*4 + 2) < len(names):
                names[i*4 + 2] = name
        content = "".join(names)

        # Replace roles
        roles = re.split(r'(class="team-role-pill"[^>]*>)(.*?)(</div>)', content, flags=re.DOTALL)
        for i, t in enumerate(team):
            lang_data = t.get(lang, {})
            role = lang_data.get('role', '')
            if role and (i*4 + 2) < len(roles):
                roles[i*4 + 2] = role
                
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("".join(roles))

def sync_pages(data):
    # Left intact from original logic
    pages = data.get('pages', [])
    if not pages: return
    print(f"\n📝 Syncing {len(pages)} pages across all languages...")
    for page in pages:
        page_id = page.get('id')
        sections = page.get('sections', [])
        if not page_id: continue
        filename = f"{page_id}.html"
        for lang, directory in DIRS.items():
            filepath = os.path.join(directory, filename)
            if not os.path.exists(filepath): continue
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            for section in sections:
                if section.get('type') == 'hero':
                    lang_data = section.get('content', {}).get(lang, {})
                    title = lang_data.get('title', '')
                    desc = lang_data.get('desc', '')
                    if title:
                        content = re.sub(r'(<h1[^>]*class="[^"]*hero-title[^"]*"[^>]*>).*?(</h1>)', rf'\g<1>{title}\g<2>', content, flags=re.DOTALL|re.IGNORECASE)
                    if desc:
                        content = re.sub(r'(<p[^>]*class="[^"]*hero-desc[^"]*"[^>]*>).*?(</p>)', rf'\g<1>{desc}\g<2>', content, flags=re.DOTALL|re.IGNORECASE)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)


def sync_diagnostik(data):
    items = data.get('diagnostik', [])
    if not items: return
    print(f"\n⏳ Syncing {len(items)} diagnostik items to diagnostik.html...")
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'diagnostik.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parts = re.split(r'(<h3 class="treatment-title">)(.*?)(</h3>)', content, flags=re.DOTALL)
        for i, tr in enumerate(items):
            title = tr.get(lang, {}).get('title', '')
            if title and (i*4 + 2) < len(parts): parts[i*4 + 2] = title
        content = "".join(parts)
        
        parts = re.split(r'(<p class="treatment-desc">)(.*?)(</p>)', content, flags=re.DOTALL)
        for i, tr in enumerate(items):
            desc = tr.get(lang, {}).get('desc', '')
            if desc and (i*4 + 2) < len(parts): parts[i*4 + 2] = desc
        content = "".join(parts)
        
        parts = re.split(r'(<div class="treatment-full-desc"[^>]*>)(.*?)(</div>)', content, flags=re.DOTALL)
        for i, tr in enumerate(items):
            fd = tr.get(lang, {}).get('full_desc', '')
            if fd and (i*4 + 2) < len(parts): parts[i*4 + 2] = fd
        content = "".join(parts)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)


def sync_faq(data):
    items = data.get('faq', [])
    if not items: return
    print(f"\n⏳ Syncing {len(items)} faq items to patienten.html...")
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'patienten.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parts = re.split(r'(<div class="faq-q"[^>]*>)(.*?)(</div>)', content, flags=re.DOTALL)
        for i, tr in enumerate(items):
            title = tr.get(lang, {}).get('title', '')
            if title and (i*4 + 2) < len(parts):
                # Ensure we don't strip internal HTML unless we are replacing it all. 
                # Since we extract plain text for now, we'll just replace the whole content inside faq-q.
                parts[i*4 + 2] = title
        content = "".join(parts)
        
        parts = re.split(r'(<div class="faq-a"[^>]*>)(.*?)(</div>)', content, flags=re.DOTALL)
        for i, tr in enumerate(items):
            desc = tr.get(lang, {}).get('desc', '')
            if desc and (i*4 + 2) < len(parts): parts[i*4 + 2] = desc
        content = "".join(parts)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)


def sync_reviews(data):
    reviews = data.get('reviews', [])
    print(f"\n⭐ Syncing {len(reviews)} reviews to index.html...")
    
    import os
    pattern = re.compile(r'<!-- REVIEWS_START -->.*?<!-- REVIEWS_END -->', re.DOTALL)
    
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'index.html')
        if not os.path.exists(filepath): continue
        
        # Build HTML for this specific language
        reviews_html = '''      <!-- REVIEWS_START -->
      <div class="testimonials-grid">
'''
        for rev in reviews:
            stars_html = '★' * rev.get('stars', 5)
            
            # Extract text for current language
            text_val = ''
            if isinstance(rev.get('text'), dict):
                text_val = rev['text'].get(lang) or rev['text'].get('de', '')
            else:
                text_val = rev.get('text', '')
                
            author = rev.get('author_name', 'Anonym')
            avatar = author[0].upper() if author else 'A'
            reviews_html += f'''        <div class="testimonial-card fade-in">
          <div class="testimonial-stars">{stars_html}</div>
          <p class="testimonial-text">"{text_val}"</p>
          <div class="testimonial-author">
            <div class="author-avatar">{avatar}</div>
            <div class="author-info">
              <div class="author-name">{author}</div>
            </div>
          </div>
        </div>
'''
        reviews_html += '''      </div>
      <!-- REVIEWS_END -->'''

        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        if pattern.search(html):
            new_html = pattern.sub(reviews_html, html)
            if new_html != html:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                print(f"  ✅ Updated {filepath}")


def main():
    print("=" * 55)
    print("  Neurochirurgie Fischer — CMS Sync Script")
    print("=" * 55)
    
    data = load_cms_data()
    if not data: return
    
    sync_pages(data)
    sync_schwerpunkte(data)
    sync_treatments(data)
    sync_diagnostik(data)
    sync_faq(data)
    sync_reviews(data)
    # sync_team(data) - DISABLED because CMS order differs from HTML order
    print("\n✅ All synchronization tasks completed successfully!")

if __name__ == '__main__':
    main()
