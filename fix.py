import os
f = 'presseschau.html'
with open(f, 'r', encoding='utf-8') as file:
    content = file.read()

replacements = {
    'Ã¼': 'ü', 'Ã¤': 'ä', 'ÃŸ': 'ß', 'Ã–': 'Ö', 'Ã„': 'Ä', 'Ãœ': 'Ü',
    'Ðóññêèé': 'Русский', 'Turkce': 'Türkçe', '???????': 'العربية',
    '<span>¡</span>': '<span>▼</span>', 'â˜°': '☰', 'âœ•': '✕'
}

for bad, good in replacements.items():
    content = content.replace(bad, good)

import re
content = re.sub(r'<div class="lang-switcher hidden-mobile">\s*<div class="lang-current">DE <span>▼</span></div>\s*<div class="lang-dropdown">\s*<a href="presseschau.html">Deutsch \(DE\)</a>\s*<a href="en/presseschau.html">English \(EN\)</a>\s*<a href="ru/presseschau.html">Русский \(RU\)</a>\s*<a href="tr/presseschau.html">Türkçe \(TR\)</a>\s*<a href="ar/presseschau.html">العربية \(AR\)</a>\s*</div>\s*</div>', '', content, count=1)

with open(f, 'w', encoding='utf-8') as file:
    file.write(content)
print("Fixed presseschau")
