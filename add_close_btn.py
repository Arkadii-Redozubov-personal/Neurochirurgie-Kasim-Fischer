import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

css_addition = '''
.fd-close {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #999;
  font-size: 20px;
  border-radius: 50%;
  background: rgba(0,0,0,0.03);
  transition: 0.3s;
  line-height: 1;
}
.fd-close:hover {
  background: rgba(0,0,0,0.1);
  color: #333;
}
[dir="rtl"] .fd-close {
  right: auto;
  left: 10px;
}

@media (max-width: 768px) {
  .fd-close {
    top: -8px;
    right: -8px;
    background: white;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    color: var(--bg-dark);
  }
  [dir="rtl"] .fd-close {
    left: -8px;
    right: auto;
  }
}
'''

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

if '.fd-close' not in css:
    css += css_addition
    with open(CSS_PATH, 'w', encoding='utf-8') as f:
        f.write(css)

base_dir = 'c:/Users/arkad/Downloads/vertex'
langs = ['', 'en', 'ru', 'tr', 'ar']
files = ['index.html', 'praxis-schwerpunkte.html', 'behandlungen.html', 'unser-team.html', 'presseschau.html', 'sprechzeiten.html']

for lang in langs:
    for filename in files:
        filepath = os.path.join(base_dir, lang, filename) if lang else os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'fd-close' not in content and 'class="floating-doctolib"' in content:
            # Insert the close button
            content = content.replace('<div class="floating-doctolib">', '<div class="floating-doctolib">\n      <div class="fd-close" onclick="this.parentElement.style.display=\'none\'">×</div>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Added close button to Doctolib widget")
