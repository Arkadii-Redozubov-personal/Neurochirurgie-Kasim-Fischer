import os
import json
import re

DIRS = {
    'de': '.',
    'en': 'en',
    'ru': 'ru',
    'tr': 'tr',
    'ar': 'ar'
}

def load_cms_data():
    if not os.path.exists('cms_data.json'):
        print('❌ cms_data.json not found.')
        return None
    with open('cms_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def to_str(val, lang='de'):
    if val is None:
        return ''
    if isinstance(val, str):
        return val.strip()
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, dict):
        if lang in val and isinstance(val[lang], str):
            return val[lang].strip()
        if 'de' in val and isinstance(val['de'], str):
            return val['de'].strip()
        for v in val.values():
            s = to_str(v, lang)
            if s: return s
    return ''

def sync_schwerpunkte(data):
    schwerpunkte = data.get('schwerpunkte', [])
    if not schwerpunkte: return
    schwerpunkte.sort(key=lambda x: x.get('order', 0))
    print(f'Syncing {len(schwerpunkte)} schwerpunkte to praxis-schwerpunkte.html...')
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'praxis-schwerpunkte.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace titles
        titles = re.split(r'(<h3 class="(?:disease|default)-card-title"[^>]*>)(.*?)(</h3>)', content, flags=re.DOTALL)
        for i, sp in enumerate(schwerpunkte):
            title = to_str(sp.get(lang, {}).get('title', '') or sp.get('title', {}).get(lang, '') or sp.get('title', ''), lang)
            idx = i * 4 + 2
            if title and idx < len(titles):
                titles[idx] = title
        content = ''.join(titles)

        # Replace descriptions
        descs = re.split(r'(<p class="(?:disease|default)-card-desc"[^>]*>)(.*?)(</p>)', content, flags=re.DOTALL)
        for i, sp in enumerate(schwerpunkte):
            desc = to_str(sp.get(lang, {}).get('desc', '') or sp.get('desc', {}).get(lang, '') or sp.get('desc', ''), lang)
            idx = i * 4 + 2
            if desc and idx < len(descs):
                descs[idx] = desc
        content = ''.join(descs)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def sync_treatments(data):
    treatments = data.get('treatments', [])
    if not treatments: return
    treatments.sort(key=lambda x: x.get('order', 0))
    print(f'Syncing {len(treatments)} treatments to behandlungen.html...')
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'behandlungen.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        titles = re.split(r'(<h3 class="(?:disease|default)-card-title"[^>]*>)(.*?)(</h3>)', content, flags=re.DOTALL)
        for i, tr in enumerate(treatments):
            title = to_str(tr.get(lang, {}).get('title', '') or tr.get('title', {}).get(lang, '') or tr.get('title', ''), lang)
            idx = i * 4 + 2
            if title and idx < len(titles):
                titles[idx] = title
        content = ''.join(titles)

        descs = re.split(r'(<p class="(?:disease|default)-card-desc"[^>]*>)(.*?)(</p>)', content, flags=re.DOTALL)
        for i, tr in enumerate(treatments):
            desc = to_str(tr.get(lang, {}).get('desc', '') or tr.get('desc', {}).get(lang, '') or tr.get('desc', ''), lang)
            idx = i * 4 + 2
            if desc and idx < len(descs):
                descs[idx] = desc
        content = ''.join(descs)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def sync_team(data):
    team = data.get('team', [])
    if not team: return
    team.sort(key=lambda x: x.get('order', 0))
    print(f'Syncing {len(team)} team members to unser-team.html...')
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'unser-team.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace names
        names = re.split(r'(<div class="team-name-new"[^>]*>)(.*?)(</div>)', content, flags=re.DOTALL)
        for i, t in enumerate(team):
            name = to_str(t.get(lang, {}).get('name', '') or t.get('name', {}).get(lang, '') or t.get('name', ''), lang)
            idx = i * 4 + 2
            if name and idx < len(names):
                inner = names[idx]
                if 'class="doc-name-text"' in inner:
                    names[idx] = re.sub(r'(class="doc-name-text"[^>]*>)(.*?)(</span>)', lambda m, n=name: f'{m.group(1)}{n}{m.group(3)}', inner, flags=re.DOTALL)
                else:
                    names[idx] = name
        content = ''.join(names)

        # Replace roles
        roles = re.split(r'(<div class="team-role-pill"[^>]*>)(.*?)(</div>)', content, flags=re.DOTALL)
        for i, t in enumerate(team):
            role = to_str(t.get(lang, {}).get('role', '') or t.get('role', {}).get(lang, '') or t.get('role', ''), lang)
            idx = i * 4 + 2
            if role and idx < len(roles):
                roles[idx] = role
        content = ''.join(roles)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def sync_diagnostik(data):
    items = data.get('diagnostik', [])
    if not items: return
    items.sort(key=lambda x: x.get('order', 0))
    print(f'Syncing {len(items)} diagnostik items to diagnostik.html...')
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'diagnostik.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parts = re.split(r'(<h3[^>]*class="[^"]*treatment-title[^"]*"[^>]*>|<h3 style="font-size: 1\.15rem[^"]*">)(.*?)(</h3>)', content, flags=re.DOTALL)
        for i, tr in enumerate(items):
            title = to_str(tr.get(lang, {}).get('title', '') or tr.get('title', {}).get(lang, '') or tr.get('title', ''), lang)
            idx = i * 4 + 2
            if title and idx < len(parts): parts[idx] = title
        content = ''.join(parts)
        
        parts = re.split(r'(<p[^>]*class="[^"]*treatment-desc[^"]*"[^>]*>|<p style="font-size: 0\.95rem[^"]*">)(.*?)(</p>)', content, flags=re.DOTALL)
        for i, tr in enumerate(items):
            desc = to_str(tr.get(lang, {}).get('desc', '') or tr.get('desc', {}).get(lang, '') or tr.get('desc', ''), lang)
            idx = i * 4 + 2
            if desc and idx < len(parts): parts[idx] = desc
        content = ''.join(parts)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def sync_faq(data):
    items = data.get('faq', [])
    if not items: return
    items.sort(key=lambda x: x.get('order', 0))
    print(f'Syncing {len(items)} faq items to patienten.html...')
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'patienten.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parts = re.split(r'(<div class="faq-q"[^>]*>)(.*?)(</div>)', content, flags=re.DOTALL)
        for i, tr in enumerate(items):
            title = to_str(tr.get(lang, {}).get('title', '') or tr.get('title', {}).get(lang, '') or tr.get('title', ''), lang)
            idx = i * 4 + 2
            if title and idx < len(parts):
                parts[idx] = title
        content = ''.join(parts)
        
        parts = re.split(r'(<div class="faq-a"[^>]*>)(.*?)(</div>)', content, flags=re.DOTALL)
        for i, tr in enumerate(items):
            desc = to_str(tr.get(lang, {}).get('desc', '') or tr.get('desc', {}).get(lang, '') or tr.get('desc', ''), lang)
            idx = i * 4 + 2
            if desc and idx < len(parts): parts[idx] = desc
        content = ''.join(parts)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def sync_reviews(data):
    reviews = data.get('reviews', [])
    if not reviews: return
    reviews.sort(key=lambda x: x.get('order', 0))
    print(f'Syncing {len(reviews)} reviews to index.html...')
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'index.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        authors = re.split(r'(<div class="author-name-text"[^>]*>)(.*?)(</div>)', content, flags=re.DOTALL)
        for i, rev in enumerate(reviews):
            name = to_str(rev.get('author_name', ''), lang)
            idx = i * 4 + 2
            if name and idx < len(authors):
                authors[idx] = name
        content = ''.join(authors)

        texts = re.split(r'(<div class="testimonial-text-content"[^>]*>)(.*?)(</div>)', content, flags=re.DOTALL)
        for i, rev in enumerate(reviews):
            txt = ''
            if isinstance(rev.get('text'), dict):
                txt = rev['text'].get(lang) or rev['text'].get('de', '')
            elif isinstance(rev.get(lang), dict):
                txt = rev[lang].get('text', '')
            else:
                txt = rev.get('text', '')
            txt = to_str(txt, lang)
                
            idx = i * 4 + 2
            if txt and idx < len(texts):
                paragraphs = [p.strip() for p in txt.split(chr(10) + chr(10)) if p.strip()]
                if not paragraphs:
                    paragraphs = [p.strip() for p in txt.split(chr(10)) if p.strip()]
                if paragraphs:
                    formatted_p = ''.join([f'<p>{p}</p>' for p in paragraphs])
                else:
                    formatted_p = f'<p>{txt}</p>'
                texts[idx] = chr(10) + '            ' + formatted_p + chr(10) + '          '
        content = ''.join(texts)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def sync_branches(data):
    branches = data.get('branches', [])
    if not branches: return
    branches.sort(key=lambda x: x.get('order', 0))
    print(f'Syncing {len(branches)} branches to sprechzeiten.html...')
    for lang, directory in DIRS.items():
        filepath = os.path.join(directory, 'sprechzeiten.html')
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        cards = re.split(r'(<div class="branch-card">)', content)
        for i, b in enumerate(branches):
            chunk_idx = i * 2 + 2
            if chunk_idx >= len(cards): break
            chunk = cards[chunk_idx]

            city = to_str(b.get(lang, {}).get('city', '') or b.get('city', ''), lang)
            if city:
                chunk = re.sub(r'(<h2 class="branch-title"[^>]*>)(.*?)(</h2>)', lambda m, c=city: f'{m.group(1)}{c}{m.group(3)}', chunk, flags=re.DOTALL)

            addr = to_str(b.get(lang, {}).get('address', '') or b.get('address', ''), lang)
            if addr:
                chunk = re.sub(r'(class="branch-address-link"[^>]*>)(.*?)(</a>)', lambda m, a=addr: f'{m.group(1)}{a}{m.group(3)}', chunk, flags=re.DOTALL)

            cards[chunk_idx] = chunk

        content = ''.join(cards)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    print('=' * 55)
    print('  Neurochirurgie Fischer — CMS Sync Script')
    print('=' * 55)
    
    data = load_cms_data()
    if not data: return
    
    sync_schwerpunkte(data) 
    sync_treatments(data)
    sync_team(data)
    sync_diagnostik(data)
    sync_faq(data)
    sync_reviews(data)
    sync_branches(data)
    print('All synchronization tasks completed successfully!')

if __name__ == '__main__':
    main()
