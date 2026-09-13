import re
import os

langs = {
    'de': {
        'path': 'index.html',
        '15+': '15+',
        'title': 'Herzlich willkommen in unserer Praxis',
        'text': 'Wir freuen uns, Sie in unseren Sprechstunden für Neurochirurgie-, Wirbelsäulenchirurgie-, psychosomatische- und Schmerztherapie begrüßen zu dürfen.<br><br>Ihre Gesundheit, Ihr Wohlbefinden und Ihr Vertrauen stehen für uns im Mittelpunkt. Wir nehmen uns Zeit für Ihre Beschwerden, hören Ihnen aufmerksam zu und suchen gemeinsam mit Ihnen nach der für Sie bestmöglichen Behandlung.<br><br>Dabei setzen wir auf fachliche Kompetenz, moderne Diagnostik und Therapie sowie eine persönliche und menschliche Betreuung.<br><br>Denn bei uns steht nicht nur die Erkrankung im Mittelpunkt, sondern der Mensch.<br><strong>Ihre Gesundheit liegt uns am Herzen.</strong>'
    },
    'en': {
        'path': 'en/index.html',
        '15+': '15+',
        'title': 'Welcome to our practice',
        'text': 'We look forward to welcoming you to our consultations for neurosurgery, spinal surgery, psychosomatic medicine, and pain therapy.<br><br>Your health, well-being, and trust are our central focus. We take the time for your complaints, listen to you carefully, and work with you to find the best possible treatment.<br><br>We rely on professional competence, modern diagnostics and therapy, as well as personal and humane care.<br><br>Because with us, the focus is not only on the illness, but on the person.<br><strong>Your health is close to our hearts.</strong>'
    },
    'ru': {
        'path': 'ru/index.html',
        '15+': '15+',
        'title': 'Добро пожаловать в нашу практику',
        'text': 'Мы рады приветствовать Вас на наших консультациях по нейрохирургии, хирургии позвоночника, психосоматической медицине и терапии боли.<br><br>Ваше здоровье, хорошее самочувствие и доверие находятся для нас на первом месте. Мы уделяем время Вашим жалобам, внимательно Вас выслушиваем и вместе с Вами ищем оптимальный вариант лечения.<br><br>В своей работе мы опираемся на профессиональную компетентность, современные методы диагностики и лечения, а также индивидуальный и человечный подход к каждому пациенту.<br><br>В центре нашего внимания находится не только заболевание, но прежде всего сам человек.<br><strong>Ваше здоровье нам небезразлично.</strong>'
    },
    'tr': {
        'path': 'tr/index.html',
        '15+': '15+',
        'title': 'Kliniğimize hoş geldiniz',
        'text': 'Sizi nöroşirürji, omurga cerrahisi, psikosomatik tıp ve ağrı tedavisi konsültasyonlarımızda ağırlamaktan mutluluk duyarız.<br><br>Sağlığınız, esenliğiniz ve güveniniz bizim için odak noktasıdır. Şikayetlerinize zaman ayırıyor, sizi dikkatle dinliyor ve sizin için en iyi tedaviyi birlikte arıyoruz.<br><br>Mesleki yetkinliğe, modern teşhis ve tedaviye, ayrıca kişisel ve insani bakıma güveniyoruz.<br><br>Çünkü bizde sadece hastalık değil, insan da odak noktasıdır.<br><strong>Sağlığınız bizim için önemlidir.</strong>'
    },
    'ar': {
        'path': 'ar/index.html',
        '15+': '15+',
        'title': 'مرحبًا بكم في عيادتنا',
        'text': 'يسعدنا أن نرحب بكم في استشاراتنا لجراحة الأعصاب وجراحة العمود الفقري والطب النفسي الجسدي وعلاج الألم.<br><br>صحتك ورفاهيتك وثقتك هي محور اهتمامنا. نأخذ وقتًا لشكاويك، ونستمع إليك بعناية ونبحث معك عن أفضل علاج ممكن لك.<br><br>نحن نعتمد على الكفاءة المهنية والتشخيص والعلاج الحديث، فضلاً عن الرعاية الشخصية والإنسانية.<br><br>لأنه معنا لا ينصب التركيز على المرض فحسب، بل على الإنسان.<br><strong>صحتك تهمنا.</strong>'
    }
}

for lang, data in langs.items():
    filepath = data['path']
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace 15+ with 25+
    content = re.sub(r'(<span class="trusted-stat-number">)15\+(</span>)', r'\g<1>25+\g<2>', content)

    # Replace the welcome text
    # The title is in an h2 tag with class "about-title fade-in"
    pattern = r'(<h2 class="about-title fade-in"[^>]*>)(.*?)(</h2>\s*<p[^>]*>.*?</p>\s*<p[^>]*>.*?</p>)'
    
    match = re.search(pattern, content, flags=re.DOTALL)
    if match:
        new_block = f'{match.group(1)}{data["title"]}</h2>\n      <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-light); margin-bottom: 40px; max-width: 860px;">{data["text"]}</p>'
        content = content[:match.start()] + new_block + content[match.end():]
        print(f"✅ Updated {filepath}")
    else:
        print(f"❌ Could not find welcome block in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done!")
