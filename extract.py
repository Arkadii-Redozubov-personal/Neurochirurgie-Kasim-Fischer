import re
import os

files = ['behandlungen.html', 'praxis-schwerpunkte.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    start_marker = '<!-- ══════ MODALS ══════ -->'
    end_marker = '<!-- ══════ JAVASCRIPT ══════ -->'
    
    start_idx = html.find(start_marker)
    end_idx = html.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        modals = html[start_idx:end_idx]
        out_name = f'{filename.replace(".html", "")}_modals.txt'
        with open(out_name, 'w', encoding='utf-8') as out:
            out.write(modals)
        print(f'Extracted {len(modals)} chars to {out_name}')
    else:
        print(f'Markers not found in {filename}')
