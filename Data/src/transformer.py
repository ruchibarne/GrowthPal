import json
import os
from src.utils import ensure_dir, current_timestamp

PROCESSED_PATH = "data/processed"
STANDARD_PATH = "data/processed/standardized"

def transform_data():
    ensure_dir(STANDARD_PATH)

    for file in os.listdir(PROCESSED_PATH):
        if not file.endswith("_extracted.json"):
            continue

        website = file.replace("_extracted.json", "").replace("_", ".")

        with open(os.path.join(PROCESSED_PATH, file)) as f:
            data = json.load(f)

        records = []
        for section, content in data.items():
            records.append({
                "website": website,
                "section": section,
                "content": content,
                "crawl_timestamp": current_timestamp(),
                "isActive": bool(content)
            })

        out_file = os.path.join(STANDARD_PATH, f"{website}.json")
        with open(out_file, "w") as f:
            json.dump(records, f, indent=2)
