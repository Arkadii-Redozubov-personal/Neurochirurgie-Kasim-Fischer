import re
import os

svg_phone = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px; vertical-align: middle; margin-top: -2px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'

folders = ['.', 'en', 'ru', 'tr', 'ar']
files = ['index.html', 'behandlungen.html', 'praxis-schwerpunkte.html', 'presseschau.html', 'sprechzeiten.html', 'unser-team.html']

for folder in folders:
    if not os.path.exists(folder): continue
    for f in files:
        path = os.path.join(folder, f)
        if not os.path.exists(path): continue
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Replace broken phone emoji in btn-outline-white with SVG
        # We look for <a href="tel:021616782683" class="btn-outline-white"> followed by any garbage until (02161)
        content = re.sub(r'(<a href="tel:021616782683" class="btn-outline-white">).*?(\(02161\))', r'\1' + svg_phone + r'\2', content)
        
        # In index.html cta-benefits, replace broken checkmarks with ✓
        # Look for <span> followed by non-word chars until a letter
        if f == 'index.html':
            # This is a bit tricky for non-english, let's just replace all <span> content starting with non-letters in cta-benefits
            # To be safe, let's just replace specifically the ones that start with â or ð or ? 
            # Or just replace the first character inside <span> if it's not a letter/number
            content = re.sub(r'(<div class="cta-benefits">\s*<span>)[^a-zA-ZА-Яа-я0-9<]+', r'\1✓ ', content)
            content = re.sub(r'(</span>\s*<span>)[^a-zA-ZА-Яа-я0-9<]+', r'\1✓ ', content)
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

print("Phone SVG and checkmarks fixed!")
