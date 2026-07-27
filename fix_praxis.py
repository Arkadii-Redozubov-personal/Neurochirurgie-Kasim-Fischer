import os

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace(
        'style="margin-top: 140px; margin-bottom: 80px;"',
        'style="margin-top: 140px; margin-bottom: 30px;"'
    )
    
    new_content = new_content.replace(
        'style="font-size: 3.5rem;"',
        'style="font-size: 2.8rem;"'
    )

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

root_dir = 'c:/Users/arkad/Downloads/vertex'
process_file(f"{root_dir}/praxis-schwerpunkte.html")
for lang in ['en', 'ru', 'tr', 'ar']:
    path = f"{root_dir}/{lang}/praxis-schwerpunkte.html"
    if os.path.exists(path):
        process_file(path)
