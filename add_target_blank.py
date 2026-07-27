import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add target="_blank" to the download button if it's not there
    pattern = r'(<a href="[^"]+" download="[^"]+" class="btn-book btn-download" style="[^"]+" onclick="event\.stopPropagation\(\)")>'
    
    def replacer(match):
        return match.group(1) + ' target="_blank">'

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
