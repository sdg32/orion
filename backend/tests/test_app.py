from fastapi import FastAPI

from orion.core.config import get_settings
from tests.conftest import get_testing_settings


def test_app(app: FastAPI):
    assert app


def test_settings():
    assert get_settings()


def test_testing_settings(app: FastAPI):
    settings = get_testing_settings()
    assert app.title == settings.title
