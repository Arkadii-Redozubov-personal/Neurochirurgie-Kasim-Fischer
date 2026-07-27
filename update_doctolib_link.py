import os

base_dir = 'c:/Users/arkad/Downloads/vertex'
langs = ['', 'en', 'ru', 'tr', 'ar']
files = ['index.html', 'praxis-schwerpunkte.html', 'behandlungen.html', 'unser-team.html', 'presseschau.html', 'sprechzeiten.html']

doctolib_url = "https://www.doctolib.de/neurochirurgie/moenchengladbach/kasim-fischer?utm_campaign=website-button&utm_source=kasim-fischer-website-button&utm_medium=referral&utm_content=custom&utm_term=kasim-fischer"

for lang in langs:
    for filename in files:
        filepath = os.path.join(base_dir, lang, filename) if lang else os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace variations of the Doctolib URL
        content = content.replace('href="https://www.doctolib.de/"', f'href="{doctolib_url}"')
        content = content.replace('href="https://www.doctolib.de"', f'href="{doctolib_url}"')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated Doctolib links in all HTML files.")
