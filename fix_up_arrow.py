import os

folders = ['.', 'en', 'ru', 'tr', 'ar']
files = ['index.html', 'behandlungen.html', 'praxis-schwerpunkte.html', 'presseschau.html', 'sprechzeiten.html', 'unser-team.html']

for folder in folders:
    if not os.path.exists(folder): continue
    for f in files:
        path = os.path.join(folder, f)
        if not os.path.exists(path): continue
        
        with open(path, 'rb') as file:
            content = file.read()
            
        try:
            # Fix up arrow ▲
            correct_bytes = '▲'.encode('utf-8')
            mojibake_bytes = correct_bytes.decode('latin-1').encode('utf-8')
            content = content.replace(mojibake_bytes, correct_bytes)
        except:
            pass

        with open(path, 'wb') as file:
            file.write(content)

print("Fixed up arrows!")
