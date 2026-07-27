import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Change the burger menu breakpoint from 1250px to 1350px
css_content = css_content.replace('@media (max-width: 1250px) {', '@media (max-width: 1350px) {')

# Remove the shrinking font sizes for nav-links
css_content = css_content.replace('''@media (max-width: 1350px) {
  .nav-links { gap: 20px; font-size: 0.85rem; }
}''', '')

# Remove the inner parts of the old 1250px media query that shrunk fonts
# Since we replaced the start of the 1250px media query with 1350px earlier, 
# wait, there were TWO @media (max-width: 1250px) blocks!
# One at line 307, one at line 1308.
# The replace above would have changed BOTH to @media (max-width: 1350px) {

css_content = css_content.replace('''  .nav-links { gap: 12px; font-size: 0.8rem; }
  .logo { font-size: 1.1rem; }''', '')

# Let's just do a clean replace to ensure no leftover shrinking:
css_content = css_content.replace('font-size: 0.85rem;', '')
css_content = css_content.replace('font-size: 0.8rem;', '')

# Also, if they want the text in the buttons to be wider, maybe I should make the base font size slightly larger.
css_content = css_content.replace('.nav-links {\n      display: flex; gap: 40px; font-size: 0.9rem; font-weight: 500;\n    }', '.nav-links {\n      display: flex; gap: 40px; font-size: 1rem; font-weight: 500;\n    }')
css_content = css_content.replace('.nav-links { display: flex; gap: 40px; font-size: 0.9rem; font-weight: 500; }', '.nav-links { display: flex; gap: 40px; font-size: 1rem; font-weight: 500; }')

# Make the btn-book slightly larger as well
css_content = css_content.replace('padding: 14px 28px;', 'padding: 14px 32px;')

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated style.css to prevent text shrinking in header buttons")
