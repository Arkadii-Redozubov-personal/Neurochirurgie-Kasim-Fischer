import os, glob, re

files = glob.glob('*.html') + glob.glob('en/*.html') + glob.glob('ru/*.html') + glob.glob('tr/*.html') + glob.glob('ar/*.html')

translations = {
    'de': {
        'title': 'Termin vereinbaren',
        'desc': 'Buchen Sie Ihren Termin schnell und einfach online.',
        'btn': 'Auf Doctolib buchen &rarr;',
        'secure': 'Ihre Daten sind sicher und vertraulich.'
    },
    'en': {
        'title': 'Book an Appointment',
        'desc': 'Book your appointment quickly and easily online.',
        'btn': 'Book on Doctolib &rarr;',
        'secure': 'Your data is secure and confidential.'
    },
    'ru': {
        'title': 'Записаться на прием',
        'desc': 'Запишитесь на прием быстро и легко онлайн.',
        'btn': 'Записаться на Doctolib &rarr;',
        'secure': 'Ваши данные в безопасности и конфиденциальны.'
    },
    'tr': {
        'title': 'Randevu Alın',
        'desc': 'Randevunuzu hızlı ve kolayca çevrimiçi alın.',
        'btn': 'Doctolib\'te Randevu Al &rarr;',
        'secure': 'Verileriniz güvende ve gizlidir.'
    },
    'ar': {
        'title': 'حجز موعد',
        'desc': 'احجز موعدك بسرعة وسهولة عبر الإنترنت.',
        'btn': 'احجز عبر Doctolib &rarr;',
        'secure': 'بياناتك آمنة وسرية.'
    }
}

for filepath in files:
    # Determine language
    lang = 'de'
    if filepath.startswith('en/'): lang = 'en'
    if filepath.startswith('ru/'): lang = 'ru'
    if filepath.startswith('tr/'): lang = 'tr'
    if filepath.startswith('ar/'): lang = 'ar'
    
    t = translations[lang]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The new widget HTML
    new_html = f"""<!-- Floating Doctolib Widget -->
    <div class="floating-doctolib">
      <div class="fd-close" onclick="this.parentElement.style.display='none'">
        <svg viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </div>
      <div class="fd-content">
        <div class="fd-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        </div>
        <div class="fd-text">
          <div class="fd-title">{t['title']}</div>
          <div class="fd-desc">{t['desc']}</div>
        </div>
      </div>
      <a href="https://www.doctolib.de/neurochirurgie/moenchengladbach/kasim-fischer?utm_campaign=website-button&utm_source=kasim-fischer-website-button&utm_medium=referral&utm_content=custom&utm_term=kasim-fischer" target="_blank" class="fd-btn">{t['btn']}</a>
      <div class="fd-secure">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        {t['secure']}
      </div>
    </div>"""

    # We need to replace from <!-- Floating Doctolib Widget --> to the end of the </div> that closes it.
    # The existing widget looks like:
    # <!-- Floating Doctolib Widget -->
    # <div class="floating-doctolib">
    #   ...
    #   <a ... class="fd-btn">...</a>
    # </div>
    pattern = r'<!-- Floating Doctolib Widget -->\s*<div class="floating-doctolib">.*?</a>\s*</div>'
    
    new_content = re.sub(pattern, new_html, content, flags=re.DOTALL)
    
    # Also if someone doesn't have the comment:
    # Just to be safe, replace if they exist
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes in {filepath}")
