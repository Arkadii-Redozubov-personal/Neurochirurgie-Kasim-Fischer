import os, re
import urllib.parse

def get_qr_url(address):
    maps_url = f"https://maps.google.com/maps?q={urllib.parse.quote(address)}"
    return f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={urllib.parse.quote(maps_url)}"

def get_maps_embed(address):
    return f"https://maps.google.com/maps?q={urllib.parse.quote(address)}&t=&z=15&ie=UTF8&iwloc=&output=embed"

data = {
    '.': {
        'title': 'Kontakt & Standorte',
        'desc': 'Nehmen Sie Kontakt mit uns auf oder besuchen Sie unsere Praxen in Viersen, Mönchengladbach und Düsseldorf.',
        'phone_lbl': 'Telefon',
        'email_lbl': 'E-Mail',
        'hours_lbl': 'Öffnungszeiten',
        'services_lbl': 'Leistungen vor Ort',
        'transport_lbl': 'Parken & ÖPNV',
        'qr_desc': 'Scannen Sie den QR-Code mit Ihrem Smartphone, um die Navigation direkt zu starten.',
        'btn_text': 'Termin auf Doctolib buchen',
        'contact_title': 'Kontakt',
        'name_ph': 'Ihr Name',
        'email_ph': 'Ihre E-Mail',
        'branch_ph': 'Standort auswählen',
        'msg_ph': 'Ihre Nachricht',
        'send_btn': 'Nachricht senden',
        'secure_disclaimer': 'Datenschutzhinweis: Bitte senden Sie über dieses Kontaktformular keine medizinischen Unterlagen, Arztbriefe oder MRT/CT-Bilder. Nutzen Sie für den Versand sensibler Gesundheitsdaten den sicheren Kanal im Bereich <a href="zweitmeinung.html" style="color: var(--primary);">Zweitmeinung</a> oder bringen Sie diese persönlich zum Termin mit.',
        'terminservice_title': '116117 Terminservice',
        'terminservice_text': 'Sie können den Terminservice der Kassenärztlichen Vereinigung unter 116117 nutzen, um nach verfügbaren Facharztterminen zu suchen. Bitte beachten Sie, dass wir nicht garantieren können, dass Ihnen über diesen Service ein Termin spezifisch in unserer Praxis zugewiesen wird.',
        'branches': [
            {
                'city': 'Viersen',
                'address': 'Theodor-Heuss-Platz 10, 41747 Viersen, 4. OG',
                'phone': '',
                'hours': '',
                'services': 'Konsultationen, Diagnostik, Nachsorge',
                'transport': '',
                'btn_link': 'https://www.doctolib.de/'
            },
            {
                'city': 'Mönchengladbach',
                'address': 'Bismarckstr. 106, 41061 Mönchengladbach, 3. OG',
                'phone': '(02161) 678 26 83',
                'hours': 'Mo - Fr: 8:00 - 18:00 Uhr',
                'services': 'Konsultationen, Diagnostik, Nachsorge',
                'transport': '',
                'btn_link': 'https://www.doctolib.de/neurochirurgie/moenchengladbach/kasim-fischer'
            },
            {
                'city': 'Düsseldorf',
                'address': 'Schadowstraße 74, 40212 Düsseldorf',
                'phone': '',
                'hours': '',
                'services': '',
                'transport': '',
                'btn_link': '#',
                'btn_disabled': True
            }
        ]
    },
    'en': {
        'title': 'Contact & Locations',
        'desc': 'Get in touch with us or visit our practices in Viersen, Mönchengladbach and Düsseldorf.',
        'phone_lbl': 'Phone',
        'email_lbl': 'Email',
        'hours_lbl': 'Opening Hours',
        'services_lbl': 'On-site Services',
        'transport_lbl': 'Parking & Transport',
        'qr_desc': 'Scan the QR code with your smartphone to start navigation directly.',
        'btn_text': 'Book on Doctolib',
        'contact_title': 'Contact',
        'name_ph': 'Your Name',
        'email_ph': 'Your Email',
        'branch_ph': 'Select Location',
        'msg_ph': 'Your Message',
        'send_btn': 'Send Message',
        'secure_disclaimer': 'Privacy Notice: Please do not send medical records, doctor\'s letters, or MRI/CT scans via this contact form. For sending sensitive health data, please use the secure channel in the <a href="en/zweitmeinung.html" style="color: var(--primary);">Second Opinion</a> section or bring them personally to your appointment.',
        'terminservice_title': '116117 Appointment Service',
        'terminservice_text': 'You can use the 116117 appointment service to search for available specialist appointments. Please note that we cannot guarantee that you will be assigned an appointment specifically in our practice through this service.',
        'branches': [
            {
                'city': 'Viersen',
                'address': 'Theodor-Heuss-Platz 10, 41747 Viersen, 4th Floor',
                'phone': '',
                'hours': '',
                'services': 'Consultations, Diagnostics, Aftercare',
                'transport': '',
                'btn_link': 'https://www.doctolib.de/'
            },
            {
                'city': 'Mönchengladbach',
                'address': 'Bismarckstr. 106, 41061 Mönchengladbach, 3rd Floor',
                'phone': '(02161) 678 26 83',
                'hours': 'Mon - Fri: 8:00 AM - 6:00 PM',
                'services': 'Consultations, Diagnostics, Aftercare',
                'transport': '',
                'btn_link': 'https://www.doctolib.de/neurochirurgie/moenchengladbach/kasim-fischer'
            },
            {
                'city': 'Düsseldorf',
                'address': 'Schadowstraße 74, 40212 Düsseldorf',
                'phone': '',
                'hours': '',
                'services': '',
                'transport': '',
                'btn_link': '#',
                'btn_disabled': True
            }
        ]
    },
    'ru': {
        'title': 'Контакты и Филиалы',
        'desc': 'Свяжитесь с нами или посетите наши клиники в Фирсене, Мёнхенгладбахе и Дюссельдорфе.',
        'phone_lbl': 'Телефон',
        'email_lbl': 'Электронная почта',
        'hours_lbl': 'Часы работы',
        'services_lbl': 'Услуги на месте',
        'transport_lbl': 'Парковка и транспорт',
        'qr_desc': 'Отсканируйте QR-код смартфоном, чтобы сразу проложить маршрут в навигаторе.',
        'btn_text': 'Записаться через Doctolib',
        'contact_title': 'Контакт',
        'name_ph': 'Ваше имя',
        'email_ph': 'Ваш Email',
        'branch_ph': 'Выберите филиал',
        'msg_ph': 'Ваше сообщение',
        'send_btn': 'Отправить сообщение',
        'secure_disclaimer': 'Конфиденциальность: Пожалуйста, не отправляйте медицинские документы, выписки или снимки МРТ/КТ через эту форму. Для передачи конфиденциальных данных о здоровье используйте защищенный канал в разделе <a href="ru/zweitmeinung.html" style="color: var(--primary);">Второе мнение</a> или принесите их лично на прием.',
        'terminservice_title': 'Служба записи 116117',
        'terminservice_text': 'Вы можете использовать сервис Terminservice 116117 для поиска доступных приемов у профильных специалистов (Facharzttermine). Обратите внимание, что мы не можем гарантировать предоставление приема именно в нашей клинике через этот сервис.',
        'branches': [
            {
                'city': 'Фирсен (Viersen)',
                'address': 'Theodor-Heuss-Platz 10, 41747 Viersen, 4. OG (4 этаж)',
                'phone': '',
                'hours': '',
                'services': 'Консультации, диагностика, уход',
                'transport': '',
                'btn_link': 'https://www.doctolib.de/'
            },
            {
                'city': 'Мёнхенгладбах (Mönchengladbach)',
                'address': 'Bismarckstr. 106, 41061 Mönchengladbach, 3. OG (3 этаж)',
                'phone': '(02161) 678 26 83',
                'hours': 'Пн - Пт: 8:00 - 18:00',
                'services': 'Консультации, диагностика, уход',
                'transport': '',
                'btn_link': 'https://www.doctolib.de/neurochirurgie/moenchengladbach/kasim-fischer'
            },
            {
                'city': 'Дюссельдорф (Düsseldorf)',
                'address': 'Schadowstraße 74, 40212 Düsseldorf',
                'phone': '',
                'hours': '',
                'services': '',
                'transport': '',
                'btn_link': '#',
                'btn_disabled': True
            }
        ]
    },
    'tr': {
        'title': 'İletişim ve Şubeler',
        'desc': 'Bizimle iletişime geçin veya Viersen, Mönchengladbach ve Düsseldorf\'taki kliniklerimizi ziyaret edin.',
        'phone_lbl': 'Telefon',
        'email_lbl': 'E-posta',
        'hours_lbl': 'Çalışma Saatleri',
        'services_lbl': 'Yerinde Hizmetler',
        'transport_lbl': 'Otopark ve Toplu Taşıma',
        'qr_desc': 'Navigasyonu doğrudan başlatmak için QR kodunu akıllı telefonunuzla tarayın.',
        'btn_text': 'Doctolib\'den Randevu Al',
        'contact_title': 'İletişim',
        'name_ph': 'Adınız',
        'email_ph': 'E-posta adresiniz',
        'branch_ph': 'Şube Seçin',
        'msg_ph': 'Mesajınız',
        'send_btn': 'Mesajı Gönder',
        'secure_disclaimer': 'Gizlilik Uyarısı: Lütfen bu iletişim formu aracılığıyla tıbbi belgeler, doktor raporları veya MR/BT taramaları göndermeyin. Hassas sağlık verilerini göndermek için <a href="tr/zweitmeinung.html" style="color: var(--primary);">İkinci Görüş</a> bölümündeki güvenli kanalı kullanın veya randevunuza şahsen getirin.',
        'terminservice_title': '116117 Randevu Hizmeti',
        'terminservice_text': 'Müsait uzman doktor randevularını aramak için 116117 randevu hizmetini kullanabilirsiniz. Lütfen bu hizmet aracılığıyla özellikle muayenehanemizde size randevu tahsis edileceğini garanti edemediğimizi unutmayın.',
        'branches': [
            {
                'city': 'Viersen',
                'address': 'Theodor-Heuss-Platz 10, 41747 Viersen, 4. Kat',
                'phone': '',
                'hours': '',
                'services': 'Konsültasyonlar, Teşhis, Bakım',
                'transport': '',
                'btn_link': 'https://www.doctolib.de/'
            },
            {
                'city': 'Mönchengladbach',
                'address': 'Bismarckstr. 106, 41061 Mönchengladbach, 3. Kat',
                'phone': '(02161) 678 26 83',
                'hours': 'Pzt - Cum: 8:00 - 18:00',
                'services': 'Konsültasyonlar, Teşhis, Bakım',
                'transport': '',
                'btn_link': 'https://www.doctolib.de/neurochirurgie/moenchengladbach/kasim-fischer'
            },
            {
                'city': 'Düsseldorf',
                'address': 'Schadowstraße 74, 40212 Düsseldorf',
                'phone': '',
                'hours': '',
                'services': '',
                'transport': '',
                'btn_link': '#',
                'btn_disabled': True
            }
        ]
    },
    'ar': {
        'title': 'الاتصال والفروع',
        'desc': 'تواصل معنا أو قم بزيارة عياداتنا في فيرسن ومونشنغلادباخ ودوسلدورف.',
        'phone_lbl': 'هاتف',
        'email_lbl': 'البريد الإلكتروني',
        'hours_lbl': 'ساعات العمل',
        'services_lbl': 'الخدمات في الموقع',
        'transport_lbl': 'موقف السيارات والمواصلات العامة',
        'qr_desc': 'قم بمسح رمز الاستجابة السريعة بهاتفك الذكي لبدء التنقل مباشرة.',
        'btn_text': 'حجز عبر Doctolib',
        'contact_title': 'اتصل بنا',
        'name_ph': 'الاسم',
        'email_ph': 'البريد الإلكتروني',
        'branch_ph': 'اختر الفرع',
        'msg_ph': 'رسالتك',
        'send_btn': 'إرسال الرسالة',
        'secure_disclaimer': 'إشعار الخصوصية: يرجى عدم إرسال السجلات الطبية أو خطابات الطبيب أو فحوصات التصوير بالرنين المغناطيسي / الأشعة المقطعية عبر نموذج الاتصال هذا. لإرسال البيانات الصحية الحساسة، يرجى استخدام القناة الآمنة في قسم <a href="ar/zweitmeinung.html" style="color: var(--primary);">الرأي الثاني</a> أو إحضارها شخصيًا إلى موعدك.',
        'terminservice_title': 'خدمة المواعيد 116117',
        'terminservice_text': 'يمكنك استخدام خدمة المواعيد 116117 للبحث عن مواعيد الأطباء المتخصصين المتاحة. يرجى ملاحظة أنه لا يمكننا ضمان تخصيص موعد لك في عيادتنا بشكل خاص من خلال هذه الخدمة.',
        'branches': [
            {
                'city': 'فيرسن (Viersen)',
                'address': 'Theodor-Heuss-Platz 10, 41747 Viersen, 4. OG',
                'phone': '',
                'hours': '',
                'services': 'استشارات، تشخيص، رعاية',
                'transport': '',
                'btn_link': 'https://www.doctolib.de/'
            },
            {
                'city': 'مونشنغلادباخ (Mönchengladbach)',
                'address': 'Bismarckstr. 106, 41061 Mönchengladbach, 3. OG',
                'phone': '(02161) 678 26 83',
                'hours': 'الإثنين - الجمعة: 8:00 ص - 6:00 م',
                'services': 'استشارات، تشخيص، رعاية',
                'transport': '',
                'btn_link': 'https://www.doctolib.de/neurochirurgie/moenchengladbach/kasim-fischer'
            },
            {
                'city': 'دوسلدورف (Düsseldorf)',
                'address': 'Schadowstraße 74, 40212 Düsseldorf',
                'phone': '',
                'hours': '',
                'services': '',
                'transport': '',
                'btn_link': '#',
                'btn_disabled': True
            }
        ]
    }
}

import json
cms_branches = []
if os.path.exists('cms_data.json'):
    try:
        with open('cms_data.json', 'r', encoding='utf-8') as f:
            cms_data = json.load(f)
            cms_branches = cms_data.get('branches', [])
    except:
        pass

for lang, lang_data in data.items():
    if cms_branches:
        new_branches = []
        lang_code = lang if lang != '.' else 'de'
        for b in sorted(cms_branches, key=lambda x: x.get('order', 0)):
            c = b.get('city', {})
            a = b.get('address', {})
            h = b.get('hours', {})
            s = b.get('services', {})
            t = b.get('transport', {})
            
            new_branch = {}
            new_branch['city'] = c.get(lang_code, c.get('de', ''))
            new_branch['address'] = a.get(lang_code, a.get('de', ''))
            new_branch['phone'] = b.get('phone', '') if type(b.get('phone')) == str else b.get('phone', {}).get('de', '')
            new_branch['hours'] = h.get(lang_code, h.get('de', ''))
            new_branch['services'] = s.get(lang_code, s.get('de', ''))
            new_branch['transport'] = t.get(lang_code, t.get('de', ''))
            
            btn_link = b.get('btn_link', '') if type(b.get('btn_link')) == str else b.get('btn_link', {}).get('de', '')
            new_branch['btn_link'] = btn_link if btn_link else '#'
            new_branch['btn_disabled'] = not btn_link
            
            new_branches.append(new_branch)
        lang_data['branches'] = new_branches
        
    file_path = f"{lang}/sprechzeiten.html" if lang != '.' else "sprechzeiten.html"
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    match_hero = re.search(r'<div class="hero-main".*?>', content)
    if not match_hero:
        continue
        
    hero_start = match_hero.start()
        
    hero_end = content.find('</div>\n  </div>\n\n  <div class="section-wrapper">', hero_start)
    if hero_end == -1:
        hero_end = content.find('</div>\n  </div>\n  <div class="section-wrapper">', hero_start)
        
    if hero_end == -1:
        hero_end = content.find('</div>\n      </div>\n    </div>\n', hero_start)
        if hero_end != -1:
            hero_end = hero_end + len('</div>\n      </div>\n    </div>\n')
    else:
        hero_end = hero_end + len('</div>\n  </div>\n')
        
    footer_start = content.find('<footer class="footer-wrapper">')
    if footer_start == -1:
        footer_start = content.find('<footer>')
    
    if hero_start == -1 or footer_start == -1:
        continue

    new_hero = f'''<div class="hero-main">
          <h1 class="hero-title" style="font-size: 4rem;">{lang_data["title"]}</h1>
          <p class="hero-desc">{lang_data["desc"]}</p>
        </div>
      </div>
    </div>
  </div>'''
        
    # Replace relative links dynamically based on lang
    zweitmeinung_url = "zweitmeinung.html" if lang == "." else f"../{lang}/zweitmeinung.html"
    secure_disclaimer_html = lang_data["secure_disclaimer"].replace('href="zweitmeinung.html"', f'href="{zweitmeinung_url}"')
    secure_disclaimer_html = secure_disclaimer_html.replace('href="en/zweitmeinung.html"', f'href="{zweitmeinung_url}"')
    secure_disclaimer_html = secure_disclaimer_html.replace('href="ru/zweitmeinung.html"', f'href="{zweitmeinung_url}"')
    secure_disclaimer_html = secure_disclaimer_html.replace('href="tr/zweitmeinung.html"', f'href="{zweitmeinung_url}"')
    secure_disclaimer_html = secure_disclaimer_html.replace('href="ar/zweitmeinung.html"', f'href="{zweitmeinung_url}"')

    new_body = f'''
  <style>
    .contact-top-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      margin-bottom: 80px;
      align-items: stretch;
    }}
    .contact-form-container {{
      background: white;
      border: 1px solid rgba(0,0,0,0.05);
      border-radius: 16px;
      padding: 40px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.03);
      height: 100%;
      display: flex;
      flex-direction: column;
    }}
    .contact-form {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .contact-info-container {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      height: 100%;
    }}
    .contact-info-card {{
      background: #f8f9fa;
      border-radius: 12px;
      padding: 24px;
      display: flex;
      align-items: center;
      gap: 20px;
      transition: all 0.3s ease;
      flex: 1;
    }}
    .contact-info-card:hover {{
      background: #f1f3f5;
    }}
    .ci-icon-wrapper {{
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: rgba(28, 194, 178, 0.15);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--primary);
    }}
    .ci-content h4 {{
      font-size: 0.9rem;
      color: var(--text-light);
      margin: 0 0 4px 0;
      font-weight: 600;
    }}
    .ci-content p {{
      font-size: 1.1rem;
      color: var(--text-dark);
      margin: 0;
      font-weight: 700;
    }}
    
    .branch-card {{
      background: white;
      border: 1px solid rgba(0,0,0,0.05);
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 10px 40px rgba(0,0,0,0.04);
      margin-bottom: 60px;
      display: flex;
      flex-direction: row;
    }}
    .branch-info {{
      padding: 40px;
      flex: 1;
      display: flex;
      flex-direction: column;
    }}
    .branch-visuals {{
      flex: 1;
      background: #f8f9fa;
      display: flex;
      flex-direction: column;
      border-left: 1px solid rgba(0,0,0,0.05);
    }}
    .branch-map {{
      width: 100%;
      height: 300px;
      border: none;
    }}
    .branch-qr-section {{
      padding: 32px;
      display: flex;
      align-items: center;
      gap: 24px;
      background: rgba(28, 194, 178, 0.05);
      flex: 1;
    }}
    .branch-qr-img {{
      width: 120px;
      height: 120px;
      background: white;
      padding: 8px;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }}
    .branch-title {{
      font-size: 2.2rem;
      font-weight: 800;
      color: var(--text-dark);
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .info-row {{
      display: flex;
      align-items: flex-start;
      gap: 16px;
      margin-bottom: 20px;
    }}
    .info-icon {{
      color: var(--primary);
      margin-top: 2px;
    }}
    .info-content h4 {{
      font-size: 0.9rem;
      color: var(--text-light);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 4px;
      font-weight: 600;
    }}
    .info-content p {{
      color: var(--text-dark);
      font-size: 1.05rem;
      line-height: 1.5;
      margin: 0;
      font-weight: 500;
    }}
    
    @media(max-width: 992px) {{
      .contact-top-grid {{
        grid-template-columns: 1fr;
      }}
      .branch-card {{
        flex-direction: column;
      }}
      .branch-visuals {{
        border-left: none;
        border-top: 1px solid rgba(0,0,0,0.05);
      }}
      .branch-qr-section {{
        flex-direction: column;
        text-align: center;
      }}
    }}
  </style>

  <div class="section-wrapper">
    <section class="container" style="padding-top: 80px; padding-bottom: 40px; max-width: 1400px;">
      
      <!-- TOP SECTION: FORM + CONTACT INFO -->
      <div class="contact-top-grid">
        <!-- LEFT: FORM -->
        <div class="contact-form-container">
          <h2 class="section-title" style="font-size: 2.2rem; margin-bottom: 32px;">{lang_data["contact_title"]}</h2>
          
          <form id="contact-form" onsubmit="sendEmail(event)" class="contact-form">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
              <input type="text" id="user_name" name="user_name" required class="form-input" placeholder="{lang_data["name_ph"]}" style="padding: 16px; border-radius: 8px; border: 1px solid #ccc; font-family: inherit;">
              <input type="email" id="user_email" name="user_email" required class="form-input" placeholder="{lang_data["email_ph"]}" style="padding: 16px; border-radius: 8px; border: 1px solid #ccc; font-family: inherit;">
            </div>
            
            <select class="form-input" style="width: 100%; padding: 16px; border-radius: 8px; border: 1px solid #ccc; font-family: inherit; background: white;">
              <option value="" disabled selected>{lang_data["branch_ph"]}</option>
              <option value="viersen">{lang_data["branches"][0]["city"]}</option>
              <option value="moenchengladbach">{lang_data["branches"][1]["city"]}</option>
              <option value="duesseldorf">{lang_data["branches"][2]["city"]}</option>
            </select>
            
            <textarea id="message" name="message" required class="form-textarea" placeholder="{lang_data["msg_ph"]}" style="flex: 1; min-height: 120px; padding: 16px; border-radius: 8px; border: 1px solid #ccc; font-family: inherit; resize: vertical;"></textarea>
            
            <!-- SECURITY DISCLAIMER -->
            <div style="font-size: 0.9rem; color: #666; margin-top: 4px; margin-bottom: 8px; line-height: 1.5;">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: text-bottom; margin-right: 4px; color: #dc3545;"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
              {secure_disclaimer_html}
            </div>

            <button type="button" class="btn-primary" style="padding: 16px 32px; font-size: 1.1rem; border: none; cursor: pointer; width: 100%;">{lang_data["send_btn"]}</button>
          </form>
        </div>
        
        <!-- RIGHT: CONTACT INFO LIST -->
        <div class="contact-info-container">
    '''
        
    for branch in lang_data['branches']:
        new_body += f'''
          <div class="contact-info-card">
            <div class="ci-icon-wrapper">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            </div>
            <div class="ci-content">
              <h4>{lang_data["phone_lbl"]} ({branch["city"]})</h4>
              <p>{branch["phone"]}</p>
            </div>
          </div>
        '''

    new_body += f'''
          <div class="contact-info-card">
            <div class="ci-icon-wrapper">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            </div>
            <div class="ci-content">
              <h4>{lang_data["email_lbl"]}</h4>
              <p>contact@my-bandscheibe.de</p>
            </div>
          </div>
        </div>
      </div>
      
      <!-- BRANCHES LIST -->
      '''
        
    for branch in lang_data['branches']:
        qr_url = get_qr_url(branch['address'])
        map_embed = get_maps_embed(branch['address'])
        
        btn_class = 'btn-primary' if not branch.get('btn_disabled') else 'btn-primary'
        btn_style = 'display: inline-block; padding: 16px 32px; font-size: 1.1rem; margin-top: auto; text-align: center;'
        if branch.get('btn_disabled'):
            btn_style += ' opacity: 0.5; cursor: not-allowed; pointer-events: none;'
            
        new_body += f'''
      <div class="branch-card">
        <div class="branch-info">
          <h2 class="branch-title">{branch["city"]}</h2>
          
          <div class="info-row">
            <div class="info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg></div>
            <div class="info-content">
              <h4>Adresse</h4>
              <p>{branch["address"]}</p>
            </div>
          </div>
          
          <div class="info-row">
            <div class="info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg></div>
            <div class="info-content">
              <h4>{lang_data["phone_lbl"]}</h4>
              <p>{branch["phone"]}</p>
            </div>
          </div>
          
          <div class="info-row">
            <div class="info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
            <div class="info-content">
              <h4>{lang_data["hours_lbl"]}</h4>
              <p>{branch["hours"]}</p>
            </div>
          </div>
          
          <div class="info-row">
            <div class="info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg></div>
            <div class="info-content">
              <h4>{lang_data["services_lbl"]}</h4>
              <p>{branch["services"]}</p>
            </div>
          </div>
          
          <div class="info-row" style="margin-bottom: 40px;">
            <div class="info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
            <div class="info-content">
              <h4>{lang_data["transport_lbl"]}</h4>
              <p>{branch["transport"]}</p>
            </div>
          </div>
          
          <a href="{branch["btn_link"]}" class="{btn_class}" style="{btn_style}" target="_blank">{lang_data["btn_text"]} &rarr;</a>
        </div>
        
        <div class="branch-visuals">
          <iframe class="branch-map" src="{map_embed}" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="branch-qr-section">
            <img src="{qr_url}" alt="QR Code Navigation" class="branch-qr-img">
            <p style="color: var(--text-dark); font-size: 0.95rem; line-height: 1.5; margin: 0; max-width: 250px;">{lang_data["qr_desc"]}</p>
          </div>
        </div>
      </div>
        '''

    new_body += f'''
      <!-- 116117 TERMINSERVICE BLOCK -->
      <div style="background: rgba(28, 194, 178, 0.05); border-left: 4px solid var(--primary); padding: 24px; border-radius: 8px; margin-bottom: 24px;">
        <h4 style="color: var(--primary); margin-bottom: 8px; font-weight: 700;">{lang_data["terminservice_title"]}</h4>
        <p style="color: var(--text-dark); margin: 0; font-size: 1.05rem;">{lang_data["terminservice_text"]}</p>
      </div>
      
    </section>
  </div>
\n\n'''

    # Ensure Doctolib Widget exists at the very end of the file, just before </body>
    doc_widget = '''
    <!-- Floating Doctolib Widget -->
    <div class="floating-doctolib">
      <div class="fd-close" onclick="this.parentElement.style.display='none'">
        <svg viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </div>
      <div class="fd-content">
        <div class="fd-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        </div>
        <div class="fd-text">
          <div class="fd-title">Termin vereinbaren</div>
          <div class="fd-desc">Buchen Sie Ihren Termin schnell und einfach online.</div>
        </div>
      </div>
      <a href="https://www.doctolib.de/neurochirurgie/moenchengladbach/kasim-fischer?utm_campaign=website-button&utm_source=kasim-fischer-website-button&utm_medium=referral&utm_content=custom&utm_term=kasim-fischer" target="_blank" class="fd-btn">Auf Doctolib buchen &rarr;</a>
      <div class="fd-secure">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        Ihre Daten sind sicher und vertraulich.
      </div>
    </div>
    '''

    new_content = content[:hero_start] + new_hero + '\n' + new_body + content[footer_start:]
    
    # If the widget was removed, append it before </body>
    if 'class="floating-doctolib"' not in new_content:
        new_content = new_content.replace('</body>', doc_widget + '\n</body>')
    
    
    if "EmailJS Integration" not in new_content:
        script_block = """
<!-- EmailJS Integration -->
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script type="text/javascript">
   (function(){
      emailjs.init({
        publicKey: "-dY76BrZbuYUmTruZ",
      });
   })();
   
   function sendEmail(e) {
      e.preventDefault();
      
      const btn = document.getElementById('submit-btn');
      const status = document.getElementById('form-status');
      
      const originalText = btn.innerHTML;
      btn.innerText = 'Senden...';
      btn.disabled = true;
      status.style.display = 'none';

      Promise.all([
        emailjs.sendForm('service_ecu13bq', 'template_bfsngtg', '#contact-form'),
        emailjs.sendForm('service_ecu13bq', 'template_uuk8onk', '#contact-form')
      ])
        .then(() => {
            btn.innerHTML = originalText;
            btn.disabled = false;
            status.style.display = 'block';
            status.style.color = '#2ecc71';
            status.innerText = 'Nachricht erfolgreich gesendet!';
            document.getElementById('contact-form').reset();
        }, (err) => {
            btn.innerHTML = originalText;
            btn.disabled = false;
            status.style.display = 'block';
            status.style.color = '#e74c3c';
            status.innerText = 'Fehler beim Senden. Bitte versuchen Sie es später noch einmal.';
            console.error('EmailJS error:', err);
        });
   }
</script>
</body>"""
        new_content = new_content.replace("</body>", script_block)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {file_path}")

print("Done updating sprechzeiten.html files.")
