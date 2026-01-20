import os
from datetime import datetime

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def current_timestamp():
    return datetime.utcnow().isoformat()
