import os
import re

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

css_addition = '''
/* Floating Doctolib Widget */
.floating-doctolib {
  position: fixed;
  right: 30px;
  bottom: 30px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.15);
  padding: 20px;
  width: 280px;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: 16px;
  border: 1px solid rgba(0,0,0,0.05);
  transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.floating-doctolib:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 50px rgba(0,0,0,0.2);
}
.fd-content {
  display: flex;
  gap: 16px;
  align-items: flex-start;
}
.fd-icon {
  background: var(--primary);
  color: white;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.fd-text {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.fd-title {
  font-size: 1rem;
  font-weight: 800;
  color: var(--bg-dark);
}
.fd-desc {
  font-size: 0.85rem;
  color: #555;
  line-height: 1.5;
  font-weight: 500;
}
.fd-btn {
  background: var(--bg-dark);
  color: white;
  text-align: center;
  padding: 12px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  transition: 0.3s;
}
.fd-btn:hover {
  background: var(--primary);
  color: white;
}
[dir="rtl"] .floating-doctolib {
  right: auto;
  left: 30px;
}
[dir="rtl"] .fd-title, [dir="rtl"] .fd-desc {
  text-align: right;
}

@media (max-width: 768px) {
  .floating-doctolib {
    right: 20px;
    bottom: 20px;
    width: auto;
    padding: 0;
    border-radius: 50px;
    flex-direction: row;
    align-items: center;
  }
  [dir="rtl"] .floating-doctolib {
    left: 20px;
    right: auto;
  }
  .fd-content { display: none; }
  .fd-btn {
    border-radius: 50px;
    padding: 14px 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  }
}
'''

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

if '.floating-doctolib' not in css:
    css += css_addition
    with open(CSS_PATH, 'w', encoding='utf-8') as f:
        f.write(css)

def get_widget_html(lang):
    title = "Termin vereinbaren"
    desc = "Buchen Sie Ihren Termin schnell und einfach online."
    btn = "Auf Doctolib buchen"
    
    if lang == 'en':
        title = "Book an Appointment"
        desc = "Book your appointment quickly and easily online."
        btn = "Book on Doctolib"
    elif lang == 'ru':
        title = "Записаться на прием"
        desc = "Забронируйте время визита быстро и удобно онлайн."
        btn = "Записаться на Doctolib"
    elif lang == 'tr':
        title = "Randevu Alın"
        desc = "Randevunuzu hızlı ve kolayca çevrimiçi alın."
        btn = "Doctolib'de Randevu Al"
    elif lang == 'ar':
        title = "احجز موعداً"
        desc = "احجز موعدك بسرعة وسهولة عبر الإنترنت."
        btn = "احجز عبر Doctolib"
        
    return f'''
    <!-- Floating Doctolib Widget -->
    <div class="floating-doctolib">
      <div class="fd-content">
        <div class="fd-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        </div>
        <div class="fd-text">
          <div class="fd-title">{title}</div>
          <div class="fd-desc">{desc}</div>
        </div>
      </div>
      <a href="https://www.doctolib.de/" target="_blank" class="fd-btn">{btn}</a>
    </div>
'''

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
            
        if 'floating-doctolib' not in content:
            # Insert before </body>
            widget_html = get_widget_html(lang if lang else 'de')
            content = content.replace('</body>', widget_html + '</body>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Added Doctolib floating widget to all pages")
