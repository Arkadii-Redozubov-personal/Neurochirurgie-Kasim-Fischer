// ── Modal Open/Close Logic ───────────────────────────────────

// ── Generic video modal (behandlungen, praxis-schwerpunkte) ──
function openModal(id) {
  var el = document.getElementById('modal-overlay-' + id);
  if (!el) return;
  el.style.display = 'flex';
  document.body.style.overflow = 'hidden';
  var vid = el.querySelector('video');
  if (vid) { vid.currentTime = 0; var p = vid.play(); if (p) p.catch(function(){}); }
  el.onclick = function(e) { if (e.target === el) closeModal(id); };
}
function closeModal(id) {
  var el = document.getElementById('modal-overlay-' + id);
  if (!el) return;
  el.style.display = 'none';
  document.body.style.overflow = '';
  var vid = el.querySelector('video');
  if (vid) { vid.pause(); vid.currentTime = 0; }
}

// Shorthand aliases (praxis-schwerpunkte.html)
function openBsvModal()       { openModal('bsv'); }
function closeBsvModal()      { closeModal('bsv'); }
function openFacettenModal()  { openModal('facetten'); }
function closeFacettenModal() { closeModal('facetten'); }

// Escape key closes any open modal
document.addEventListener('keydown', function(e) {
  if (e.key !== 'Escape') return;
  ['bandscheibe','dekompression','kyphoplastie','nervenop','neuromod','hwsop',
   'bsv','spinal','facetten','hws','kts','sulcus','chron','neuro','isg','wkf','nervkomp']
  .forEach(function(id) {
    var el = document.getElementById('modal-overlay-' + id);
    if (el && el.style.display === 'flex') closeModal(id);
  });
});

// ── diagnostik.html – Fraktur / OP modals ───────────────────
function openFrakturModal() {
  var m = document.getElementById('fraktur-modal');
  if (m) { m.style.display = 'flex'; document.body.style.overflow = 'hidden'; }
}
function closeFrakturModal() {
  var m = document.getElementById('fraktur-modal');
  if (m) {
    m.style.display = 'none'; document.body.style.overflow = '';
    var iframe = m.querySelector('iframe');
    if (iframe) { var s = iframe.src; iframe.src = ''; iframe.src = s; }
  }
}
function openOpModal() {
  var m = document.getElementById('op-modal');
  if (m) { m.style.display = 'flex'; document.body.style.overflow = 'hidden'; }
}
function closeOpModal() {
  var m = document.getElementById('op-modal');
  if (m) { m.style.display = 'none'; document.body.style.overflow = ''; }
}

// ── diagnostik/patienten/zweitmeinung – Treatment modal ─────
function openTreatmentModal(btn) {
  var contentDiv = btn.closest('.treatment-content');
  if (!contentDiv) return;
  var title = contentDiv.querySelector('.treatment-title').innerText;
  var fullDesc = contentDiv.querySelector('.treatment-full-desc');
  var desc = fullDesc ? fullDesc.innerHTML : contentDiv.querySelector('.treatment-desc').innerHTML;
  document.getElementById('tModalTitle').innerText = title;
  document.getElementById('tModalDesc').innerHTML = desc;
  document.getElementById('treatmentModal').classList.add('show');
}
var treatmentModal = document.getElementById('treatmentModal');
var closeTreatmentModalBtn = document.getElementById('closeTreatmentModalBtn');
if (closeTreatmentModalBtn && treatmentModal) {
  closeTreatmentModalBtn.addEventListener('click', function() {
    treatmentModal.classList.remove('show');
  });
  window.addEventListener('click', function(e) {
    if (e.target === treatmentModal) treatmentModal.classList.remove('show');
  });
}
