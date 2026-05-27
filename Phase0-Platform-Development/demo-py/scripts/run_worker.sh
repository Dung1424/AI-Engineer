#!/usr/bin/env bash
cd "$(dirname "$0")/.."
source venv/bin/activate
celery -A app.core.celery_app:celery_app worker --loglevel=info
