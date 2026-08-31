import os
import re
import urllib.request

# 1. DOWNLOAD FONTS
font_url = "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

req = urllib.request.Request(font_url, headers=headers)
with urllib.request.urlopen(req) as response:
    css_content = response.read().decode('utf-8')

os.makedirs('fonts', exist_ok=True)

# Find all url(...) in CSS
urls = re.findall(r'url\((https://[^)]+)\)', css_content)
url_map = {}

for idx, url in enumerate(set(urls)):
    filename = f"plus-jakarta-sans-{idx}.woff2"
    filepath = os.path.join('fonts', filename)
    print(f"Downloading {url} to {filepath}")
    
    req_font = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req_font) as res:
        with open(filepath, 'wb') as f:
            f.write(res.read())
            
    url_map[url] = f"../fonts/{filename}" # Default relative for subfolders, we'll fix it in the css

# Replace URLs in CSS
local_css = css_content
for url, local_path in url_map.items():
    # Store just the filename in the css, we will link it properly
    local_css = local_css.replace(url, f"../fonts/{local_path.split('/')[-1]}")

with open('fonts/fonts.css', 'w', encoding='utf-8') as f:
    f.write(local_css)
with open('fonts/fonts-root.css', 'w', encoding='utf-8') as f:
    f.write(local_css.replace('../fonts/', 'fonts/'))

print("Fonts downloaded successfully.")

# 2. UPDATE HTML FILES TO USE LOCAL FONTS
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'admin', 'fonts']]
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root_dir, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            # Remove google fonts links
            content = re.sub(r'<link[^>]+fonts\.googleapis\.com[^>]+>', '', content)
            content = re.sub(r'<link[^>]+fonts\.gstatic\.com[^>]+>', '', content)
            
            # Add local font link before style.css
            is_root = root_dir == '.'
            css_link = '<link rel="stylesheet" href="fonts/fonts-root.css">' if is_root else '<link rel="stylesheet" href="../fonts/fonts.css">'
            
            if 'style.css' in content and 'fonts-root.css' not in content and 'fonts.css' not in content:
                content = re.sub(
                    r'(<link[^>]+href="[^"]*style\.css"[^>]*>)',
                    f'{css_link}\n  \\1',
                    content
                )
                
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated fonts in {filepath}")
