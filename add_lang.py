import os, re

files = ['index.html', 'behandlungen.html', 'praxis-schwerpunkte.html', 'presseschau.html', 'sprechzeiten.html', 'unser-team.html']

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        with open(f, 'r', encoding='latin-1') as file:
            content = file.read()
    
    html = f'''
          <div class="lang-switcher hidden-mobile">
            <div class="lang-current">DE <span>▼</span></div>
            <div class="lang-dropdown">
              <a href="{f}">Deutsch (DE)</a>
              <a href="en/{f}">English (EN)</a>
              <a href="ru/{f}">Русский (RU)</a>
              <a href="tr/{f}">Türkçe (TR)</a>
              <a href="ar/{f}">العربية (AR)</a>
            </div>
          </div>
'''
    mobile_html = f'''
          <div class="mobile-lang-switcher">
            <a href="{f}" class="active">DE</a>
            <a href="en/{f}">EN</a>
            <a href="ru/{f}">RU</a>
            <a href="tr/{f}">TR</a>
            <a href="ar/{f}">AR</a>
          </div>
'''

    content = content.replace('<a href="sprechzeiten.html" class="btn-book hidden-mobile">Termin vereinbaren</a>', html + '          <a href="sprechzeiten.html" class="btn-book hidden-mobile">Termin vereinbaren</a>')
    content = re.sub(r'(<a href="sprechzeiten.html">Kontakt</a>\s*</div>)', r'\1\n' + mobile_html, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Language switchers added successfully.")
