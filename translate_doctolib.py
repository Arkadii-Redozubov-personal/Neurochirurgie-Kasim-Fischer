import os, glob, re

langs = ['en', 'ru', 'tr', 'ar']

translations = {
    'en': {
        'title': 'Book an appointment',
        'desc': 'Book your appointment quickly and easily online.',
        'btn': 'Book on Doctolib &rarr;',
        'secure': 'Your data is safe and confidential.'
    },
    'ru': {
        'title': 'Записаться на прием',
        'desc': 'Забронируйте время визита быстро и легко онлайн.',
        'btn': 'Записаться на Doctolib &rarr;',
        'secure': 'Ваши данные в безопасности и конфиденциальны.'
    },
    'tr': {
        'title': 'Randevu al',
        'desc': 'Randevunuzu hızlı ve kolayca çevrimiçi alın.',
        'btn': 'Doctolib\'de yer ayırt &rarr;',
        'secure': 'Verileriniz güvende ve gizlidir.'
    },
    'ar': {
        'title': 'احجز موعدًا',
        'desc': 'احجز موعدك بسرعة وسهولة عبر الإنترنت.',
        'btn': 'احجز على Doctolib &rarr;',
        'secure': 'بياناتك آمنة وسرية.'
    }
}

for lang in langs:
    files = glob.glob(f"{lang}/*.html")
    t = translations[lang]
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace title
        content = re.sub(
            r'<div class="fd-title">.*?</div>',
            f'<div class="fd-title">{t["title"]}</div>',
            content
        )
        
        # Replace desc
        content = re.sub(
            r'<div class="fd-desc">.*?</div>',
            f'<div class="fd-desc">{t["desc"]}</div>',
            content
        )
        
        # Replace btn
        content = re.sub(
            r'class="fd-btn">.*?</a>',
            f'class="fd-btn">{t["btn"]}</a>',
            content
        )
        
        # Replace secure text
        content = re.sub(
            r'(<div class="fd-secure">.*?</svg>)\s*Ihre Daten sind sicher und vertraulich\.\s*</div>',
            rf'\1\n          {t["secure"]}\n        </div>',
            content,
            flags=re.DOTALL
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {filepath}")
