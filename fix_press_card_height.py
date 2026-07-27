import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Change height: 160px to min-height: 160px for press cards
css_content = css_content.replace('''
.press-card-horizontal {
  background: white;
  border: 1px solid #f1f5f9;
  border-radius: var(--radius-md);
  box-shadow: 0 4px 20px rgba(0,0,0,0.03);
  display: flex;
  align-items: stretch;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  transition: transform 0.3s, box-shadow 0.3s;
  height: 160px;
}''', '''
.press-card-horizontal {
  background: white;
  border: 1px solid #f1f5f9;
  border-radius: var(--radius-md);
  box-shadow: 0 4px 20px rgba(0,0,0,0.03);
  display: flex;
  align-items: stretch;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  transition: transform 0.3s, box-shadow 0.3s;
  min-height: 160px;
  height: 100%;
}''')

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Fixed press-card-horizontal height issue")
