import os, re

data = {
    '.': {
        'title': 'Zweitmeinung',
        'desc': 'Unabhängige ärztliche Expertise für Ihre Sicherheit und Gesundheit.',
        'steps_title': 'Der Ablauf der Zweitmeinung',
        'steps': [
            {'title': 'Sichere Datenübermittlung', 'desc': 'Sie übermitteln Ihre medizinischen Dokumente (MRT/CT, Arztbriefe) über einen sicheren Kanal oder bringen diese direkt mit.'},
            {'title': 'Terminvereinbarung', 'desc': 'Sie buchen einen Termin für eine ausführliche, persönliche oder telemedizinische Konsultation.'},
            {'title': 'Unabhängige Beurteilung', 'desc': 'Herr Fischer begutachtet Ihre Befunde neutral und führt, falls nötig, eine ergänzende Untersuchung durch.'},
            {'title': 'Ausführliche Beratung', 'desc': 'Gemeinsame Besprechung aller konservativen, interventionellen und operativen Behandlungsoptionen ohne Zeitdruck.'}
        ],
        'alert_title': 'Sicherheit Ihrer Gesundheitsdaten',
        'alert_text': 'Ihre Gesundheitsdaten (MRT/CT-Bilder, Arztbriefe, OP-Berichte, Medikamentenpläne) sind streng vertraulich. Bitte nutzen Sie für die Übermittlung dieser Dokumente niemals unverschlüsselte E-Mails oder einfache Webformulare. Nutzen Sie zur Terminbuchung unser sicheres Doctolib-System oder bringen Sie Ihre Unterlagen persönlich zum Termin mit.',
        'btn_text': 'Termin auf Doctolib anfragen'
    },
    'en': {
        'title': 'Second Opinion',
        'desc': 'Independent medical expertise for your safety and health.',
        'steps_title': 'The Second Opinion Process',
        'steps': [
            {'title': 'Secure Data Transmission', 'desc': 'You transmit your medical documents (MRI/CT, doctor\'s letters) via a secure channel or bring them directly with you.'},
            {'title': 'Appointment Booking', 'desc': 'You book an appointment for a detailed, personal, or telemedical consultation.'},
            {'title': 'Independent Assessment', 'desc': 'Mr. Fischer neutrally evaluates your findings and, if necessary, performs an additional examination.'},
            {'title': 'Detailed Consultation', 'desc': 'Joint discussion of all conservative, interventional, and surgical treatment options without time pressure.'}
        ],
        'alert_title': 'Security of Your Health Data',
        'alert_text': 'Your health data (MRI/CT images, doctor\'s letters, surgical reports, medication plans) are strictly confidential. Please never use unencrypted emails or simple web forms to transmit these documents. Use our secure Doctolib system to book an appointment or bring your documents personally to the appointment.',
        'btn_text': 'Request Appointment on Doctolib'
    },
    'ru': {
        'title': 'Второе мнение',
        'desc': 'Независимая медицинская экспертиза для вашей безопасности и здоровья.',
        'steps_title': 'Процесс получения второго мнения',
        'steps': [
            {'title': 'Безопасная передача данных', 'desc': 'Вы передаете свои медицинские документы (МРТ/КТ, выписки) по безопасному каналу или приносите их с собой.'},
            {'title': 'Запись на прием', 'desc': 'Вы записываетесь на прием для подробной очной или телемедицинской консультации.'},
            {'title': 'Независимая оценка', 'desc': 'Врач объективно оценивает ваши результаты и, при необходимости, проводит дополнительное обследование.'},
            {'title': 'Подробная консультация', 'desc': 'Совместное обсуждение всех консервативных, интервенционных и оперативных вариантов лечения без спешки.'}
        ],
        'alert_title': 'Безопасность ваших медицинских данных',
        'alert_text': 'Ваши медицинские данные (снимки МРТ/КТ, выписки, протоколы операций, планы лечения) строго конфиденциальны. Пожалуйста, никогда не используйте незашифрованные email или обычные веб-формы для передачи этих документов. Используйте нашу безопасную систему Doctolib для записи на прием или принесите документы лично.',
        'btn_text': 'Запросить прием через Doctolib'
    },
    'tr': {
        'title': 'İkinci Görüş',
        'desc': 'Güvenliğiniz ve sağlığınız için bağımsız tıbbi uzmanlık.',
        'steps_title': 'İkinci Görüş Süreci',
        'steps': [
            {'title': 'Güvenli Veri İletimi', 'desc': 'Tıbbi belgelerinizi (MR/BT, doktor mektupları) güvenli bir kanal aracılığıyla iletirsiniz veya doğrudan yanınızda getirirsiniz.'},
            {'title': 'Randevu Alma', 'desc': 'Ayrıntılı, yüz yüze veya telemedikal bir konsültasyon için randevu alırsınız.'},
            {'title': 'Bağımsız Değerlendirme', 'desc': 'Dr. Fischer bulgularınızı tarafsız bir şekilde değerlendirir ve gerekirse ek bir muayene yapar.'},
            {'title': 'Ayrıntılı Danışmanlık', 'desc': 'Zaman baskısı olmadan tüm konservatif, girişimsel ve cerrahi tedavi seçeneklerinin ortak tartışılması.'}
        ],
        'alert_title': 'Sağlık Verilerinizin Güvenliği',
        'alert_text': 'Sağlık verileriniz (MR/BT görüntüleri, doktor mektupları, ameliyat raporları, ilaç planları) kesinlikle gizlidir. Lütfen bu belgeleri iletmek için asla şifrelenmemiş e-postalar veya basit web formları kullanmayın. Randevu almak için güvenli Doctolib sistemimizi kullanın veya belgelerinizi randevuya şahsen getirin.',
        'btn_text': 'Doctolib Üzerinden Randevu İste'
    },
    'ar': {
        'title': 'الرأي الثاني',
        'desc': 'خبرة طبية مستقلة من أجل سلامتك وصحتك.',
        'steps_title': 'عملية الرأي الثاني',
        'steps': [
            {'title': 'نقل آمن للبيانات', 'desc': 'تقوم بإرسال مستنداتك الطبية (الرنين المغناطيسي / المقطعية، تقارير الطبيب) عبر قناة آمنة أو تحضرها معك مباشرة.'},
            {'title': 'حجز موعد', 'desc': 'تقوم بحجز موعد لاستشارة مفصلة، سواء شخصيًا أو عبر التطبيب عن بعد.'},
            {'title': 'تقييم مستقل', 'desc': 'يقوم الطبيب بتقييم نتائجك بشكل محايد وإجراء فحص إضافي إذا لزم الأمر.'},
            {'title': 'استشارة مفصلة', 'desc': 'مناقشة مشتركة لجميع خيارات العلاج التحفظية والتداخلية والجراحية دون ضغط الوقت.'}
        ],
        'alert_title': 'أمان بياناتك الصحية',
        'alert_text': 'بياناتك الصحية (صور الرنين / المقطعية، خطابات الطبيب، تقارير العمليات، خطط الأدوية) سرية للغاية. يرجى عدم استخدام رسائل البريد غير المشفرة أو نماذج الويب البسيطة لنقل هذه المستندات. استخدم نظام Doctolib الآمن الخاص بنا لحجز موعد أو أحضر مستنداتك شخصيًا.',
        'btn_text': 'طلب موعد عبر Doctolib'
    }
}

arrow_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; opacity: 0.5;"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>'
shield_svg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'

for lang, lang_data in data.items():
    file_path = f"{lang}/zweitmeinung.html" if lang != '.' else "zweitmeinung.html"
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    hero_start = content.find('<div class="hero-main">')
    if hero_start == -1:
        continue
        
    hero_end = content.find('</div>\n  </div>\n\n  <div class="section-wrapper">', hero_start)
    if hero_end == -1:
        hero_end = content.find('</div>\n  </div>\n  <div class="section-wrapper">', hero_start)
    
    footer_start = content.find('<footer class="footer-wrapper">')
    
    if hero_start == -1 or footer_start == -1:
        print(f"Skipping {file_path}, tags not found")
        continue

    new_hero = f'''<div class="hero-main">
          <h1 class="hero-title" style="font-size: 4rem;">{lang_data["title"]}</h1>
          <p class="hero-desc">{lang_data["desc"]}</p>
        </div>'''
        
    new_body = f'''
  <style>
    .process-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      max-width: 1400px;
      margin: 0 auto;
    }}
    .process-box {{
      background: white; 
      border: 1px solid rgba(0,0,0,0.05); 
      padding: 24px; 
      border-radius: 12px; 
      box-shadow: 0 4px 20px rgba(0,0,0,0.03); 
      position: relative; 
      overflow: hidden;
      flex: 1;
      min-height: 200px;
      display: flex;
      flex-direction: column;
    }}
    .process-arrow-desktop {{
      display: block;
    }}
    .process-arrow-mobile {{
      display: none;
      transform: rotate(90deg);
      margin: 16px auto;
    }}
    @media(max-width: 992px) {{
      .process-row {{
        flex-direction: column;
        max-width: 500px;
      }}
      .process-arrow-desktop {{
        display: none;
      }}
      .process-arrow-mobile {{
        display: block;
      }}
      .process-box {{
        width: 100%;
        min-height: auto;
      }}
    }}
  </style>
  <div class="section-wrapper">
    <section class="container" style="padding-top: 60px; padding-bottom: 80px; max-width: 1400px;">
      
      <!-- Security Alert -->
      <div style="background: rgba(28, 194, 178, 0.05); border-left: 4px solid var(--primary); padding: 24px; border-radius: 8px; margin-bottom: 60px; max-width: 1400px; margin-left: auto; margin-right: auto;">
        <h3 style="font-size: 1.1rem; margin-bottom: 8px; font-weight: 600; display: flex; align-items: center; gap: 8px; color: var(--primary);">
          {shield_svg}
          {lang_data["alert_title"]}
        </h3>
        <p style="font-size: 0.95rem; line-height: 1.6; color: var(--text-dark); margin: 0;">{lang_data["alert_text"]}</p>
      </div>

      <h2 style="text-align: center; font-size: 2.2rem; margin-bottom: 40px; color: var(--text-dark);">{lang_data["steps_title"]}</h2>
      
      <div class="process-row">
        '''
        
    for i, step in enumerate(lang_data['steps']):
        new_body += f'''
        <div class="process-box">
          <div style="font-size: 4rem; font-weight: 900; color: rgba(28, 194, 178, 0.08); position: absolute; top: -15px; right: 5px; line-height: 1;">0{i+1}</div>
          <h4 style="font-size: 1.05rem; font-weight: 700; color: var(--text-dark); margin-bottom: 12px; position: relative; z-index: 1;">{step["title"]}</h4>
          <p style="color: var(--text-light); font-size: 0.9rem; line-height: 1.6; margin: 0; position: relative; z-index: 1;">{step["desc"]}</p>
        </div>'''
        
        if i < len(lang_data['steps']) - 1:
            new_body += f'''
        <div class="process-arrow-desktop">{arrow_svg}</div>
        <div class="process-arrow-mobile">{arrow_svg}</div>
            '''
        
    new_body += f'''
      </div>
      
      <div style="text-align: center; margin-top: 60px;">
        <a href="https://www.doctolib.de/neurochirurgie/moenchengladbach/kasim-fischer?utm_campaign=website-button&utm_source=kasim-fischer-website-button&utm_medium=referral&utm_content=custom&utm_term=kasim-fischer" target="_blank" class="btn-primary" style="display: inline-block; font-size: 1.1rem; padding: 16px 32px;">
          {lang_data["btn_text"]} &rarr;
        </a>
      </div>
      
    </section>
  </div>
  '''

    new_content = content[:hero_start] + new_hero + '\n      </div>\n    </div>\n  </div>\n\n' + new_body + content[footer_start:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {file_path}")

print("Done updating zweitmeinung.html files.")
