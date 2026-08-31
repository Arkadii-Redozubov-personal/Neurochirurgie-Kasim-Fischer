import os

languages = {
    '.': {
        'imp_title': 'Impressum',
        'dat_title': 'Datenschutz',
        'back': 'Zurück zur Startseite',
        'placeholder': '[Hier wird der finale Text von Ihrem Rechtsanwalt eingefügt]'
    },
    'en': {
        'imp_title': 'Imprint',
        'dat_title': 'Privacy Policy',
        'back': 'Back to Homepage',
        'placeholder': '[The final text from your lawyer will be inserted here]'
    },
    'ru': {
        'imp_title': 'Выходные данные (Impressum)',
        'dat_title': 'Политика конфиденциальности',
        'back': 'Вернуться на главную',
        'placeholder': '[Здесь будет размещен финальный текст от вашего юриста]'
    },
    'tr': {
        'imp_title': 'Künye',
        'dat_title': 'Gizlilik Politikası',
        'back': 'Ana Sayfaya Dön',
        'placeholder': '[Avukatınızın hazırladığı nihai metin buraya eklenecektir]'
    },
    'ar': {
        'imp_title': 'بيانات النشر',
        'dat_title': 'سياسة الخصوصية',
        'back': 'العودة إلى الصفحة الرئيسية',
        'placeholder': '[سيتم إدراج النص النهائي من محاميك هنا]'
    }
}

def generate_html(lang, lang_data, page_type):
    prefix = "" if lang == "." else "../"
    title = lang_data['imp_title'] if page_type == 'impressum' else lang_data['dat_title']
    url = f"https://my-bandscheibe.de/{'' if lang == '.' else lang + '/'}{page_type}.html"
    dir_attr = 'rtl' if lang == 'ar' else 'ltr'
    html_lang = lang if lang != '.' else 'de'
    
    html = f'''<!DOCTYPE html>
<html lang="{html_lang}" dir="{dir_attr}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Neurochirurgie Fischer</title>
  <link rel="stylesheet" href="{prefix}fonts/fonts.css">
  <link rel="stylesheet" href="{prefix}style.css">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="de" href="https://my-bandscheibe.de/{page_type}.html">
  <link rel="alternate" hreflang="en" href="https://my-bandscheibe.de/en/{page_type}.html">
  <link rel="alternate" hreflang="ru" href="https://my-bandscheibe.de/ru/{page_type}.html">
  <link rel="alternate" hreflang="tr" href="https://my-bandscheibe.de/tr/{page_type}.html">
  <link rel="alternate" hreflang="ar" href="https://my-bandscheibe.de/ar/{page_type}.html">
  <link rel="alternate" hreflang="x-default" href="https://my-bandscheibe.de/{page_type}.html">
</head>
<body class="page-body">
  
  <div class="hero-wrapper" style="min-height: 30vh; padding: 40px 0;">
    <div class="container">
      <div class="hero-main" style="text-align: center; max-width: 800px; margin: 0 auto;">
        <h1 class="hero-title">{title}</h1>
      </div>
    </div>
  </div>

  <div class="section-wrapper" style="background: white;">
    <div class="container" style="max-width: 800px; padding: 60px 20px;">
      
      <div style="background: #f8f9fa; padding: 40px; border-radius: 12px; text-align: center; border: 2px dashed #ccc;">
        <p style="color: var(--text-light); font-size: 1.1rem; margin: 0;">{lang_data['placeholder']}</p>
      </div>

    </div>
  </div>

  <div style="text-align: center; padding: 40px;">
    <a href="{prefix}index.html" class="btn-primary" style="display: inline-block; padding: 12px 24px;">&larr; {lang_data['back']}</a>
  </div>
  
</body>
</html>
'''
    return html

for lang, data in languages.items():
    if not os.path.exists(lang) and lang != '.':
        os.makedirs(lang)
    
    # Impressum
    imp_file = f"{lang}/impressum.html" if lang != '.' else "impressum.html"
    with open(imp_file, 'w', encoding='utf-8') as f:
        f.write(generate_html(lang, data, 'impressum'))
    print(f"Generated {imp_file}")
    
    # Datenschutz
    dat_file = f"{lang}/datenschutz.html" if lang != '.' else "datenschutz.html"
    with open(dat_file, 'w', encoding='utf-8') as f:
        f.write(generate_html(lang, data, 'datenschutz'))
    print(f"Generated {dat_file}")

print("Done building legal pages.")
