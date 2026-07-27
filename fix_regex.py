import re
import os

langs = ['en', 'ru', 'tr', 'ar']
files = ['index.html', 'behandlungen.html', 'praxis-schwerpunkte.html', 'presseschau.html', 'sprechzeiten.html', 'unser-team.html']

for lang in langs:
    if not os.path.exists(lang): continue
    for f in files:
        path = os.path.join(lang, f)
        if not os.path.exists(path): continue
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        content = re.sub(r'<div class="stars">.*?</div>', r'<div class="stars">★★★★★</div>', content)
        content = re.sub(r'<span class="stars">.*?</span>', r'<span class="stars">★★★★★</span>', content)
        content = re.sub(r'<span class="faq-icon">.*?</span>', r'<span class="faq-icon">▼</span>', content)
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

print("Regex fixes applied to translated files!")
