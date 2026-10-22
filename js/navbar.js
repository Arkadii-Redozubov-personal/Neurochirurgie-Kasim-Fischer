// ── Mobile Menu & Sticky Navbar ───────────────────────────────
// Mobile Menu Toggle
  const burgerMenu = document.getElementById('burgerMenu');
  const mobileMenu = document.getElementById('mobileMenu');
  if (burgerMenu && mobileMenu) {
    const toggleMenu = () => {
      const isExpanded = mobileMenu.style.display === 'flex' || burgerMenu.classList.contains('open');
      const burgerIcon = burgerMenu.querySelector('.burger-icon');
      const closeIcon = burgerMenu.querySelector('.close-icon');

      if (isExpanded) {
        mobileMenu.style.display = 'none';
        document.body.style.overflow = '';
        burgerMenu.classList.remove('open');
        burgerMenu.setAttribute('aria-expanded', 'false');
        if (burgerIcon) burgerIcon.style.display = 'block';
        if (closeIcon) closeIcon.style.display = 'none';
      } else {
        mobileMenu.style.display = 'flex';
        document.body.style.overflow = 'hidden';
        burgerMenu.classList.add('open');
        burgerMenu.setAttribute('aria-expanded', 'true');
        if (burgerIcon) burgerIcon.style.display = 'none';
        if (closeIcon) closeIcon.style.display = 'block';
      }
    };

    burgerMenu.addEventListener('click', toggleMenu);
    burgerMenu.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleMenu();
      }
    });

    // Mobile Dropdown Accordion Toggle
    mobileMenu.querySelectorAll('.mobile-dropdown-toggle').forEach(toggle => {
      toggle.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const wrapper = toggle.closest('.mobile-dropdown-wrapper');
        if (wrapper) {
          wrapper.classList.toggle('open');
        }
      });
      toggle.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          e.stopPropagation();
          const wrapper = toggle.closest('.mobile-dropdown-wrapper');
          if (wrapper) {
            wrapper.classList.toggle('open');
          }
        }
      });
    });

    // Auto-expand dropdown if any sublink is active or current page
    const curPath = window.location.pathname.split('/').pop() || 'index.html';
    mobileMenu.querySelectorAll('a.mobile-link, a.mobile-sublink').forEach(link => {
      const href = link.getAttribute('href');
      if (href && (href === curPath || href.endsWith('/' + curPath))) {
        link.classList.add('active');
        const parentWrapper = link.closest('.mobile-dropdown-wrapper');
        if (parentWrapper) {
          parentWrapper.classList.add('open');
        }
      }
    });

    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        if (!link.closest('.mobile-dropdown-toggle')) {
          mobileMenu.style.display = 'none';
          document.body.style.overflow = '';
          burgerMenu.classList.remove('open');
          burgerMenu.setAttribute('aria-expanded', 'false');
          const burgerIcon = burgerMenu.querySelector('.burger-icon');
          const closeIcon = burgerMenu.querySelector('.close-icon');
          if (burgerIcon) burgerIcon.style.display = 'block';
          if (closeIcon) closeIcon.style.display = 'none';
        }
      });
    });
  }

  // FAQ Accordion Toggle
  const faqItems = document.querySelectorAll('.faq-question');
  faqItems.forEach(item => {
    item.addEventListener('click', () => {
      const parent = item.closest('.faq-item') || item;
      const answer = item.nextElementSibling;
      const isAlreadyActive = parent.classList.contains('active');

      // Close all other items
      faqItems.forEach(otherItem => {
        if (otherItem !== item) {
          const otherParent = otherItem.closest('.faq-item') || otherItem;
          otherParent.classList.remove('active');
          otherItem.classList.remove('active');
          if (otherItem.nextElementSibling) {
            otherItem.nextElementSibling.style.display = 'none';
          }
        }
      });

      // Toggle current item
      if (isAlreadyActive) {
        parent.classList.remove('active');
        item.classList.remove('active');
        if (answer) answer.style.display = 'none';
      } else {
        parent.classList.add('active');
        item.classList.add('active');
        if (answer) answer.style.display = 'block';
      }
    });
  });

  // Counter Animation
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseFloat(el.getAttribute('data-target'));
        const duration = 2000;
        const stepTime = 30;
        const steps = duration / stepTime;
        const stepVal = target / steps;
        let current = 0;
        
        const suffix = el.getAttribute('data-suffix') || '';
        const isDecimal = target % 1 !== 0;

        const timer = setInterval(() => {
          current += stepVal;
          if (current >= target) {
            current = target;
            clearInterval(timer);
          }
          
          let displayVal = current;
          let currentSuffix = suffix;
          if (isDecimal) {
            displayVal = current.toFixed(1);
          } else {
            displayVal = Math.floor(current);
            if (target === 1000) {
              if (current >= 1000) {
                displayVal = "1";
                currentSuffix = "k+";
              } else {
                currentSuffix = "+";
              }
            }
          }
          el.innerHTML = displayVal + currentSuffix;
        }, stepTime);
        counterObserver.unobserve(el);
      }
    });
  }, { threshold: 0.5 });
  
  document.querySelectorAll('.counter-value').forEach(el => counterObserver.observe(el));

  // Fade-in Animation
  const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        fadeObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.fade-in').forEach(el => fadeObserver.observe(el));

// Sticky Navbar & Mobile Lang Switcher Toggle
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    const handleScroll = () => {
      if (window.scrollY > 10) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
  }

  // Touch support for language dropdown
  const langSwitcher = document.querySelector('.lang-switcher');
  if (langSwitcher) {
    langSwitcher.addEventListener('click', (e) => {
      if (e.target.closest('.lang-current')) {
        const dd = langSwitcher.querySelector('.lang-dropdown');
        if (dd) {
          const isFlex = window.getComputedStyle(dd).display === 'flex';
          dd.style.display = isFlex ? 'none' : 'flex';
        }
      }
    });
    document.addEventListener('click', (e) => {
      if (!langSwitcher.contains(e.target)) {
        const dd = langSwitcher.querySelector('.lang-dropdown');
        if (dd && dd.style.display === 'flex') {
          dd.style.display = '';
        }
      }
    });
  }

// ── Floating Appointment Widget Toggle (Desktop & Mobile) ─────
function toggleFdMobile(e) {
  if (e && e.target && e.target.closest('.fd-pill-close')) return;
  const widget = document.querySelector('.floating-doctolib');
  if (widget) {
    widget.classList.toggle('fd-open');
    const pill = widget.querySelector('.fd-mobile-pill');
    if (pill) {
      pill.setAttribute('aria-expanded', widget.classList.contains('fd-open') ? 'true' : 'false');
    }
  }
}
window.toggleFdMobile = toggleFdMobile;

function closeFdWidget(e) {
  if (e) {
    e.preventDefault();
    e.stopPropagation();
  }
  const widget = document.querySelector('.floating-doctolib');
  if (widget) {
    if (widget.classList.contains('fd-open')) {
      widget.classList.remove('fd-open');
      const pill = widget.querySelector('.fd-mobile-pill');
      if (pill) pill.setAttribute('aria-expanded', 'false');
    } else {
      widget.style.display = 'none';
    }
  }
}
window.closeFdWidget = closeFdWidget;

// Close mobile popup if clicking outside
document.addEventListener('click', function(e) {
  const widget = document.querySelector('.floating-doctolib');
  if (widget && widget.classList.contains('fd-open')) {
    if (!widget.contains(e.target)) {
      widget.classList.remove('fd-open');
      const pill = widget.querySelector('.fd-mobile-pill');
      if (pill) pill.setAttribute('aria-expanded', 'false');
    }
  }
});

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    const widget = document.querySelector('.floating-doctolib');
    if (widget && widget.classList.contains('fd-open')) {
      widget.classList.remove('fd-open');
      const pill = widget.querySelector('.fd-mobile-pill');
      if (pill) pill.setAttribute('aria-expanded', 'false');
    }
  }
});
