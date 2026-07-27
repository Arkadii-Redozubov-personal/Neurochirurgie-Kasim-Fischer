import re

with open('c:/Users/arkad/Downloads/vertex/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace padding: 32px max(40px, calc(50% - 800px)); with 50vw - 680px
css = re.sub(
    r'padding:\s*32px\s*max\(\s*40px\s*,\s*calc\(50%\s*-\s*800px\)\s*\);',
    'padding: 32px max(40px, calc(50vw - 680px));',
    css
)

css = re.sub(
    r'padding:\s*16px\s*max\(\s*40px\s*,\s*calc\(50%\s*-\s*800px\)\s*\);',
    'padding: 16px max(40px, calc(50vw - 680px));',
    css
)

with open('c:/Users/arkad/Downloads/vertex/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated style.css")
