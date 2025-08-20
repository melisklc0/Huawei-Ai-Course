import os
import re
import shutil

# Not dosyasının yolu ve hedef klasör
note_path = r'D:\Üniversite\Huawei-Ai-Course\notes\Speech-Processing.md'
images_dir = r'd:\Üniversite\Huawei-Ai-Course\images'
target_dir = r'D:\Üniversite\Huawei-Ai-Course\images\speech-processing'

# Hedef klasörü oluştur
os.makedirs(target_dir, exist_ok=True)

# Not dosyasındaki görsel referanslarını sırayla bul
with open(note_path, encoding='utf-8') as f:
    content = f.read()

# Markdown görsel referanslarını bul
img_refs = re.findall(r'!\[.*?\]\(\.\./notes-images/(image[-\w]+\.png)\)', content)

# Her görseli sıralı ve yeni isimle kopyala
for idx, img_name in enumerate(img_refs, 1):
    src = os.path.join(images_dir, img_name)
    dst = os.path.join(target_dir, f"{idx:02d}-{img_name}")
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied: {src} -> {dst}")
    else:
        print(f"Not found: {src}")