from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import notification_log as crud_notification
from app.models.user import User
from app.schemas.notification import NotificationLogResponse
from app.schemas.stats import UserStatsResponse
from app.schemas.user import UserResponse, UserUpdate
from app.services.stats_service import stats_service
from app.services.user_service import user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResponse)
def read_me(current_user: User = Depends(deps.get_current_active_user)):
    return current_user


@router.get("/me/stats", response_model=UserStatsResponse)
def read_my_stats(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    return stats_service.get_user_stats(db, current_user.id)


@router.get("/me/notifications", response_model=List[NotificationLogResponse])
def read_my_notifications(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    return crud_notification.get_by_user(
        db, user_id=current_user.id, skip=skip, limit=limit
    )


@router.post("/me/send-daily-summary")
def send_my_daily_summary(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    return user_service.request_daily_summary(db, current_user.id, current_user)


@router.put("/me", response_model=UserResponse)
def update_me(
    user_in: UserUpdate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    return user_service.update_user(db, current_user.id, user_in, current_user)


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_me(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    user_service.delete_user(db, current_user.id, current_user)
