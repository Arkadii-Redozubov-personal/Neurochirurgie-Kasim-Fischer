import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace all occurrences of 1350px with 1550px to trigger burger menu earlier
css_content = css_content.replace('(max-width: 1350px)', '(max-width: 1550px)')

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated style.css: Burger menu now triggers at 1550px")
