import pytest
from fastapi.testclient import TestClient

from app.core.config import Settings
from app.main import create_app


@pytest.fixture
def settings(tmp_path):
    return Settings(database_url="sqlite:///" + (tmp_path / "test.db").as_posix(), _env_file=None)


@pytest.fixture
def client(settings):
    application = create_app(settings)
    with TestClient(application) as test_client:
        yield test_client
