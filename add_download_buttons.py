import os
import re

image_to_pdf = {
    'Starke_Partner_September_2017_klein-150x150.jpg': 'Starke_Partner_September_2017.pdf',
    'A6880993-1.1.pdf_klein-150x150.jpg': 'A6880993-1.1.pdf.pdf',
    'A7367086-2.1-150x150.jpg': 'A7367086-2.1.pdf',
    'Starke-Partner-März-2018.compressed_klein-150x150.jpg': 'Starke-Partner-Marz-2018.compressed.pdf',
    'A6756051-1.1.pd_kleinf-150x150.jpg': 'A6756051-1.1.pdf.pdf',
    'Der-Experte-fuer-Rueckeleiden-150x150.jpg': 'Der-Experte-fuer-Rueckenleiden.pdf',
    'Der-Helfer-bei-Rueckenschmerz-150x150.jpg': 'Der-Helfer-bei-Rueckenschmerz.pdf',
    'Kleiner-Eingriff-mit-grosser-Wirkung-150x150.jpg': 'Kleiner-Eingriff-mit-grosser-Wirkung.pdf',
    'Patienten-als-Ganzes-sehen-150x150.jpg': 'Patienten-als-Ganzes-sehen.pdf',
    'Wenn-das-Kreuz-streikt-150x150.jpg': 'Wenn-das-Kreuz-streikt.pdf',
    'Volkskrankheit-Ruecken-150x150.jpg': '#',
    'A7331467-1.2-150x150.jpg': 'A7331467-1.2.pdf',
    'A6595623-1.1.pdf_klein-150x150.jpg': 'A6595623-1.1.pdf.pdf',
    'Rueckenschmerz-Dagehtwas-150x150.jpg': 'Rueckenschmerz-Dagehtwas.pdf'
}

download_text = {
    'DE': 'PDF Herunterladen',
    'EN': 'Download PDF',
    'RU': 'Скачать PDF',
    'TR': 'PDF İndir',
    'AR': 'تحميل PDF'
}

def process_file(filepath, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = '../' if lang != 'DE' else ''
    btn_text = download_text.get(lang, 'Download PDF')

    pattern = r'(<a href="artikel_\d+\.pdf" target="_blank" class="press-card-horizontal">.*?<img src="(?:\.\./)?img/([^"]+)".*?<div class="press-card-meta" style="margin-bottom: 0; margin-top: auto; color: var\(--text-light\); font-weight: 500;">\s*(.*?)\s*</div>\s*</div>\s*</a>)'

    def replacer(match):
        full_match = match.group(1)
        img_name = match.group(2)
        date_text = match.group(3)
        
        pdf_name = image_to_pdf.get(img_name, '#')
        pdf_url = f"{prefix}pdfs/{pdf_name}" if pdf_name != '#' else '#'
        
        new_block = full_match.replace('<a href=', f'<div class="press-card-horizontal" style="cursor: pointer;" onclick="window.open(\'{pdf_url}\', \'_blank\')" data-old-href=')
        
        new_block = new_block.rsplit('</a>', 1)[0] + '</div>'
        
        new_date_block = f"""<div style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: auto; width: 100%;">
              <div class="press-card-meta" style="margin-bottom: 0; color: var(--text-light); font-weight: 500;">
                {date_text}
              </div>
              <a href="{pdf_url}" download class="btn-book" style="padding: 8px 16px; font-size: 0.85rem; border-radius: 99px;" onclick="event.stopPropagation()">{btn_text}</a>
            </div>"""
            
        new_block = re.sub(r'<div class="press-card-meta" style="margin-bottom: 0; margin-top: auto; color: var\(--text-light\); font-weight: 500;">\s*.*?\s*</div>', new_date_block, new_block, flags=re.DOTALL)
        
        # also remove target="_blank" class="press-card-horizontal" from the opening div because we already replaced it, wait, we replaced `<a href=...` with `<div class="press-card-horizontal"... data-old-href=...`. We should remove the rest.
        new_block = re.sub(r'data-old-href="artikel_\d+\.pdf"\s+target="_blank"\s+class="press-card-horizontal">', '>', new_block, count=1)
        
        return new_block

    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

root_dir = 'c:/Users/arkad/Downloads/vertex'
process_file(f"{root_dir}/presseschau.html", 'DE')
for lang in ['en', 'ru', 'tr', 'ar']:
    path = f"{root_dir}/{lang}/presseschau.html"
    if os.path.exists(path):
        process_file(path, lang.upper())
