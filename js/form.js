// ── Server-Side Contact Form Handler (ALL-INKL / send-mail.php) ─────────────
function sendEmail(e) {
  e.preventDefault();
  
  const form = e.target.closest('form') || document.getElementById('contact-form');
  if (!form) return;

  const emailInput = form.querySelector('#user_email') || form.querySelector('input[type="email"]');
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (emailInput && !emailRegex.test(emailInput.value)) {
    const alertMsg = document.documentElement.lang === 'ru' ? 'Пожалуйста, введите корректный email.' :
                     document.documentElement.lang === 'en' ? 'Please enter a valid email address.' :
                     document.documentElement.lang === 'tr' ? 'Lütfen geçerli bir e-posta adresi girin.' :
                     document.documentElement.lang === 'ar' ? 'يرجى إدخال عنوان بريد إلكتروني صالح.' :
                     document.documentElement.lang === 'uz' ? 'Iltimos, toʻgʻri elektron pochta manzilini kiriting.' :
                     'Bitte geben Sie eine gültige E-Mail-Adresse ein.';
    alert(alertMsg);
    emailInput.focus();
    return;
  }
  
  const btn = form.querySelector('#submit-btn') || form.querySelector('button[type="submit"]');
  const status = form.querySelector('#form-status') || document.getElementById('form-status');
  
  const originalText = btn ? btn.innerHTML : '';
  
  // Localized status texts
  const lang = document.documentElement.lang || 'de';
  const texts = {
    de: { sending: 'Senden...', success: 'Nachricht erfolgreich gesendet!', error: 'Fehler beim Senden. Bitte versuchen Sie es später noch einmal.' },
    ru: { sending: 'Отправка...', success: 'Сообщение успешно отправлено!', error: 'Ошибка отправки. Пожалуйста, попробуйте позже.' },
    en: { sending: 'Sending...', success: 'Message sent successfully!', error: 'Error sending message. Please try again later.' },
    tr: { sending: 'Gönderiliyor...', success: 'Mesaj başarıyla gönderildi!', error: 'Gönderme hatası. Lütfen daha sonra tekrar deneyin.' },
    ar: { sending: 'جارٍ الإرسال...', success: 'تم إرسال الرسالة بنجاح!', error: 'حدث خطأ أثناء الإرسال. يرجى المحاولة لاحقاً.' },
    uz: { sending: 'Yuborilmoqda...', success: 'Xabar muvaffaqiyatli yuborildi!', error: 'Xatolik yuz berdi. Iltimos, keyinroq qayta urinib koʻring.' }
  };
  const t = texts[lang] || texts.de;

  if (btn) {
    btn.innerText = t.sending;
    btn.disabled = true;
  }
  if (status) {
    status.style.display = 'none';
  }

  // Determine correct endpoint path
  const isSubdir = /\/(ru|en|tr|ar|uz)\//.test(window.location.pathname);
  const endpoint = isSubdir ? '../send-mail.php' : 'send-mail.php';

  const formData = new FormData(form);

  fetch(endpoint, {
    method: 'POST',
    body: formData
  })
    .then(async (response) => {
      const data = await response.json().catch(() => null);
      if (!response.ok || (data && !data.success)) {
        throw new Error((data && data.error) || 'Server error');
      }
      return data;
    })
    .then(() => {
      if (btn) {
        btn.innerHTML = originalText;
        btn.disabled = false;
      }
      if (status) {
        status.style.display = 'block';
        status.style.color = '#2ecc71';
        status.innerText = t.success;
      }
      form.reset();
    })
    .catch((err) => {
      if (btn) {
        btn.innerHTML = originalText;
        btn.disabled = false;
      }
      if (status) {
        status.style.display = 'block';
        status.style.color = '#e74c3c';
        status.innerText = t.error;
      }
      console.error('Form submission error:', err);
    });
}
