from __future__ import annotations

from typing import Dict, List

from pydantic import BaseModel, Field

from app.models.todo import Priority


class UserStatsResponse(BaseModel):
    user_id: int
    username: str
    plan: str
    total_todos: int
    completed_todos: int
    pending_todos: int
    completion_rate: float
    max_active_todos: int
    by_priority: Dict[str, int]
    by_category: Dict[str, int]


class BulkCompleteRequest(BaseModel):
    todo_ids: List[int] = Field(..., min_length=1, max_length=50)


class BulkCompleteResponse(BaseModel):
    completed_count: int
    todo_ids: List[int]
    notifications_queued: int
