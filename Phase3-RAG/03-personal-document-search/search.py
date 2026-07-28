from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def read(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        return "\n".join(page.extract_text() or "" for page in PdfReader(path).pages)
    return path.read_text(encoding="utf-8")


def split(text: str, size: int = 800) -> list[str]:
    paragraphs = [item.strip() for item in text.split("\n") if item.strip()]
    output: list[str] = []
    current = ""
    for paragraph in paragraphs:
        if current and len(current) + len(paragraph) > size:
            output.append(current)
            current = paragraph
        else:
            current = f"{current}\n{paragraph}".strip()
    if current:
        output.append(current)
    return output


def build(directory: Path) -> None:
    records = [
        {"source": path.name, "text": part}
        for path in directory.rglob("*")
        if path.suffix.lower() in {".pdf", ".txt", ".md"}
        for part in split(read(path))
    ]
    model = SentenceTransformer(MODEL)
    vectors = model.encode([item["text"] for item in records], normalize_embeddings=True)
    np.save("vectors.npy", vectors)
    Path("records.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã index {len(records)} đoạn.")


def query(text: str, top_k: int) -> None:
    records = json.loads(Path("records.json").read_text(encoding="utf-8"))
    vectors = np.load("vectors.npy")
    query_vector = SentenceTransformer(MODEL).encode([text], normalize_embeddings=True)[0]
    scores = vectors @ query_vector
    for index in np.argsort(scores)[::-1][:top_k]:
        print(f"\n{scores[index]:.3f} · {records[index]['source']}\n{records[index]['text']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    build_parser = sub.add_parser("build")
    build_parser.add_argument("directory", type=Path)
    query_parser = sub.add_parser("search")
    query_parser.add_argument("query")
    query_parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()
    build(args.directory) if args.command == "build" else query(args.query, args.top_k)


if __name__ == "__main__":
    main()
