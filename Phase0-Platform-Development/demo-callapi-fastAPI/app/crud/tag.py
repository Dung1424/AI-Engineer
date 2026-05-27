from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.tag import Tag
from app.schemas.tag import TagCreate, TagUpdate


class CRUDTag(CRUDBase[Tag, TagCreate, TagUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Tag]:
        return db.query(Tag).filter(Tag.name == name).first()

    def get_by_ids(self, db: Session, *, ids: List[int]) -> List[Tag]:
        if not ids:
            return []
        return db.query(Tag).filter(Tag.id.in_(ids)).all()


tag = CRUDTag(Tag)
