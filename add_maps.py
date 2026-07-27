import os

base_dir = 'c:/Users/arkad/Downloads/vertex'
langs = ['', 'en', 'ru', 'tr', 'ar']

map_html = '''    </div>
    
    <!-- Google Map Section -->
    <div style="width: 100%; height: 450px; margin-top: 80px; margin-bottom: -100px; filter: grayscale(10%) contrast(110%);">
      <iframe src="https://maps.google.com/maps?q=Viersener%20Str.%2050,%2041061%20M%C3%B6nchengladbach&t=&z=15&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
    </div>
    
  <div style="height: 100px;"></div></div>'''

for lang in langs:
    filepath = os.path.join(base_dir, lang, 'sprechzeiten.html') if lang else os.path.join(base_dir, 'sprechzeiten.html')
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace old Bismarckstraße address if it exists
    content = content.replace('Bismarckstraße 106', 'Viersener Str. 50')
    
    # Inject the map if not already present
    if 'Google Map Section' not in content:
        content = content.replace('    </div>\n  <div style="height: 100px;"></div></div>', map_html)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added maps to sprechzeiten.html across all languages")
