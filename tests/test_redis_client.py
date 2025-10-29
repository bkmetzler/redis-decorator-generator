from typing import Any

from redis_decorator import generate
from redis_decorator import RedisCache


def test_redis_client(redis: RedisCache) -> None:
    @generate(redis_client=redis)(ttl=5)
    def my_func(*args: Any, **kwargs: Any) -> Any:
        sarg = ":".join([str(arg) for arg in args])
        skwarg = ":".join([f"{key}={str(value)}" for key, value in kwargs.items()])
        return sarg + "::" + skwarg

    expected = "1:2:3:4::key1=value1:key2=value2"
    results = my_func(*(1, 2, 3, 4), **{"key1": "value1", "key2": "value2"})
    assert results == expected

    expected = "1:2:3:4::key1=value1:key2=value2"
    results = my_func(*(1, 2), **{"key1": "value1"})
    assert results == expected


def test_delete_redis_client(redis: RedisCache) -> None:
    @generate(redis_client=redis)(ttl=5)
    def my_func(*args: Any, **kwargs: Any) -> Any:
        sarg = ":".join([str(arg) for arg in args])
        skwarg = ":".join([f"{key}={str(value)}" for key, value in kwargs.items()])
        return sarg + "::" + skwarg

    expected = "1:2:3:4::key1=value1:key2=value2"
    results = my_func(*(1, 2, 3, 4), **{"key1": "value1", "key2": "value2"})
    assert results == expected

    results = my_func(*(1, 2), **{"key1": "value1"})
    assert results == expected

    rkey = RedisCache.key(my_func, *(1, 2, 3, 4), **{"key1": "value1", "key2": "value2"})
    redis.delete(rkey)

    expected = "1:2::key1=value1"
    results = my_func(*(1, 2), **{"key1": "value1"})
    assert results == expected
