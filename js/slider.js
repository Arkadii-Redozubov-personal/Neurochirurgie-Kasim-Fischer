// ── Sliders Initialization ────────────────────────────
function initAllSliders() {
  // ── Team Splide Slider ──────────────────────────────
  var el = document.querySelector('.team-splide');
  if (el && typeof Splide !== 'undefined') {
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
  }

  // ── Expertise Mobile Snap Slider ────────────────────
  initExpertiseSlider();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initAllSliders);
} else {
  initAllSliders();
}

function initExpertiseSlider() {
  var containers = document.querySelectorAll('.expertise-container');
  containers.forEach(function (container) {
    var track = container.querySelector('.expertise-grid');
    if (!track) return;

    var cards = track.querySelectorAll('.expertise-card');
    if (!cards.length) return;

    var nextBtn = container.querySelector('.expertise-slider-next');
    var dotsContainer = container.querySelector('.expertise-slider-dots');

    var isRTL = document.documentElement.dir === 'rtl' ||
                document.body.classList.contains('rtl') ||
                document.querySelector('html[dir="rtl"]') !== null;

    var dotCount = Math.max(1, Math.ceil(cards.length / 2)); // 3 dots for 6 cards

    var dots = [];
    if (dotsContainer) {
      dotsContainer.innerHTML = '';
      for (var i = 0; i < dotCount; i++) {
        var dot = document.createElement('button');
        dot.type = 'button';
        dot.className = 'expertise-slider-dot' + (i === 0 ? ' active' : '');
        dot.setAttribute('aria-label', (isRTL ? 'شريحة ' : 'Slide ') + (i + 1));
        if (i === 0) dot.setAttribute('aria-current', 'true');
        (function (idx) {
          dot.addEventListener('click', function (e) {
            e.preventDefault();
            scrollToDot(idx);
          });
        })(i);
        dotsContainer.appendChild(dot);
        dots.push(dot);
      }
    }

    var activeDot = 0;

    function updateActiveDot(idx) {
      activeDot = Math.max(0, Math.min(idx, dotCount - 1));
      dots.forEach(function (d, i) {
        if (i === activeDot) {
          d.classList.add('active');
          d.setAttribute('aria-current', 'true');
        } else {
          d.classList.remove('active');
          d.removeAttribute('aria-current');
        }
      });
    }

    function scrollToDot(idx) {
      var maxScroll = track.scrollWidth - track.clientWidth;
      if (maxScroll <= 0) return;
      var targetRatio = dotCount > 1 ? idx / (dotCount - 1) : 0;
      var targetPos = maxScroll * targetRatio;

      if (isRTL) {
        track.scrollTo({
          left: -targetPos,
          behavior: 'smooth'
        });
      } else {
        track.scrollTo({
          left: targetPos,
          behavior: 'smooth'
        });
      }
      updateActiveDot(idx);
    }

    function handleScroll() {
      var maxScroll = track.scrollWidth - track.clientWidth;
      if (maxScroll <= 0) return;
      var currentPos = Math.abs(track.scrollLeft);
      var currentRatio = Math.min(1, Math.max(0, currentPos / maxScroll));
      var computedDot = Math.round(currentRatio * (dotCount - 1));
      updateActiveDot(computedDot);
    }

    track.addEventListener('scroll', handleScroll, { passive: true });

    if (nextBtn) {
      nextBtn.addEventListener('click', function (e) {
        e.preventDefault();
        var nextIdx = activeDot >= dotCount - 1 ? 0 : activeDot + 1;
        scrollToDot(nextIdx);
      });
    }
  });
}

