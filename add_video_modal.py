import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'
with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

modal_css = '''
/* Video Modal */
.video-modal {
  display: none; 
  position: fixed; 
  z-index: 9999; 
  left: 0;
  top: 0;
  width: 100%; 
  height: 100%; 
  overflow: hidden; 
  background-color: rgba(0,0,0,0.85); 
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.video-modal.show {
  display: flex;
  opacity: 1;
}

.video-modal-content {
  position: relative;
  width: 90%;
  max-width: 900px;
  background: #000;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
  transform: scale(0.95);
  transition: transform 0.3s ease;
  aspect-ratio: 16/9;
}

.video-modal.show .video-modal-content {
  transform: scale(1);
}

.close-video {
  position: absolute;
  top: 16px;
  right: 24px;
  color: white;
  font-size: 32px;
  font-weight: bold;
  cursor: pointer;
  z-index: 2;
  transition: opacity 0.2s;
  opacity: 0.7;
}

.close-video:hover {
  opacity: 1;
}

.btn-play-video {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 12px 24px;
  background: rgba(45, 203, 168, 0.1);
  color: var(--primary);
  border: 1px solid var(--primary);
  border-radius: 99px;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
}

.btn-play-video:hover {
  background: var(--primary);
  color: white;
  transform: translateY(-2px);
}

.btn-play-video svg {
  width: 20px;
  height: 20px;
  fill: currentColor;
}
'''
if 'video-modal' not in css_content:
    with open(CSS_PATH, 'a', encoding='utf-8') as f:
        f.write('\n' + modal_css)

HTML_PATH = 'c:/Users/arkad/Downloads/vertex/praxis-schwerpunkte.html'
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Add button
btn_html = '''<p>Kasim Fischer ist Mitglied der Deutschen Gesellschaft für Wirbelsäulenchirurgie und der Gesellschaft für Wirbelsäulenforschung. Bei der Behandlung von Bandscheibenvorfällen legt er besonderen Wert auf schonende, minimalinvasive Verfahren.</p>
          <div style="margin-top: 32px;">
            <button class="btn-play-video" id="openVideoModalBtn">
              <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              Beispiel-Video ansehen
            </button>
          </div>'''
html_content = html_content.replace(
    '<p>Kasim Fischer ist Mitglied der Deutschen Gesellschaft für Wirbelsäulenchirurgie und der Gesellschaft für Wirbelsäulenforschung. Bei der Behandlung von Bandscheibenvorfällen legt er besonderen Wert auf schonende, minimalinvasive Verfahren.</p>',
    btn_html
)

# Add Modal HTML and JS before </body>
modal_html = '''
<!-- Video Modal -->
<div id="videoModal" class="video-modal">
  <div class="video-modal-content">
    <span class="close-video" id="closeVideoModalBtn">&times;</span>
    <iframe id="videoIframe" width="100%" height="100%" src="https://www.youtube.com/embed/ScMzIvxBSi4?enablejsapi=1&rel=0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
</div>

<script>
  const videoModal = document.getElementById('videoModal');
  const openVideoBtn = document.getElementById('openVideoModalBtn');
  const closeVideoBtn = document.getElementById('closeVideoModalBtn');
  const iframe = document.getElementById('videoIframe');

  if(openVideoBtn && videoModal) {
    openVideoBtn.addEventListener('click', () => {
      videoModal.classList.add('show');
      // Auto play video when opening
      iframe.contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
    });

    closeVideoBtn.addEventListener('click', () => {
      videoModal.classList.remove('show');
      // Stop video when closing
      iframe.contentWindow.postMessage('{"event":"command","func":"stopVideo","args":""}', '*');
    });

    window.addEventListener('click', (e) => {
      if (e.target === videoModal) {
        videoModal.classList.remove('show');
        iframe.contentWindow.postMessage('{"event":"command","func":"stopVideo","args":""}', '*');
      }
    });
  }
</script>
</body>'''
if 'id="videoModal"' not in html_content:
    html_content = html_content.replace('</body>', modal_html)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Added Video Modal structure to praxis-schwerpunkte.html")
