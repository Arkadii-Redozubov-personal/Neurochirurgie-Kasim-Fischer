// ── Mobile Menu & Sticky Navbar ───────────────────────────────
// Mobile Menu Toggle
  const burgerMenu = document.getElementById('burgerMenu');
  const mobileMenu = document.getElementById('mobileMenu');
  burgerMenu.addEventListener('click', () => {
    if (mobileMenu.style.display === 'flex') {
      mobileMenu.style.display = 'none';
      burgerMenu.textContent = '☰';
    } else {
      mobileMenu.style.display = 'flex';
      burgerMenu.textContent = '✕';
    }
  });

  // FAQ Accordion Toggle
  const faqItems = document.querySelectorAll('.faq-question');
  faqItems.forEach(item => {
    item.addEventListener('click', () => {
      // Close other items
      faqItems.forEach(otherItem => {
        if (otherItem !== item) {
          otherItem.nextElementSibling.style.display = 'none';
          otherItem.querySelector('.faq-icon').textContent = '▼';
        }
      });
      
      const answer = item.nextElementSibling;
      const icon = item.querySelector('.faq-icon');
      if (answer.style.display === 'block') {
        answer.style.display = 'none';
        icon.textContent = '▼';
      } else {
        answer.style.display = 'block';
        icon.textContent = '▲';
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

// Sticky Navbar
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 10) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  }