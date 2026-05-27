"""Khởi tạo database và chạy migration."""

import os
import sys

import pymysql
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)


def get_db_config() -> dict:
    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "3306")),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", ""),
        "charset": "utf8mb4",
    }


def create_database():
    db_name = os.getenv("DB_NAME", "todo_db")
    connection = pymysql.connect(**get_db_config())
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {db_name} "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            )
        connection.commit()
        print(f"Database '{db_name}' đã sẵn sàng.")
    finally:
        connection.close()


def run_migrations():
    from alembic import command
    from alembic.config import Config

    alembic_cfg = Config(os.path.join(ROOT_DIR, "alembic.ini"))
    command.upgrade(alembic_cfg, "head")
    print("Migration hoàn tất.")


if __name__ == "__main__":
    create_database()
    run_migrations()
    print("Khởi tạo database hoàn tất!")
