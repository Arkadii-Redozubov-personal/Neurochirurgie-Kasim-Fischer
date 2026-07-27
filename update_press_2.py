import os

articles = [
    ("Minimaler Eingriff, maximale Wirkung", "Starke_Partner_September_2017_klein-150x150.jpg", "Medical Tribune", "15 April 2024", "Über die Vorteile der minimalinvasiven Wirbelsäulenchirurgie und schnelle Genesung."),
    ("Kleiner Schnitt mit großer Wirkung", "A6880993-1.1.pdf_klein-150x150.jpg", "Gesundheit Heute", "28 März 2024", "Wie moderne Technologien den Ansatz zur Behandlung von Bandscheibenvorfällen verändern."),
    ("Rückenschmerz? Da gibt's Hilfe", "A7367086-2.1-150x150.jpg", "Die Presse", "10 März 2024", "Wann Sie einen Spezialisten aufsuchen sollten und welche Methoden wirklich funktionieren."),
    ("Künstliche Bandscheibe als bewegliche Wirbelsäule", "Starke-Partner-März-2018.compressed_klein-150x150.jpg", "ÄrzteZeitung", "27 Februar 2024", "Alternative zu traditionellen Methoden der chirurgischen Behandlung."),
    ("Wieder fit mit Bandscheibenprothese", "A6756051-1.1.pd_kleinf-150x150.jpg", "Health Österreich", "12 Februar 2024", "In welchen Fällen eine Revisionsoperation möglich ist und welche Ergebnisse sie bringt."),
    ("Der Experte für Rückenleiden", "Der-Experte-fuer-Rueckeleiden-150x150.jpg", "Medizin & Forschung", "30 Januar 2024", "Interview mit Kasim Fischer über Ansätze zur Behandlung komplexer Fälle."),
    ("Der Helfer bei Rückenschmerz", "Der-Helfer-bei-Rueckenschmerz-150x150.jpg", "Wiener Zeitung", "18 Januar 2024", "Die Rolle der Navigation in der genauen Diagnose und Behandlung der Wirbelsäule."),
    ("Kleiner Eingriff mit großer Wirkung", "Kleiner-Eingriff-mit-grosser-Wirkung-150x150.jpg", "Kurier Gesundheit", "5 Januar 2024", "Geschichten von Patienten und ihr Weg zu einem Leben ohne Schmerzen."),
    ("Patienten als Ganzes sehen", "Patienten-als-Ganzes-sehen-150x150.jpg", "ORF Gesundheit", "20 Dezember 2023", "Was erwartet die Patienten im führenden Zentrum für Neurochirurgie."),
    ("Wenn das Kreuz streikt", "Wenn-das-Kreuz-streikt-150x150.jpg", "Gesundheitsmagazin", "15 November 2023", "Häufige Ursachen für Rückenschmerzen und erste Schritte zur Linderung."),
    ("Volkskrankheit Rücken", "Volkskrankheit-Ruecken-150x150.jpg", "Medical Tribune", "2 November 2023", "Statistiken und neue Ansätze zur Prävention von Wirbelsäulenerkrankungen."),
    ("Schmerzquelle Iliosakralgelenk", "A7331467-1.2-150x150.jpg", "Ärzteblatt", "10 Oktober 2023", "Diagnostik und minimalinvasive Therapie bei ISG-Syndrom."),
    ("Schmerzfrei nach kurzer Zeit", "A6595623-1.1.pdf_klein-150x150.jpg", "Orthopädie Nachrichten", "25 September 2023", "Erfolgsgeschichten von Patienten nach der Behandlung."),
    ("Rückenschmerz? Da geht was!", "Rueckenschmerz-Dagehtwas-150x150.jpg", "Gesund Leben", "5 September 2023", "Neue Perspektiven in der modernen Schmerztherapie.")
]

html_template = """        <a href="artikel_{idx}.pdf" target="_blank" class="press-card-horizontal">
          <div class="press-card-img-wrapper">
            <img src="img/{img}" alt="{title}">
          </div>
          <div class="press-card-content">
            <div class="press-card-meta">
              <span class="press-card-source">{source}</span>
            </div>
            <div class="press-card-title">{title}</div>
            <div class="press-card-desc">{desc}</div>
            <div class="press-card-meta" style="margin-bottom: 0; margin-top: auto; color: var(--text-light); font-weight: 500;">
              {date}
            </div>
          </div>
        </a>"""

generated_html = "\n"
for i, (title, img, source, date, desc) in enumerate(articles, 1):
    generated_html += html_template.format(idx=i, img=img, title=title, source=source, date=date, desc=desc) + "\n\n"

# read file
filepath = r"c:\Users\arkad\Downloads\vertex\presseschau.html"
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<div class="press-grid-horizontal">' in line:
        start_idx = i
    if '<!-- Newsletter CTA -->' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_lines = lines[:start_idx + 1] + [generated_html] + lines[end_idx - 2:]
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("Success")
else:
    print("Failed to find boundaries")
