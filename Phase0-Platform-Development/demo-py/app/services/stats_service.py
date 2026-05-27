from __future__ import annotations

from collections import Counter

from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundError
from app.crud import todo as crud_todo
from app.crud import user as crud_user
from app.schemas.stats import UserStatsResponse


class StatsService:
    def get_user_stats(self, db: Session, user_id: int) -> UserStatsResponse:
        user = crud_user.get(db, id=user_id)
        if not user:
            raise NotFoundError("User không tồn tại")

        todos = crud_todo.get_multi(db, user_id=user_id, limit=10000)
        total = len(todos)
        completed = sum(1 for t in todos if t.completed)
        pending = total - completed
        rate = round((completed / total) * 100, 2) if total else 0.0

        by_priority = Counter(t.priority.value for t in todos)
        by_category = Counter(
            t.category.name if t.category else "Không phân loại" for t in todos
        )

        return UserStatsResponse(
            user_id=user.id,
            username=user.username,
            plan=user.plan.value,
            total_todos=total,
            completed_todos=completed,
            pending_todos=pending,
            completion_rate=rate,
            max_active_todos=user.max_active_todos,
            by_priority=dict(by_priority),
            by_category=dict(by_category),
        )


stats_service = StatsService()
