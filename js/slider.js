// ── Splide Slider Initialization ────────────────────────────
// Team slider
document.addEventListener('DOMContentLoaded', function () {
    var el = document.querySelector('.team-splide');
    if(el) {
      new Splide(el, {
        type   : 'loop',
        perPage: 4,
        perMove: 1,
        focus: 0,
        gap    : '24px',
        autoplay: true,
        interval: 3000,
        breakpoints: {
          1024: { perPage: 2 },
          768 : { perPage: 1 }
        }
      }).mount();
    }
  });