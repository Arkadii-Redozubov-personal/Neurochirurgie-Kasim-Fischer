import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Increase size and margins of close button on desktop
css_content = css_content.replace('''
.fd-close {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 24px;
  height: 24px;''', '''
.fd-close {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 32px;
  height: 32px;''')

# Fix RTL offset to match the new right offset
css_content = css_content.replace('''[dir="rtl"] .fd-close {
  right: auto;
  left: 10px;
}''', '''[dir="rtl"] .fd-close {
  right: auto;
  left: 14px;
}''')

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Added more padding/margins to the close button")
