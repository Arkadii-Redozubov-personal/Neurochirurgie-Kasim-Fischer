from PIL import Image

# Load the generated sprite sheet
sprite_path = r"C:\Users\arkad\.gemini\antigravity-ide\brain\b8b862da-a2e2-4be0-825b-474c1ae17f29\medical_icons_sprite_1786449816618.png"
img = Image.open(sprite_path).convert("RGBA")

# Make black transparent
datas = img.getdata()
new_data = []
threshold = 30
for item in datas:
    # change all black (also shades of blacks) pixels to transparent
    if item[0] < threshold and item[1] < threshold and item[2] < threshold:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(item)

img2 = Image.new("RGBA", img.size)
img2.putdata(new_data)

w, h = img2.size
part_w = w // 5

names = ['icon_spine.png', 'icon_disc.png', 'icon_nerves.png', 'icon_brain.png', 'icon_pain.png']
out_dir = r"c:\Users\arkad\Downloads\vertex\img"

for i in range(5):
    left = i * part_w
    right = (i + 1) * part_w
    icon = img2.crop((left, 0, right, h))
    
    # Optionally, we don't tight crop if we want them to be uniform size, 
    # but the image generation might have placed them unevenly. 
    # Let's crop to tight bound, then pad to a square 256x256
    bbox = icon.getbbox()
    if bbox:
        icon = icon.crop(bbox)
        # Create a blank 256x256 image
        square = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
        # Paste the icon into the center
        iw, ih = icon.size
        # Scale down if it's larger than 200
        if iw > 200 or ih > 200:
            ratio = min(200/iw, 200/ih)
            new_w, new_h = int(iw*ratio), int(ih*ratio)
            icon = icon.resize((new_w, new_h), Image.Resampling.LANCZOS)
            iw, ih = new_w, new_h
        
        offset = ((256 - iw) // 2, (256 - ih) // 2)
        square.paste(icon, offset)
        icon = square

    icon.save(f"{out_dir}\\{names[i]}")
    
print("Icons processed and saved!")
