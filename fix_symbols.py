import os

folders = ['.', 'en', 'ru', 'tr', 'ar']
files = ['index.html', 'behandlungen.html', 'praxis-schwerpunkte.html', 'presseschau.html', 'sprechzeiten.html', 'unser-team.html']

replacements = {
    'â˜…': '★',
    'â†’': '→',
    'â†': '←',
    'â†“': '↓',
    'â†‘': '↑',
    'âœ“': '✓',
    'â€”': '—',
    'â€“': '–',
    'â€œ': '“',
    'â€': '”',
    'â€™': '’',
    'â€š': '‚',
    'â€ž': '„'
}

for folder in folders:
    if not os.path.exists(folder): continue
    for f in files:
        path = os.path.join(folder, f)
        if not os.path.exists(path): continue
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            
        for bad, good in replacements.items():
            content = content.replace(bad, good)
            
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

print("Fixed stars and arrows globally!")
