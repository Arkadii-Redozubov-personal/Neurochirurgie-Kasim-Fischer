import sys, codecs
import re

with open('sync_cms.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix all multiline f-strings that use single quotes instead of triple quotes
text = re.sub(r'reviews_html \+= f\'        <div class=\"testimonial-card fade-in\">.*?        </div>\n\'', 
              r'reviews_html += f\'\'\'        <div class=\"testimonial-card fade-in\">\n          <div class=\"testimonial-stars\">{stars_html}</div>\n          <p class=\"testimonial-text\">\"{text_val}\"</p>\n          <div class=\"testimonial-author\">\n            <div class=\"author-avatar\">{avatar}</div>\n            <div class=\"author-info\">\n              <div class=\"author-name\">{author}</div>\n            </div>\n          </div>\n        </div>\n\'\'\'', 
              text, flags=re.DOTALL)

text = re.sub(r'reviews_html \+= \'      </div>\n      <!-- REVIEWS_END -->\'', 
              r'reviews_html += \'\'\'      </div>\n      <!-- REVIEWS_END -->\'\'\'', text)

with open('sync_cms.py', 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed multiline strings.')
