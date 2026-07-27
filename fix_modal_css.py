import os

# Fix style.css
css_path = 'c:/Users/arkad/Downloads/vertex/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('aspect-ratio: 16/9;', '/* aspect-ratio: 16/9; removed for text modal */')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Fix video URL in behandlungen.html
base_dir = 'c:/Users/arkad/Downloads/vertex'
langs = ['', 'en', 'ru', 'tr', 'ar']

for lang in langs:
    filepath = os.path.join(base_dir, lang, 'behandlungen.html') if lang else os.path.join(base_dir, 'behandlungen.html')
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    html = html.replace('https://www.youtube.com/embed/ScMzIvxBSi4?enablejsapi=1&rel=0&autoplay=1', 'https://www.youtube.com/embed/aqz-KE-bpKQ?enablejsapi=1&rel=0')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed CSS aspect-ratio and placeholder video URL")
