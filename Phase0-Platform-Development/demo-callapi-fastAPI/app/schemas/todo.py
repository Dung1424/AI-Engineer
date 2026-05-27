from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from app.models.todo import Priority
from app.schemas.category import CategoryResponse
from app.schemas.tag import TagResponse
from app.schemas.user import UserResponse


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    completed: bool = False
    priority: Priority = Priority.MEDIUM
    category_id: Optional[int] = None
    tag_ids: List[int] = Field(default_factory=list)


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[Priority] = None
    category_id: Optional[int] = None
    tag_ids: Optional[List[int]] = None


class TodoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    priority: Priority
    user_id: int
    category_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    owner: UserResponse
    category: Optional[CategoryResponse] = None
    tags: List[TagResponse] = Field(default_factory=list)
