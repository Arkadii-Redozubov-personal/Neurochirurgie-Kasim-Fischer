import os
import json
import urllib.request
import urllib.parse
from html.parser import HTMLParser
import time

def translate_text(text, target_lang):
    text = text.strip()
    if not text:
        return text
    
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=de&tl=" + target_lang + "&dt=t&q=" + urllib.parse.quote(text)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            translated = "".join([sentence[0] for sentence in result[0]])
            return translated
    except Exception as e:
        print(f"Translation failed for '{text}': {e}")
        return text

class TranslatorParser(HTMLParser):
    def __init__(self, target_lang):
        super().__init__(convert_charrefs=False)
        self.target_lang = target_lang
        self.output = []
        self.skip_tags = ['style', 'script']
        self.in_skip_tag = False
    
    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.in_skip_tag = True
        
        attr_str = ""
        for k, v in attrs:
            if v is None:
                attr_str += f' {k}'
            else:
                attr_str += f' {k}="{v}"'
        self.output.append(f"<{tag}{attr_str}>")
        
    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.in_skip_tag = False
        self.output.append(f"</{tag}>")
        
    def handle_startendtag(self, tag, attrs):
        attr_str = ""
        for k, v in attrs:
            if v is None:
                attr_str += f' {k}'
            else:
                attr_str += f' {k}="{v}"'
        self.output.append(f"<{tag}{attr_str} />")
        
    def handle_data(self, data):
        if self.in_skip_tag or not data.strip():
            self.output.append(data)
        else:
            leading = data[:len(data)-len(data.lstrip())]
            trailing = data[len(data.rstrip()):]
            text = data.strip()
            
            if len(text) > 1 and any(c.isalpha() for c in text) and text != "Deutsch (DE)":
                translated = translate_text(text, self.target_lang)
                self.output.append(leading + translated + trailing)
                time.sleep(0.05)
            else:
                self.output.append(data)
                
    def handle_entityref(self, name):
        self.output.append(f"&{name};")
        
    def handle_charref(self, name):
        self.output.append(f"&#{name};")
        
    def handle_comment(self, data):
        self.output.append(f"<!--{data}-->")
        
    def handle_decl(self, decl):
        self.output.append(f"<!{decl}>")

files = ['index.html', 'behandlungen.html', 'praxis-schwerpunkte.html', 'presseschau.html', 'sprechzeiten.html', 'unser-team.html']
langs = {'en': 'en', 'ru': 'ru', 'tr': 'tr', 'ar': 'ar'}

for lang_code, google_lang in langs.items():
    os.makedirs(lang_code, exist_ok=True)
    for f in files:
        print(f"Translating {f} to {lang_code}...")
        try:
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
        except:
            with open(f, 'r', encoding='latin-1') as file:
                content = file.read()
                
        parser = TranslatorParser(google_lang)
        parser.feed(content)
        translated_html = "".join(parser.output)
        
        translated_html = translated_html.replace('href="style.css"', 'href="../style.css"')
        translated_html = translated_html.replace('src="img/', 'src="../img/')
        translated_html = translated_html.replace("url('img/", "url('../img/")
        
        for switch_lang in ['en', 'ru', 'tr', 'ar']:
            translated_html = translated_html.replace(f'href="{switch_lang}/', f'href="../{switch_lang}/')
        
        for orig_file in files:
            translated_html = translated_html.replace(f'href="{orig_file}">Deutsch (DE)', f'href="../{orig_file}">Deutsch (DE)')
            translated_html = translated_html.replace(f'href="{orig_file}" class="active">DE', f'href="../{orig_file}">DE')
        
        if lang_code == 'en':
            translated_html = translated_html.replace('DE <span>▼', 'EN <span>▼')
        elif lang_code == 'ru':
            translated_html = translated_html.replace('DE <span>▼', 'RU <span>▼')
        elif lang_code == 'tr':
            translated_html = translated_html.replace('DE <span>▼', 'TR <span>▼')
        elif lang_code == 'ar':
            translated_html = translated_html.replace('DE <span>▼', 'AR <span>▼')
            translated_html = translated_html.replace('<html lang="de">', '<html lang="ar" dir="rtl">')
            
        if lang_code != 'ar':
            translated_html = translated_html.replace('<html lang="de">', f'<html lang="{lang_code}">')
            
        with open(os.path.join(lang_code, f), 'w', encoding='utf-8') as out_file:
            out_file.write(translated_html)

print("All translations completed!")
