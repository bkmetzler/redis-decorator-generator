from flask import Flask

from .extensions import cache
from .settings import get_settings


def create_app() -> Flask:
    settings = get_settings()
    app = Flask(settings.app_name)

    @app.route("/")
    @cache(ttl=60)
    def index(stuff: str) -> str:
        return stuff

    return app
