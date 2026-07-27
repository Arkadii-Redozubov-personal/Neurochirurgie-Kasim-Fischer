import os

base_dir = 'c:/Users/arkad/Downloads/vertex'
langs = ['', 'en', 'ru', 'tr', 'ar']

for lang in langs:
    filepath = os.path.join(base_dir, lang, 'presseschau.html') if lang else os.path.join(base_dir, 'presseschau.html')
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace flex-end with center for the container holding the date and download button
    content = content.replace(
        'align-items: flex-end; margin-top: auto;', 
        'align-items: center; margin-top: auto;'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated vertical alignment to 'center' in presseschau.html across all languages")
