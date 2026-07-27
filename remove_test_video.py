import os

HTML_PATH = 'c:/Users/arkad/Downloads/vertex/praxis-schwerpunkte.html'
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Remove the button
btn_html = '''<p>Kasim Fischer ist Mitglied der Deutschen Gesellschaft für Wirbelsäulenchirurgie und der Gesellschaft für Wirbelsäulenforschung. Bei der Behandlung von Bandscheibenvorfällen legt er besonderen Wert auf schonende, minimalinvasive Verfahren.</p>
          <div style="margin-top: 32px;">
            <button class="btn-play-video" id="openVideoModalBtn">
              <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              Beispiel-Video ansehen
            </button>
          </div>'''
original_p = '<p>Kasim Fischer ist Mitglied der Deutschen Gesellschaft für Wirbelsäulenchirurgie und der Gesellschaft für Wirbelsäulenforschung. Bei der Behandlung von Bandscheibenvorfällen legt er besonderen Wert auf schonende, minimalinvasive Verfahren.</p>'
html_content = html_content.replace(btn_html, original_p)

# Remove the Modal HTML and JS
modal_start = '<!-- Video Modal -->'
if modal_start in html_content:
    html_content = html_content[:html_content.find(modal_start)] + '</body>'

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Removed test video button and modal from praxis-schwerpunkte.html")
