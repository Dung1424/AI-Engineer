from __future__ import annotations

import argparse
import hashlib
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import chromadb
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

DB_PATH = ".chroma"
COLLECTION = "company_knowledge"


@dataclass(frozen=True)
class Chunk:
    id: str
    text: str
    source: str
    page: int
    index: int


def split_text(text: str, size: int = 1200, overlap: int = 200) -> Iterable[str]:
    clean = " ".join(text.split())
    start = 0
    while start < len(clean):
        end = min(start + size, len(clean))
        if end < len(clean):
            boundary = clean.rfind(" ", start, end)
            if boundary > start:
                end = boundary
        yield clean[start:end]
        if end == len(clean):
            break
        start = max(end - overlap, start + 1)


def load_chunks(path: Path) -> list[Chunk]:
    pages: list[tuple[int, str]]
    if path.suffix.lower() == ".pdf":
        pages = [(number, page.extract_text() or "") for number, page in enumerate(PdfReader(path).pages, 1)]
    elif path.suffix.lower() in {".txt", ".md"}:
        pages = [(1, path.read_text(encoding="utf-8"))]
    else:
        return []

    chunks: list[Chunk] = []
    for page, text in pages:
        for index, part in enumerate(split_text(text)):
            digest = hashlib.sha256(f"{path.resolve()}:{page}:{index}:{part}".encode()).hexdigest()
            chunks.append(Chunk(digest, part, path.name, page, index))
    return chunks


def get_collection():
    return chromadb.PersistentClient(path=DB_PATH).get_or_create_collection(
        COLLECTION, metadata={"hnsw:space": "cosine"}
    )


def embed(client: OpenAI, texts: list[str]) -> list[list[float]]:
    model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
    return [item.embedding for item in client.embeddings.create(model=model, input=texts).data]


def ingest(directory: Path) -> None:
    client = OpenAI()
    collection = get_collection()
    chunks = [chunk for path in directory.rglob("*") if path.is_file() for chunk in load_chunks(path)]
    if not chunks:
        raise SystemExit("Không tìm thấy PDF/TXT/MD để index.")
    for start in range(0, len(chunks), 64):
        batch = chunks[start : start + 64]
        collection.upsert(
            ids=[item.id for item in batch],
            documents=[item.text for item in batch],
            embeddings=embed(client, [item.text for item in batch]),
            metadatas=[{"source": item.source, "page": item.page, "chunk": item.index} for item in batch],
        )
    print(f"Đã index {len(chunks)} chunks; collection hiện có {collection.count()} chunks.")


def ask(question: str, top_k: int = 5) -> None:
    client = OpenAI()
    results = get_collection().query(
        query_embeddings=embed(client, [question]),
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    context = "\n\n".join(
        f"[SOURCE: {meta['source']} p.{meta['page']}]\n{text}"
        for text, meta in zip(documents, metadatas)
    )
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        instructions=(
            "Chỉ dùng CONTEXT. Trích dẫn dạng [SOURCE: file p.N] sau từng claim. "
            "Nếu context không đủ, trả lời 'Không tìm thấy trong tài liệu'."
        ),
        input=f"QUESTION:\n{question}\n\nCONTEXT:\n{context}",
    )
    print(response.output_text)


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    ingest_parser = sub.add_parser("ingest")
    ingest_parser.add_argument("directory", type=Path)
    ask_parser = sub.add_parser("ask")
    ask_parser.add_argument("question")
    ask_parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()
    ingest(args.directory) if args.command == "ingest" else ask(args.question, args.top_k)


if __name__ == "__main__":
    main()
