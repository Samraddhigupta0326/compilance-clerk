import json
from datetime import datetime
import os

def log_llm(text, output):
    os.makedirs("logs", exist_ok=True)

    log = {
        "timestamp": str(datetime.now()),
        "input_text": text,
        "output": output
    }

    with open("logs/llm_logs.jsonl", "a") as f:
        f.write(json.dumps(log) + "\n")