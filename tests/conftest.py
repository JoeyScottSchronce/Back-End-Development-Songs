import pytest
from backend import app


@pytest.fixture()
def client():
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def song():
    return {
        "id":1234567890,
        "lyrics":"This is a test. This is a test. This is a test. This is a test.",
        "title":"This is a test."
        }

