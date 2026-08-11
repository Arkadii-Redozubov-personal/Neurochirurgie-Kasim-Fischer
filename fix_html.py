import os, re

files = [
    'index.html',
    'en/index.html',
    'ru/index.html',
    'tr/index.html',
    'ar/index.html'
]

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the expertise block
    pattern = r'(\s*<!-- Areas of Expertise -->\s*<div class="expertise-wrapper fade-in">.*?<div class="expertise-title">.*?</div>\s*</div>\s*</div>)'
    match = re.search(pattern, content, flags=re.DOTALL)
    
    if match:
        expertise_block = match.group(1)
        # Remove it from its current position
        content = content.replace(expertise_block, '')
        
        # Insert it after hero-main closes. 
        # hero-main ends right after trusted-expertise closes.
        # trusted-expertise looks like: <div class="trusted-expertise"> ... </div>
        # And then there is a </div> to close hero-main.
        insert_pattern = r'(<div class="trusted-expertise">.*?</div>\s*</div>\s*</div>)'
        
        # Wait, trusted-expertise contains trusted-stats, which contains trusted-stat.
        # Let's just find the "Patient satisfaction" block (the last stat) and trace the closing tags.
        # <span class="trusted-stat-label">.*?</span>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>
        
        # A safer way: just match the exact end of hero-main by looking for trusted-expertise block.
        # Since regex with .*? can be tricky, let's use a split.
        
        split_marker = 'Patient satisfaction'
        if 'Patientenzufriedenheit' in content:
            split_marker = 'Patientenzufriedenheit'
        elif 'Удовлетворенность' in content:
            split_marker = 'Удовлетворенность'
        elif 'memnuniyeti' in content:
            split_marker = 'memnuniyeti'
        elif 'رضا' in content:
            split_marker = 'رضا'
            
        # We find the split marker. Then we find the 5th </div> after it.
        # 1: close trusted-stat-text
        # 2: close trusted-stat
        # 3: close trusted-stats
        # 4: close trusted-expertise
        # 5: close hero-main
        
        # Let's just do a manual string search.
        idx = content.find(split_marker)
        if idx != -1:
            # find 5 </div>s
            div_count = 0
            search_idx = idx
            while div_count < 5:
                search_idx = content.find('</div>', search_idx) + 6
                div_count += 1
            
            # search_idx is now right after the 5th </div>.
            # We insert expertise_block here!
            new_content = content[:search_idx] + expertise_block + content[search_idx:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filepath}")
        else:
            print(f"Could not find marker in {filepath}")
    else:
        print(f"Could not find expertise block in {filepath}")
