from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from orion.core.config import AbstractSettings
from orion.core.config import get_settings


def create_app(settings: AbstractSettings = None) -> FastAPI:
    """Create backend API application."""
    from . import __version__

    settings = settings or get_settings()
    app = FastAPI(debug=settings.debug,
                  title=settings.title,
                  description='A simple IT asset management API backend.',
                  version=__version__)
    app.add_middleware(CORSMiddleware,
                       allow_origins=['*'],
                       allow_credentials=True,
                       allow_methods=['*'],
                       allow_headers=['*'])

    return app
