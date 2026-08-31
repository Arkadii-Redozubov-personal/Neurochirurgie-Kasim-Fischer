import os, re

# Data structure for Behandlungen (13 items, 5 languages, neutral wording)
data = {
    '.': {
        'intro_title': 'Behandlungen & Operationen',
        'intro_text': '<p style="margin-bottom: 20px;">Unser Leistungsspektrum umfasst spezialisierte konservative und operative Verfahren. Jede Behandlung wird nach ausführlicher Diagnostik individuell auf Ihre medizinische Indikation abgestimmt.</p>',
        'learn_more': 'Mehr erfahren &rarr;',
        'items': [
            {'title': 'Mikrochirurgische Bandscheibenoperationen', 'desc': 'Operative Entlastung von Nervenstrukturen.', 'full_desc': 'Ziel des Eingriffs ist die Entfernung von vorgefallenem Bandscheibenmaterial unter Einsatz eines Operationsmikroskops, um komprimierte Nervenwurzeln zu entlasten.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>'},
            {'title': 'Endoskopische/minimalinvasive Bandscheibenchirurgie', 'desc': 'Gewebe- und muskelschonende Eingriffe.', 'full_desc': 'Über kleine Zugänge und mit Hilfe spezieller Endoskope wird Bandscheibenmaterial entfernt. Diese Technik zielt darauf ab, die umgebende Muskulatur möglichst wenig zu irritieren.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="4"></circle></svg>'},
            {'title': 'Dekompressionsoperationen bei Spinalkanalstenosen', 'desc': 'Erweiterung des verengten Wirbelkanals.', 'full_desc': 'Bei einer Verengung des Spinalkanals wird durch die operative Abtragung von Knochen- und Bandstrukturen mehr Raum für das Rückenmark und die Nervenwurzeln geschaffen.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 3.5l6 6-12 12h-6v-6z"></path><path d="M12 8l4 4"></path></svg>'},
            {'title': 'Operationen bei Neuroforamenstenosen', 'desc': 'Erweiterung der Nervenaustrittslöcher.', 'full_desc': 'Eine gezielte operative Erweiterung der Neuroforamina (Nervenaustrittslöcher) dient dazu, den mechanischen Druck von der entsprechenden Nervenwurzel zu nehmen.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v4l3 3"></path></svg>'},
            {'title': 'Stabilisationsoperationen', 'desc': 'Wiederherstellung der Wirbelsäulenstabilität.', 'full_desc': 'Bei Instabilitäten (z.B. Wirbelgleiten) werden benachbarte Wirbelkörper durch spezielle Implantatsysteme miteinander verbunden, um abnormale Bewegungen zu unterbinden.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg>'},
            {'title': 'Bandscheibenprothetik', 'desc': 'Implantation künstlicher Bandscheiben.', 'full_desc': 'Nach Entfernung einer degenerierten Bandscheibe kann unter bestimmten medizinischen Voraussetzungen eine Prothese eingesetzt werden, mit dem Ziel, die Beweglichkeit des entsprechenden Segments zu erhalten.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M8 12h8"></path><path d="M12 8v8"></path></svg>'},
            {'title': 'Kyphoplastie / Vertebroplastie', 'desc': 'Behandlung von Wirbelkörperfrakturen.', 'full_desc': 'Durch das Einbringen von medizinischem Knochenzement in den gebrochenen Wirbelkörper soll dieser stabilisiert und die frakturbedingten Schmerzen reduziert werden.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>'},
            {'title': 'Operationen bei Karpaltunnel / Sulcus ulnaris', 'desc': 'Entlastung peripherer Nervenengpässe.', 'full_desc': 'Bei Nervenkompressionssyndromen an der Hand oder am Ellenbogen wird durch Spaltung des einengenden Bandes oder Gewebes der Druck auf den betroffenen Nerven verringert.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path></svg>'},
            {'title': 'Rekonstruktion peripherer Nervenschäden', 'desc': 'Mikrochirurgische Wiederherstellung von Nerven.', 'full_desc': 'Nach traumatischen Läsionen können periphere Nerven durch mikrochirurgische Nähte oder Nerventransplantate adaptiert werden, um die Voraussetzung für eine mögliche Regeneration zu schaffen.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"></path></svg>'},
            {'title': 'Interventionelle Schmerztherapie', 'desc': 'Gezielte Injektionsbehandlungen.', 'full_desc': 'Minimalinvasive Applikation von entzündungshemmenden und schmerzlindernden Medikamenten direkt an die betroffenen Nervenwurzeln oder Wirbelgelenke unter bildgebender Kontrolle.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>'},
            {'title': 'Radiofrequenztherapie', 'desc': 'Thermische Denervierung zur Schmerzbehandlung.', 'full_desc': 'Durch Applikation von Wärmeenergie an spezifischen Nervenfasern (z.B. an den Facettengelenken) wird die Schmerzweiterleitung temporär oder längerfristig unterbrochen.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.5 19c2.5-2 2.5-6 0-8M21.5 22c4.5-4 4.5-11 0-15M6.5 19c-2.5-2-2.5-6 0-8M2.5 22c-4.5-4-4.5-11 0-15M12 15v6"></path><circle cx="12" cy="11" r="4"></circle></svg>'},
            {'title': 'Neuromodulation / Spinal Cord Stimulation', 'desc': 'Elektrische Stimulation des Rückenmarks.', 'full_desc': 'Bei chronischen, therapierefraktären Schmerzsyndromen werden Elektroden im Epiduralraum platziert. Leichte elektrische Impulse überlagern die Schmerzsignale auf dem Weg zum Gehirn.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>'},
            {'title': 'Tumor-/Metastasenchirurgie an Wirbelsäule und Nerven', 'desc': 'Operative Behandlung onkologischer Befunde.', 'full_desc': 'Mikrochirurgische Resektion von Tumoren oder Metastasen im Bereich der Wirbelsäule oder peripherer Nerven. Je nach Befund erfolgt dies in Kombination mit stabilisierenden Maßnahmen.', 'icon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>'}
        ]
    },
    'en': {
        'intro_title': 'Treatments & Surgeries',
        'intro_text': '<p style="margin-bottom: 20px;">Our range of services includes specialized conservative and surgical procedures. Each treatment is tailored individually to your medical indication after thorough diagnosis.</p>',
        'learn_more': 'Learn more &rarr;',
        'items': [
            {'title': 'Microsurgical Disc Operations', 'desc': 'Surgical decompression of nerve structures.', 'full_desc': 'The aim of the procedure is to remove herniated disc material using an operating microscope to relieve compressed nerve roots.'},
            {'title': 'Endoscopic/Minimally Invasive Disc Surgery', 'desc': 'Tissue- and muscle-sparing procedures.', 'full_desc': 'Disc material is removed through small incisions using special endoscopes. This technique aims to minimize irritation to the surrounding musculature.'},
            {'title': 'Decompression Surgery for Spinal Canal Stenosis', 'desc': 'Widening of the narrowed spinal canal.', 'full_desc': 'In the case of spinal canal stenosis, more space is created for the spinal cord and nerve roots through the surgical removal of bone and ligament structures.'},
            {'title': 'Surgeries for Neuroforaminal Stenosis', 'desc': 'Widening of the nerve exit holes.', 'full_desc': 'A targeted surgical widening of the neuroforamina (nerve exit holes) serves to relieve the mechanical pressure from the respective nerve root.'},
            {'title': 'Stabilization Surgeries', 'desc': 'Restoration of spinal stability.', 'full_desc': 'In cases of instability (e.g., spondylolisthesis), adjacent vertebral bodies are connected to each other using special implant systems to prevent abnormal movements.'},
            {'title': 'Disc Prosthetics', 'desc': 'Implantation of artificial discs.', 'full_desc': 'After removal of a degenerated disc, a prosthesis can be inserted under certain medical conditions with the aim of maintaining the mobility of the respective segment.'},
            {'title': 'Kyphoplasty / Vertebroplasty', 'desc': 'Treatment of vertebral body fractures.', 'full_desc': 'By introducing medical bone cement into the fractured vertebral body, it aims to stabilize it and reduce fracture-related pain.'},
            {'title': 'Surgeries for Carpal Tunnel / Cubital Tunnel', 'desc': 'Relief of peripheral nerve bottlenecks.', 'full_desc': 'For nerve compression syndromes in the hand or elbow, the pressure on the affected nerve is reduced by splitting the constricting ligament or tissue.'},
            {'title': 'Reconstruction of Peripheral Nerve Damage', 'desc': 'Microsurgical restoration of nerves.', 'full_desc': 'After traumatic lesions, peripheral nerves can be adapted using microsurgical sutures or nerve grafts to create the prerequisite for possible regeneration.'},
            {'title': 'Interventional Pain Therapy', 'desc': 'Targeted injection treatments.', 'full_desc': 'Minimally invasive application of anti-inflammatory and pain-relieving medications directly to the affected nerve roots or vertebral joints under imaging control.'},
            {'title': 'Radiofrequency Therapy', 'desc': 'Thermal denervation for pain treatment.', 'full_desc': 'By applying thermal energy to specific nerve fibers (e.g., at the facet joints), the transmission of pain is temporarily or longer-term interrupted.'},
            {'title': 'Neuromodulation / Spinal Cord Stimulation', 'desc': 'Electrical stimulation of the spinal cord.', 'full_desc': 'In chronic, therapy-refractory pain syndromes, electrodes are placed in the epidural space. Mild electrical impulses overlay the pain signals on their way to the brain.'},
            {'title': 'Tumor/Metastasis Surgery on the Spine and Nerves', 'desc': 'Surgical treatment of oncological findings.', 'full_desc': 'Microsurgical resection of tumors or metastases in the spine or peripheral nerves. Depending on the findings, this is done in combination with stabilizing measures.'}
        ]
    },
    'ru': {
        'intro_title': 'Лечение и операции',
        'intro_text': '<p style="margin-bottom: 20px;">Спектр наших услуг включает специализированные консервативные и хирургические процедуры. Каждое лечение подбирается индивидуально в соответствии с вашими медицинскими показаниями после тщательной диагностики.</p>',
        'learn_more': 'Узнать больше &rarr;',
        'items': [
            {'title': 'Микрохирургические операции на дисках', 'desc': 'Хирургическая декомпрессия нервных структур.', 'full_desc': 'Цель процедуры — удаление выпавшего материала диска с использованием операционного микроскопа для снятия давления с компрессированных нервных корешков.'},
            {'title': 'Эндоскопическая/минимально инвазивная хирургия дисков', 'desc': 'Щадящие для тканей и мышц процедуры.', 'full_desc': 'Материал диска удаляется через небольшие разрезы с помощью специальных эндоскопов. Эта техника направлена на минимальное раздражение окружающей мускулатуры.'},
            {'title': 'Декомпрессионные операции при стенозе спинномозгового канала', 'desc': 'Расширение суженного спинномозгового канала.', 'full_desc': 'При сужении спинномозгового канала создается больше пространства для спинного мозга и нервных корешков путем хирургического удаления костных и связочных структур.'},
            {'title': 'Операции при фораминальном стенозе', 'desc': 'Расширение отверстий выхода нервов.', 'full_desc': 'Целенаправленное хирургическое расширение нейрофораминальных отверстий (мест выхода нервов) служит для снятия механического давления с соответствующего нервного корешка.'},
            {'title': 'Стабилизирующие операции', 'desc': 'Восстановление стабильности позвоночника.', 'full_desc': 'В случаях нестабильности (например, при спондилолистезе) смежные тела позвонков соединяются друг с другом с помощью специальных систем имплантатов для предотвращения аномальных движений.'},
            {'title': 'Протезирование межпозвонковых дисков', 'desc': 'Имплантация искусственных дисков.', 'full_desc': 'После удаления дегенерированного диска при определенных медицинских показаниях может быть установлен протез с целью сохранения подвижности соответствующего сегмента.'},
            {'title': 'Кифопластика / Вертебропластика', 'desc': 'Лечение переломов тел позвонков.', 'full_desc': 'Путем введения медицинского костного цемента в сломанное тело позвонка достигается его стабилизация и уменьшение боли, связанной с переломом.'},
            {'title': 'Операции при синдроме карпального / кубитального канала', 'desc': 'Снятие компрессии периферических нервов.', 'full_desc': 'При синдромах компрессии нервов кисти или локтя давление на пораженный нерв снижается путем рассечения сдавливающей связки или ткани.'},
            {'title': 'Реконструкция повреждений периферических нервов', 'desc': 'Микрохирургическое восстановление нервов.', 'full_desc': 'После травматических повреждений периферические нервы могут быть адаптированы с помощью микрохирургических швов или нервных трансплантатов для создания условий возможной регенерации.'},
            {'title': 'Интервенционная терапия боли', 'desc': 'Целенаправленные инъекционные процедуры.', 'full_desc': 'Минимально инвазивное введение противовоспалительных и обезболивающих препаратов непосредственно в область пораженных нервных корешков или суставов позвоночника под визуальным контролем.'},
            {'title': 'Радиочастотная терапия', 'desc': 'Термическая денервация для лечения боли.', 'full_desc': 'Путем приложения тепловой энергии к специфическим нервным волокнам (например, в фасеточных суставах) временно или на длительный срок прерывается передача болевых импульсов.'},
            {'title': 'Нейромодуляция / Стимуляция спинного мозга (SCS)', 'desc': 'Электрическая стимуляция спинного мозга.', 'full_desc': 'При хронических болевых синдромах, не поддающихся терапии, в эпидуральное пространство устанавливаются электроды. Легкие электрические импульсы перекрывают болевые сигналы на их пути к мозгу.'},
            {'title': 'Хирургия опухолей и метастазов позвоночника и нервов', 'desc': 'Хирургическое лечение онкологических заболеваний.', 'full_desc': 'Микрохирургическая резекция опухолей или метастазов в области позвоночника или периферических нервов. В зависимости от показаний это делается в сочетании со стабилизирующими мерами.'}
        ]
    },
    'tr': {
        'intro_title': 'Tedaviler ve Ameliyatlar',
        'intro_text': '<p style="margin-bottom: 20px;">Hizmet yelpazemiz özelleşmiş konservatif ve cerrahi prosedürleri içerir. Her tedavi, kapsamlı bir teşhis sonrasında tıbbi endikasyonunuza göre bireysel olarak uyarlanır.</p>',
        'learn_more': 'Daha fazla bilgi &rarr;',
        'items': [
            {'title': 'Mikrocerrahi Disk Operasyonları', 'desc': 'Sinir yapılarının cerrahi dekompresyonu.', 'full_desc': 'Prosedürün amacı, sıkışmış sinir köklerini rahatlatmak için bir ameliyat mikroskobu kullanarak fıtıklaşmış disk materyalini çıkarmaktır.'},
            {'title': 'Endoskopik/Minimal İnvaziv Disk Cerrahisi', 'desc': 'Doku ve kas koruyucu prosedürler.', 'full_desc': 'Disk materyali, özel endoskoplar kullanılarak küçük kesilerle çıkarılır. Bu teknik, çevredeki kasların tahrişini en aza indirmeyi amaçlar.'},
            {'title': 'Spinal Kanal Stenozu için Dekompresyon Cerrahisi', 'desc': 'Daralan spinal kanalın genişletilmesi.', 'full_desc': 'Spinal kanal stenozu durumunda, kemik ve bağ yapılarının cerrahi olarak çıkarılmasıyla omurilik ve sinir kökleri için daha fazla alan yaratılır.'},
            {'title': 'Nöroforaminal Stenoz Ameliyatları', 'desc': 'Sinir çıkış deliklerinin genişletilmesi.', 'full_desc': 'Nöroforaminanın (sinir çıkış delikleri) hedefe yönelik cerrahi olarak genişletilmesi, ilgili sinir kökü üzerindeki mekanik baskıyı hafifletmeye yarar.'},
            {'title': 'Stabilizasyon Ameliyatları', 'desc': 'Omurga stabilitesinin restorasyonu.', 'full_desc': 'İnstabilite durumlarında (örn. spondilolistezis), anormal hareketleri önlemek için özel implant sistemleri kullanılarak komşu omur gövdeleri birbirine bağlanır.'},
            {'title': 'Disk Protezleri', 'desc': 'Yapay disklerin implantasyonu.', 'full_desc': 'Dejenere olmuş bir diskin çıkarılmasından sonra, ilgili segmentin hareketliliğini korumak amacıyla belirli tıbbi koşullar altında bir protez yerleştirilebilir.'},
            {'title': 'Kifoplasti / Vertebroplasti', 'desc': 'Omurga kırıklarının tedavisi.', 'full_desc': 'Kırık omur gövdesine tıbbi kemik çimentosu enjekte edilerek stabilize edilmesi ve kırığa bağlı ağrının azaltılması amaçlanır.'},
            {'title': 'Karpal Tünel / Kübital Tünel Ameliyatları', 'desc': 'Periferik sinir sıkışmalarının rahatlatılması.', 'full_desc': 'El veya dirsekteki sinir sıkışması sendromlarında, daraltan bağ veya dokunun kesilmesiyle etkilenen sinir üzerindeki baskı azaltılır.'},
            {'title': 'Periferik Sinir Hasarının Rekonstrüksiyonu', 'desc': 'Sinirlerin mikrocerrahi restorasyonu.', 'full_desc': 'Travmatik lezyonlardan sonra periferik sinirler, olası yenilenme için ön koşulu oluşturmak üzere mikrocerrahi sütürler veya sinir greftleri kullanılarak adapte edilebilir.'},
            {'title': 'Girişimsel Ağrı Tıbbı', 'desc': 'Hedefe yönelik enjeksiyon tedavileri.', 'full_desc': 'Görüntüleme kontrolü altında doğrudan etkilenen sinir köklerine veya omurga eklemlerine anti-enflamatuar ve ağrı kesici ilaçların minimal invaziv uygulaması.'},
            {'title': 'Radyofrekans Terapisi', 'desc': 'Ağrı tedavisi için termal denervasyon.', 'full_desc': 'Belirli sinir liflerine (örneğin faset eklemlerdeki) termal enerji uygulanarak, ağrı iletimi geçici veya daha uzun süreli olarak kesilir.'},
            {'title': 'Nöromodülasyon / Omurilik Stimülasyonu', 'desc': 'Omuriliğin elektriksel stimülasyonu.', 'full_desc': 'Kronik, tedaviye dirençli ağrı sendromlarında epidural boşluğa elektrotlar yerleştirilir. Hafif elektrik uyarıları, beyne giden ağrı sinyallerini baskılar.'},
            {'title': 'Omurga ve Sinirlerde Tümör/Metastaz Cerrahisi', 'desc': 'Onkolojik bulguların cerrahi tedavisi.', 'full_desc': 'Omurga veya periferik sinirlerdeki tümör veya metastazların mikrocerrahi rezeksiyonu. Bulgulara bağlı olarak bu işlem stabilize edici önlemlerle birlikte yapılır.'}
        ]
    },
    'ar': {
        'intro_title': 'العلاجات والعمليات الجراحية',
        'intro_text': '<p style="margin-bottom: 20px;">تشمل مجموعة خدماتنا إجراءات تحفظية وجراحية متخصصة. يتم تصميم كل علاج بشكل فردي وفقًا لدواعييك الطبية بعد التشخيص الدقيق.</p>',
        'learn_more': 'اعرف المزيد &rarr;',
        'items': [
            {'title': 'عمليات الديسك بالجراحة المجهرية', 'desc': 'إزالة الضغط الجراحي عن الهياكل العصبية.', 'full_desc': 'الهدف من الإجراء هو إزالة مادة القرص المنفتق باستخدام مجهر جراحي لتخفيف الضغط عن جذور الأعصاب.'},
            {'title': 'جراحة الديسك بالمنظار/طفيفة التوغل', 'desc': 'إجراءات تحافظ على الأنسجة والعضلات.', 'full_desc': 'يتم إزالة مادة القرص من خلال شقوق صغيرة باستخدام مناظير خاصة. تهدف هذه التقنية إلى تقليل تهيج العضلات المحيطة.'},
            {'title': 'جراحة تخفيف الضغط لتضيق القناة الشوكية', 'desc': 'توسيع القناة الشوكية الضيقة.', 'full_desc': 'في حالة تضيق القناة الشوكية، يتم توفير مساحة أكبر للحبل الشوكي وجذور الأعصاب من خلال الإزالة الجراحية للعظام والأربطة.'},
            {'title': 'عمليات تضيق الثقبة العصبية', 'desc': 'توسيع ثقوب خروج الأعصاب.', 'full_desc': 'يساعد التوسيع الجراحي الموجه للثقبة العصبية (ثقوب خروج العصب) على تخفيف الضغط الميكانيكي عن جذر العصب المعني.'},
            {'title': 'عمليات التثبيت', 'desc': 'استعادة استقرار العمود الفقري.', 'full_desc': 'في حالات عدم الاستقرار (مثل انزلاق الفقار)، يتم ربط الأجسام الفقرية المتجاورة ببعضها باستخدام أنظمة زرع خاصة لمنع الحركات غير الطبيعية.'},
            {'title': 'الأطراف الصناعية للأقراص', 'desc': 'زرع أقراص صناعية.', 'full_desc': 'بعد إزالة القرص المنحط، يمكن إدخال طرف صناعي في ظل ظروف طبية معينة بهدف الحفاظ على حركة الجزء المعني.'},
            {'title': 'رأب الحدبة / رأب الفقرات', 'desc': 'علاج كسور الأجسام الفقرية.', 'full_desc': 'من خلال إدخال أسمنت العظام الطبي في جسم الفقرة المكسورة، يهدف الإجراء إلى تثبيته وتقليل الألم المرتبط بالكسر.'},
            {'title': 'عمليات النفق الرسغي / النفق المرفقي', 'desc': 'تخفيف اختناقات الأعصاب المحيطية.', 'full_desc': 'في متلازمات انضغاط العصب في اليد أو المرفق، يتم تقليل الضغط على العصب المصاب عن طريق شق الرباط أو النسيج المضيق.'},
            {'title': 'إعادة بناء تلف الأعصاب المحيطية', 'desc': 'استعادة الأعصاب بالجراحة المجهرية.', 'full_desc': 'بعد الآفات الرضحية، يمكن تكييف الأعصاب المحيطية باستخدام خيوط الجراحة المجهرية أو الطعوم العصبية لخلق شرط أساسي للتجدد المحتمل.'},
            {'title': 'علاج الألم التداخلي', 'desc': 'علاجات الحقن الموجهة.', 'full_desc': 'تطبيق طفيف التوغل للأدوية المضادة للالتهابات والمسكنة للألم مباشرة على جذور الأعصاب أو مفاصل العمود الفقري المصابة تحت إشراف التصوير.'},
            {'title': 'العلاج بالترددات الراديوية', 'desc': 'استئصال العصب الحراري لعلاج الألم.', 'full_desc': 'من خلال تطبيق الطاقة الحرارية على ألياف عصبية معينة (مثل مفاصل الوجه)، يتم إيقاف انتقال الألم مؤقتًا أو لفترة أطول.'},
            {'title': 'التعديل العصبي / تحفيز الحبل الشوكي', 'desc': 'التحفيز الكهربائي للحبل الشوكي.', 'full_desc': 'في متلازمات الألم المزمنة المقاومة للعلاج، يتم وضع أقطاب كهربائية في الحيز فوق الجافية. تتداخل النبضات الكهربائية الخفيفة مع إشارات الألم في طريقها إلى الدماغ.'},
            {'title': 'جراحة الأورام/النقائل في العمود الفقري والأعصاب', 'desc': 'العلاج الجراحي للنتائج المتعلقة بالأورام.', 'full_desc': 'الاستئصال المجهري للأورام أو النقائل في العمود الفقري أو الأعصاب المحيطية. اعتمادًا على النتائج، يتم ذلك بالاقتران مع تدابير الاستقرار.'}
        ]
    }
}

# Copy icons from DE to other languages where missing
for lang in ['en', 'ru', 'tr', 'ar']:
    for i, item in enumerate(data['.']['items']):
        data[lang]['items'][i]['icon'] = item['icon']

for lang, lang_data in data.items():
    file_path = f"{lang}/behandlungen.html" if lang != '.' else "behandlungen.html"
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the treatment grid
    grid_start = content.find('<div class="treatment-grid">')
    if grid_start == -1:
        print(f"Skipping {file_path}, grid not found")
        continue
        
    grid_end = content.find('</section>', grid_start)
    if grid_end == -1:
        grid_end = content.find('</div>\n  </div>\n  <footer', grid_start)
        
    if grid_end == -1:
        print(f"Skipping {file_path}, grid end not found")
        continue
        
    # Generate new HTML for the grid
    new_html = '<div class="treatment-grid">\n'
      
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
        
    new_html += '\n      </div>'
    
    # Also update the section title and text if possible
    # We find '<h2 class="section-title"' before grid_start
    h2_idx = content.rfind('<h2 class="section-title"', 0, grid_start)
    if h2_idx != -1:
        # Find closing tag of h2
        h2_close = content.find('</h2>', h2_idx)
        if h2_close != -1:
            # Reconstruct the h2
            h2_start_tag = content[h2_idx:content.find('>', h2_idx)+1]
            # Replace the title
            content = content[:content.find('>', h2_idx)+1] + lang_data['intro_title'] + content[h2_close:]
            
            # Now update the <p> after h2
            # It's <p style="...">
            p_idx = content.find('<p style="', h2_close)
            if p_idx != -1 and p_idx < grid_start:
                p_close = content.find('</p>', p_idx)
                if p_close != -1:
                    # Replace the entire p tag
                    content = content[:p_idx] + lang_data['intro_text'] + content[p_close+4:]
    
    # Recalculate grid_start and grid_end after content length changed
    grid_start = content.find('<div class="treatment-grid">')
    # The end of the grid is a bit tricky, let's find the closing div of the grid
    # It should be followed by </section>
    grid_end = content.find('</section>', grid_start)
    
    if grid_start != -1 and grid_end != -1:
        new_content = content[:grid_start] + new_html + content[grid_end:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Failed to replace grid in {file_path}")

print("Done updating behandlungen.html files.")
