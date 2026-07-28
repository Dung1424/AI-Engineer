import argparse
import os
import re
from typing import Literal, TypedDict

from dotenv import load_dotenv
from langgraph.graph import END, START, StateGraph
from openai import OpenAI
from pydantic import BaseModel


class Classification(BaseModel):
    intent: Literal["order_status", "refund", "technical", "other"]
    risk: Literal["low", "high"]


class State(TypedDict, total=False):
    ticket: str
    intent: str
    risk: str
    order_context: str
    answer: str
    needs_human: bool


ORDERS = {"A102": "Đã giao ngày 18/07/2026", "B205": "Đang vận chuyển, dự kiến 22/07/2026"}
load_dotenv()
client = OpenAI()


def classify(state: State) -> State:
    result = client.responses.parse(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        input=state["ticket"],
        text_format=Classification,
    ).output_parsed
    if result is None:
        return {"intent": "other", "risk": "high"}
    return {"intent": result.intent, "risk": result.risk}


def lookup(state: State) -> State:
    match = re.search(r"\b[A-Z]\d{3}\b", state["ticket"])
    context = ORDERS.get(match.group(0), "Không tìm thấy đơn") if match else "Không có mã đơn"
    return {"order_context": context}


def draft(state: State) -> State:
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        instructions="Soạn phản hồi hỗ trợ ngắn gọn. Không hứa hoàn tiền hoặc hành động chưa thực hiện.",
        input=f"Ticket: {state['ticket']}\nIntent: {state['intent']}\nOrder: {state.get('order_context', 'N/A')}",
    )
    return {"answer": response.output_text, "needs_human": False}


def escalate(state: State) -> State:
    return {"answer": "Ticket cần nhân viên xem xét trước khi phản hồi.", "needs_human": True}


def route(state: State) -> str:
    return "escalate" if state["risk"] == "high" or state["intent"] == "refund" else "lookup"


graph = StateGraph(State)
graph.add_node("classify", classify)
graph.add_node("lookup", lookup)
graph.add_node("draft", draft)
graph.add_node("escalate", escalate)
graph.add_edge(START, "classify")
graph.add_conditional_edges("classify", route, {"lookup": "lookup", "escalate": "escalate"})
graph.add_edge("lookup", "draft")
graph.add_edge("draft", END)
graph.add_edge("escalate", END)
app = graph.compile()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticket")
    print(app.invoke({"ticket": parser.parse_args().ticket}))
