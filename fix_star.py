import os
import re

folders = ['.', 'en', 'ru', 'tr', 'ar']
files = ['index.html', 'behandlungen.html', 'praxis-schwerpunkte.html', 'presseschau.html', 'sprechzeiten.html', 'unser-team.html']

for folder in folders:
    if not os.path.exists(folder): continue
    for f in files:
        path = os.path.join(folder, f)
        if not os.path.exists(path): continue
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        # Replace the mangled star in the stats section
        content = re.sub(r'data-suffix="<span([^>]*?)>[^<]*?</span>"', r'data-suffix="<span\1>★</span>"', content)
        content = re.sub(r'0\.0<span([^>]*?)>[^<]*?</span></div>', r'0.0<span\1>★</span></div>', content)
        
        # Fix any other stray 'â...' sequences using latin-1 fallback if they are simple
        # But specifically, looking at the screenshot, the stat is 2.4 â<menu-icon>
        # Just replace the whole corrupted data-suffix content with ★
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

print("Fixed specifically using python file")
