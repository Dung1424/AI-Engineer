import csv
import json
from pathlib import Path


def read_csv(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def build_report(records):
    scores = [float(record["score"]) for record in records]
    return {"row_count": len(scores),
            "mean_score": sum(scores) / len(scores) if scores else None}


def write_json(path, report):
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")
