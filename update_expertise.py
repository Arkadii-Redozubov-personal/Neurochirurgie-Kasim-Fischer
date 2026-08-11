import os, glob, re

files = [
    'index.html',
    'en/index.html',
    'ru/index.html',
    'tr/index.html',
    'ar/index.html'
]

translations = {
    'index.html': {
        'title': 'FACHGEBIETE',
        'cards': [
            {'title': 'Wirbelsäulenerkrankungen', 'desc': 'Diagnostik und Behandlung'},
            {'title': 'Bandscheibenvorfall', 'desc': 'Minimalinvasive Lösungen'},
            {'title': 'Karpaltunnelsyndrom', 'desc': 'Endoskopische Behandlung'},
            {'title': 'Tumorbehandlung', 'desc': 'Moderne Methoden'},
            {'title': 'Schmerztherapie', 'desc': 'Individuelle Schmerzbehandlung'}
        ]
    },
    'en/index.html': {
        'title': 'AREAS OF EXPERTISE',
        'cards': [
            {'title': 'Spinal Diseases', 'desc': 'Diagnostics and treatment'},
            {'title': 'Herniated Disc', 'desc': 'Minimally invasive solutions'},
            {'title': 'Carpal Tunnel Syndrome', 'desc': 'Endoscopic treatment'},
            {'title': 'Tumor Treatment', 'desc': 'Modern methods and care'},
            {'title': 'Pain Therapy', 'desc': 'Individual pain management'}
        ]
    },
    'ru/index.html': {
        'title': 'НАПРАВЛЕНИЯ ДЕЯТЕЛЬНОСТИ',
        'cards': [
            {'title': 'Заболевания позвоночника', 'desc': 'Диагностика и лечение'},
            {'title': 'Грыжа диска', 'desc': 'Минимально инвазивные решения'},
            {'title': 'Карпальный синдром', 'desc': 'Эндоскопическое лечение'},
            {'title': 'Лечение опухолей', 'desc': 'Современные методы'},
            {'title': 'Терапия боли', 'desc': 'Индивидуальный подход'}
        ]
    },
    'tr/index.html': {
        'title': 'UZMANLIK ALANLARI',
        'cards': [
            {'title': 'Omurga Hastalıkları', 'desc': 'Teşhis ve tedavi'},
            {'title': 'Bel Fıtığı', 'desc': 'Minimal invaziv çözümler'},
            {'title': 'Karpal Tünel Sendromu', 'desc': 'Endoskopik tedavi'},
            {'title': 'Tümör Tedavisi', 'desc': 'Modern yöntemler'},
            {'title': 'Ağrı Tedavisi', 'desc': 'Bireysel ağrı yönetimi'}
        ]
    },
    'ar/index.html': {
        'title': 'مجالات الخبرة',
        'cards': [
            {'title': 'أمراض العمود الفقري', 'desc': 'التشخيص والعلاج'},
            {'title': 'الانزلاق الغضروفي', 'desc': 'حلول طفيفة التوغل'},
            {'title': 'متلازمة النفق الرسغي', 'desc': 'العلاج بالمنظار'},
            {'title': 'علاج الأورام', 'desc': 'الطرق الحديثة'},
            {'title': 'علاج الألم', 'desc': 'إدارة الألم الفردية'}
        ]
    }
}

svgs = [
    '''<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M10 2h4l-2 3z"></path>
  <path d="M9 7c1 1 3 1 4 0l1 1c-1.5 2-4.5 2-6 0z"></path>
  <path d="M9 11c1 1 3 1 4 0l1 1c-1.5 2-4.5 2-6 0z"></path>
  <path d="M9 15c1 1 3 1 4 0l1 1c-1.5 2-4.5 2-6 0z"></path>
  <path d="M12 18c-2 2-4 3-5 1l2-2c1.5 1 2.5.5 3-1z"></path>
  <line x1="12" y1="5" x2="12" y2="18"></line>
</svg>''',
    '''<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="9"></circle>
  <circle cx="12" cy="12" r="3"></circle>
  <line x1="3" y1="12" x2="9" y2="12"></line>
  <line x1="15" y1="12" x2="21" y2="12"></line>
</svg>''',
    '''<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M18 11V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2v4"></path>
  <path d="M14 10V4a2 2 0 0 0-2-2a2 2 0 0 0-2 2v6"></path>
  <path d="M10 10.5V5a2 2 0 0 0-2-2a2 2 0 0 0-2 2v8"></path>
  <path d="M18 11a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"></path>
  <path d="M12 11c-1 2-2 3-1 5c1 1 1 3 1 6"></path>
  <path d="M12 13c1 1 2 2 2 3"></path>
</svg>''',
    '''<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 4c-3-3-8-1-8 3 0 1-1 1-1 3 0 2 1 2 1 3 0 3 3 5 8 5"></path>
  <path d="M12 4c3-3 8-1 8 3 0 1 1 1 1 3 0 2-1 2-1 3 0 3-3 5-8 5"></path>
  <line x1="12" y1="4" x2="12" y2="18"></line>
  <path d="M8 8c1 1 2 0 2-1"></path>
  <path d="M16 8c-1 1-2 0-2-1"></path>
  <path d="M7 13c1.5 1 2.5 0 3-1"></path>
  <path d="M17 13c-1.5 1-2.5 0-3-1"></path>
  <path d="M9 16c1-1 2-1 2-2"></path>
  <path d="M15 16c-1-1-2-1-2-2"></path>
</svg>''',
    '''<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="7"></circle>
  <circle cx="12" cy="12" r="2"></circle>
  <circle cx="12" cy="12" r="0.5" fill="currentColor"></circle>
  <line x1="12" y1="1" x2="12" y2="4"></line>
  <line x1="12" y1="20" x2="12" y2="23"></line>
  <line x1="1" y1="12" x2="4" y2="12"></line>
  <line x1="20" y1="12" x2="23" y2="12"></line>
</svg>'''
]

links = [
    'praxis-schwerpunkte.html#service-0',
    'praxis-schwerpunkte.html#service-4',
    'praxis-schwerpunkte.html#service-6',
    'praxis-schwerpunkte.html#service-5',
    'praxis-schwerpunkte.html'
]

for filepath in files:
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    t = translations[filepath]
    prefix = '../' if filepath != 'index.html' else ''
    
    cards_html = ""
    for i in range(5):
        card = t['cards'][i]
        link = prefix + links[i]
        svg_code = svgs[i]
        cards_html += f"""
              <a href="{link}" class="expertise-card">
                <div class="expertise-icon">
                  {svg_code}
                </div>
                <div class="expertise-text">
                  <span class="expertise-card-title">{card['title']}</span>
                  <span class="expertise-card-desc">{card['desc']}</span>
                </div>
              </a>"""

    new_html = f"""<!-- Areas of Expertise -->
        <div class="expertise-wrapper fade-in">
          <div class="expertise-container">
            <div class="expertise-title">{t['title']}</div>
            <div class="expertise-grid">{cards_html}
            </div>
          </div>
        </div>"""

    # Replace the block
    pattern = r'<!-- Areas of Expertise -->\s*<div class="expertise-wrapper fade-in">.*?</div>\s*</div>\s*</div>'
    new_content = re.sub(pattern, new_html, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {filepath}")
