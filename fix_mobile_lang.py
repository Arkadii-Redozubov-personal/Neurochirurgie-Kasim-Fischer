import os
import re

def fix_mobile_menu(filepath, filename):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<div class="mobile-lang-switcher">' not in content:
        # We need to insert it right before the closing </div> of <div class="mobile-menu"...>
        # Let's find <div class="mobile-menu"
        if '<div class="mobile-menu"' in content:
            # The mobile menu usually ends with:
            #           <a href="sprechzeiten.html" style="color: var(--primary);">Termin vereinbaren</a>
            #         </div>
            # OR something similar in other languages.
            
            # Determine path prefix (for languages)
            prefix = ''
            if '/ru/' in filepath.replace('\\', '/') or '/en/' in filepath.replace('\\', '/') or '/tr/' in filepath.replace('\\', '/') or '/ar/' in filepath.replace('\\', '/'):
                prefix = '../'
            
            # Determine active class for each language
            active_de = ' class="active"' if prefix == '' else ''
            active_en = ' class="active"' if '/en/' in filepath.replace('\\', '/') else ''
            active_ru = ' class="active"' if '/ru/' in filepath.replace('\\', '/') else ''
            active_tr = ' class="active"' if '/tr/' in filepath.replace('\\', '/') else ''
            active_ar = ' class="active"' if '/ar/' in filepath.replace('\\', '/') else ''
            
            switcher_html = f'''
        <div class="mobile-lang-switcher">
            <a href="{prefix}{filename}"{active_de}>DE</a>
            <a href="{prefix}en/{filename}"{active_en}>EN</a>
            <a href="{prefix}ru/{filename}"{active_ru}>RU</a>
            <a href="{prefix}tr/{filename}"{active_tr}>TR</a>
            <a href="{prefix}ar/{filename}"{active_ar}>AR</a>
          </div>
        </div>'''
            
            # Find the closing </div> of the mobile-menu
            # We can just replace the last link + </div>
            content = re.sub(r'(<a href="[^"]*sprechzeiten\.html"[^>]*>.*?</a>\s*)</div>', r'\1' + switcher_html, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {filepath}")
        else:
            print(f"Could not find mobile-menu in {filepath}")
    else:
        print(f"Already fixed {filepath}")

base_dir = 'c:/Users/arkad/Downloads/vertex'
files_to_check = ['praxis-schwerpunkte.html', 'behandlungen.html', 'unser-team.html', 'presseschau.html', 'sprechzeiten.html', 'index.html']
langs = ['', 'ru', 'en', 'ar', 'tr']

for f in files_to_check:
    for lang in langs:
        path = os.path.join(base_dir, lang, f) if lang else os.path.join(base_dir, f)
        fix_mobile_menu(path, f)

print("Done checking all files.")
