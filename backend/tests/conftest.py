import pytest
from fastapi import FastAPI

from orion import create_app
from orion.core.config import AbstractSettings


class TestingSettings(AbstractSettings):
    """Testing settings."""

    title: str = 'ORION-TEST'
    debug: bool = False


def get_testing_settings() -> TestingSettings:
    """Get testing settings."""
    return TestingSettings()


@pytest.fixture(scope='module', autouse=True)
def app() -> FastAPI:
    _app = create_app(get_testing_settings())
    yield _app
