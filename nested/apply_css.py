#!/usr/bin/env python3
# Extract CSS from final doc.html and apply to Documentation Beewant (1).html

# Read final doc.html and extract CSS
with open('final doc.html', 'r', encoding='utf-8') as f:
    final_content = f.read()

# Find the CSS block in final doc.html
style_start = final_content.find('<style>')
style_end = final_content.find('</style>') + len('</style>')

if style_start == -1 or style_end == -1:
    print("ERROR: Could not find CSS in final doc.html")
    exit(1)

css_block = final_content[style_start:style_end]
print(f"Extracted CSS ({len(css_block)} characters)")

# Read Documentation Beewant (1).html
with open('Documentation Beewant (1).html', 'r', encoding='utf-8') as f:
    doc_content = f.read()

# Find the existing CSS block in Documentation Beewant (1).html
doc_style_start = doc_content.find('<style>')
doc_style_end = doc_content.find('</style>') + len('</style>')

if doc_style_start == -1 or doc_style_end == -1:
    print("ERROR: Could not find CSS in Documentation Beewant (1).html")
    exit(1)

# Replace the CSS block
new_content = doc_content[:doc_style_start] + css_block + doc_content[doc_style_end:]

# Write the result
with open('Documentation Beewant (1).html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✓ CSS from final doc.html applied to Documentation Beewant (1).html")
