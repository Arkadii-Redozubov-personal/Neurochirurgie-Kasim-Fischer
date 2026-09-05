import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
count = 0

for filepath in html_files:
    if 'admin' in filepath: continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Fix explicit width and height for logo
    content = re.sub(
        r'<img src="img/logo_white\.webp" alt="Nabiota Health Group" style="height:60px;width:auto;border-radius:12px;">',
        '<img src="img/logo_white.webp" alt="Nabiota Health Group" width="92" height="120" style="height:60px;width:auto;border-radius:12px;">',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Added explicit width/height to logo in {count} HTML files.")
