import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add padding to the text container so it doesn't overlap the absolute close button
css_content = css_content.replace('''
.fd-text {
  display: flex;
  flex-direction: column;
  gap: 4px;
}''', '''
.fd-text {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding-right: 36px;
}
[dir="rtl"] .fd-text {
  padding-right: 0;
  padding-left: 36px;
}''')

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Added right padding to the Doctolib widget text to prevent close button overlap")
