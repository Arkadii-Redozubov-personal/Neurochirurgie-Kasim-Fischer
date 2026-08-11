import re
import os

filepath = r"admin/dashboard.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert Sidebar Nav
nav_btn = """      <button class="nav-item" onclick="showSection('pages')">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
        Seiteninhalte
      </button>"""

if "showSection('pages')" not in content:
    content = content.replace(
        """<button class="nav-item" onclick="showSection('texts')">""",
        nav_btn + "\n" + """      <button class="nav-item" onclick="showSection('texts')">"""
    )

# 2. Update sections & titles JS arrays
if "'pages'" not in content:
    content = content.replace(
        "const sections = ['dashboard', 'treatments', 'team', 'texts', 'sync', 'press', 'coordinators'];",
        "const sections = ['dashboard', 'pages', 'treatments', 'team', 'texts', 'sync', 'press', 'coordinators'];"
    )
    content = content.replace(
        "treatments: ['Behandlungen', 'Inhalte bearbeiten'],",
        "pages: ['Seiteninhalte', 'Inhalte aller Seiten verwalten'],\n      treatments: ['Behandlungen', 'Inhalte bearbeiten'],"
    )

# 3. Insert Section HTML
section_html = """
      <!-- ===== PAGES SECTION ===== -->
      <section id="section-pages" style="display:none;">
        <div class="content-card">
          <div class="content-card-header">
            <div>
              <div class="content-card-title">Seiteninhalte (Pages)</div>
              <div class="content-card-sub">Inhalte für jede Seite bearbeiten (Hero-Titel, etc.)</div>
            </div>
            <!-- <button class="btn btn-primary" onclick="openPageModal()">+ Neue Seite (WIP)</button> -->
          </div>
          <table class="table" id="pagesTable">
            <thead>
              <tr>
                <th>Seiten-ID</th>
                <th>Name</th>
                <th>Sektionen</th>
                <th style="width:120px;">Aktion</th>
              </tr>
            </thead>
            <tbody id="pagesTbody">
              <tr><td colspan="4" class="text-center" style="padding: 20px; color: #94a3b8;">Lädt...</td></tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- ===== PAGES MODAL ===== -->
      <div class="modal-overlay" id="pageModal">
        <div class="modal">
          <div class="modal-header">
            <div class="modal-title" id="pageModalTitle">Seite bearbeiten</div>
            <button class="btn btn-outline" style="border:none; padding:4px;" onclick="closeModal('pageModal')">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
          <div class="modal-body" id="pageModalBody">
            <input type="hidden" id="pageId">
            <div style="margin-bottom: 20px;">
              <label>Name der Seite (intern)</label>
              <input type="text" id="pageName" class="form-input" disabled>
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 12px;">
              <h4 style="margin:0; font-size: 1.1rem; color: #fff;">Sektionen</h4>
              <!-- <button class="btn btn-outline btn-sm" onclick="addPageSection()">+ Sektion hinzufügen</button> -->
            </div>
            
            <div id="pageSectionsContainer">
              <!-- Sections will be rendered here dynamically -->
            </div>

          </div>
          <div class="modal-footer">
            <button class="btn btn-outline" onclick="closeModal('pageModal')">Abbrechen</button>
            <button class="btn btn-primary" id="savePageBtn" onclick="savePage()">Speichern</button>
          </div>
        </div>
      </div>
"""

if "id=\"section-pages\"" not in content:
    content = content.replace(
        "<!-- ===== DASHBOARD SECTION ===== -->",
        section_html + "\n      <!-- ===== DASHBOARD SECTION ===== -->"
    )

# 4. Insert Page JS Logic
page_js = """
    // ========= PAGES LOGIC =========
    let pagesData = [];
    
    async function loadPages() {
      try {
        const snap = await getDocs(collection(db, 'pages'));
        pagesData = snap.docs.map(d => ({ id: d.id, ...d.data() }));
        
        pagesData.sort((a, b) => a.id.localeCompare(b.id));
        
        const tbody = document.getElementById('pagesTbody');
        tbody.innerHTML = '';
        
        pagesData.forEach(page => {
          const numSecs = page.sections ? page.sections.length : 0;
          tbody.innerHTML += `
            <tr>
              <td><strong>${page.id}</strong></td>
              <td>${page.name || ''}</td>
              <td>${numSecs} Abschnitt(e)</td>
              <td>
                <button class="action-btn" title="Bearbeiten" onclick="editPage('${page.id}')">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                </button>
              </td>
            </tr>
          `;
        });
      } catch (err) {
        console.error(err);
        showToast('Fehler beim Laden der Seiteninhalte', 'error');
      }
    }

    let currentPageSections = [];
    
    function editPage(pid) {
      const page = pagesData.find(p => p.id === pid);
      if(!page) return;
      
      document.getElementById('pageId').value = page.id;
      document.getElementById('pageName').value = page.name || '';
      
      currentPageSections = page.sections ? JSON.parse(JSON.stringify(page.sections)) : [];
      renderPageSections();
      
      document.getElementById('pageModalTitle').textContent = `Seite bearbeiten: ${page.id}`;
      document.getElementById('pageModal').classList.add('active');
    }
    
    function renderPageSections() {
      const container = document.getElementById('pageSectionsContainer');
      container.innerHTML = '';
      
      currentPageSections.forEach((sec, idx) => {
        let langsHtml = '';
        ['de', 'en', 'ru', 'tr', 'ar'].forEach(lang => {
          const lData = sec.content && sec.content[lang] ? sec.content[lang] : {title: '', desc: ''};
          langsHtml += `
            <div style="margin-bottom: 12px; padding-left: 12px; border-left: 2px solid rgba(255,255,255,0.1);">
              <label style="color:var(--primary); font-weight:600;">Sprache: ${lang.toUpperCase()}</label>
              <input type="text" class="form-input" style="margin-bottom:8px;" placeholder="Titel (${lang})" 
                value="${lData.title ? lData.title.replace(/"/g, '&quot;') : ''}" 
                onchange="updatePageSec(${idx}, '${lang}', 'title', this.value)">
              <textarea class="form-input" rows="2" placeholder="Beschreibung (${lang})"
                onchange="updatePageSec(${idx}, '${lang}', 'desc', this.value)">${lData.desc || ''}</textarea>
            </div>
          `;
        });
        
        container.innerHTML += `
          <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); padding: 16px; border-radius: 8px; margin-bottom: 16px;">
            <div style="display:flex; justify-content:space-between; margin-bottom: 12px;">
              <h5 style="margin:0; font-size:1rem;">Abschnitt: ${sec.id} (${sec.type})</h5>
            </div>
            ${langsHtml}
          </div>
        `;
      });
    }
    
    window.updatePageSec = function(idx, lang, field, val) {
      if(!currentPageSections[idx].content) currentPageSections[idx].content = {};
      if(!currentPageSections[idx].content[lang]) currentPageSections[idx].content[lang] = {};
      currentPageSections[idx].content[lang][field] = val;
    }
    
    async function savePage() {
      const pid = document.getElementById('pageId').value;
      const btn = document.getElementById('savePageBtn');
      btn.disabled = true;
      btn.textContent = 'Speichert...';
      
      try {
        await setDoc(doc(db, 'pages', pid), {
          id: pid,
          name: document.getElementById('pageName').value,
          sections: currentPageSections
        }, { merge: true });
        
        showToast('Seite erfolgreich gespeichert');
        closeModal('pageModal');
        loadPages();
      } catch (err) {
        console.error(err);
        showToast('Fehler beim Speichern', 'error');
      } finally {
        btn.disabled = false;
        btn.textContent = 'Speichern';
      }
    }
"""

if "loadPages()" not in content:
    content = content.replace(
        "loadTexts();",
        "loadTexts();\n      loadPages();"
    )
    content = content.replace(
        "// ========= TREATMENTS LOGIC =========",
        page_js + "\n    // ========= TREATMENTS LOGIC ========="
    )

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Dashboard patched successfully")
