import json
import os
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv
from openai import OpenAI


def timed(call):
    start = time.perf_counter()
    output = call()
    return {"latency_seconds": round(time.perf_counter() - start, 3), "output": output}


def call_ollama(prompt: str) -> str:
    response = httpx.post(
        f"{os.getenv('OLLAMA_URL', 'http://127.0.0.1:11434')}/api/chat",
        json={
            "model": os.getenv("OLLAMA_MODEL", "qwen3:4b"),
            "stream": False,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=180,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]


def main() -> None:
    load_dotenv()
    client = OpenAI()
    prompts = json.loads(Path("prompts.json").read_text(encoding="utf-8"))
    results = []
    for prompt in prompts:
        api = timed(lambda: client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"), input=prompt
        ).output_text)
        local = timed(lambda: call_ollama(prompt))
        results.append({"prompt": prompt, "api": api, "local": local, "human_scores": {"api": None, "local": None}})
    Path("results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Đã ghi results.json; hãy chấm quality trên cùng rubric.")


if __name__ == "__main__":
    main()
