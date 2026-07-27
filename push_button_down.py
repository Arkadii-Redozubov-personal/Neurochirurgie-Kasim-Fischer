import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add a bottom margin to the description to push the button/date row further down
css_content = css_content.replace('''
.press-card-desc {
  
  color: var(--text-light);''', '''
.press-card-desc {
  margin-bottom: 20px;
  color: var(--text-light);''')

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Added margin-bottom to press-card-desc to push the date/button down")
