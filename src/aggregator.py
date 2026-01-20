import os
import json
import pandas as pd
from src.utils import ensure_dir

STANDARD_PATH = "data/processed/standardized"
AGG_PATH = "data/aggregated"

def aggregate_metrics():
    ensure_dir(AGG_PATH)

    rows = []

    for file in os.listdir(STANDARD_PATH):
        with open(os.path.join(STANDARD_PATH, file)) as f:
            rows.extend(json.load(f))

    df = pd.DataFrame(rows)

    metrics = {
        "total_websites": df["website"].nunique(),
        "websites_with_case_study": df[
            (df["section"] == "case_study") & (df["isActive"])
        ]["website"].nunique(),
        "content_length_by_section": df.groupby("section")["content"].apply(
            lambda x: x.str.len().mean()
        ).to_dict()
    }

    with open(os.path.join(AGG_PATH, "metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)
