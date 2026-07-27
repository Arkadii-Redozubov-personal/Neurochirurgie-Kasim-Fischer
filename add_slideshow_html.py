import os
import re

base_dir = 'c:/Users/arkad/Downloads/vertex'
langs = ['', 'en', 'ru', 'tr', 'ar']

for lang in langs:
    filepath = os.path.join(base_dir, lang, 'index.html') if lang else os.path.join(base_dir, 'index.html')
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Determine the image prefix based on language directory
    img_prefix = '../img/' if lang else 'img/'
    
    # Replacement string
    replacement = f'''<div class="hero-inner">
  <div class="hero-bg-slider">
    <div class="hero-bg-slide" style="background-image: url('{img_prefix}Neurochirurgie_Fischer_Web_13-1024x684.jpg');"></div>
    <div class="hero-bg-slide" style="background-image: url('{img_prefix}Neurochirurgie_Fischer_Web_07-1024x684.jpg');"></div>
    <div class="hero-bg-slide" style="background-image: url('{img_prefix}Neurochirurgie_Fischer_Web_11-1024x684.jpg');"></div>
  </div>
  <div class="hero-overlay"></div>'''
    
    # Regex to match the old div
    pattern = r'<div class="hero-inner" style="background-image:[^>]+">'
    
    content = re.sub(pattern, replacement, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated index.html files with slideshow HTML")
