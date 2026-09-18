// ── Cookie Consent Banner ────────────────────────────────────
document.addEventListener("DOMContentLoaded", function() {
      const cookieBanner = document.getElementById('cookie-consent-banner');
      const btnAccept = document.getElementById('cookie-accept-all');
      const btnEssential = document.getElementById('cookie-essential-only');
      
      if (!localStorage.getItem('cookieConsent')) {
        cookieBanner.style.display = 'block';
      }
      
      function hideBanner(choice) {
        localStorage.setItem('cookieConsent', choice);
        cookieBanner.style.display = 'none';
      }
      
      btnAccept.addEventListener('click', () => hideBanner('all'));
      btnEssential.addEventListener('click', () => hideBanner('essential'));
    });