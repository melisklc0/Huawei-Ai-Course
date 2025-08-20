import re

note_path = r'D:\Üniversite\Huawei-Ai-Course\notes\Speech-Processing.md'
new_note_path = r'd:\Üniversite\Huawei-Ai-Course\notes\updated.md'

with open(note_path, encoding='utf-8') as f:
    content = f.read()

# ../notes-images/altklasor/dosya.png -> ../images/altklasor/dosya.png
content = re.sub(r'\.\./notes-images/([^/]+/[^)]+)', r'../images/\1', content)

with open(new_note_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("All image paths updated to use ../images/ instead of ../notes-images/")