import requests
from src.utils import ensure_dir, current_timestamp
import os

WEBSITES = [
    "https://stripe.com",
    "https://airbnb.com",
    "https://slack.com",
    "https://notion.so",
    "https://shopify.com"
]

RAW_PATH = "data/raw"

def crawl_websites():
    ensure_dir(RAW_PATH)

    results = []

    for site in WEBSITES:
        try:
            response = requests.get(site, timeout=10)
            site_name = site.replace("https://", "").replace(".", "_")

            site_dir = os.path.join(RAW_PATH, site_name)
            ensure_dir(site_dir)

            html_file = os.path.join(site_dir, "homepage.html")
            meta_file = os.path.join(site_dir, "metadata.txt")

            with open(html_file, "w", encoding="utf-8") as f:
                f.write(response.text)

            with open(meta_file, "w") as f:
                f.write(f"""
URL: {site}
STATUS: {response.status_code}
CRAWL_TIME: {current_timestamp()}
""")

            results.append(site)

        except Exception as e:
            print(f"Failed to crawl {site}: {e}")

    return results
