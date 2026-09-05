import glob

html_files = glob.glob('**/*.html', recursive=True)
count = 0

preload_font = '<link rel="preload" href="fonts/plus-jakarta-sans-2.woff2" as="font" type="font/woff2" crossorigin>\n  '

for filepath in html_files:
    if 'admin' in filepath: continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Preload the main font
    if '<link rel="preload" href="fonts/plus-jakarta-sans-2.woff2"' not in content:
        if '<link rel="stylesheet" href="fonts/fonts.css">' in content:
            content = content.replace('<link rel="stylesheet" href="fonts/fonts.css">', preload_font + '<link rel="stylesheet" href="fonts/fonts.css">')
        elif '<link rel="stylesheet" href="../fonts/fonts.css">' in content:
            content = content.replace('<link rel="stylesheet" href="../fonts/fonts.css">', preload_font.replace('fonts/', '../fonts/') + '<link rel="stylesheet" href="../fonts/fonts.css">')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Added font preload to {count} files.')
