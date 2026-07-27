import re

with open('c:/Users/arkad/Downloads/vertex/ru/presseschau.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'(<a href="artikel_\d+\.pdf" target="_blank" class="press-card-horizontal">.*?<img src="(?:\.\./)?img/([^"]+)".*?<div class="press-card-meta" style="margin-bottom: 0; margin-top: auto; color: var\(--text-light\); font-weight: 500;">\s*(.*?)\s*</div>\s*</div>\s*</a>)'

matches = re.findall(pattern, content, re.DOTALL)
print("Matches found:", len(matches))
