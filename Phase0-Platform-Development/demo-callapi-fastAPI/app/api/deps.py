from __future__ import annotations

from collections.abc import Generator

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.database import SessionLocal
from app.core.exceptions import ForbiddenError, UnauthorizedError
from app.core.security import decode_access_token
from app.crud import user as crud_user
from app.models.user import User

settings = get_settings()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_PREFIX}/auth/login",
    auto_error=True,
)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
) -> User:
    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")
        if user_id is None:
            raise UnauthorizedError("Token không hợp lệ")
    except JWTError as exc:
        raise UnauthorizedError("Token không hợp lệ") from exc

    user = crud_user.get(db, id=int(user_id))
    if not user:
        raise UnauthorizedError("User không tồn tại")
    if not user.is_active:
        raise UnauthorizedError("Tài khoản đã bị vô hiệu hóa")
    return user


def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    return current_user


def ensure_self(current_user: User, user_id: int) -> None:
    if current_user.id != user_id:
        raise ForbiddenError("Không có quyền truy cập tài nguyên của user khác")
