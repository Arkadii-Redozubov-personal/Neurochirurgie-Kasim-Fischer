with open('build_sprechzeiten.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('content = content.replace("</body>", script_block)', 'new_content = new_content.replace("</body>", script_block)')
text = text.replace('if "EmailJS Integration" not in content:', 'if "EmailJS Integration" not in new_content:')

with open('build_sprechzeiten.py', 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed variable names in build_sprechzeiten.py')
