import os, re

# 1. Update patienten.html styles
data = {
    '.': {
        'title': 'Für Patienten',
        'desc': 'Wichtige Informationen für Ihren Besuch, Ihre Operation und die Zeit danach.',
        'sec1_title': 'Ihr Behandlungspfad',
        'phases': [
            {
                'title': 'Vor dem Besuch',
                'desc': 'Um Ihre Diagnose schnellstmöglich stellen zu können, bitten wir Sie, folgende Unterlagen zu Ihrem Erstgespräch mitzubringen:',
                'list': [
                    'Aktuelle MRT- oder CT-Aufnahmen (auf CD oder digital)',
                    'Relevante Vorbefunde und Arztbriefe',
                    'Einen aktuellen Medikamentenplan',
                    'Ihre Versichertenkarte und ggf. Überweisung'
                ],
                'icon': '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'
            },
            {
                'title': 'Vor der Operation',
                'desc': 'Sollte ein operativer Eingriff notwendig sein, erhalten Sie von uns detaillierte, ärztlich freigegebene Verhaltensregeln:',
                'list': [
                    'Ausführliches Aufklärungsgespräch mit dem Operateur',
                    'Individuelle Anpassung Ihrer blutverdünnenden Medikamente',
                    'Informationen zur Nüchternheit vor der OP',
                    'Klärung aller offenen Fragen in Ruhe'
                ],
                'icon': '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>'
            },
            {
                'title': 'Nach der Operation',
                'desc': 'Der Heilungsprozess ist individuell. Wir begleiten Sie bei der Nachsorge, Rehabilitation und Wiedereingliederung:',
                'list': [
                    'Regelmäßige Wundkontrollen und Nachsorgeuntersuchungen',
                    'Planung von physiotherapeutischen Maßnahmen oder Reha',
                    'Schrittweise Wiedereingliederung in den Alltag',
                    'Jeder Heilungsverlauf ist einzigartig – wir passen die Maßnahmen an Ihren Fortschritt an.'
                ],
                'icon': '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>'
            }
        ],
        'faq_title': 'Häufig gestellte Fragen (FAQ)',
        'faq_desc': 'Hier finden Sie organisatorische und allgemeine medizinische Antworten. Bitte beachten Sie, dass diese Informationen keine ärztliche Diagnose ersetzen.',
        'faqs': [
            {'q': 'Wie schnell bekomme ich einen Termin?', 'a': 'Akutfälle werden nach Möglichkeit priorisiert. Reguläre Termine können Sie am besten bequem über unser Doctolib-System buchen.'},
            {'q': 'Benötige ich eine Überweisung?', 'a': 'Als gesetzlich Versicherter bringen Sie bitte Ihre Versichertenkarte mit. Eine Überweisung ist hilfreich, aber in der Regel nicht zwingend erforderlich. Privatpatienten und Selbstzahler benötigen keine Überweisung.'},
            {'q': 'Sind Begleitpersonen beim Termin erlaubt?', 'a': 'Selbstverständlich dürfen Sie eine Vertrauensperson zu Ihrem Gespräch mitbringen. Insbesondere bei Aufklärungsgesprächen ist dies oft hilfreich.'},
            {'q': 'Wie lange dauert die Krankschreibung nach einer OP?', 'a': 'Dies hängt stark von der Art des Eingriffs und Ihrer beruflichen Tätigkeit ab. Ihr behandelnder Arzt wird dies individuell mit Ihnen besprechen.'}
        ]
    },
    'en': {
        'title': 'For Patients',
        'desc': 'Important information for your visit, your surgery, and the time after.',
        'sec1_title': 'Your Treatment Path',
        'phases': [
            {
                'title': 'Before the Visit',
                'desc': 'To ensure a quick and precise diagnosis, please bring the following documents to your first consultation:',
                'list': [
                    'Current MRI or CT scans (on CD or digital)',
                    'Relevant previous findings and doctor\'s letters',
                    'A current medication plan',
                    'Your health insurance card and referral (if applicable)'
                ]
            },
            {
                'title': 'Before Surgery',
                'desc': 'If a surgical procedure is necessary, you will receive detailed, doctor-approved instructions from us:',
                'list': [
                    'Detailed educational consultation with the surgeon',
                    'Individual adjustment of your blood-thinning medications',
                    'Information on fasting before surgery',
                    'Clarification of all open questions in peace'
                ]
            },
            {
                'title': 'After Surgery',
                'desc': 'The healing process is individual. We accompany you through aftercare, rehabilitation, and reintegration:',
                'list': [
                    'Regular wound checks and follow-up examinations',
                    'Planning of physiotherapeutic measures or rehab',
                    'Gradual reintegration into everyday life',
                    'Every healing process is unique – we adapt the measures to your progress.'
                ]
            }
        ],
        'faq_title': 'Frequently Asked Questions (FAQ)',
        'faq_desc': 'Here you will find organizational and general medical answers. Please note that this information does not replace a medical diagnosis.',
        'faqs': [
            {'q': 'How quickly can I get an appointment?', 'a': 'Acute cases are prioritized whenever possible. Regular appointments are best booked conveniently via our Doctolib system.'},
            {'q': 'Do I need a referral?', 'a': 'As a statutorily insured patient, please bring your insurance card. A referral is helpful but generally not mandatory. Private patients and self-payers do not need a referral.'},
            {'q': 'Are accompanying persons allowed at the appointment?', 'a': 'Of course, you may bring a trusted person to your consultation. This is often particularly helpful during educational consultations.'},
            {'q': 'How long is the sick leave after surgery?', 'a': 'This depends heavily on the type of procedure and your professional activity. Your attending doctor will discuss this with you individually.'}
        ]
    },
    'ru': {
        'title': 'Пациентам',
        'desc': 'Важная информация для вашего визита, операции и периода после нее.',
        'sec1_title': 'Путь лечения',
        'phases': [
            {
                'title': 'Перед посещением',
                'desc': 'Чтобы мы могли максимально быстро поставить точный диагноз, просим вас принести на первую консультацию следующие документы:',
                'list': [
                    'Свежие снимки МРТ или КТ (на CD или в цифровом виде)',
                    'Соответствующие предыдущие заключения и выписки',
                    'Актуальный план приема медикаментов',
                    'Страховую карту и направление (если применимо)'
                ]
            },
            {
                'title': 'Перед операцией',
                'desc': 'Если потребуется хирургическое вмешательство, вы получите от нас подробные, утвержденные врачом инструкции:',
                'list': [
                    'Подробная разъяснительная беседа с хирургом',
                    'Индивидуальная корректировка приема препаратов, разжижающих кровь',
                    'Информация о режиме питания перед операцией (натощак)',
                    'Спокойное прояснение всех оставшихся вопросов'
                ]
            },
            {
                'title': 'После операции',
                'desc': 'Процесс заживления индивидуален. Мы сопровождаем вас во время последующего ухода, реабилитации и возвращения к нормальной жизни:',
                'list': [
                    'Регулярные проверки ран и контрольные осмотры',
                    'Планирование физиотерапевтических мероприятий или реабилитации',
                    'Постепенное возвращение к повседневной жизни',
                    'Каждый процесс заживления уникален — мы адаптируем меры к вашему прогрессу.'
                ]
            }
        ],
        'faq_title': 'Часто задаваемые вопросы (FAQ)',
        'faq_desc': 'Здесь вы найдете ответы на организационные и общие медицинские вопросы. Обратите внимание, что эта информация не заменяет индивидуальную врачебную диагностику.',
        'faqs': [
            {'q': 'Как быстро я смогу попасть на прием?', 'a': 'Острые случаи по возможности рассматриваются в приоритетном порядке. Обычные приемы удобнее всего бронировать через нашу систему Doctolib.'},
            {'q': 'Нужно ли мне направление?', 'a': 'Пациентам по государственной страховке необходимо принести страховую карту. Направление желательно, но, как правило, не обязательно. Частным пациентам направление не требуется.'},
            {'q': 'Можно ли прийти на прием с сопровождающим?', 'a': 'Конечно, вы можете взять с собой доверенное лицо. Это часто бывает полезно, особенно во время бесед перед операцией.'},
            {'q': 'Как долго длится больничный после операции?', 'a': 'Это сильно зависит от типа вмешательства и вашей профессиональной деятельности. Лечащий врач обсудит это с вами индивидуально.'}
        ]
    },
    'tr': {
        'title': 'Hastalar İçin',
        'desc': 'Ziyaretiniz, ameliyatınız ve sonrası için önemli bilgiler.',
        'sec1_title': 'Tedavi Süreciniz',
        'phases': [
            {
                'title': 'Ziyaretten Önce',
                'desc': 'Mümkün olan en kısa sürede doğru bir teşhis koyabilmemiz için, ilk görüşmenize lütfen aşağıdaki belgeleri getirin:',
                'list': [
                    'Güncel MR veya BT taramaları (CD\'de veya dijital)',
                    'İlgili önceki bulgular ve doktor mektupları',
                    'Güncel bir ilaç planı',
                    'Sağlık sigortası kartınız ve (varsa) sevk kağıdı'
                ]
            },
            {
                'title': 'Ameliyattan Önce',
                'desc': 'Cerrahi bir müdahale gerekiyorsa, bizden ayrıntılı, doktor onaylı talimatlar alacaksınız:',
                'list': [
                    'Cerrah ile ayrıntılı bilgilendirme görüşmesi',
                    'Kan sulandırıcı ilaçlarınızın bireysel olarak ayarlanması',
                    'Ameliyat öncesi açlık durumu hakkında bilgi',
                    'Tüm açık soruların sakin bir şekilde netleştirilmesi'
                ]
            },
            {
                'title': 'Ameliyattan Sonra',
                'desc': 'İyileşme süreci bireyseldir. Bakım, rehabilitasyon ve yeniden entegrasyon süreçlerinde size eşlik ediyoruz:',
                'list': [
                    'Düzenli yara kontrolleri ve takip muayeneleri',
                    'Fizyoterapi veya rehabilitasyon planlaması',
                    'Günlük hayata kademeli olarak dönüş',
                    'Her iyileşme süreci benzersizdir - önlemleri ilerlemenize göre uyarlıyoruz.'
                ]
            }
        ],
        'faq_title': 'Sıkça Sorulan Sorular (SSS)',
        'faq_desc': 'Burada organizasyonel ve genel tıbbi cevaplar bulacaksınız. Lütfen bu bilgilerin tıbbi bir teşhisin yerini almadığını unutmayın.',
        'faqs': [
            {'q': 'Ne kadar çabuk randevu alabilirim?', 'a': 'Acil vakalara mümkün olduğunca öncelik verilir. Düzenli randevular en rahat şekilde Doctolib sistemimiz üzerinden alınabilir.'},
            {'q': 'Sevk kağıdına ihtiyacım var mı?', 'a': 'Yasal sigortalı bir hasta olarak lütfen sigorta kartınızı getirin. Sevk kağıdı yardımcı olur ancak genellikle zorunlu değildir. Özel hastaların ve kendi ödeyenlerin sevke ihtiyacı yoktur.'},
            {'q': 'Randevuya refakatçi ile gelinebilir mi?', 'a': 'Elbette, görüşmenize güvendiğiniz bir kişiyi getirebilirsiniz. Bu, özellikle ameliyat öncesi bilgilendirme görüşmelerinde genellikle yardımcı olur.'},
            {'q': 'Ameliyattan sonra rapor süresi ne kadardır?', 'a': 'Bu büyük ölçüde prosedürün türüne ve mesleki faaliyetinize bağlıdır. Tedavi eden doktorunuz bunu sizinle bireysel olarak görüşecektir.'}
        ]
    },
    'ar': {
        'title': 'للمرضى',
        'desc': 'معلومات هامة لزيارتك، لعمليتك الجراحية وللفترة التي تليها.',
        'sec1_title': 'مسار علاجك',
        'phases': [
            {
                'title': 'قبل الزيارة',
                'desc': 'من أجل إجراء التشخيص في أسرع وقت ممكن، يرجى إحضار المستندات التالية معك إلى الاستشارة الأولى:',
                'list': [
                    'صور الرنين المغناطيسي أو المقطعية الحديثة (على قرص مضغوط أو رقمية)',
                    'النتائج السابقة وتقارير الطبيب ذات الصلة',
                    'خطة الأدوية الحالية',
                    'بطاقة التأمين الصحي الخاصة بك والتحويل (إن وجد)'
                ]
            },
            {
                'title': 'قبل الجراحة',
                'desc': 'إذا كان التدخل الجراحي ضروريًا، فستتلقى منا تعليمات مفصلة معتمدة من الطبيب:',
                'list': [
                    'استشارة تثقيفية مفصلة مع الجراح',
                    'تعديل فردي لأدوية سيولة الدم الخاصة بك',
                    'معلومات حول الصيام قبل الجراحة',
                    'توضيح جميع الأسئلة المفتوحة بهدوء'
                ]
            },
            {
                'title': 'بعد الجراحة',
                'desc': 'عملية الشفاء فردية. نحن نرافقك خلال فترة الرعاية اللاحقة وإعادة التأهيل وإعادة الإدماج:',
                'list': [
                    'فحوصات الجروح المنتظمة ومواعيد المتابعة',
                    'تخطيط إجراءات العلاج الطبيعي أو إعادة التأهيل',
                    'العودة التدريجية إلى الحياة اليومية',
                    'كل عملية شفاء فريدة من نوعها - نحن نكيف الإجراءات وفقًا لتقدمك.'
                ]
            }
        ],
        'faq_title': 'الأسئلة المتداولة (FAQ)',
        'faq_desc': 'ستجد هنا إجابات تنظيمية وطبية عامة. يرجى ملاحظة أن هذه المعلومات لا تحل محل التشخيص الطبي.',
        'faqs': [
            {'q': 'متى يمكنني الحصول على موعد؟', 'a': 'يتم إعطاء الأولوية للحالات الحادة كلما أمكن ذلك. من الأفضل حجز المواعيد العادية بسهولة عبر نظام Doctolib الخاص بنا.'},
            {'q': 'هل أحتاج إلى تحويل طبي؟', 'a': 'كمريض مؤمن عليه قانونيًا، يرجى إحضار بطاقة التأمين الخاصة بك. التحويل مفيد ولكنه ليس إلزاميًا بشكل عام. المرضى الخصوصيون والذين يدفعون بأنفسهم لا يحتاجون إلى تحويل.'},
            {'q': 'هل يُسمح بوجود مرافقين في الموعد؟', 'a': 'بالطبع، يمكنك إحضار شخص تثق به إلى استشارتك. غالبًا ما يكون هذا مفيدًا بشكل خاص أثناء الاستشارات التثقيفية.'},
            {'q': 'ما هي مدة الإجازة المرضية بعد الجراحة؟', 'a': 'هذا يعتمد بشكل كبير على نوع الإجراء ونشاطك المهني. سيناقش طبيبك المعالج هذا معك بشكل فردي.'}
        ]
    }
}

# Copy icons from DE to other languages
icons = [p['icon'] for p in data['.']['phases']]
for lang in ['en', 'ru', 'tr', 'ar']:
    for i in range(3):
        data[lang]['phases'][i]['icon'] = icons[i]

for lang, lang_data in data.items():
    file_path = f"{lang}/patienten.html" if lang != '.' else "patienten.html"
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # FIX LINKS IN NAV
    content = content.replace('href="behandlungen.html">Deutsch (DE)', 'href="patienten.html">Deutsch (DE)')
    content = content.replace('href="en/behandlungen.html">English', 'href="en/patienten.html">English')
    content = content.replace('href="ru/behandlungen.html">Ру', 'href="ru/patienten.html">Ру')
    content = content.replace('href="tr/behandlungen.html">Tü', 'href="tr/patienten.html">Tü')
    content = content.replace('href="ar/behandlungen.html">ال', 'href="ar/patienten.html">ال')
    
    content = content.replace('href="behandlungen.html" class="active">DE', 'href="patienten.html" class="active">DE')
    content = content.replace('href="en/behandlungen.html">EN', 'href="en/patienten.html">EN')
    content = content.replace('href="ru/behandlungen.html">RU', 'href="ru/patienten.html">RU')
    content = content.replace('href="tr/behandlungen.html">TR', 'href="tr/patienten.html">TR')
    content = content.replace('href="ar/behandlungen.html">AR', 'href="ar/patienten.html">AR')
        
    hero_start = content.find('<div class="hero-main">')
    if hero_start == -1:
        continue
        
    hero_end = content.find('</div>\n  </div>\n\n  <div class="section-wrapper">', hero_start)
    if hero_end == -1:
        hero_end = content.find('</div>\n  </div>\n  <div class="section-wrapper">', hero_start)
    
    footer_start = content.find('<footer class="footer-wrapper">')
    
    if hero_start == -1 or footer_start == -1:
        continue

    new_hero = f'''<div class="hero-main">
          <h1 class="hero-title" style="font-size: 4rem;">{lang_data["title"]}</h1>
          <p class="hero-desc">{lang_data["desc"]}</p>
        </div>'''
        
    new_body = f'''
  <style>
    .phase-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 32px;
      margin-bottom: 80px;
    }}
    .phase-card {{
      background: white;
      border: 1px solid rgba(0,0,0,0.05);
      border-radius: 12px;
      padding: 32px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }}
    .phase-icon {{
      margin-bottom: 24px;
      background: rgba(28, 194, 178, 0.1);
      width: 64px;
      height: 64px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .phase-title {{
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--text-dark);
      margin-bottom: 16px;
    }}
    .phase-desc {{
      color: var(--text-light);
      line-height: 1.6;
      margin-bottom: 20px;
    }}
    .phase-list {{
      list-style: none;
      padding: 0;
      margin: 0;
    }}
    .phase-list li {{
      position: relative;
      padding-left: 24px;
      margin-bottom: 12px;
      color: var(--text-dark);
      font-size: 0.95rem;
      line-height: 1.5;
    }}
    .phase-list li::before {{
      content: "•";
      color: var(--primary);
      font-weight: bold;
      position: absolute;
      left: 0;
      font-size: 1.2rem;
      top: -2px;
    }}
    
    /* FAQ styles */
    .faq-container {{
      width: 100%;
      margin: 0 auto;
    }}
    .faq-item {{
      border-bottom: 1px solid rgba(0,0,0,0.1);
      padding: 24px 0;
    }}
    .faq-q {{
      font-size: 1.2rem;
      font-weight: 600;
      color: var(--text-dark);
      margin-bottom: 12px;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .faq-q::after {{
      content: "+";
      font-size: 1.5rem;
      color: var(--primary);
    }}
    .faq-a {{
      color: var(--text-light);
      line-height: 1.6;
      display: none;
    }}
    .faq-item.active .faq-a {{
      display: block;
    }}
    .faq-item.active .faq-q::after {{
      content: "-";
    }}
  </style>

  <div class="section-wrapper">
    <section class="container" style="padding-top: 60px; padding-bottom: 80px; max-width: 1400px;">
      
      <h2 style="text-align: center; font-size: 2.2rem; margin-bottom: 40px; color: var(--text-dark);">{lang_data["sec1_title"]}</h2>
      
      <div class="phase-grid">
        '''
        
    for phase in lang_data['phases']:
        new_body += f'''
        <div class="phase-card">
          <div class="phase-icon">{phase["icon"]}</div>
          <h3 class="phase-title">{phase["title"]}</h3>
          <p class="phase-desc">{phase["desc"]}</p>
          <ul class="phase-list">
        '''
        for item in phase['list']:
            new_body += f'<li>{item}</li>\n'
            
        new_body += '''
          </ul>
        </div>
        '''
        
    new_body += f'''
      </div>

      <div class="faq-container">
        <h2 style="text-align: center; font-size: 2.2rem; margin-bottom: 16px; color: var(--text-dark);">{lang_data["faq_title"]}</h2>
        <p style="text-align: center; color: var(--text-light); margin-bottom: 40px; max-width: 800px; margin-left: auto; margin-right: auto;">{lang_data["faq_desc"]}</p>
        
        <div class="faq-list">
    '''
    
    for faq in lang_data['faqs']:
        new_body += f'''
          <div class="faq-item" onclick="this.classList.toggle('active')">
            <div class="faq-q">{faq["q"]}</div>
            <div class="faq-a">{faq["a"]}</div>
          </div>
        '''
        
    new_body += '''
        </div>
      </div>
      
    </section>
  </div>
  '''

    new_content = content[:hero_start] + new_hero + '\n      </div>\n    </div>\n  </div>\n\n' + new_body + content[footer_start:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {file_path}")

print("Done updating patienten.html files.")
