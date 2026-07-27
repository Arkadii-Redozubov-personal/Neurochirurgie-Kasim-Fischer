import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add position relative to .hero-inner
css_content = css_content.replace('''
    .hero-inner {
      background-image: linear-gradient(to right, rgba(9, 31, 34, 0.9) 0%, rgba(9, 31, 34, 0.4) 100%), url('https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&w=1600&q=80');
      background-size: cover;
      background-position: center 20%;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      color: white;
      padding: 32px 0 80px 0;
      width: 100%;
    }''', '''
    .hero-inner {
      position: relative;
      background-image: linear-gradient(to right, rgba(9, 31, 34, 0.9) 0%, rgba(9, 31, 34, 0.4) 100%), url('https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&w=1600&q=80');
      background-size: cover;
      background-position: center 20%;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      color: white;
      padding: 32px 0 80px 0;
      width: 100%;
    }''')

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Added position: relative to .hero-inner")
