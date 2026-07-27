import os

chars_to_fix = [
    '★', '▼', 'Ö', 'ö', 'Ä', 'ä', 'Ü', 'ü', 'ß', 
    '–', '—', '“', '”', '’', '→', '←', '↓', '↑', '✓', '☰', '✕'
]

folders = ['.', 'en', 'ru', 'tr', 'ar']
files = [
    'index.html', 'behandlungen.html', 'praxis-schwerpunkte.html', 
    'presseschau.html', 'sprechzeiten.html', 'unser-team.html', 'style.css'
]

for folder in folders:
    if not os.path.exists(folder): continue
    for f in files:
        path = os.path.join(folder, f)
        if not os.path.exists(path): continue
        
        with open(path, 'rb') as file:
            content = file.read()
            
        for char in chars_to_fix:
            try:
                correct_bytes = char.encode('utf-8')
                mojibake_bytes = correct_bytes.decode('latin-1').encode('utf-8')
                content = content.replace(mojibake_bytes, correct_bytes)
            except Exception as e:
                pass
                
        with open(path, 'wb') as file:
            file.write(content)

print('Fixed mojibake at the binary level')
