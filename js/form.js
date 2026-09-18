// ── EmailJS Contact Form ─────────────────────────────────────
(function(){
      emailjs.init({
        publicKey: "-dY76BrZbuYUmTruZ",
      });
   })();
   
   function sendEmail(e) {
      e.preventDefault();
      
      const emailInput = document.getElementById('user_email');
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(emailInput.value)) {
          alert('Bitte geben Sie eine gültige E-Mail-Adresse ein.');
          emailInput.focus();
          return;
      }
      
      const btn = document.getElementById('submit-btn');
      const status = document.getElementById('form-status');
      
      const originalText = btn.innerHTML;
      btn.innerText = 'Senden...';
      btn.disabled = true;
      status.style.display = 'none';

      Promise.all([
        emailjs.sendForm('service_ecu13bq', 'template_bfsngtg', '#contact-form'),
        emailjs.sendForm('service_ecu13bq', 'template_uuk8onk', '#contact-form')
      ])
        .then(() => {
            btn.innerHTML = originalText;
            btn.disabled = false;
            status.style.display = 'block';
            status.style.color = '#2ecc71';
            status.innerText = 'Nachricht erfolgreich gesendet!';
            document.getElementById('contact-form').reset();
        }, (err) => {
            btn.innerHTML = originalText;
            btn.disabled = false;
            status.style.display = 'block';
            status.style.color = '#e74c3c';
            status.innerText = 'Fehler beim Senden. Bitte versuchen Sie es später noch einmal.';
            console.error('EmailJS error:', err);
        });
   }