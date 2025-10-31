import os, shutil
import argostranslate.package
import argostranslate.translate

SRC_DIR = "docs"
TMP_FR_DIR = "tmp_docs_fr"
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

for filename in os.listdir(SRC_DIR):
    if filename.endswith(".md"):
        with open(f"{SRC_DIR}/{filename}", "r", encoding="utf-8") as f:
            text = f.read()
        french = trans.translate(text)
        with open(f"{TMP_FR_DIR}/{filename}", "w", encoding="utf-8") as f:
            f.write(french)
    elif os.path.isdir(f"{SRC_DIR}/{filename}"):
        # Recursively copy non-markdown directories (like images or nested folders)
        shutil.copytree(f"{SRC_DIR}/{filename}", f"{TMP_FR_DIR}/{filename}", dirs_exist_ok=True)
    else:
        # Copy over any non-markdown files
        shutil.copy2(f"{SRC_DIR}/{filename}", f"{TMP_FR_DIR}/{filename}")
