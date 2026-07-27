import os

filepath = 'c:/Users/arkad/Downloads/vertex/ru/praxis-schwerpunkte.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = content.replace('Упражняться', 'клиники')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated ru/praxis-schwerpunkte.html translation")
