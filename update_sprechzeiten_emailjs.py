import re

def update_sprechzeiten():
    with open('build_sprechzeiten.py', 'r', encoding='utf-8') as f:
        py_content = f.read()

    # Find the form replacement in build_sprechzeiten.py
    old_form_head = r'<form class="contact-form">'
    new_form_head = r'<form id="contact-form" onsubmit="sendEmail(event)" class="contact-form">'

    py_content = re.sub(old_form_head, new_form_head, py_content)

    # Add id and name to inputs in the form
    py_content = py_content.replace(
        '<input type="text" class="form-input" placeholder="{lang_data["name_ph"]}"',
        '<input type="text" id="user_name" name="user_name" required class="form-input" placeholder="{lang_data["name_ph"]}"'
    )
    py_content = py_content.replace(
        '<input type="email" class="form-input" placeholder="{lang_data["email_ph"]}"',
        '<input type="email" id="user_email" name="user_email" required class="form-input" placeholder="{lang_data["email_ph"]}"'
    )
    
    # We replaced the branch dropdown in a previous task, let's look for it
    old_select = r'<select class="form-input" id="branch" name="branch" required>'
    # The select already has id and name from my previous refactor: id="branch" name="branch". So we don't need to change it.
    
    # Update textarea
    py_content = py_content.replace(
        '<textarea class="form-textarea" placeholder="{lang_data["msg_ph"]}"',
        '<textarea id="message" name="message" required class="form-textarea" placeholder="{lang_data["msg_ph"]}"'
    )

    # Add form-status div below the button
    old_btn = r'<button type="submit" class="btn btn-primary" style="margin-top: 16px; padding: 16px; font-size: 1.1rem; width: 100%;">\s*<svg.*?</svg>\s*\{lang_data\["send_btn"\]\}\s*</button>'
    new_btn = r'''<button type="submit" id="submit-btn" class="btn btn-primary" style="margin-top: 16px; padding: 16px; font-size: 1.1rem; width: 100%;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right: 8px;"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
              {lang_data["send_btn"]}
            </button>
            <div id="form-status" style="display:none; text-align:center; margin-top:16px; font-weight:500;"></div>'''
    py_content = re.sub(old_btn, new_btn, py_content)
    
    # Add EmailJS script block before </body>
    script_block = '''
<!-- EmailJS Integration -->
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

      emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', '#contact-form')
        .then(() => {
            btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right: 8px;"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg> {lang_data["send_btn"]}';
            btn.disabled = false;
            status.style.display = 'block';
            status.style.color = '#2ecc71';
            status.innerText = 'Nachricht erfolgreich gesendet!';
            document.getElementById('contact-form').reset();
        }, (err) => {
            btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right: 8px;"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg> {lang_data["send_btn"]}';
            btn.disabled = false;
            status.style.display = 'block';
            status.style.color = '#e74c3c';
            status.innerText = 'Fehler beim Senden. Bitte versuchen Sie es später noch einmal.';
            console.error('EmailJS error:', err);
        });
   }
</script>
</body>'''
    
    # We have to inject this before </body> in the generated HTML
    # The build_sprechzeiten.py file has `html = f"""<!DOCTYPE html> ... </body></html>"""` but wait!
    # I saw earlier that build_sprechzeiten.py DOES NOT have `html = f"""<!DOCTYPE html>` ! It uses regex to replace parts of the existing sprechzeiten.html files!
    # Oh! Yes, we found out that it modifies existing HTML files!
    # So `script_block` should be injected directly into the HTML files, or added via `build_sprechzeiten.py` by replacing `</body>` with the script + `</body>`.
    
    # Let's add logic in build_sprechzeiten.py to inject the script block right before </body> for each file it processes.
    
    injection_logic = '''
    if "EmailJS Integration" not in content:
        script_block = """
<!-- EmailJS Integration -->
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
      
      const originalText = btn.innerHTML;
      btn.innerText = 'Senden...';
      btn.disabled = true;
      status.style.display = 'none';

      emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', '#contact-form')
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
</script>
</body>"""
        content = content.replace("</body>", script_block)
'''
    # We need to find where `content` is written back.
    # It ends with:
    # with open(file_path, 'w', encoding='utf-8') as f:
    #     f.write(content)
    
    py_content = py_content.replace(
        "with open(file_path, 'w', encoding='utf-8') as f:",
        injection_logic + "\n    with open(file_path, 'w', encoding='utf-8') as f:"
    )
    
    with open('build_sprechzeiten.py', 'w', encoding='utf-8') as f:
        f.write(py_content)
    print('Updated build_sprechzeiten.py')

update_sprechzeiten()
