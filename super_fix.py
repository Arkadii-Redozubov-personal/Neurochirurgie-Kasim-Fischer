import os
import re

folders = ['.', 'en', 'ru', 'tr', 'ar']
files = ['index.html', 'behandlungen.html', 'praxis-schwerpunkte.html', 'presseschau.html', 'sprechzeiten.html', 'unser-team.html']

def fix_corrupted_chars(text):
    # Fix common mojibake from UTF-8 interpreted as Latin-1
    replacements = {
        'Ã¼': 'ü', 'Ã¤': 'ä', 'ÃŸ': 'ß', 'Ã–': 'Ö', 'Ã„': 'Ä', 'Ãœ': 'Ü',
        'Ðóññêèé': 'Русский', 'Turkce': 'Türkçe', '???????': 'العربية',
        '<span>¡</span>': '<span>▼</span>', 'â˜°': '☰', 'âœ•': '✕',
        'WirbelsĂ¤': 'Wirbelsä', 'WirbelsÄ': 'Wirbelsä',
        'groÃŸer': 'großer', 'fÃ¼hrenden': 'führenden'
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text

for folder in folders:
    if folder != '.' and not os.path.exists(folder):
        continue
    
    lang = 'de' if folder == '.' else folder
    current_label = lang.upper() + ' <span>▼</span>'
    
    for f in files:
        filepath = os.path.join(folder, f)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            
        content = fix_corrupted_chars(content)
        
        # Strip OUT all existing language switchers to start fresh
        content = re.sub(r'<div class="lang-switcher hidden-mobile">.*?</div>\s*</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div class="mobile-lang-switcher">.*?</div>', '', content, flags=re.DOTALL)
        
        # Build the correct paths
        prefix = '' if folder == '.' else '../'
        
        # Build Desktop Switcher
        desktop_html = f'''<div class="lang-switcher hidden-mobile">
            <div class="lang-current">{current_label}</div>
            <div class="lang-dropdown">
              <a href="{prefix}{f}">Deutsch (DE)</a>
              <a href="{prefix}en/{f}">English (EN)</a>
              <a href="{prefix}ru/{f}">Русский (RU)</a>
              <a href="{prefix}tr/{f}">Türkçe (TR)</a>
              <a href="{prefix}ar/{f}">العربية (AR)</a>
            </div>
          </div>'''
          
        # Build Mobile Switcher
        def act(l): return 'class="active"' if l == lang else ''
        mobile_html = f'''<div class="mobile-lang-switcher">
            <a href="{prefix}{f}" {act('de')}>DE</a>
            <a href="{prefix}en/{f}" {act('en')}>EN</a>
            <a href="{prefix}ru/{f}" {act('ru')}>RU</a>
            <a href="{prefix}tr/{f}" {act('tr')}>TR</a>
            <a href="{prefix}ar/{f}" {act('ar')}>AR</a>
          </div>'''
          
        # Inject Desktop Switcher exactly before Termin vereinbaren
        content = content.replace('<a href="sprechzeiten.html" class="btn-book hidden-mobile">', desktop_html + '\n          <a href="sprechzeiten.html" class="btn-book hidden-mobile">')
        content = content.replace('<a href="../sprechzeiten.html" class="btn-book hidden-mobile">', desktop_html + '\n          <a href="../sprechzeiten.html" class="btn-book hidden-mobile">')
        
        # Inject Mobile Switcher exactly after Kontakt inside mobile-menu
        # Find mobile menu block
        mobile_menu_match = re.search(r'(<div class="mobile-menu".*?>)(.*?)(</div>)', content, re.DOTALL)
        if mobile_menu_match:
            # We want to put it inside the mobile menu at the very end
            mobile_inner = mobile_menu_match.group(2)
            content = content.replace(mobile_menu_match.group(0), mobile_menu_match.group(1) + mobile_inner + mobile_html + '\n        ' + mobile_menu_match.group(3))
            
        # Fix burger menu visual bugs
        content = re.sub(r'id="burgerMenu"(.*?)>.*?</div>', r'id="burgerMenu"\1>☰</div>', content)
        content = content.replace("burgerMenu.textContent = 'â˜°';", "burgerMenu.textContent = '☰';")
        content = content.replace("burgerMenu.textContent = 'âœ•';", "burgerMenu.textContent = '✕';")
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)

print("All files cleaned and fixed globally!")
