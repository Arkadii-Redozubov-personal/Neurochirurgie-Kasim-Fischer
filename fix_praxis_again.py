import os
import re

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add hero-title-sub and hero-bottom-grid max-width
if '.hero-title-sub' not in css_content:
    new_css = '''
/* Added for praxis-schwerpunkte */
.hero-title-sub {
  font-size: 3.5rem !important;
}
@media (max-width: 1200px) {
  .hero-title-sub {
    font-size: 2.8rem !important;
  }
}
@media (max-width: 768px) {
  .hero-title-sub {
    font-size: 2.2rem !important;
  }
}

.hero-bottom-grid.container {
  max-width: 1100px !important;
  margin: 0 auto !important;
}
'''
    css_content += new_css

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css_content)

def process_html_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the inline font-size with hero-title-sub
    content = re.sub(r'class="hero-title"\s+style="font-size:\s*2\.8rem;"', 'class="hero-title hero-title-sub"', content)
    content = re.sub(r'class="hero-title"\s+style="font-size:\s*3\.5rem;"', 'class="hero-title hero-title-sub"', content)
    content = re.sub(r'class="hero-title"\s+style="font-size:\s*3\.5rem;\s*"', 'class="hero-title hero-title-sub"', content)
    content = re.sub(r'class="hero-title hero-title-sub"\s+style="font-size:\s*2\.8rem;"', 'class="hero-title hero-title-sub"', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = 'c:/Users/arkad/Downloads/vertex'
process_html_file(os.path.join(base_dir, 'praxis-schwerpunkte.html'))
for lang in ['ru', 'en', 'ar', 'tr']:
    process_html_file(os.path.join(base_dir, lang, 'praxis-schwerpunkte.html'))

print("Updated style.css and praxis-schwerpunkte.html files")
