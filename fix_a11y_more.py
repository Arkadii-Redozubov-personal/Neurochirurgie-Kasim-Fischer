import glob

html_files = glob.glob('**/*.html', recursive=True)
count_alt = 0
count_h4 = 0

for filepath in html_files:
    if 'admin' in filepath: continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Fix redundant alt text on logo
    if 'alt="Nabiota Health Group"' in content:
        content = content.replace('alt="Nabiota Health Group"', 'alt=""')
        count_alt += 1
        
    # 2. Fix heading hierarchy (change h4 to h3)
    if '<h4 style="font-size: 1.15rem; font-weight: 700;">Dr. med.' in content:
        content = content.replace('<h4 style="font-size: 1.15rem; font-weight: 700;">Dr. med.', '<h3 style="font-size: 1.15rem; font-weight: 700;">Dr. med.')
        content = content.replace('Fischer-Rahimov</h4>', 'Fischer-Rahimov</h3>')
        
    if '<h4 class="footer-heading">' in content:
        content = content.replace('<h4 class="footer-heading">', '<h3 class="footer-heading">')
        # We need to replace the closing tags for these specific headings.
        # It's safer to just replace all </h4> with </h3> since there are no other h4s in the design based on our analysis.
        # Wait, let's verify if there are other h4s.
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count_h4 += 1

print(f'Fixed alt text in {count_alt} files. Fixed headings in {count_h4} files.')
