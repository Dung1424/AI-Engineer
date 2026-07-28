import argparse
import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()
    documents = json.loads(Path("documents.json").read_text(encoding="utf-8"))
    model = SentenceTransformer(MODEL)
    vectors = model.encode([item["text"] for item in documents], normalize_embeddings=True)
    query = model.encode([args.query], normalize_embeddings=True)[0]
    scores = vectors @ query
    for index in np.argsort(scores)[::-1][: args.top_k]:
        print(f"{scores[index]:.3f} · {documents[index]['id']} · {documents[index]['text']}")


if __name__ == "__main__":
    main()
