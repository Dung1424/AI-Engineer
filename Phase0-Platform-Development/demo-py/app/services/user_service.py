from __future__ import annotations

from sqlalchemy.orm import Session

from app.api.deps import ensure_self
from app.core.exceptions import BusinessError, NotFoundError
from app.core.security import hash_password
from app.crud import user as crud_user
from app.models.user import User
from app.schemas.user import UserUpdate


class UserService:
    def get_user(self, db: Session, user_id: int, current_user: User) -> User:
        ensure_self(current_user, user_id)
        user = crud_user.get(db, id=user_id)
        if not user:
            raise NotFoundError("User không tồn tại")
        return user

    def update_user(
        self, db: Session, user_id: int, user_in: UserUpdate, current_user: User
    ) -> User:
        user = self.get_user(db, user_id, current_user)

        if user_in.username and user_in.username != user.username:
            if crud_user.get_by_username(db, username=user_in.username):
                raise BusinessError("Username đã tồn tại")
        if user_in.email and user_in.email != user.email:
            if crud_user.get_by_email(db, email=user_in.email):
                raise BusinessError("Email đã tồn tại")

        hashed = hash_password(user_in.password) if user_in.password else None
        return crud_user.update(
            db, db_obj=user, obj_in=user_in, hashed_password=hashed
        )

    def delete_user(self, db: Session, user_id: int, current_user: User) -> None:
        ensure_self(current_user, user_id)
        user = crud_user.remove(db, id=user_id)
        if not user:
            raise NotFoundError("User không tồn tại")

    def request_daily_summary(
        self, db: Session, user_id: int, current_user: User
    ) -> dict:
        ensure_self(current_user, user_id)
        user = crud_user.get(db, id=user_id)
        if not user:
            raise NotFoundError("User không tồn tại")

        from app.workers.tasks import send_daily_summary

        task = send_daily_summary.delay(user.id)
        return {"message": "Daily summary đã được đưa vào hàng đợi", "task_id": task.id}


user_service = UserService()
