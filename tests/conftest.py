"""Shared pytest fixtures for FastAPI endpoint tests."""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Provide a synchronous FastAPI test client."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Restore in-memory activity data around each test for isolation."""
    snapshot = deepcopy(activities)
    yield
    activities.clear()
    activities.update(snapshot)
