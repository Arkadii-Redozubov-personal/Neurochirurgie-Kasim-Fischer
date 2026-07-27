import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add gap to navbar
if 'gap: 20px;' not in css.split('.navbar {')[1].split('}')[0]:
    css = css.replace('.navbar {\n      display: flex;', '.navbar {\n      display: flex;\n      gap: 20px;')

# Add flex-shrink: 0 and white-space: nowrap to logo
if 'white-space: nowrap;' not in css.split('.logo {')[1].split('}')[0]:
    css = css.replace('.logo {\n      font-weight: 800;', '.logo {\n      font-weight: 800;\n      flex-shrink: 0;\n      white-space: nowrap;')

# Add white-space: nowrap to btn-book
if 'white-space: nowrap;' not in css.split('.btn-book {')[1].split('}')[0]:
    css = css.replace('.btn-book {\n      background: var(--primary);', '.btn-book {\n      background: var(--primary);\n      flex-shrink: 0;\n      white-space: nowrap;')

# Add white-space: nowrap to lang-switcher
if 'white-space: nowrap;' not in css.split('.lang-switcher {')[1].split('}')[0]:
    css = css.replace('.lang-switcher {\n      position: relative;', '.lang-switcher {\n      position: relative;\n      flex-shrink: 0;\n      white-space: nowrap;')

# Add dynamic gap to nav-links and media queries
if '@media (max-width: 1350px)' not in css:
    css += '''
@media (max-width: 1350px) {
  .nav-links { gap: 20px; font-size: 0.85rem; }
}
@media (max-width: 1250px) {
  .nav-links { gap: 12px; font-size: 0.8rem; }
  .logo { font-size: 1.1rem; }
}
'''

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css patched!")
