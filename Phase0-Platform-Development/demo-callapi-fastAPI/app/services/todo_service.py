from __future__ import annotations

import logging
from typing import List, Optional

from sqlalchemy.orm import Session

from app.core.exceptions import BusinessError, ForbiddenError, NotFoundError
from app.crud import category as crud_category
from app.crud import tag as crud_tag
from app.crud import todo as crud_todo
from app.models.todo import Priority, Todo
from app.models.user import User
from app.schemas.stats import BulkCompleteResponse
from app.schemas.todo import TodoCreate, TodoUpdate
from app.workers.tasks import (
    send_todo_completed_notification,
    send_welcome_notification,
)

logger = logging.getLogger(__name__)

URGENT_TAG_NAME = "urgent"


class TodoService:
    def list_todos(self, db: Session, owner: User, **filters):
        return crud_todo.get_multi(db, user_id=owner.id, **filters)

    def get_todo(self, db: Session, todo_id: int, owner: User) -> Todo:
        todo = crud_todo.get(db, id=todo_id)
        if not todo:
            raise NotFoundError("Todo không tồn tại")
        self._ensure_owner(todo, owner)
        return todo

    def create_todo(self, db: Session, todo_in: TodoCreate, owner: User) -> Todo:
        if not owner.is_active:
            raise ForbiddenError("User đã bị vô hiệu hóa")

        self._validate_relations(
            db,
            category_id=todo_in.category_id,
            tag_ids=todo_in.tag_ids,
        )
        self._ensure_todo_quota(db, owner)

        payload = todo_in.model_copy()
        if self._has_urgent_tag(db, todo_in.tag_ids):
            payload.priority = Priority.HIGH

        todo = crud_todo.create(db, obj_in=payload, user_id=owner.id)

        if crud_todo.count_by_user(db, user_id=owner.id) == 1:
            self._enqueue_welcome(owner.id)

        return todo

    def update_todo(
        self, db: Session, todo_id: int, todo_in: TodoUpdate, owner: User
    ) -> Todo:
        todo = self.get_todo(db, todo_id, owner)

        was_completed = todo.completed
        category_id = (
            todo_in.category_id if todo_in.category_id is not None else todo.category_id
        )
        tag_ids = (
            todo_in.tag_ids if todo_in.tag_ids is not None else [t.id for t in todo.tags]
        )
        self._validate_relations(
            db,
            category_id=category_id,
            tag_ids=tag_ids,
        )

        updated = crud_todo.update(db, db_obj=todo, obj_in=todo_in)

        if updated.completed and not was_completed:
            self._enqueue_completion(updated.user_id, updated.id)

        return updated

    def delete_todo(self, db: Session, todo_id: int, owner: User) -> None:
        todo = crud_todo.get(db, id=todo_id)
        if not todo:
            raise NotFoundError("Todo không tồn tại")
        self._ensure_owner(todo, owner)
        crud_todo.remove(db, id=todo_id)

    def bulk_complete(
        self, db: Session, *, owner: User, todo_ids: List[int]
    ) -> BulkCompleteResponse:
        todos = crud_todo.get_by_ids_for_user(
            db, user_id=owner.id, todo_ids=todo_ids
        )

        if len(todos) != len(set(todo_ids)):
            raise BusinessError("Một hoặc nhiều todo không tồn tại hoặc không thuộc bạn")

        completed_ids: List[int] = []
        notifications = 0

        for todo in todos:
            if todo.completed:
                continue
            crud_todo.update(db, db_obj=todo, obj_in=TodoUpdate(completed=True))
            completed_ids.append(todo.id)
            self._enqueue_completion(owner.id, todo.id)
            notifications += 1

        return BulkCompleteResponse(
            completed_count=len(completed_ids),
            todo_ids=completed_ids,
            notifications_queued=notifications,
        )

    def _ensure_owner(self, todo: Todo, owner: User) -> None:
        if todo.user_id != owner.id:
            raise ForbiddenError("Không có quyền với todo này")

    def _validate_relations(
        self,
        db: Session,
        *,
        category_id: Optional[int],
        tag_ids: List[int],
    ) -> None:
        if category_id is not None and not crud_category.get(db, id=category_id):
            raise BusinessError("Category không tồn tại")
        if tag_ids:
            tags = crud_tag.get_by_ids(db, ids=tag_ids)
            if len(tags) != len(set(tag_ids)):
                raise BusinessError("Một hoặc nhiều tag không tồn tại")

    def _ensure_todo_quota(self, db: Session, owner: User) -> None:
        active = crud_todo.count_active_by_user(db, user_id=owner.id)
        if active >= owner.max_active_todos:
            raise BusinessError(
                f"Gói {owner.plan.value} chỉ được tối đa "
                f"{owner.max_active_todos} todo chưa hoàn thành"
            )

    def _has_urgent_tag(self, db: Session, tag_ids: List[int]) -> bool:
        if not tag_ids:
            return False
        tags = crud_tag.get_by_ids(db, ids=tag_ids)
        return any(tag.name.lower() == URGENT_TAG_NAME for tag in tags)

    def _enqueue_welcome(self, user_id: int) -> None:
        try:
            send_welcome_notification.delay(user_id)
        except Exception as exc:
            logger.warning("Không enqueue welcome notification: %s", exc)

    def _enqueue_completion(self, user_id: int, todo_id: int) -> None:
        try:
            send_todo_completed_notification.delay(user_id, todo_id)
        except Exception as exc:
            logger.warning("Không enqueue completion notification: %s", exc)


todo_service = TodoService()
