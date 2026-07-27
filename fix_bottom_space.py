import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace padding-bottom in hero-inner-sub
css_content = css_content.replace('padding: 120px 0 80px 0 !important;', 'padding: 120px 0 0 0 !important;')
css_content = css_content.replace('.hero-inner-sub { padding-bottom: 40px !important; }', '.hero-inner-sub { padding-bottom: 0 !important; }')

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated style.css to remove extra bottom space in hero-inner-sub")
