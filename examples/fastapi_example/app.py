from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import APIRouter
from fastapi import FastAPI
from fastapi import Request

from .extensions import cache

route = APIRouter(prefix="/api")


@route.get("/")
@cache(ttl=60)
async def root(request: Request) -> dict[str, str]:
    return {"hello": "world"}


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    app.state = {"cache": cache}
    yield


def main() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    return app
