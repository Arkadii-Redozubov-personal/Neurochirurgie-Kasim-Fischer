// ── Splide Slider Initialization ────────────────────────────
document.addEventListener('DOMContentLoaded', function () {
  var el = document.querySelector('.team-splide');
  if (!el) return;

  // Detect RTL pages (Arabic)
  var isRTL = document.documentElement.dir === 'rtl' ||
              document.body.classList.contains('rtl') ||
              document.querySelector('html[dir="rtl"]') !== null;

  new Splide(el, {
    type       : 'loop',
    perPage    : 4,
    perMove    : 1,
    focus      : 0,
    gap        : '24px',
    autoplay   : true,
    interval   : 3000,
    direction  : isRTL ? 'rtl' : 'ltr',
    breakpoints: {
      1024: { perPage: 2 },
      768 : { perPage: 1 }
    }
  }).mount();
});
