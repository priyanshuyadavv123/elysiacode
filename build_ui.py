import re

with open('web/index.html.bak', 'r') as f:
    orig_html = f.read()

# Find the start of tab-handbook
tab_handbook_pos = orig_html.find('<section id="tab-handbook"')
tail_content = orig_html[tab_handbook_pos:]

# Remove the trailing </div>\n</body>\n</html> from tail_content if present
# so we can close app-layout and app-main-viewport properly
tail_content = re.sub(r'</div>\s*<!--\s*===+\s*MODAL 1:.*?-->', r'<!-- === MODAL 1: -->', tail_content, flags=re.DOTALL)
# Let's inspect where the closing </div> of app-wrapper was
closing_app_wrapper_pos = tail_content.find('</div>\n\n  <!--\n    ===========================================================================\n    MODAL 1:')
if closing_app_wrapper_pos != -1:
    tabs_part = tail_content[:closing_app_wrapper_pos]
    modals_part = tail_content[closing_app_wrapper_pos + 7:] # skip </div>\n\n
else:
    # fallback search
    split_target = '<div id="modal-lab-exporter"'
    idx = tail_content.find(split_target)
    # search backwards for </div>
    div_idx = tail_content.rfind('</div>', 0, idx)
    tabs_part = tail_content[:div_idx]
    modals_part = tail_content[idx:]

print('Tabs part length:', len(tabs_part))
print('Modals part length:', len(modals_part))
