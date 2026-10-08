import os
import json
import re

DIRS = {
    'de': '.',
    'en': 'en',
    'ru': 'ru',
    'tr': 'tr',
    'ar': 'ar',
    'uz': 'uz'
}

SP_MODAL_MAP = {
    'sp_1': 'bsv',
    'sp_2': 'spinal',
    'sp_3': 'facetten',
    'sp_4': 'hws',
    'sp_5': 'isg',
    'sp_6': 'wkf',
    'sp_7': 'kts',
    'sp_8': 'sulcus',
    'sp_9': 'nervkomp',
    'sp_10': 'tarsal',
    'sp_13': 'chron',
    'sp_14': 'neuro',
    'sp_15': 'neuropath-post',
    'sp_16': 'psycho-schmerz',
    'sp_17': 'schmerztherapie'
}

TREAT_MODAL_MAP = {
    'treatment_1': 'bandscheibe',
    'treatment_2': 'dekompression',
    'treatment_3': 'kyphoplastie',
    'treatment_4': 'nervenop',
    'treatment_5': 'neuromod',
    'treatment_6': 'hwsop'
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

def get_field(item, field, lang):
    val = item.get(lang, {}).get(field) if isinstance(item.get(lang), dict) else None
    if val:
        return to_str(val, lang)
    val = item.get(field)
    if isinstance(val, dict):
        return to_str(val.get(lang) or val.get('de') or val, lang)
    if isinstance(val, str) and val.strip():
        return val.strip()
    return ''

def format_steps_html(steps_text):
    step_items = [s.strip() for s in steps_text.split('\n\n') if s.strip()]
    if not step_items:
        step_items = [s.strip() for s in steps_text.split('\n') if s.strip()]
    parts = []
    for idx, item in enumerate(step_items):
        clean = re.sub(r'^\d+\.\s*', '', item).strip()
        if ':' in clean:
            t_part, d_part = clean.split(':', 1)
            parts.append(f'<div class="modal-step"><div class="modal-step-num">{idx+1}</div><div class="modal-step-text"><strong>{t_part.strip()}</strong><p>{d_part.strip()}</p></div></div>')
        else:
            parts.append(f'<div class="modal-step"><div class="modal-step-num">{idx+1}</div><div class="modal-step-text"><p>{clean}</p></div></div>')
    return '\n'.join(parts)

def format_markdown_inlines(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text

def update_modal_chunk(chunk, subtitle=None, content=None, steps=None):
    panel_start_m = re.search(r'<div class=["\']modal-content-panel["\']>', chunk)
    if not panel_start_m:
        return chunk
    panel_start_idx = panel_start_m.end()

    all_closing = list(re.finditer(r'</div>\s*</div>\s*</div>', chunk))
    if not all_closing:
        return chunk
    last_closing = all_closing[-1]
    panel_end_idx = last_closing.start()

    panel_body = chunk[panel_start_idx:panel_end_idx]

    # 1. Subtitle
    if subtitle:
        panel_body = re.sub(
            r'(<p class=["\']modal-subtitle["\'][^>]*>)(.*?)(</p>)',
            lambda m: f'{m.group(1)}{subtitle}{m.group(3)}',
            panel_body,
            flags=re.DOTALL
        )

    header_m = re.search(r'<div class=["\']modal-content-header["\']>.*?</div>', panel_body, flags=re.DOTALL)
    if not header_m:
        return chunk[:panel_start_idx] + panel_body + chunk[panel_end_idx:]
    header_end = header_m.end()

    # Trailer detection
    candidates = []
    m_step_h = re.search(r'<div[^>]*>\s*<h3 class=["\']modal-section-h["\']>[^<]+</h3>\s*<div class=["\']modal-steps["\']', panel_body[header_end:])
    if m_step_h:
        candidates.append(('step_with_h', header_end + m_step_h.start()))
    else:
        m_step = re.search(r'<div class=["\']modal-steps["\']', panel_body[header_end:])
        if m_step:
            candidates.append(('step_no_h', header_end + m_step.start()))

    m_alert = re.search(r'<div class=["\']modal-alert["\']', panel_body[header_end:])
    if m_alert:
        candidates.append(('alert', header_end + m_alert.start()))

    m_action = re.search(r'<div class=["\']modal-action-row["\']', panel_body[header_end:])
    if m_action:
        candidates.append(('action', header_end + m_action.start()))

    trailer_type = 'end_of_panel'
    trailer_pos = len(panel_body)
    if candidates:
        candidates.sort(key=lambda x: x[1])
        trailer_type, trailer_pos = candidates[0]

    trailer = panel_body[trailer_pos:]

    # 2. Steps in trailer
    if steps and steps.strip() and 'modal-steps' in trailer:
        pos = trailer.find('modal-steps')
        start_div = trailer.rfind('<div', 0, pos)
        if start_div != -1:
            depth = 0
            end_div = -1
            for m in re.finditer(r'</?div', trailer[start_div:]):
                tag = m.group(0)
                if tag == '<div':
                    depth += 1
                elif tag == '</div':
                    depth -= 1
                    if depth == 0:
                        end_div = start_div + m.end() + 1
                        break
            if end_div != -1:
                new_steps_html = format_steps_html(steps)
                trailer = trailer[:start_div] + f'<div class="modal-steps">\n{new_steps_html}\n</div>' + trailer[end_div:]

    # 3. Content sections
    if content and content.strip():
        clean_content = re.sub(r'<\s*div[^>]*\s*$', '', content.strip(), flags=re.I).strip()
        raw_secs = [s.strip() for s in re.split(r'\n(?=###\s+)', clean_content) if s.strip()]

        sections_html = []
        for idx, sec in enumerate(raw_secs):
            if sec.startswith('###'):
                parts = sec.split('\n', 1)
                heading = re.sub(r'^###\s*', '', parts[0]).strip()
                body = parts[1] if len(parts) > 1 else ''
            else:
                heading = ''
                body = sec

            paragraphs = [format_markdown_inlines(p.strip()) for p in body.split('\n\n') if p.strip()]
            if not paragraphs and body.strip():
                paragraphs = [format_markdown_inlines(body.strip())]

            if idx == len(raw_secs) - 1 and len(paragraphs) == 0 and trailer_type == 'step_with_h' and heading:
                trailer = re.sub(
                    r'(<div[^>]*>\s*<h3 class=["\']modal-section-h["\']>)[^<]+(</h3>\s*<div class=["\']modal-steps["\'])',
                    lambda m: f'{m.group(1)}{heading}{m.group(2)}',
                    trailer,
                    count=1
                )
            else:
                p_html = ''.join([f'\n<p class="modal-section-p">{p}</p>' for p in paragraphs])
                if heading:
                    sections_html.append(f'<div><h3 class="modal-section-h">{heading}</h3>{p_html}\n</div>')
                else:
                    sections_html.append(f'<div>{p_html}\n</div>')

        new_sections_str = '\n' + '\n'.join(sections_html) + '\n'
        panel_body = panel_body[:header_end] + new_sections_str + trailer
    elif steps and steps.strip():
        panel_body = panel_body[:trailer_pos] + trailer

    return chunk[:panel_start_idx] + panel_body + chunk[panel_end_idx:]

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
        
        # Replace card titles
        titles = re.split(r'(<h3 class="(?:disease|default)-card-title"[^>]*>)(.*?)(</h3>)', content, flags=re.DOTALL)
        for i, sp in enumerate(schwerpunkte):
            title = get_field(sp, 'title', lang)
            idx = i * 4 + 2
            if title and idx < len(titles):
                titles[idx] = title
        content = ''.join(titles)

        # Replace card descriptions
        descs = re.split(r'(<p class="(?:disease|default)-card-desc"[^>]*>)(.*?)(</p>)', content, flags=re.DOTALL)
        for i, sp in enumerate(schwerpunkte):
            desc = get_field(sp, 'desc', lang)
            idx = i * 4 + 2
            if desc and idx < len(descs):
                descs[idx] = desc
        content = ''.join(descs)

        # Sync modal contents
        for sp in schwerpunkte:
            mid = sp.get('modalId') or SP_MODAL_MAP.get(sp.get('id'))
            if not mid: continue
            m_sub = get_field(sp, 'modalSubtitle', lang)
            m_content = get_field(sp, 'modalContent', lang)
            m_steps = get_field(sp, 'modalSteps', lang)
            if not m_sub and not m_content and not m_steps:
                continue

            pattern = rf'(<div\s+id=["\']modal-overlay-{re.escape(mid)}["\'].*?)(?=(?:<div\s+id=["\']modal-overlay-|\Z))'
            m = re.search(pattern, content, flags=re.DOTALL)
            if m:
                old_chunk = m.group(1)
                new_chunk = update_modal_chunk(old_chunk, subtitle=m_sub, content=m_content, steps=m_steps)
                content = content[:m.start(1)] + new_chunk + content[m.end(1):]

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
        
        # Replace card titles
        titles = re.split(r'(<h3 class="(?:disease|default)-card-title"[^>]*>)(.*?)(</h3>)', content, flags=re.DOTALL)
        for i, tr in enumerate(treatments):
            title = get_field(tr, 'title', lang)
            idx = i * 4 + 2
            if title and idx < len(titles):
                titles[idx] = title
        content = ''.join(titles)

        # Replace card descriptions
        descs = re.split(r'(<p class="(?:disease|default)-card-desc"[^>]*>)(.*?)(</p>)', content, flags=re.DOTALL)
        for i, tr in enumerate(treatments):
            desc = get_field(tr, 'desc', lang)
            idx = i * 4 + 2
            if desc and idx < len(descs):
                descs[idx] = desc
        content = ''.join(descs)

        # Sync modal contents
        for tr in treatments:
            mid = tr.get('modalId') or TREAT_MODAL_MAP.get(tr.get('id'))
            if not mid: continue
            m_sub = get_field(tr, 'modalSubtitle', lang)
            m_content = get_field(tr, 'fullDesc', lang) or get_field(tr, 'modalContent', lang)
            m_steps = get_field(tr, 'modalSteps', lang)
            if not m_sub and not m_content and not m_steps:
                continue

            pattern = rf'(<div\s+id=["\']modal-overlay-{re.escape(mid)}["\'].*?)(?=(?:<div\s+id=["\']modal-overlay-|\Z))'
            m = re.search(pattern, content, flags=re.DOTALL)
            if m:
                old_chunk = m.group(1)
                new_chunk = update_modal_chunk(old_chunk, subtitle=m_sub, content=m_content, steps=m_steps)
                content = content[:m.start(1)] + new_chunk + content[m.end(1):]

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
                paragraphs = [p.strip() for p in txt.split('\n\n') if p.strip()]
                if not paragraphs:
                    paragraphs = [p.strip() for p in txt.split('\n') if p.strip()]
                if paragraphs:
                    formatted_p = ''.join([f'<p>{p}</p>' for p in paragraphs])
                else:
                    formatted_p = f'<p>{txt}</p>'
                texts[idx] = '\n            ' + formatted_p + '\n          '
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
