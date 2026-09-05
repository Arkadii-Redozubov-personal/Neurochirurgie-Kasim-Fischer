import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
count = 0

preload_link = '<link rel="preload" as="image" href="https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&w=1600&q=80">\n  <link rel="stylesheet"'

emailjs_script = '<script defer type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>'

for filepath in html_files:
    if 'admin' in filepath: continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Preload the Unsplash image
    if '<link rel="preload" as="image" href="https://images.unsplash.com' not in content:
        content = content.replace('<link rel="stylesheet"', preload_link)
        
    # Defer EmailJS
    content = content.replace('<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>', emailjs_script)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated {count} HTML files to fix Core Web Vitals.")
