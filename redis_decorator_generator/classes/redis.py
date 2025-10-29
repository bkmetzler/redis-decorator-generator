from collections.abc import Callable
from hashlib import sha256
from typing import Any
from typing import cast

from redis import Redis


class RedisCache(Redis):
    @staticmethod
    def key(func: Callable, *args: Any, **kwargs: Any) -> str:
        arg_str = ":".join([str(arg) for arg in args if callable(arg)])
        kwarg_str = [f"{str(key)}={value}" for key, value in kwargs.items() if callable(value)]
        return sha256(f"{func.__name__}::{arg_str}::{kwarg_str}".encode()).hexdigest()

    @classmethod
    def from_url(cls, url: str, **kwargs: Any) -> "RedisCache":
        redis = super().from_url(url, **kwargs)
        return cast(RedisCache, redis)
