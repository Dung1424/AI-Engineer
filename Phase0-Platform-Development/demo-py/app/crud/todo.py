from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from app.crud.base import CRUDBase
from app.models.category import Category
from app.models.tag import Tag
from app.models.todo import Priority, Todo
from app.models.user import User
from app.schemas.todo import TodoCreate, TodoUpdate


class CRUDTodo(CRUDBase[Todo, TodoCreate, TodoUpdate]):
    def _base_query(self, db: Session):
        return db.query(Todo).options(
            joinedload(Todo.owner),
            joinedload(Todo.category),
            joinedload(Todo.tags),
        )

    def get(self, db: Session, id: int) -> Optional[Todo]:
        return self._base_query(db).filter(Todo.id == id).first()

    def get_multi(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
        user_id: Optional[int] = None,
        category_id: Optional[int] = None,
        completed: Optional[bool] = None,
        priority: Optional[Priority] = None,
        tag_id: Optional[int] = None,
    ) -> List[Todo]:
        query = self._base_query(db)

        if user_id is not None:
            query = query.filter(Todo.user_id == user_id)
        if category_id is not None:
            query = query.filter(Todo.category_id == category_id)
        if completed is not None:
            query = query.filter(Todo.completed == completed)
        if priority is not None:
            query = query.filter(Todo.priority == priority)
        if tag_id is not None:
            query = query.filter(Todo.tags.any(Tag.id == tag_id))

        return (
            query.order_by(Todo.created_at.desc()).offset(skip).limit(limit).all()
        )

    def count_active_by_user(self, db: Session, *, user_id: int) -> int:
        return (
            db.query(Todo)
            .filter(Todo.user_id == user_id, Todo.completed.is_(False))
            .count()
        )

    def count_by_user(self, db: Session, *, user_id: int) -> int:
        return db.query(Todo).filter(Todo.user_id == user_id).count()

    def get_by_ids_for_user(
        self, db: Session, *, user_id: int, todo_ids: List[int]
    ) -> List[Todo]:
        if not todo_ids:
            return []
        return (
            self._base_query(db)
            .filter(Todo.user_id == user_id, Todo.id.in_(todo_ids))
            .all()
        )

    def create(self, db: Session, *, obj_in: TodoCreate, user_id: int) -> Todo:
        data = obj_in.model_dump(exclude={"tag_ids"})
        tag_ids = obj_in.tag_ids

        db_obj = Todo(**data, user_id=user_id)
        if tag_ids:
            db_obj.tags = db.query(Tag).filter(Tag.id.in_(tag_ids)).all()

        db.add(db_obj)
        db.commit()
        return self.get(db, db_obj.id)

    def update(
        self,
        db: Session,
        *,
        db_obj: Todo,
        obj_in: TodoUpdate,
    ) -> Todo:
        update_data = obj_in.model_dump(exclude_unset=True)
        tag_ids = update_data.pop("tag_ids", None)

        for field, value in update_data.items():
            setattr(db_obj, field, value)

        if tag_ids is not None:
            db_obj.tags = db.query(Tag).filter(Tag.id.in_(tag_ids)).all()

        db.commit()
        return self.get(db, db_obj.id)


todo = CRUDTodo(Todo)
