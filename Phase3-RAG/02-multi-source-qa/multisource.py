from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path

import chromadb
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader


def chunks(text: str, size: int = 1000, overlap: int = 150) -> list[str]:
    text = " ".join(text.split())
    return [text[start : start + size] for start in range(0, len(text), size - overlap) if text[start : start + size]]


def read_source(source: str) -> tuple[str, str, str]:
    if source.startswith(("http://", "https://")):
        response = requests.get(source, timeout=15, headers={"User-Agent": "learning-rag-bot/1.0"})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for element in soup(["script", "style", "nav", "footer"]):
            element.decompose()
        return source, "website", soup.get_text(" ")
    path = Path(source)
    if path.suffix.lower() == ".pdf":
        return path.name, "pdf", "\n".join(page.extract_text() or "" for page in PdfReader(path).pages)
    return path.name, "notion_export" if "notion" in str(path).lower() else "file", path.read_text(encoding="utf-8")


def collection():
    return chromadb.PersistentClient(path=".chroma").get_or_create_collection("multi_source", metadata={"hnsw:space": "cosine"})


def embeddings(client: OpenAI, texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"), input=texts)
    return [item.embedding for item in response.data]


def ingest(sources: list[str]) -> None:
    client, store = OpenAI(), collection()
    for raw_source in sources:
        name, source_type, text = read_source(raw_source)
        parts = chunks(text)
        ids = [hashlib.sha256(f"{name}:{index}:{part}".encode()).hexdigest() for index, part in enumerate(parts)]
        store.upsert(
            ids=ids,
            documents=parts,
            embeddings=embeddings(client, parts),
            metadatas=[{"source": name, "source_type": source_type, "chunk": index} for index in range(len(parts))],
        )
        print(f"{name}: {len(parts)} chunks")


def search(query: str, source_type: str | None) -> None:
    client = OpenAI()
    result = collection().query(
        query_embeddings=embeddings(client, [query]),
        n_results=6,
        where={"source_type": source_type} if source_type else None,
    )
    context = "\n\n".join(
        f"[{meta['source']}#{meta['chunk']}] {doc}"
        for doc, meta in zip(result["documents"][0], result["metadatas"][0])
    )
    answer = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        instructions="Chỉ trả lời từ context và trích dẫn [source#chunk]. Không đủ evidence thì nói không tìm thấy.",
        input=f"Question: {query}\n\nContext:\n{context}",
    )
    print(answer.output_text)


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    loader = sub.add_parser("ingest")
    loader.add_argument("sources", nargs="+")
    query = sub.add_parser("ask")
    query.add_argument("question")
    query.add_argument("--type", choices=["pdf", "website", "notion_export", "file"])
    args = parser.parse_args()
    ingest(args.sources) if args.command == "ingest" else search(args.question, args.type)


if __name__ == "__main__":
    main()
