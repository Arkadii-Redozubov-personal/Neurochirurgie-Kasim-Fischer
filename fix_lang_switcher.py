import os, re

html_files = []
for root, dirs, files in os.walk(r'c:\Users\arkad\Downloads\vertex'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'class="lang-switcher hidden-mobile"' in content:
        continue

    rel_path = os.path.relpath(filepath, r'c:\Users\arkad\Downloads\vertex')
    parts = rel_path.split(os.sep)
    basename = parts[-1]
    
    if len(parts) > 1:
        lang_code = parts[0].upper()
        prefix = '../'
    else:
        lang_code = 'DE'
        prefix = ''

    switcher_desktop = f'''          <div class="lang-switcher hidden-mobile">
            <div class="lang-current">{lang_code} <span>▼</span></div>
            <div class="lang-dropdown">
              <a href="{prefix}{basename}">Deutsch (DE)</a>
              <a href="{prefix}en/{basename}">English (EN)</a>
              <a href="{prefix}ru/{basename}">Русский (RU)</a>
              <a href="{prefix}tr/{basename}">Türkçe (TR)</a>
              <a href="{prefix}ar/{basename}">العربية (AR)</a>
            </div>
          </div>'''

    switcher_mobile = f'''        <div class="mobile-lang-switcher">
            <a href="{prefix}{basename}"{' class="active"' if lang_code == 'DE' else ''}>DE</a>
            <a href="{prefix}en/{basename}"{' class="active"' if lang_code == 'EN' else ''}>EN</a>
            <a href="{prefix}ru/{basename}"{' class="active"' if lang_code == 'RU' else ''}>RU</a>
            <a href="{prefix}tr/{basename}"{' class="active"' if lang_code == 'TR' else ''}>TR</a>
            <a href="{prefix}ar/{basename}"{' class="active"' if lang_code == 'AR' else ''}>AR</a>
          </div>'''

    # Insert desktop switcher
    content = re.sub(r'(<a[^>]*class="btn-book hidden-mobile"[^>]*>)', switcher_desktop + r'\n          \1', content, count=1)

    # Insert mobile switcher
    content = re.sub(r'(</a>\s*)(</div>\s*<div class="hero(?:-main)?")', r'\1' + '\n' + switcher_mobile + '\n        ' + r'\2', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done!')
