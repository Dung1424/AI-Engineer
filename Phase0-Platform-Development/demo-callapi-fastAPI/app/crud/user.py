from __future__ import annotations

from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_by_username_or_email(
        self, db: Session, *, identifier: str
    ) -> Optional[User]:
        return (
            db.query(User)
            .filter((User.username == identifier) | (User.email == identifier))
            .first()
        )

    def create(self, db: Session, *, obj_in: UserCreate, hashed_password: str) -> User:
        data = obj_in.model_dump(exclude={"password"})
        db_obj = User(**data, hashed_password=hashed_password)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: User,
        obj_in: UserUpdate,
        hashed_password: Optional[str] = None,
    ) -> User:
        update_data = obj_in.model_dump(exclude_unset=True, exclude={"password"})
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        if hashed_password:
            db_obj.hashed_password = hashed_password
        db.commit()
        db.refresh(db_obj)
        return db_obj


user = CRUDUser(User)
