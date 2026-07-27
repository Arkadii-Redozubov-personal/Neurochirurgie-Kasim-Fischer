import os

CSS_PATH = 'c:/Users/arkad/Downloads/vertex/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add slideshow CSS
slideshow_css = '''
/* Hero Slideshow CSS */
.hero-bg-slider {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  z-index: 0;
  overflow: hidden;
}
.hero-bg-slide {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-size: cover;
  background-position: center;
  opacity: 0;
  animation: bg-crossfade 18s infinite;
}
/* We have 3 images, so 18s total, 6s each */
.hero-bg-slide:nth-child(1) { animation-delay: 0s; }
.hero-bg-slide:nth-child(2) { animation-delay: 6s; }
.hero-bg-slide:nth-child(3) { animation-delay: 12s; }

@keyframes bg-crossfade {
  0% { opacity: 0; transform: scale(1.05); }
  10% { opacity: 1; transform: scale(1.03); }
  33% { opacity: 1; transform: scale(1.01); }
  43% { opacity: 0; transform: scale(1); }
  100% { opacity: 0; transform: scale(1.05); }
}

.hero-overlay {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: linear-gradient(to right, rgba(9, 31, 34, 0.9) 0%, rgba(9, 31, 34, 0.4) 100%);
  z-index: 1;
}

.hero-inner .container {
  position: relative;
  z-index: 2;
}
'''

if 'bg-crossfade' not in css_content:
    css_content += '\n' + slideshow_css

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Added slideshow CSS to style.css")
