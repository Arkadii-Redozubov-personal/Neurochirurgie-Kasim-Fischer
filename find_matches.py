import re
import io

with open('c:/Users/arkad/Downloads/vertex/presseschau.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'<a href="(artikel_\d+\.pdf)".*?<img src="img/([^"]+)"', html, re.DOTALL)
with io.open('c:/Users/arkad/Downloads/vertex/matches.txt', 'w', encoding='utf-8') as f:
    for m in matches:
        f.write(f"{m[0]} -> {m[1]}\n")
