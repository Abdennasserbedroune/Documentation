import re
import sys

# Read the Markdown content
try:
    with open('content_fr.md', 'r') as f:
        md_content = f.read()
except FileNotFoundError:
    print("content_fr.md not found. Make sure you generated it.")
    sys.exit(1)

def convert_to_html(text_block):
    lines = text_block.split('\n')
    html = []
    
    in_code_block = False
    code_lang = ""
    code_content = []
    
    in_table = False
    table_content = []
    
    in_ul = False
    
    for line in lines:
        stripped = line.rstrip()
        
        # --- Code Blocks ---
        if stripped.startswith('```'):
            if in_code_block:
                # End code block
                in_code_block = False
                code_text = '\n'.join(code_content).replace('<', '&lt;').replace('>', '&gt;')
                
                # Use structure similar to original file
                block_html = f'''<div class="code-block">
                  <div class="code-content">
                    <pre><code class="language-{code_lang}">{code_text}</code></pre>
                  </div>
                </div>'''
                html.append(block_html)
                code_content = []
            else:
                # Start code block
                in_code_block = True
                code_lang = stripped.strip('`').strip() or 'text'
                # Close any open lists before code block
                if in_ul:
                    html.append('</ul>')
                    in_ul = False
            continue
            
        if in_code_block:
            code_content.append(stripped)
            continue

        # --- Tables ---
        is_table_row = stripped.strip().startswith('|')
        if is_table_row:
            if not in_table:
                in_table = True
                table_content = [stripped]
                # Close list if open
                if in_ul:
                    html.append('</ul>')
                    in_ul = False
            else:
                table_content.append(stripped)
            continue
        elif in_table:
            # End of table
            in_table = False
            # Process table content
            html.append('<table>')
            # Check for header
            header_row = table_content[0]
            start_body = 0
            if len(table_content) > 1 and set(table_content[1].strip()) <= set('| -:'):
                cols = [c.strip() for c in header_row.strip('|').split('|')]
                html.append('<thead><tr>' + ''.join(f'<th>{c}</th>' for c in cols) + '</tr></thead>')
                start_body = 2 
            else:
                # No header row separator, treat first row as body? usually markdown tables require separator
                pass
            
            html.append('<tbody>')
            for row in table_content[start_body:]:
                cols = [c.strip() for c in row.strip('|').split('|')]
                html.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cols) + '</tr>')
            html.append('</tbody></table>')
            table_content = []

        # --- Lists ---
        # Simple detection for "- " or "* "
        is_list_item = stripped.strip().startswith('- ') or stripped.strip().startswith('* ')
        if is_list_item:
            if not in_ul:
                html.append('<ul>')
                in_ul = True
            
            content = stripped.strip()[2:]
            # Inline formatting
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'`(.*?)`', r'<code>\1</code>', content)
            content = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', content)
            
            html.append(f'<li>{content}</li>')
            continue
        else:
            if in_ul and stripped.strip():
                html.append('</ul>')
                in_ul = False

        # --- Headers ---
        if stripped.startswith('#'):
            level = len(stripped.split(' ')[0])
            content = stripped[level:].strip()
            # ID generation
            slug = re.sub(r'[^a-z0-9]+', '-', content.lower()).strip('-')
            html.append(f'<h{level} id="{slug}">{content}</h{level}>')
            continue

        # --- Info Cards (💡) ---
        if '💡' in stripped:
            content = stripped.replace('💡', '').strip()
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            html.append(f'<div class="info-card"><div class="info-card-icon">💡</div><div class="info-card-content"><p>{content}</p></div></div>')
            continue

        # --- REQUÊTE Block ---
        if "REQUÊTE :" in stripped:
             html.append(f'<div class="note-card"><strong>REQUÊTE :</strong></div>')
             continue

        # --- Standard Paragraphs ---
        if stripped:
            content = stripped
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'`(.*?)`', r'<code>\1</code>', content)
            content = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', content)
            html.append(f'<p>{content}</p>')
            
    if in_ul:
        html.append('</ul>')
    if in_code_block: # Should not happen if well formed
        pass 
        
    return '\n'.join(html)

# Split by sections
sections = {}
current_sec = "overview"
buffer = []

for line in md_content.split('\n'):
    if line.strip() == "## Index":
        sections[current_sec] = '\n'.join(buffer)
        current_sec = "indexes"
        buffer = [line]
    elif line.strip() == "## Collections":
        sections[current_sec] = '\n'.join(buffer)
        current_sec = "collections"
        buffer = [line]
    elif line.strip() == "## Chat":
        sections[current_sec] = '\n'.join(buffer)
        current_sec = "chat"
        buffer = [line]
    else:
        buffer.append(line)
sections[current_sec] = '\n'.join(buffer)

# Generate HTML for each section
final_html_parts = []

# Overview
final_html_parts.append('<section class="doc-page" data-page="overview" id="overview" data-active="true">')
final_html_parts.append(convert_to_html(sections.get("overview", "")))
final_html_parts.append('</section>')

# Indexes
final_html_parts.append('<section class="doc-page" data-page="indexes" id="indexes" data-active="false">')
final_html_parts.append(convert_to_html(sections.get("indexes", "")))
final_html_parts.append('</section>')

# Collections
final_html_parts.append('<section class="doc-page" data-page="collections" id="collections" data-active="false">')
final_html_parts.append(convert_to_html(sections.get("collections", "")))
final_html_parts.append('</section>')

# Chat
final_html_parts.append('<section class="doc-page" data-page="chat" id="chat" data-active="false">')
final_html_parts.append(convert_to_html(sections.get("chat", "")))
final_html_parts.append('</section>')

# Agents & Sources (Empty placeholders to avoid JS errors)
final_html_parts.append('<section class="doc-page" data-page="agents" id="agents" data-active="false"></section>')
final_html_parts.append('<section class="doc-page" data-page="sources" id="sources" data-active="false"></section>')


# Read target HTML file
target_file = 'Beewant-Documentation-Clean-Template-11 (3) copy.html'
with open(target_file, 'r') as f:
    original_lines = f.readlines()

# Find insertion points
start_insert = -1
end_insert = -1

for i, line in enumerate(original_lines):
    if '<div class="content-inner">' in line:
        start_insert = i + 1
    if '</main>' in line:
        # Assuming </main> is preceeded by </div></div>
        end_insert = i - 2 
        # Check if lines before are div closers
        # Lines 8152, 8153 were divs. 8155 was /main.
        # So i-2 (8153) is </div>? No, i is index of </main>.
        # i = 8155 approx. i-1 = space? i-2 = </div>.
        # Let's be safe: Find start_insert, keep everything BEFORE.
        # Keep everything AFTER end_insert.
        # But end_insert needs to be precise.
        pass

# Harder approach: Count open/close divs? No.
# Just use the grep knowledge:
# Start: 3209 (after <div class="content-inner">)
# End: 8151 (before last two closing divs)
# Wait, grep numbers are 1-based. Python list is 0-based.
# Grep: 3208: <div class="content-inner"> -> Index 3207.
# Grep: 8155: </main> -> Index 8154.
# So keep 0 to 3207 inclusive (up to content-inner opening).
# Then insert new HTML.
# Then find where </main> is in python list.
# Keep from (index of </main>) - 2 to end.
# (Assuming standard indentation of closing divs).

main_close_idx = -1
for i, line in enumerate(original_lines):
    if '</main>' in line:
        main_close_idx = i
        break

if start_insert == -1 or main_close_idx == -1:
    print("Could not find start or end markers.")
    sys.exit(1)

# Logic:
# Keep 0..start_insert-1 (lines up to content-inner open)
# Insert new HTML
# Keep main_close_idx-2..end (closing divs + main + rest)
# Note: main_close_idx is index of </main>. -1 is empty line? -2 is </div>. -3 is </div>.
# Let's verify closing divs.
# If I just keep </main> and everything after, and I manually append </div></div> before it, strict structure is maintained.

new_file_content = original_lines[:start_insert] 
new_file_content.append('\n'.join(final_html_parts))
new_file_content.append('\n      </div>\n    </div>\n') # Close content-inner and content-grid manually
new_file_content.extend(original_lines[main_close_idx:]) # Append from </main> onwards

with open(target_file, 'w') as f:
    f.writelines(new_file_content)

print("Successfully updated file.")
