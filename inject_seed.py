import json
import re

with open("pages_seed.json", "r", encoding="utf-8") as f:
    pages_data = json.load(f)

# Convert dict to array of pages
pages_array = list(pages_data.values())
pages_js = "const PAGES = " + json.dumps(pages_array, ensure_ascii=False, indent=2) + ";"

with open("admin/seed.html", "r", encoding="utf-8") as f:
    content = f.read()

# Insert const PAGES after const COORDINATORS
content = re.sub(
    r'(const COORDINATORS = \[.*?\];)',
    r'\1\n\n    ' + pages_js,
    content,
    flags=re.DOTALL
)

# Insert seed logic for PAGES
seed_logic = """
        // Step 4: Clear & seed pages
        log('');
        log('🗑️  Lösche vorhandene Seiteninhalte...', '#f59e0b');
        const pagesSnap = await getDocs(collection(db, 'pages'));
        for (const d of pagesSnap.docs) await deleteDoc(doc(db, 'pages', d.id));
        log(`   ${pagesSnap.size} Seiten gelöscht.`);
        
        log('📄 Lade Seiteninhalte...', '#00c9a7');
        for (let i = 0; i < PAGES.length; i++) {
          await addDoc(collection(db, 'pages'), PAGES[i]);
          log(`   ✅ ${i + 1}/${PAGES.length}: ${PAGES[i].name}`, '#86efac');
        }
"""

content = re.sub(
    r'(setProgress\(100\);)',
    seed_logic.strip() + '\n\n        \\1',
    content
)

# Update finish log
content = re.sub(
    r'(log\(`   • \$\{COORDINATORS\.length\} Koordinatoren`, \'#86efac\'\);)',
    r'\1\n        log(`   • ${PAGES.length} Seiten`, \'#86efac\');',
    content
)

with open("admin/seed.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated seed.html with PAGES data.")
