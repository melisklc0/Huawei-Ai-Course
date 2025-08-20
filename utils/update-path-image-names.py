import os
import re

note_path = r'D:\Üniversite\Huawei-Ai-Course\notes\Speech-Processing.md'
target_folder = 'speech-processing'  # yeni klasör adı
new_note_path = r'D:\Üniversite\Huawei-Ai-Course\notes\Speech-Processing-updated.md'

with open(note_path, encoding='utf-8') as f:
    content = f.read()

# Görsel referanslarını sırayla bul
img_refs = re.findall(r'!\[.*?\]\(\.\./notes-images/(image[-\w]+\.png)\)', content)

# Eski referansları yeni referanslarla değiştir
for idx, old_img in enumerate(img_refs, 1):
    new_img = f"{idx:02d}-{old_img}"
    old_path = f'../notes-images/{old_img}'
    new_path = f'../notes-images/{target_folder}/{new_img}'
    content = content.replace(old_path, new_path, 1)  # sırayla değiştir

with open(new_note_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated note saved as: {new_note_path}")