from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import tag as crud_tag
from app.models.user import User
from app.schemas.tag import TagCreate, TagResponse, TagUpdate

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("/", response_model=List[TagResponse])
def list_tags(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    return crud_tag.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=TagResponse, status_code=status.HTTP_201_CREATED)
def create_tag(
    tag_in: TagCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    if crud_tag.get_by_name(db, name=tag_in.name):
        raise HTTPException(status_code=400, detail="Tag đã tồn tại")
    return crud_tag.create(db, obj_in=tag_in)


@router.get("/{tag_id}", response_model=TagResponse)
def get_tag(
    tag_id: int,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    tag = crud_tag.get(db, id=tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag không tồn tại")
    return tag


@router.put("/{tag_id}", response_model=TagResponse)
def update_tag(
    tag_id: int,
    tag_in: TagUpdate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    tag = crud_tag.get(db, id=tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag không tồn tại")
    return crud_tag.update(db, db_obj=tag, obj_in=tag_in)


@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tag(
    tag_id: int,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    tag = crud_tag.remove(db, id=tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag không tồn tại")
