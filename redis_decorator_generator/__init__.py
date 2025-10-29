import pickle
from collections.abc import Callable
from functools import wraps
from typing import Any
from typing import cast
from typing import ParamSpec
from typing import TypeVar

from .classes.redis import RedisCache

T = TypeVar("T")
P = ParamSpec("P")


def generate(redis_url: str | None = None, redis_client: RedisCache | None = None) -> Any:
    redis: RedisCache
    if redis_client is not None:
        redis = redis_client
    else:
        if redis_url is None:
            raise Exception("redis_decorator.generate's redis_url and redis_client are mutually exclusive")
        redis = RedisCache.from_url(redis_url)

    def cache(ttl: int = 60) -> Callable[[Callable[P, T]], Callable[P, T]]:
        def decorator(func: Callable[P, T]) -> Callable[P, T]:
            @wraps(func)
            def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
                rkey = redis.key(func, *args, **kwargs)
                cached = redis.get(rkey)
                if cached is not None:
                    p_cached = cast(bytes, cached)
                    return pickle.loads(p_cached)

                result = func(*args, **kwargs)
                redis.setex(rkey, ttl, pickle.dumps(result))
                return result

            return wrapper

        return decorator

    return cache
