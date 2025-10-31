import os
from argostranslate import package, translate

import shutil
import urllib.request

SRC_DIR = "docs"
TMP_FR_DIR = "tmp_docs_fr"

MODEL_URL = "https://www.argosopentech.com/argospm/packages/translate-en_fr-1_2.argosmodel"
MODEL_PATH = "translate-en_fr.argosmodel"

# Install model if needed
if not os.path.exists(MODEL_PATH):
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    package.install_from_path(MODEL_PATH)

translate.load_installed_languages()
langs = translate.get_installed_languages()
from_lang = [l for l in langs if l.code == "en"][0]
to_lang = [l for l in langs if l.code == "fr"][0]
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
