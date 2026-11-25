from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import sessionmaker


def create_session_factory(database_url: str):
    url = make_url(database_url)
    connect_args = {}
    if url.get_backend_name() == "sqlite":
        connect_args = {"check_same_thread": False}
        if url.database and url.database != ":memory:":
            Path(url.database).parent.mkdir(parents=True, exist_ok=True)
    engine = create_engine(url, connect_args=connect_args)
    factory = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    return engine, factory
