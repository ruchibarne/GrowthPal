from bs4 import BeautifulSoup
from src.utils import ensure_dir
import os
import json

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

def extract_sections():
    ensure_dir(PROCESSED_PATH)

    for site_folder in os.listdir(RAW_PATH):
        site_path = os.path.join(RAW_PATH, site_folder)
        html_path = os.path.join(site_path, "homepage.html")

        if not os.path.exists(html_path):
            continue

        with open(html_path, encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        sections = {
            "navbar": soup.find("nav"),
            "footer": soup.find("footer"),
            "homepage": soup.find("body"),
            "case_study": soup.find(string=lambda x: x and "case" in x.lower())
        }

        extracted = {}
        for key, value in sections.items():
            extracted[key] = value.get_text(strip=True) if value else ""

        with open(
            os.path.join(PROCESSED_PATH, f"{site_folder}_extracted.json"),
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(extracted, f, indent=2)
