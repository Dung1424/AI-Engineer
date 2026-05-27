from __future__ import annotations

from typing import List, Optional

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api import deps
from app.models.todo import Priority
from app.models.user import User
from app.schemas.stats import BulkCompleteRequest, BulkCompleteResponse
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate
from app.services.todo_service import todo_service

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=List[TodoResponse])
def list_todos(
    skip: int = 0,
    limit: int = 100,
    category_id: Optional[int] = None,
    completed: Optional[bool] = None,
    priority: Optional[Priority] = None,
    tag_id: Optional[int] = None,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    return todo_service.list_todos(
        db,
        current_user,
        skip=skip,
        limit=limit,
        category_id=category_id,
        completed=completed,
        priority=priority,
        tag_id=tag_id,
    )


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(
    todo_in: TodoCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    return todo_service.create_todo(db, todo_in, current_user)


@router.post("/bulk-complete", response_model=BulkCompleteResponse)
def bulk_complete_todos(
    payload: BulkCompleteRequest,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    return todo_service.bulk_complete(
        db, owner=current_user, todo_ids=payload.todo_ids
    )


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    return todo_service.get_todo(db, todo_id, current_user)


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    todo_in: TodoUpdate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    return todo_service.update_todo(db, todo_id, todo_in, current_user)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    todo_id: int,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    todo_service.delete_todo(db, todo_id, current_user)
