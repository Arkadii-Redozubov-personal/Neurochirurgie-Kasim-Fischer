import os
import re

base_dir = 'c:/Users/arkad/Downloads/vertex'
langs = ['', 'en', 'ru', 'tr', 'ar']
files = ['index.html', 'praxis-schwerpunkte.html', 'behandlungen.html', 'unser-team.html', 'presseschau.html', 'sprechzeiten.html']

brand_html = '''<div class="footer-brand">
        <div class="logo" style="margin-bottom: 24px;">
          <div class="logo-icon">N</div>
          NEUROCHIRURGIE FISCHER
        </div>
        <div style="color: rgba(255,255,255,0.7); font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">
          Viersener Str. 50<br>41061 Mönchengladbach
        </div>
        <div style="color: rgba(255,255,255,0.9); font-weight: 600; margin-bottom: 4px;">
          (02161) 678 26 83
        </div>
        <a href="mailto:kontakt@my-bandscheibe.de" style="color: var(--primary); text-decoration: none; font-size: 0.95rem; display: inline-block; margin-bottom: 24px;">kontakt@my-bandscheibe.de</a>
        <div class="footer-socials">
          <a href="https://www.facebook.com/neurokaz/" target="_blank" style="color: white; opacity: 0.7; transition: 0.3s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.7'">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
          </a>
        </div>
      </div>
      
      '''

bottom_html = '''
    </div>
    <div class="footer-bottom" style="text-align: center; padding-top: 32px; margin-top: 32px; border-top: 1px solid rgba(255,255,255,0.1); color: rgba(255,255,255,0.5); font-size: 0.85rem;">
      &copy; 2026 Neurochirurgie Fischer
    </div>
  </footer>'''

for lang in langs:
    for filename in files:
        filepath = os.path.join(base_dir, lang, filename) if lang else os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace footer-brand
        start = content.find('<div class="footer-brand">')
        end = content.find('<div class="footer-links">', start)
        if start != -1 and end != -1:
            content = content[:start] + brand_html + content[end:]
            
        # Replace the end of footer to add copyright, ONLY if not already there
        if 'class="footer-bottom"' not in content:
            # The footer usually ends with:
            #     </div>
            #   </footer>
            content = re.sub(r'(\s*)</div>\s*</footer>', r'\1' + bottom_html, content, count=1)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated footer across all pages.")
