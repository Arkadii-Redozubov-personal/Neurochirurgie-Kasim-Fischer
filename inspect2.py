with open('build_sprechzeiten.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("with open(file_path, 'w', encoding='utf-8') as f:")
print(text[idx-200:idx+200])
