import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the overly complex JS fetch block and replace it with just event.stopPropagation()
    pattern = r'(onclick="event\.stopPropagation\(\);\s*event\.preventDefault\(\);\s*fetch\([^)]+\)\.then[^"]+")'
    
    def replacer(match):
        return 'onclick="event.stopPropagation()"'

    new_content = re.sub(pattern, replacer, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

root_dir = 'c:/Users/arkad/Downloads/vertex'
process_file(f"{root_dir}/presseschau.html")
for lang in ['en', 'ru', 'tr', 'ar']:
    path = f"{root_dir}/{lang}/presseschau.html"
    if os.path.exists(path):
        process_file(path)
