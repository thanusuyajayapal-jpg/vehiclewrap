import os
import re
import glob

image_files = [
    "car wrap (1).jpg", "car wrap (2).jpg", "car wrap (3).jpg", "car wrap (4).jpg", "car wrap (5).jpg",
    "car wrap (6).jpg", "car wrap (7).jpg", "car wrap (8).jpg", "car wrap (9).jpg", "car wrap (10).jpg",
    "car wrap (11).jpg", "car wrap (12).jpg", "car wrap (13).jpg", "car wrap (14).jpg", "car wrap (15).jpg",
    "car wrap (16).jpg", "car wrap (17).jpg", "car wrap (18).jpg", "car wrap (19).jpg", "car wrap (20).jpg",
    "car wrap (21).jpg", "car wrap (22).jpg", "car wrap (23).jpg", "car wrap (24).jpg", "car wrap (25).jpg",
    "car wrap (26).jpg", "car wrap (27).jpg",
    "pexels-107932638-18988952.jpg", "pexels-107932638-29032784.jpg",
    "pexels-andres-chirrisco-174853810-20612567.jpg", "pexels-artempodrez-8985971.jpg",
    "pexels-autorecords-10126666.jpg", "pexels-autorecords-10162529.jpg",
    "pexels-autorecords-10292240.jpg", "pexels-ayyeee-ayyeee-434363205-19868900.jpg",
    "pexels-bertellifotografia-10182880.jpg", "pexels-bulat843-1243575272-31154212.jpg"
]

img_idx = 0

def get_next_img():
    global img_idx
    img = "image/" + image_files[img_idx % len(image_files)]
    img_idx += 1
    return img

html_files = glob.glob("*.html")

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace all unsplash links
    def replacer(match):
        return get_next_img()
        
    new_content = re.sub(r'https://images\.unsplash\.com/[^"\']+', replacer, content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"No changes in {file}")
