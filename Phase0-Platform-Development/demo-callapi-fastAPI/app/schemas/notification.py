from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models.notification_log import NotificationChannel, NotificationStatus


class NotificationLogResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    todo_id: Optional[int]
    channel: NotificationChannel
    subject: str
    body: str
    status: NotificationStatus
    sent_at: Optional[datetime]
    created_at: datetime
