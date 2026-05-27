from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.notification_log import NotificationLog
from app.schemas.notification import NotificationLogResponse


class CRUDNotificationLog(CRUDBase[NotificationLog, NotificationLogResponse, dict]):
    def get_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 50
    ) -> List[NotificationLog]:
        return (
            db.query(NotificationLog)
            .filter(NotificationLog.user_id == user_id)
            .order_by(NotificationLog.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create_log(
        self,
        db: Session,
        *,
        user_id: int,
        subject: str,
        body: str,
        todo_id: Optional[int] = None,
        channel=None,
        status=None,
    ) -> NotificationLog:
        from app.models.notification_log import NotificationChannel, NotificationStatus

        log = NotificationLog(
            user_id=user_id,
            todo_id=todo_id,
            subject=subject,
            body=body,
            channel=channel or NotificationChannel.EMAIL,
            status=status or NotificationStatus.PENDING,
        )
        db.add(log)
        db.commit()
        db.refresh(log)
        return log


notification_log = CRUDNotificationLog(NotificationLog)
