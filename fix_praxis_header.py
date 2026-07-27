import os
import re

base_dir = 'c:/Users/arkad/Downloads/vertex'
langs = ['', 'en', 'ru', 'tr', 'ar']

for lang in langs:
    filepath = os.path.join(base_dir, lang, 'praxis-schwerpunkte.html') if lang else os.path.join(base_dir, 'praxis-schwerpunkte.html')
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = r'<div class="mobile-lang-switcher">.*?</div>\s*(</div>\s*<div class="lang-switcher hidden-mobile">)'
    
    content = re.sub(pattern, r'\1', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed header bug on praxis-schwerpunkte.html across all languages")
