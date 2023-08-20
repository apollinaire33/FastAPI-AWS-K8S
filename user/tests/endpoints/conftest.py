from unittest.mock import Mock, patch

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from user.core.dependencies import get_user_service


@pytest.fixture
def mock_user_service() -> Mock:
    with patch("user.services.user_service.ModelUserService") as mock:
        return mock


@pytest.fixture()
def app(mock_user_service) -> FastAPI:
    from user.main import app

    app.dependency_overrides[get_user_service] = lambda: mock_user_service
    return app


@pytest.fixture()
async def async_api_client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
