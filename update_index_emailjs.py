import re

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    old_form = r'''<form action="#" method="POST" style="display: flex; flex-direction: column; gap: 16px; margin: 40px auto 80px; background: rgba(255,255,255,0.02); padding: 48px; border-radius: var\(--radius-lg\); border: 1px solid rgba(255,255,255,0.05); max-width: 800px;">
        <h3 style="font-size: 1.5rem; margin-bottom: 8px; font-weight: 700; text-align: center;">Direktnachricht</h3>
        <input type="text" placeholder="Ihr Name" required style="padding: 16px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.05); color: white; width: 100%; box-sizing: border-box; font-family: inherit; font-size: 1rem;">
        <input type="email" placeholder="Ihre E-Mail" required style="padding: 16px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.05); color: white; width: 100%; box-sizing: border-box; font-family: inherit; font-size: 1rem;">
        <textarea placeholder="Ihre Nachricht" required rows="4" style="padding: 16px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.05); color: white; width: 100%; box-sizing: border-box; font-family: inherit; font-size: 1rem; resize: vertical;"></textarea>
        <button type="submit" class="btn btn-primary" style="margin-top: 8px;">Nachricht Senden</button>
      </form>'''

    new_form = '''<form id="contact-form" onsubmit="sendEmail(event)" style="display: flex; flex-direction: column; gap: 16px; margin: 40px auto 80px; background: rgba(255,255,255,0.02); padding: 48px; border-radius: var(--radius-lg); border: 1px solid rgba(255,255,255,0.05); max-width: 800px;">
        <h3 style="font-size: 1.5rem; margin-bottom: 8px; font-weight: 700; text-align: center;">Direktnachricht</h3>
        <input type="text" id="user_name" name="user_name" placeholder="Ihr Name" required style="padding: 16px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.05); color: white; width: 100%; box-sizing: border-box; font-family: inherit; font-size: 1rem;">
        <input type="email" id="user_email" name="user_email" placeholder="Ihre E-Mail" required style="padding: 16px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.05); color: white; width: 100%; box-sizing: border-box; font-family: inherit; font-size: 1rem;">
        <textarea id="message" name="message" placeholder="Ihre Nachricht" required rows="4" style="padding: 16px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.05); color: white; width: 100%; box-sizing: border-box; font-family: inherit; font-size: 1rem; resize: vertical;"></textarea>
        <button type="submit" id="submit-btn" class="btn btn-primary" style="margin-top: 8px;">Nachricht Senden</button>
        <div id="form-status" style="display:none; text-align:center; margin-top:8px; font-weight:500;"></div>
      </form>'''

    html = re.sub(old_form, new_form, html)

    script_block = '''<!-- EmailJS Integration -->
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script type="text/javascript">
   (function(){
      emailjs.init({
        publicKey: "YOUR_PUBLIC_KEY",
      });
   })();
   
   function sendEmail(e) {
      e.preventDefault();
      
      const btn = document.getElementById('submit-btn');
      const status = document.getElementById('form-status');
      
      btn.innerText = 'Senden...';
      btn.disabled = true;
      status.style.display = 'none';

      // emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', '#contact-form')
      emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', '#contact-form')
        .then(() => {
            btn.innerText = 'Nachricht Senden';
            btn.disabled = false;
            status.style.display = 'block';
            status.style.color = '#2ecc71';
            status.innerText = 'Nachricht erfolgreich gesendet!';
            document.getElementById('contact-form').reset();
        }, (err) => {
            btn.innerText = 'Nachricht Senden';
            btn.disabled = false;
            status.style.display = 'block';
            status.style.color = '#e74c3c';
            status.innerText = 'Fehler beim Senden. Bitte versuchen Sie es später noch einmal.';
            console.error('EmailJS error:', err);
        });
   }
</script>
</body>'''

    html = html.replace('</body>', script_block)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated index.html')

update_index()
