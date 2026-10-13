/* =============================================
   DRUCKZENTRUM — Briefbogen A4 & Visitenkarten
   Vanilla-JS port of AdminStationeryPanel + CorporateStationerySection
   from Holding-NabiOta-Health-Group-Germany (Next.js → static admin).
   ============================================= */
(function () {
  'use strict';

  // Practice data (source: impressum.html / sprechzeiten.html)
  var practiceInfo = {
    name: 'Praxis für Neurochirurgie',
    owner: 'Dr. med. Kasim Fischer-Rahimov & Kollegen',
    ownerShort: 'Dr. med. Kasim Fischer-Rahimov',
    street: 'Bismarckstraße 106',
    postalCode: '41061',
    city: 'Mönchengladbach',
    country: 'Deutschland',
    phone: 'Tel. 02161 678 26 83',
    fax: 'Fax 02161 678 03 81',
    email: 'kontakt@my-bandscheibe.de',
    website: 'www.my-bandscheibe.de',
    chamber: 'Ärztekammer Nordrhein',
    kv: 'Kassenärztliche Vereinigung Nordrhein',
    kvShort: 'KV Nordrhein'
  };

  var LOCALES = ['de', 'ru', 'en', 'uz', 'tr'];

  var COPY = {
    title: { de: 'Geschäftsausstattung', ru: 'Фирменные материалы', en: 'Corporate stationery', tr: 'Kurumsal materyaller', ar: 'المطبوعات المؤسسية', uz: 'Korporativ materiallar' },
    intro: {
      de: 'Briefbogen und zweiseitige Visitenkarte der Praxis für Neurochirurgie Dr. Fischer-Rahimov & Kollegen.',
      ru: 'Фирменный бланк и двусторонняя визитная карточка Практики нейрохирургии д-ра Фишера-Рахимова и коллег.',
      en: 'Official letterhead and a two-sided business card for the Neurosurgery Practice Dr. Fischer-Rahimov & Colleagues.',
      tr: 'Dr. Fischer-Rahimov & Meslektaşları Nöroşirürji Muayenehanesi için resmi antetli kağıt ve çift taraflı kartvizit.',
      ar: 'ورق مراسلات رسمي وبطاقة عمل بوجهين لعيادة جراحة الأعصاب د. فيشر-رحيموف وزملاؤه.',
      uz: 'Dr. Fischer-Rahimov va hamkasblari neyroxirurgiya amaliyoti uchun rasmiy xat blanki va ikki tomonlama tashrif qog‘ozi.'
    },
    printAll: { de: 'Gesamtes Set drucken', ru: 'Печать всего комплекта', en: 'Print complete set', tr: 'Tüm seti yazdır', ar: 'طباعة المجموعة كاملة', uz: 'To‘liq to‘plamni chop etish' },
    printLetter: { de: 'Briefbogen A4 drucken', ru: 'Печать бланка A4', en: 'Print A4 letterhead', tr: 'A4 antetli kağıdı yazdır', ar: 'طباعة ورق المراسلات A4', uz: 'A4 xat blankini chop etish' },
    printCards: { de: 'Visitenkarten drucken', ru: 'Печать визиток', en: 'Print business cards', tr: 'Kartvizitleri yazdır', ar: 'طباعة بطاقات العمل', uz: 'Tashrif qog‘ozlarini chop etish' },
    printHint: {
      de: 'Drucken oder als PDF speichern. Visitenkarten beidseitig auf A4 drucken, an der langen Kante wenden und entlang der gestrichelten Linien ausschneiden.',
      ru: 'Откроется окно печати или сохранения в PDF. Визитки печатаются с двух сторон на листах A4: выберите переворот по длинному краю и обрежьте по пунктирной линии.',
      en: 'Choose a printer or Save as PDF. Print the cards double-sided on A4, flip on the long edge, then cut along the dashed lines.',
      tr: 'Yazıcıyı veya PDF olarak kaydetmeyi seçin. Kartvizitleri A4\'e çift taraflı, uzun kenardan çevirmeli yazdırın ve kesikli çizgilerden kesin.',
      ar: 'اختر الطابعة أو الحفظ بصيغة PDF. اطبع البطاقات على الوجهين بحجم A4 مع التقليب على الحافة الطويلة، ثم قصها على الخطوط المتقطعة.',
      uz: 'Printer yoki PDF sifatida saqlashni tanlang. Tashrif qog‘ozlarini A4 da ikki tomonlama, uzun chetidan aylantirib chop eting va punktir chiziqlardan kesing.'
    },
    letterLabel: { de: 'Briefbogen · A4', ru: 'Фирменный бланк · A4', en: 'Letterhead · A4', tr: 'Antetli kağıt · A4', ar: 'ورق مراسلات · A4', uz: 'Xat blanki · A4' },
    cardFront: { de: 'Visitenkarte · Vorderseite', ru: 'Визитка · лицевая сторона', en: 'Business card · front', tr: 'Kartvizit · ön yüz', ar: 'بطاقة العمل · الوجه الأمامي', uz: 'Tashrif qog‘ozi · old tomoni' },
    cardBack: { de: 'Visitenkarte · Rückseite', ru: 'Визитка · оборотная сторона', en: 'Business card · reverse', tr: 'Kartvizit · arka yüz', ar: 'بطاقة العمل · الوجه الخلفي', uz: 'Tashrif qog‘ozi · orqa tomoni' },
    orgLabel: { de: 'Praxis für Neurochirurgie', ru: 'Практика нейрохирургии', en: 'Neurosurgery Practice', tr: 'Nöroşirürji Muayenehanesi', ar: 'عيادة جراحة الأعصاب', uz: 'Neyroxirurgiya amaliyoti' },
    recipient: { de: 'Empfänger', ru: 'Получатель', en: 'Recipient', tr: 'Alıcı', ar: 'المستلم', uz: 'Qabul qiluvchi' },
    date: { de: 'Datum', ru: 'Дата', en: 'Date', tr: 'Tarih', ar: 'التاريخ', uz: 'Sana' },
    subject: { de: 'Betreff', ru: 'Тема', en: 'Subject', tr: 'Konu', ar: 'الموضوع', uz: 'Mavzu' },
    pageCount: {
      de: 'Komplettset · 4 A4-Seiten inklusive Trennseite für Duplexdruck · 8 Visitenkarten',
      ru: 'Полный комплект · 4 страницы A4, включая разделитель для двусторонней печати · 8 визиток',
      en: 'Complete set · 4 A4 pages including a duplex separator · 8 business cards',
      tr: 'Tam set · çift taraflı baskı ayıracı dahil 4 A4 sayfa · 8 kartvizit',
      ar: 'المجموعة كاملة · 4 صفحات A4 مع فاصل للطباعة على الوجهين · 8 بطاقات',
      uz: 'To‘liq to‘plam · ikki tomonlama chop uchun ajratgich bilan 4 ta A4 sahifa · 8 ta tashrif qog‘ozi'
    }
  };

  var PRINTER_ICON = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>';
  var GLOBE_ICON = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>';

  var state = { locale: 'de', mount: null };

  function esc(value) {
    return String(value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function t(key) {
    var entry = COPY[key];
    return esc(entry[state.locale] || entry.de);
  }

  // Port of <Logo variant size />
  function logo(variant, size) {
    return '<div class="stn-logo stn-logo--' + variant + ' stn-logo--' + size + '" aria-label="NabiOta Health Group Germany">' +
      '<img src="../img/nLogo.svg" alt="NabiOta Health Group Germany Emblem">' +
      '<div class="stn-logo-text"><span class="stn-logo-brand">NABIOTA</span><span class="stn-logo-sub">HEALTH GROUP GERMANY</span></div>' +
      '</div>';
  }

  function renderCard(side, print) {
    var p = practiceInfo;
    var cls = 'stationery-card-face stationery-card-' + side + (print ? ' stationery-card-print' : '');
    if (side === 'front') {
      return '<div class="' + cls + '">' +
        logo('dark', 'sm') +
        '<div class="stationery-card-front-name"><span>' + t('orgLabel') + '</span><strong>' + esc(p.owner) + '</strong></div>' +
        '<span class="stationery-card-gold-line"></span>' +
        '</div>';
    }
    return '<div class="' + cls + '">' +
      '<p class="stationery-card-back-company">' + esc(p.name) + '<br>' + esc(p.owner) + '</p>' +
      '<div class="stationery-card-back-details">' +
      '<span>' + esc(p.street) + '</span>' +
      '<span>' + esc(p.postalCode + ' ' + p.city) + '</span>' +
      '<span>' + esc(p.phone) + '</span>' +
      '<span>' + esc(p.email) + '</span>' +
      '<span>' + esc(p.website) + '</span>' +
      '</div>' +
      '<span class="stationery-card-gold-line"></span>' +
      '</div>';
  }

  function printCardSheet(side) {
    var cells = '';
    for (var i = 0; i < 8; i++) {
      cells += '<div class="stationery-print-card-cut">' + renderCard(side, true) + '</div>';
    }
    return '<div class="stationery-print-sheet stationery-print-card-sheet" data-print-document="card-' + side + '">' + cells + '</div>';
  }

  function renderLocaleSwitch() {
    var buttons = LOCALES.map(function (l) {
      return '<button type="button" class="stn-locale-btn' + (l === state.locale ? ' active' : '') + '" data-stn-locale="' + l + '">' + l + '</button>';
    }).join('');
    return '<div class="stn-locale-switch">' + GLOBE_ICON + '<span class="stn-locale-label">Sprache:</span>' + buttons + '</div>';
  }

  function renderScreen() {
    var p = practiceInfo;
    return '' +
      '<div class="stn-module-head">' +
        '<div>' +
          '<div class="stn-module-title">' + PRINTER_ICON.replace('width="16" height="16"', 'width="20" height="20"') + '<span>Druckzentrum · Briefbogen &amp; Visitenkarten</span></div>' +
          '<p class="stn-module-sub">Erstellen und drucken Sie offizielle A4-Briefbögen und doppelseitige Visitenkarten der Praxis.</p>' +
        '</div>' +
        renderLocaleSwitch() +
      '</div>' +
      '<div class="stn-module-card">' +
        '<section class="nabiota-stationery-screen">' +
          '<div class="stn-glow"></div>' +
          '<div class="stn-container">' +
            '<div class="stn-head">' +
              '<h2 class="stn-title">' + t('title') + '</h2>' +
              '<p class="stn-intro">' + t('intro') + '</p>' +
              '<div class="stn-actions">' +
                '<button type="button" id="stnPrintAll" class="stn-btn stn-btn--primary" data-stn-print="all">' + PRINTER_ICON + t('printAll') + '</button>' +
                '<button type="button" id="stnPrintLetter" class="stn-btn" data-stn-print="letter">' + PRINTER_ICON + t('printLetter') + '</button>' +
                '<button type="button" id="stnPrintCards" class="stn-btn" data-stn-print="cards">' + PRINTER_ICON + t('printCards') + '</button>' +
              '</div>' +
              '<p class="stn-hint">' + t('printHint') + '</p>' +
            '</div>' +
            '<div class="stn-grid">' +
              '<div class="stn-col">' +
                '<div class="stationery-letter-preview">' +
                  '<div class="stn-lp-head">' + logo('light', 'md') +
                    '<div class="stn-lp-legal"><p>' + esc(p.name) + '</p><p>' + esc(p.ownerShort) + '</p><p>' + esc(p.street) + '</p><p>' + esc(p.postalCode + ' ' + p.city) + '</p></div>' +
                  '</div>' +
                  '<div class="stn-lp-sender"><span>' + esc(p.street + ' · ' + p.postalCode + ' ' + p.city) + '</span><span>' + esc(p.website) + '</span></div>' +
                  '<div class="stn-lp-lines"><div class="stn-lp-line" style="width:60%"></div><div class="stn-lp-line" style="width:40%"></div></div>' +
                  '<div class="stn-lp-subject">' + t('subject') + '</div>' +
                  '<div class="stn-lp-lines stn-lp-lines--body">' +
                    '<div class="stn-lp-line" style="width:100%"></div><div class="stn-lp-line" style="width:100%"></div>' +
                    '<div class="stn-lp-line" style="width:92%"></div><div class="stn-lp-line" style="width:96%"></div><div class="stn-lp-line" style="width:70%"></div>' +
                  '</div>' +
                  '<div class="stn-lp-footer">' +
                    '<div class="stn-lp-footer-row"><span>' + esc(p.phone) + '</span><span>' + esc(p.email) + '</span><span>' + esc(p.website) + '</span></div>' +
                    '<p>' + esc(p.chamber + ' · ' + p.kvShort) + '</p>' +
                  '</div>' +
                  '<div class="stn-lp-gold"></div>' +
                '</div>' +
                '<p class="stn-caption">' + t('letterLabel') + '</p>' +
              '</div>' +
              '<div class="stn-col stn-col--cards">' +
                '<div>' + renderCard('front') + '<p class="stn-caption">' + t('cardFront') + '</p></div>' +
                '<div>' + renderCard('back') + '<p class="stn-caption">' + t('cardBack') + '</p></div>' +
              '</div>' +
            '</div>' +
            '<p class="stn-pagecount">' + t('pageCount') + '</p>' +
          '</div>' +
        '</section>' +
      '</div>';
  }

  // Equivalent of the createPortal(..., document.body) print source
  function renderPrintRoot() {
    var p = practiceInfo;
    var root = document.getElementById('nabiota-stationery-print-root');
    if (!root) {
      root = document.createElement('div');
      root.id = 'nabiota-stationery-print-root';
      root.className = 'stationery-print-source';
      root.setAttribute('aria-hidden', 'true');
      document.body.appendChild(root);
    }
    root.innerHTML = '' +
      '<div class="stationery-print-sheet stationery-print-letter" data-print-document="letter">' +
        '<header class="stationery-print-letter-header">' + logo('light', 'md') +
          '<div class="stationery-print-legal">' +
            '<strong>' + esc(p.name) + '</strong>' +
            '<span>' + esc(p.owner) + '</span>' +
            '<span>' + esc(p.street) + '</span>' +
            '<span>' + esc(p.postalCode + ' ' + p.city + ', ' + p.country) + '</span>' +
          '</div>' +
        '</header>' +
        '<div class="stationery-print-sender-line">' + esc(p.name + ' · ' + p.street + ' · ' + p.postalCode + ' ' + p.city) + '</div>' +
        '<div class="stationery-print-recipient">' + t('recipient') + '</div>' +
        '<div class="stationery-print-date">' + t('date') + ': ____________________</div>' +
        '<div class="stationery-print-body"><span>' + t('subject') + ':</span></div>' +
        '<footer class="stationery-print-letter-footer">' +
          '<div><strong>' + esc(p.name) + '</strong><span>' + esc(p.ownerShort) + '</span><span>' + esc(p.street) + '</span><span>' + esc(p.postalCode + ' ' + p.city + ', ' + p.country) + '</span></div>' +
          '<div><strong>Kontakt</strong><span>' + esc(p.phone) + '</span><span>' + esc(p.fax) + '</span><span>' + esc(p.email) + '</span><span>' + esc(p.website) + '</span></div>' +
          '<div><strong>Berufsaufsicht</strong><span>' + esc(p.chamber) + '</span><span>' + esc(p.kv) + '</span><span>Tersteegenstraße 9, 40474 Düsseldorf</span></div>' +
        '</footer>' +
        '<div class="stationery-print-gold-rule"></div>' +
      '</div>' +
      '<div class="stationery-print-sheet stationery-print-blank" data-print-document="blank"></div>' +
      printCardSheet('front') +
      printCardSheet('back');
  }

  function printSet(target) {
    var clearTarget = function () {
      delete document.body.dataset.nabiotaStationeryPrint;
      window.removeEventListener('afterprint', clearTarget);
    };
    document.body.dataset.nabiotaStationeryPrint = target;
    window.addEventListener('afterprint', clearTarget, { once: true });
    window.requestAnimationFrame(function () { window.print(); });
  }

  function render() {
    if (!state.mount) return;
    state.mount.innerHTML = renderScreen();
    renderPrintRoot();
  }

  function init(mountId) {
    state.mount = document.getElementById(mountId || 'stationeryMount');
    if (!state.mount) return;
    state.mount.addEventListener('click', function (e) {
      var localeBtn = e.target.closest('[data-stn-locale]');
      if (localeBtn) {
        state.locale = localeBtn.getAttribute('data-stn-locale');
        render();
        return;
      }
      var printBtn = e.target.closest('[data-stn-print]');
      if (printBtn) printSet(printBtn.getAttribute('data-stn-print'));
    });
    render();
  }

  window.NabiotaStationery = { init: init, print: printSet };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { init(); });
  } else {
    init();
  }
})();
