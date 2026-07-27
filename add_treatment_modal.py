import os

base_dir = 'c:/Users/arkad/Downloads/vertex'
langs = ['', 'en', 'ru', 'tr', 'ar']

modal_code = '''
<!-- Treatment Modal -->
<div id="treatmentModal" class="video-modal" style="z-index: 99999;">
  <div class="video-modal-content" style="background: white; max-width: 800px; display: flex; flex-direction: column; height: auto; max-height: 90vh; border-radius: 20px; overflow: hidden; box-shadow: 0 24px 60px rgba(0,0,0,0.2);">
    <span class="close-video" id="closeTreatmentModalBtn" style="color: white; top: 16px; right: 20px; background: rgba(0,0,0,0.5); width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 50%; z-index: 10;">&times;</span>
    
    <div style="width: 100%; aspect-ratio: 16/9; background: #000; position: relative; flex-shrink: 0;">
      <iframe id="tModalVideo" width="100%" height="100%" src="" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0;"></iframe>
    </div>
    
    <div style="padding: 32px 40px; text-align: left; overflow-y: auto; background: white;">
      <h3 id="tModalTitle" style="font-size: 1.8rem; color: #091f22; margin-bottom: 16px; font-weight: 700; line-height: 1.3;"></h3>
      <p id="tModalDesc" style="color: #4a5568; font-size: 1.05rem; line-height: 1.7; margin-bottom: 24px;"></p>
      
      <a href="sprechzeiten.html" class="btn-primary" style="display: inline-block;">Termin anfragen</a>
    </div>
  </div>
</div>

<script>
  function openTreatmentModal(btn) {
    const contentDiv = btn.closest('.treatment-content');
    if(!contentDiv) return;
    
    const title = contentDiv.querySelector('.treatment-title').innerText;
    const desc = contentDiv.querySelector('.treatment-desc').innerHTML;
    
    document.getElementById('tModalTitle').innerText = title;
    document.getElementById('tModalDesc').innerHTML = desc;
    
    // Placeholder AI Video (using the YouTube ID for now)
    document.getElementById('tModalVideo').src = "https://www.youtube.com/embed/ScMzIvxBSi4?enablejsapi=1&rel=0&autoplay=1";
    
    document.getElementById('treatmentModal').classList.add('show');
  }

  const treatmentModal = document.getElementById('treatmentModal');
  const closeTreatmentModalBtn = document.getElementById('closeTreatmentModalBtn');

  if(closeTreatmentModalBtn && treatmentModal) {
    closeTreatmentModalBtn.addEventListener('click', () => {
      treatmentModal.classList.remove('show');
      document.getElementById('tModalVideo').src = ""; // Stop video
    });

    window.addEventListener('click', (e) => {
      if (e.target === treatmentModal) {
        treatmentModal.classList.remove('show');
        document.getElementById('tModalVideo').src = ""; // Stop video
      }
    });
  }
</script>
'''

for lang in langs:
    filepath = os.path.join(base_dir, lang, 'behandlungen.html') if lang else os.path.join(base_dir, 'behandlungen.html')
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the Mehr erfahren links
    content = content.replace('<a href="#" class="treatment-link">', '<a href="javascript:void(0)" class="treatment-link" onclick="openTreatmentModal(this)">')
    
    # Inject modal before </body>
    if 'id="treatmentModal"' not in content:
        content = content.replace('</body>', modal_code + '\n</body>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added Treatment Details Modal to behandlungen.html across all languages")
