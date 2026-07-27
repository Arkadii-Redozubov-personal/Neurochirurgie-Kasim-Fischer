import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

# Make the header wider (from 1360px max-width to 1600px max-width)
css = css.replace('calc(50vw - 680px)', 'calc(50vw - 800px)')

# Add white-space: nowrap to links so they don't break onto two lines
css = css.replace('.nav-links a { color: rgba(255,255,255,0.8); text-decoration: none; transition: 0.3s; }', '.nav-links a { color: rgba(255,255,255,0.8); text-decoration: none; transition: 0.3s; white-space: nowrap; }')

# Reduce the gap slightly to help them fit better without wrapping
css = css.replace('.nav-links { display: flex; gap: 40px; font-size: 1rem; font-weight: 500; }', '.nav-links { display: flex; gap: 32px; font-size: 1rem; font-weight: 500; }')
css = css.replace('.nav-links {\n      display: flex; gap: 40px; font-size: 1rem; font-weight: 500;\n    }', '.nav-links {\n      display: flex; gap: 32px; font-size: 1rem; font-weight: 500;\n    }')

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css to expand header width and prevent text wrap")
