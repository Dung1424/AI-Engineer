from __future__ import annotations

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps
from app.schemas.auth import Token
from app.schemas.user import UserRegister, UserResponse
from app.services.auth_service import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=201)
def register(user_in: UserRegister, db: Session = Depends(deps.get_db)):
    return auth_service.register(db, user_in)


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(deps.get_db),
):
    return auth_service.login(
        db, username=form_data.username, password=form_data.password
    )


@router.get("/me", response_model=UserResponse)
def read_current_user(current_user=Depends(deps.get_current_active_user)):
    return current_user
