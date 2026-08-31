import os, re

data = {
    '.': {
        'intro_title': 'Diagnostik',
        'intro_text': '<p style="margin-bottom: 20px;">Eine exakte Diagnose ist der erste Schritt zu einer erfolgreichen Behandlung. Wir setzen auf modernste Verfahren und eine enge interdisziplinäre Zusammenarbeit.</p>',
        'learn_more': 'Mehr erfahren &rarr;',
        'items': [
            {
                'title': 'Klinische Diagnostik',
                'desc': 'Umfassende neurochirurgische und neurologische Untersuchung sowie Schmerzbeurteilung.',
                'full_desc': 'Am Anfang jeder Behandlung steht ein ausführliches Anamnesegespräch sowie eine sorgfältige neurochirurgische und neurologische Untersuchung. Wir beurteilen Ihre Schmerzsituation detailliert, prüfen Reflexe, Sensibilität und motorische Funktionen, um die genaue Ursache Ihrer Beschwerden zu lokalisieren.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>'
            },
            {
                'title': 'Neurophysiologie',
                'desc': 'Präzise Messung der Nerven- und Muskelfunktion (EMG, ENG, NLG, SEP).',
                'full_desc': 'Mit modernen neurophysiologischen Methoden (wie Elektromyografie - EMG, Elektroneurografie - ENG, Nervenleitgeschwindigkeit - NLG und somatosensibel evozierte Potenziale - SEP) können wir die Leitfähigkeit und Funktionsfähigkeit Ihrer Nerven und Muskeln objektiv messen. So lassen sich Nervenschädigungen exakt lokalisieren.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>'
            },
            {
                'title': 'Bildgebung',
                'desc': 'Spezialisierte Auswertung von MRT, CT und Röntgenbildern in enger radiologischer Kooperation.',
                'full_desc': 'Wir arbeiten eng mit spezialisierten radiologischen Zentren zusammen. Wir werten Ihre MRT-, CT- oder Röntgenbilder gemeinsam mit Ihnen detailliert aus. Durch diese kooperative Netzwerkarbeit mit der Radiologie gewährleisten wir höchste diagnostische Präzision und schnelle Terminvergaben für bildgebende Verfahren.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>'
            },
            {
                'title': 'Spezielle Diagnostik',
                'desc': 'Gezielte Untersuchungen für Bandscheibe, Stenosen, Nervenkompressionen und Zweitmeinungen.',
                'full_desc': 'Bei komplexen Krankheitsbildern wie Bandscheibenvorfällen, Spinalkanalstenosen oder unklaren Nervenkompressionen führen wir eine spezifische Schmerzdiagnostik durch. Zudem bieten wir eine fundierte fachärztliche Zweitmeinung an, insbesondere wenn Ihnen andernorts zu einer Operation geraten wurde.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'
            }
        ]
    },
    'en': {
        'intro_title': 'Diagnostics',
        'intro_text': '<p style="margin-bottom: 20px;">An accurate diagnosis is the first step to successful treatment. We rely on state-of-the-art procedures and close interdisciplinary cooperation.</p>',
        'learn_more': 'Learn more &rarr;',
        'items': [
            {
                'title': 'Clinical Diagnostics',
                'desc': 'Comprehensive neurosurgical and neurological examination and pain assessment.',
                'full_desc': 'Every treatment begins with a detailed medical history and a careful neurosurgical and neurological examination. We assess your pain situation in detail, test reflexes, sensitivity, and motor functions to pinpoint the exact cause of your symptoms.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>'
            },
            {
                'title': 'Neurophysiology',
                'desc': 'Precise measurement of nerve and muscle function (EMG, ENG, NLG, SEP).',
                'full_desc': 'With modern neurophysiological methods (such as electromyography - EMG, electroneurography - ENG, nerve conduction velocity - NLG, and somatosensory evoked potentials - SEP), we can objectively measure the conductivity and functionality of your nerves and muscles. This allows nerve damage to be localized precisely.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>'
            },
            {
                'title': 'Imaging',
                'desc': 'Specialized evaluation of MRI, CT, and X-ray images in close radiological cooperation.',
                'full_desc': 'We work closely with specialized radiological centers. We evaluate your MRI, CT, or X-ray images together with you in detail. Through this cooperative network with radiology, we ensure the highest diagnostic precision and fast appointment scheduling for imaging procedures.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>'
            },
            {
                'title': 'Specialized Diagnostics',
                'desc': 'Targeted examinations for intervertebral discs, stenosis, nerve compressions, and second opinions.',
                'full_desc': 'For complex conditions such as herniated discs, spinal canal stenosis, or unclear nerve compressions, we perform specific pain diagnostics. In addition, we offer a well-founded specialist second opinion, especially if you have been advised to have surgery elsewhere.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'
            }
        ]
    },
    'ru': {
        'intro_title': 'Диагностика',
        'intro_text': '<p style="margin-bottom: 20px;">Точный диагноз — это первый шаг к успешному лечению. Мы опираемся на самые современные методы и тесное междисциплинарное сотрудничество.</p>',
        'learn_more': 'Узнать больше &rarr;',
        'items': [
            {
                'title': 'Клиническая диагностика',
                'desc': 'Комплексное нейрохирургическое и неврологическое обследование, оценка боли.',
                'full_desc': 'Любое лечение начинается с подробного сбора анамнеза и тщательного нейрохирургического и неврологического обследования. Мы детально оцениваем болевой синдром, проверяем рефлексы, чувствительность и моторные функции, чтобы точно установить причину ваших жалоб.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>'
            },
            {
                'title': 'Нейрофизиология',
                'desc': 'Точное измерение функции нервов и мышц (ЭМГ, ЭНГ, СРВ, ССВП).',
                'full_desc': 'С помощью современных нейрофизиологических методов (таких как электромиография - ЭМГ, электронейрография - ЭНГ, скорость распространения возбуждения - СРВ и соматосенсорные вызванные потенциалы - ССВП) мы можем объективно измерить проводимость и функциональность ваших нервов и мышц. Это позволяет точно локализовать повреждение нерва.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>'
            },
            {
                'title': 'Визуализация',
                'desc': 'Специализированная оценка МРТ, КТ и рентгеновских снимков в сотрудничестве с радиологией.',
                'full_desc': 'Мы тесно сотрудничаем со специализированными радиологическими центрами. Мы детально анализируем ваши снимки МРТ, КТ или рентген вместе с вами. Благодаря такому сотрудничеству с радиологией мы обеспечиваем высочайшую диагностическую точность и быстрое назначение времени для исследований.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>'
            },
            {
                'title': 'Специальная диагностика',
                'desc': 'Целенаправленные обследования позвоночника, стенозов, компрессии нервов и второе мнение.',
                'full_desc': 'При сложных клинических картинах, таких как грыжа межпозвоночного диска, стеноз спинномозгового канала или неясная компрессия нервов, мы проводим специфическую диагностику боли. Кроме того, мы предлагаем обоснованное второе мнение специалиста, особенно если вам рекомендовали операцию в другом месте.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'
            }
        ]
    },
    'tr': {
        'intro_title': 'Teşhis',
        'intro_text': '<p style="margin-bottom: 20px;">Doğru teşhis, başarılı bir tedavinin ilk adımıdır. En modern yöntemlere ve disiplinler arası yakın işbirliğine güveniyoruz.</p>',
        'learn_more': 'Daha fazla bilgi &rarr;',
        'items': [
            {
                'title': 'Klinik Teşhis',
                'desc': 'Kapsamlı nöroşirürjik ve nörolojik muayene ve ağrı değerlendirmesi.',
                'full_desc': 'Her tedavi, ayrıntılı bir tıbbi öykü ve dikkatli bir nöroşirürjik ve nörolojik muayene ile başlar. Şikayetlerinizin kesin nedenini belirlemek için ağrı durumunuzu ayrıntılı olarak değerlendiriyor, refleksleri, hassasiyeti ve motor fonksiyonları test ediyoruz.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>'
            },
            {
                'title': 'Nörofizyoloji',
                'desc': 'Sinir ve kas fonksiyonunun hassas ölçümü (EMG, ENG, NLG, SEP).',
                'full_desc': 'Modern nörofizyolojik yöntemlerle (elektromiyografi - EMG, elektronörografi - ENG, sinir iletim hızı - NLG ve somatosensori uyarılmış potansiyeller - SEP gibi), sinirlerinizin ve kaslarınızın iletkenliğini ve işlevselliğini nesnel olarak ölçebiliriz. Bu, sinir hasarının tam olarak lokalize edilmesini sağlar.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>'
            },
            {
                'title': 'Görüntüleme',
                'desc': 'Radyoloji ile yakın işbirliği içinde MR, BT ve röntgen görüntülerinin uzman değerlendirmesi.',
                'full_desc': 'Uzmanlaşmış radyoloji merkezleriyle yakın çalışıyoruz. MR, BT veya röntgen görüntülerinizi sizinle birlikte ayrıntılı olarak değerlendiriyoruz. Radyoloji ile bu kooperatif ağ sayesinde, görüntüleme prosedürleri için en yüksek tanısal kesinliği ve hızlı randevu planlamasını sağlıyoruz.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>'
            },
            {
                'title': 'Özel Teşhis',
                'desc': 'Fıtıklar, stenozlar, sinir sıkışmaları ve ikinci görüşler için hedefe yönelik muayeneler.',
                'full_desc': 'Bel fıtığı, spinal kanal stenozu veya belirsiz sinir sıkışmaları gibi karmaşık durumlar için spesifik ağrı teşhisi yapıyoruz. Ek olarak, özellikle başka bir yerde ameliyat olmanız tavsiye edildiyse, sağlam temellere dayanan bir uzman ikinci görüşü sunuyoruz.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'
            }
        ]
    },
    'ar': {
        'intro_title': 'التشخيص',
        'intro_text': '<p style="margin-bottom: 20px;">التشخيص الدقيق هو الخطوة الأولى لعلاج ناجح. نحن نعتمد على أحدث الإجراءات والتعاون الوثيق بين التخصصات.</p>',
        'learn_more': 'اعرف المزيد &rarr;',
        'items': [
            {
                'title': 'التشخيص السريري',
                'desc': 'فحص جراحة الأعصاب والأعصاب الشامل وتقييم الألم.',
                'full_desc': 'يبدأ كل علاج بتاريخ طبي مفصل وفحص دقيق لجراحة الأعصاب والأعصاب. نحن نقيم حالة الألم لديك بالتفصيل، ونختبر ردود الفعل، والحساسية، والوظائف الحركية لتحديد السبب الدقيق للأعراض.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>'
            },
            {
                'title': 'الفيزيولوجيا العصبية',
                'desc': 'القياس الدقيق لوظيفة الأعصاب والعضلات (EMG, ENG, NLG, SEP).',
                'full_desc': 'باستخدام الأساليب الفيزيولوجية العصبية الحديثة (مثل تخطيط كهربية العضل، وتخطيط كهربية الأعصاب، وسرعة التوصيل العصبي، والجهد المحرض الحسي الجسدي)، يمكننا قياس موصلية ووظيفة أعصابك وعضلاتك بشكل موضوعي. هذا يسمح بتحديد تلف الأعصاب بدقة.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>'
            },
            {
                'title': 'التصوير',
                'desc': 'التقييم المتخصص لصور الرنين المغناطيسي، والأشعة المقطعية، والأشعة السينية بالتعاون الوثيق مع قسم الأشعة.',
                'full_desc': 'نحن نعمل بشكل وثيق مع مراكز الأشعة المتخصصة. نقوم بتقييم صور الرنين المغناطيسي أو الأشعة المقطعية أو الأشعة السينية معًا بالتفصيل. من خلال هذه الشبكة التعاونية مع الأشعة، نضمن أعلى درجات الدقة التشخيصية وتحديد المواعيد السريعة لإجراءات التصوير.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>'
            },
            {
                'title': 'التشخيص المتخصص',
                'desc': 'فحوصات مستهدفة للأقراص الفقرية، والتضيق، وانضغاط الأعصاب، والآراء الثانية.',
                'full_desc': 'في الحالات المعقدة مثل الانزلاق الغضروفي، أو تضيق القناة الشوكية، أو انضغاط الأعصاب غير الواضح، نقوم بإجراء تشخيص محدد للألم. بالإضافة إلى ذلك، نقدم رأيًا ثانيًا متخصصًا ومبنيًا على أسس سليمة، خاصة إذا نُصحت بإجراء عملية جراحية في مكان آخر.',
                'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'
            }
        ]
    }
}

for lang, lang_data in data.items():
    file_path = f"{lang}/diagnostik.html" if lang != '.' else "diagnostik.html"
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the section-wrapper which wraps the grid
    start_str = 'class="section-wrapper"'
    start_idx = content.find(start_str)
    if start_idx == -1:
        continue
        
    # We want to replace everything from <div style="display: flex; gap: 60px; margin-bottom: 80px; ...">
    # up to the end of the <div class="treatment-grid">
    # Then there is <!-- Bottom Feature Row 4 Cols --> which we can keep.
    
    split_start = content.find('<!-- Split Overview -->', start_idx)
    if split_start == -1:
        # Fallback if comment is missing
        split_start = content.find('<div style="display: flex; gap: 60px;', start_idx)
        
    if split_start == -1:
        continue
        
    bottom_feature_start = content.find('<!-- Bottom Feature Row 4 Cols -->', split_start)
    if bottom_feature_start == -1:
        bottom_feature_start = content.find('<div class="feature-row-4"', split_start)
        
    if bottom_feature_start == -1:
        continue
        
    # Generate new HTML
    new_html = f'''<!-- Split Overview -->
      <div style="display: flex; gap: 60px; margin-bottom: 80px; flex-wrap: wrap; margin-top: 40px;">
        <div style="flex: 1; min-width: 300px;">
          <h2 class="section-title" style="font-size: 2.5rem; max-width: 400px; margin-top: 16px;">{lang_data["intro_title"]}</h2>
        </div>
        <div style="flex: 1; min-width: 300px; color: var(--text-light); line-height: 1.8; font-size: 1.05rem;">
          {lang_data["intro_text"]}
        </div>
      </div>
      
      <div class="treatment-grid">'''
      
    for item in lang_data['items']:
        new_html += f'''
        <div class="treatment-card">
          <div class="treatment-icon-wrap">{item["icon"]}</div>
          <div class="treatment-content">
            <h3 class="treatment-title">{item["title"]}</h3>
            <p class="treatment-desc">{item["desc"]}</p>
            <div class="treatment-full-desc" style="display: none;">
              {item["full_desc"]}
            </div>
            <a href="javascript:void(0)" class="treatment-link" onclick="openTreatmentModal(this)">{lang_data["learn_more"]}</a>
          </div>
        </div>'''
        
    new_html += '''
      </div>
      
      '''
      
    # Replace content
    new_content = content[:split_start] + new_html + content[bottom_feature_start:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {file_path}")

print("Done updating diagnostik.html files.")
