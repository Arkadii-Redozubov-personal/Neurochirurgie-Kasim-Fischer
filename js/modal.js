// ── Modal Open/Close Logic ───────────────────────────────────
function openTreatmentModal(btn) {
    const contentDiv = btn.closest('.treatment-content');
    if(!contentDiv) return;
    
    const title = contentDiv.querySelector('.treatment-title').innerText;
    const fullDesc = contentDiv.querySelector('.treatment-full-desc');
      const desc = fullDesc ? fullDesc.innerHTML : contentDiv.querySelector('.treatment-desc').innerHTML;
    
    document.getElementById('tModalTitle').innerText = title;
    document.getElementById('tModalDesc').innerHTML = desc;
    
    // Placeholder AI Video (using the YouTube ID for now)
    document.getElementById('tModalVideo').src = "https://www.youtube.com/embed/diagnostics_placeholder?enablejsapi=1&rel=0&autoplay=1";
    
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

function openFrakturModal() {
    const m = document.getElementById('fraktur-modal');
    if(m) { m.style.display = 'flex'; document.body.style.overflow = 'hidden'; }
  }
  function closeFrakturModal() {
    const m = document.getElementById('fraktur-modal');
    if(m) {
      m.style.display = 'none';
      document.body.style.overflow = '';
      const iframe = m.querySelector('iframe');
      if(iframe) {
        let src = iframe.src;
        iframe.src = src;
      }
    }
  }
  function openOpModal() {
    const m = document.getElementById('op-modal');
    if(m) { m.style.display = 'flex'; document.body.style.overflow = 'hidden'; }
  }
  function closeOpModal() {
    const m = document.getElementById('op-modal');
    if(m) {
      m.style.display = 'none';
      document.body.style.overflow = '';
      const iframe = m.querySelector('iframe');
      if(iframe) {
        let src = iframe.src;
        iframe.src = src;
      }
    }
  }
  function openKtsModal() {
    const m = document.getElementById('kts-modal');
    if(m) { m.style.display = 'flex'; document.body.style.overflow = 'hidden'; }
  }
  function closeKtsModal() {
    const m = document.getElementById('kts-modal');
    if(m) {
      m.style.display = 'none';
      document.body.style.overflow = '';
      const iframe = m.querySelector('iframe');
      if(iframe) {
        let src = iframe.src;
        iframe.src = src;
      }
    }
  }
  function openNeuroModal() {
    const m = document.getElementById('neuro-modal');
    if(m) { m.style.display = 'flex'; document.body.style.overflow = 'hidden'; }
  }
  function closeNeuroModal() {
    const m = document.getElementById('neuro-modal');
    if(m) {
      m.style.display = 'none';
      document.body.style.overflow = '';
      const iframe = m.querySelector('iframe');
      if(iframe) {
        let src = iframe.src;
        iframe.src = src;
      }
    }
  }

