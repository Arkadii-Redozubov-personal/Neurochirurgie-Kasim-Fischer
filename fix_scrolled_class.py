import os
import re

base_dir = 'c:/Users/arkad/Downloads/vertex'

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Replace navbar.classList.add('...') with navbar.classList.add('scrolled')
            content = re.sub(
                r"navbar\.classList\.add\(['\"].*?['\"]\)", 
                "navbar.classList.add('scrolled')", 
                content
            )
            # Replace navbar.classList.remove('...') with navbar.classList.remove('scrolled')
            content = re.sub(
                r"navbar\.classList\.remove\(['\"].*?['\"]\)", 
                "navbar.classList.remove('scrolled')", 
                content
            )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Fixed translated 'scrolled' class in all HTML files")
