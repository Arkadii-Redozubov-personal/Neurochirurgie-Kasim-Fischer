import glob

html_files = glob.glob('**/*.html', recursive=True)
count = 0

for filepath in html_files:
    if 'admin' in filepath: continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Add aria-label to facebook link
    target = '<a href="https://www.facebook.com/neurokaz/" target="_blank" style="color: white; opacity: 0.7; transition: 0.3s;" onmouseover="this.style.opacity=\'1\'" onmouseout="this.style.opacity=\'0.7\'">'
    replacement = '<a href="https://www.facebook.com/neurokaz/" target="_blank" aria-label="Facebook" style="color: white; opacity: 0.7; transition: 0.3s;" onmouseover="this.style.opacity=\'1\'" onmouseout="this.style.opacity=\'0.7\'">'
    content = content.replace(target, replacement)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Added aria-label to Facebook link in {count} files.')
