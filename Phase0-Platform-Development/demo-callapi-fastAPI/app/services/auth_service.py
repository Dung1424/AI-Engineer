from __future__ import annotations

from datetime import timedelta

from sqlalchemy.orm import Session

from app.core.exceptions import BusinessError, UnauthorizedError
from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.crud import user as crud_user
from app.models.user import User
from app.schemas.auth import Token
from app.schemas.user import UserRegister, UserResponse


class AuthService:
    def register(self, db: Session, user_in: UserRegister) -> User:
        if crud_user.get_by_username(db, username=user_in.username):
            raise BusinessError("Username đã tồn tại")
        if crud_user.get_by_email(db, email=user_in.email):
            raise BusinessError("Email đã tồn tại")

        from app.schemas.user import UserCreate

        create_data = UserCreate(
            username=user_in.username,
            email=user_in.email,
            full_name=user_in.full_name,
            password=user_in.password,
        )
        return crud_user.create(
            db,
            obj_in=create_data,
            hashed_password=hash_password(user_in.password),
        )

    def authenticate(self, db: Session, *, username: str, password: str) -> User:
        user = crud_user.get_by_username_or_email(db, identifier=username)
        if not user or not user.hashed_password:
            raise UnauthorizedError("Sai username/email hoặc mật khẩu")
        if not verify_password(password, user.hashed_password):
            raise UnauthorizedError("Sai username/email hoặc mật khẩu")
        if not user.is_active:
            raise UnauthorizedError("Tài khoản đã bị vô hiệu hóa")
        return user

    def login(self, db: Session, *, username: str, password: str) -> Token:
        user = self.authenticate(db, username=username, password=password)
        token = create_access_token(subject=str(user.id))
        return Token(access_token=token)


auth_service = AuthService()
