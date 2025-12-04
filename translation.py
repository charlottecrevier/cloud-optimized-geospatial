import os, shutil, re
import argostranslate.package
import argostranslate.translate

SRC_DIR = "docs/en"
TMP_FR_DIR = "docs/fr"
from_code = "en"
to_code = "fr"

# Download and install Argos Translate model if needed
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(lambda x: x.from_code == from_code and x.to_code == to_code, available_packages)
)
argostranslate.package.install_from_path(package_to_install.download())

argostranslate.translate.load_installed_languages()
langs = argostranslate.translate.get_installed_languages()
from_lang = [l for l in langs if l.code == from_code][0]
to_lang = [l for l in langs if l.code == to_code][0]
trans = from_lang.get_translation(to_lang)

if os.path.exists(TMP_FR_DIR):
    shutil.rmtree(TMP_FR_DIR)
os.makedirs(TMP_FR_DIR, exist_ok=True)

def escape_blocks(text):
    """
    Replaces each
    - <!-- START: ... --> ... <!-- END: ... -->
    - [ ... ]
    - ``` ... ```
    block with a unique HTML comment placeholder.
    Returns (new_text, blocks), where blocks is a list of the skipped blocks.
    """
    regex = re.compile(
        r'('
        r'<!-- START:.*?-->(?:.|\n)*?<!-- END:.*?-->'        # HTML comment blocks
        r'|```(?:.|\n)*?```'                                 # Any fenced code block
        r'|$$[^\[$$]*?\]'                                    # [ ... ] (not nested, simple)
        r')',
        re.MULTILINE
    )

    blocks = []
    def replacer(match):
        blocks.append(match.group(0))
        return f"<!--SKIP {len(blocks)-1}-->"
    new_text = regex.sub(replacer, text)
    return new_text, blocks

def restore_blocks(text, blocks):
    for idx, block in enumerate(blocks):
        text = text.replace(f"<!--SKIP {idx}-->", block)
    return text

for filename in os.listdir(SRC_DIR):
    src_path = os.path.join(SRC_DIR, filename)
    dst_path = os.path.join(TMP_FR_DIR, filename)
    if filename.endswith(".md") and os.path.isfile(src_path):
        with open(src_path, "r", encoding="utf-8") as f:
            text = f.read()
        # --- Skip/escape block translation ---
        escaped_text, blocks = escape_blocks(text)
        french_translated = trans.translate(escaped_text)
        # --- Restore blocks after translation ---
        final_text = restore_blocks(french_translated, blocks)
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(final_text)
    elif os.path.isdir(src_path):
        shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
    else:
        shutil.copy2(src_path, dst_path)
