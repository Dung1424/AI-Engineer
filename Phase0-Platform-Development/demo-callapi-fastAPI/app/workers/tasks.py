from __future__ import annotations

import logging
from datetime import datetime

from sqlalchemy.orm import Session

from app.core.celery_app import celery_app
from app.core.database import SessionLocal
from app.crud import notification_log as crud_notification
from app.crud import todo as crud_todo
from app.crud import user as crud_user
from app.models.notification_log import NotificationStatus

logger = logging.getLogger(__name__)


def _get_db() -> Session:
    return SessionLocal()


@celery_app.task(name="app.workers.tasks.send_welcome_notification", bind=True, max_retries=3)
def send_welcome_notification(self, user_id: int) -> dict:
    db = _get_db()
    try:
        user = crud_user.get(db, id=user_id)
        if not user:
            return {"status": "skipped", "reason": "user not found"}

        subject = f"Chào mừng {user.username} đến Todo List!"
        body = (
            f"Xin chào {user.full_name or user.username},\n\n"
            f"Tài khoản của bạn (gói {user.plan.value}) đã sẵn sàng.\n"
            f"Bạn có thể tạo tối đa {user.max_active_todos} todo chưa hoàn thành."
        )

        log = crud_notification.create_log(
            db, user_id=user.id, subject=subject, body=body
        )
        log.status = NotificationStatus.SENT
        log.sent_at = datetime.now()
        db.commit()

        logger.info("[WORKER] Welcome email sent to user_id=%s", user_id)
        return {"status": "sent", "notification_id": log.id}
    except Exception as exc:
        logger.exception("Welcome notification failed")
        raise self.retry(exc=exc, countdown=10)
    finally:
        db.close()


@celery_app.task(
    name="app.workers.tasks.send_todo_completed_notification",
    bind=True,
    max_retries=3,
)
def send_todo_completed_notification(self, user_id: int, todo_id: int) -> dict:
    db = _get_db()
    try:
        user = crud_user.get(db, id=user_id)
        todo = crud_todo.get(db, id=todo_id)
        if not user or not todo:
            return {"status": "skipped", "reason": "user or todo not found"}

        subject = f"Todo hoàn thành: {todo.title}"
        body = (
            f"Chúc mừng {user.username}!\n\n"
            f'Bạn vừa hoàn thành: "{todo.title}"\n'
            f"Priority: {todo.priority.value}\n"
            f"Thời gian: {datetime.now().isoformat()}"
        )

        log = crud_notification.create_log(
            db,
            user_id=user.id,
            todo_id=todo.id,
            subject=subject,
            body=body,
        )
        log.status = NotificationStatus.SENT
        log.sent_at = datetime.now()
        db.commit()

        logger.info("[WORKER] Completion notification user_id=%s todo_id=%s", user_id, todo_id)
        return {"status": "sent", "notification_id": log.id}
    except Exception as exc:
        logger.exception("Completion notification failed")
        raise self.retry(exc=exc, countdown=10)
    finally:
        db.close()


@celery_app.task(name="app.workers.tasks.send_daily_summary", bind=True, max_retries=2)
def send_daily_summary(self, user_id: int) -> dict:
    db = _get_db()
    try:
        from app.services.stats_service import stats_service

        user = crud_user.get(db, id=user_id)
        if not user:
            return {"status": "skipped", "reason": "user not found"}

        stats = stats_service.get_user_stats(db, user_id)
        subject = f"Báo cáo todo hàng ngày — {user.username}"
        body = (
            f"Tổng: {stats.total_todos} | Hoàn thành: {stats.completed_todos} | "
            f"Chưa xong: {stats.pending_todos} | Tỷ lệ: {stats.completion_rate}%\n"
            f"Theo priority: {stats.by_priority}\n"
            f"Theo category: {stats.by_category}"
        )

        log = crud_notification.create_log(
            db, user_id=user.id, subject=subject, body=body
        )
        log.status = NotificationStatus.SENT
        log.sent_at = datetime.now()
        db.commit()

        logger.info("[WORKER] Daily summary sent to user_id=%s", user_id)
        return {"status": "sent", "notification_id": log.id}
    except Exception as exc:
        logger.exception("Daily summary failed")
        raise self.retry(exc=exc, countdown=30)
    finally:
        db.close()
