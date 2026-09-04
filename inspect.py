with open('build_sprechzeiten.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('if "EmailJS Integration" not in content:')
if idx != -1:
    print(text[idx-50:idx+300])
else:
    print('Not found')
