import os
import re

svg_icon = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'<a href="([^"]+)" download class="btn-book" style="padding: 8px 16px; font-size: 0\.85rem; border-radius: 99px;" onclick="event\.stopPropagation\(\)">([^<]+)</a>'

    def replacer(match):
        pdf_url = match.group(1)
        text = match.group(2)
        pdf_name = pdf_url.split('/')[-1]
        
        onclick_js = f"event.stopPropagation(); event.preventDefault(); fetch('{pdf_url}').then(r=>r.blob()).then(b=>{{let a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='{pdf_name}';a.click()}})"
        
        return f'<a href="{pdf_url}" download="{pdf_name}" class="btn-book btn-download" style="padding: 8px 16px; font-size: 0.85rem; border-radius: 99px;" onclick="{onclick_js}">{svg_icon}<span>{text}</span></a>'

    new_content = re.sub(pattern, replacer, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

root_dir = 'c:/Users/arkad/Downloads/vertex'
process_file(f"{root_dir}/presseschau.html")
for lang in ['en', 'ru', 'tr', 'ar']:
    path = f"{root_dir}/{lang}/presseschau.html"
    if os.path.exists(path):
        process_file(path)
