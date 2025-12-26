from dotenv import load_dotenv
load_dotenv()

import os
import time
import json
import pandas as pd
from fredapi import Fred



BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
PARQUET_DIR = os.path.join(DATA_DIR, "parquet")
MANIFEST_PATH = os.path.join(DATA_DIR, "manifest.json")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PARQUET_DIR, exist_ok=True)


def load_fred_series(series_id, api_key=None):
    parquet_path = os.path.join(PARQUET_DIR, f"{series_id}.parquet")

    if os.path.exists(parquet_path):
        return pd.read_parquet(parquet_path)

    fred = Fred(api_key=api_key)
    data = fred.get_series(series_id)

    df = data.to_frame(name=series_id)
    df.index.name = "date"

    df.to_csv(os.path.join(RAW_DIR, f"{series_id}.csv"))
    df.to_parquet(parquet_path)

    _register_manifest(series_id)

    return df


def _register_manifest(series_id):
    manifest = {}
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH, "r") as f:
            manifest = json.load(f)

    manifest[series_id] = {
        "parquet": f"{series_id}.parquet",
        "registered_at": time.time()
    }

    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)
