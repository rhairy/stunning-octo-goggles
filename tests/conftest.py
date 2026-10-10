"""Pytest fixtures for The Room Dialogue API."""

import pytest
from room_api import create_app


@pytest.fixture
def app():
    """Create and configure a test Flask app instance."""
    app = create_app({"TESTING": True})
    return app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
