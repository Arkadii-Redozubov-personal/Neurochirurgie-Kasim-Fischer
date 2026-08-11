import os, json, re

langs = ['de', 'en', 'ru', 'tr', 'ar']
pages = ['index.html', 'behandlungen.html', 'praxis-schwerpunkte.html', 'presseschau.html', 'sprechzeiten.html', 'unser-team.html']

def extract_content(html):
    title_match = re.search(r'<h1[^>]*class="[^"]*hero-title[^"]*"[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
    desc_match = re.search(r'<p[^>]*class="[^"]*hero-desc[^"]*"[^>]*>(.*?)</p>', html, re.DOTALL | re.IGNORECASE)
    
    return {
        "title": title_match.group(1).strip() if title_match else "",
        "desc": desc_match.group(1).strip() if desc_match else ""
    }

page_data = {}

for page in pages:
    page_id = page.replace('.html', '')
    page_data[page_id] = {
        "id": page_id,
        "name": page_id.capitalize(),
        "sections": [
            {
                "id": "hero",
                "type": "hero",
                "content": {}
            }
        ]
    }
    
    for lang in langs:
        dir_path = '.' if lang == 'de' else lang
        filepath = os.path.join(dir_path, page)
        
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()
            extracted = extract_content(html)
            page_data[page_id]["sections"][0]["content"][lang] = extracted

with open("pages_seed.json", "w", encoding='utf-8') as f:
    json.dump(page_data, f, ensure_ascii=False, indent=2)

print("✅ Extracted page data to pages_seed.json")
