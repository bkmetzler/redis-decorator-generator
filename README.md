# Redis Decorator Generator

[![Deploy Workflow](https://github.com/bkmetzler/redis-decorator-generator/actions/workflows/deploy.yaml/badge.svg?branch=main)](https://github.com/bkmetzler/redis-decorator-generator/actions/workflows/deploy.yaml)

[![CI Workflow](https://github.com/bkmetzler/redis-decorator-generator/actions/workflows/pull_request.yaml/badge.svg?branch=main)](https://github.com/bkmetzler/redis-decorator-generator/actions/workflows/pull_request.yaml)

## Description
This package is a simple wrapper around the standard redis.Redis package `pip install redis`.

The 'generate' function is meant to help speed up the integration process.

## Purpose
I personally like using decorators for caching.  This allows for quick add/remove caching of a function.

`redis_decorator_generator.generate` is a quick way to point to a custom (Redis server)[https://redis.io/].


## Examples
### Example 1
Use the generator directly on a function.

```python
    @generate(redis_url="redis://:foobared@localhost:6379/0")(ttl=60)
    def my_func(*args: Any, **kwargs: Any) -> Any:
        sarg = ":".join([str(arg) for arg in args])
        skwarg = ":".join([f"{key}={str(value)}" for key, value in kwargs.items()])
        return sarg + "::" + skwarg
```

### Example 2
Generate the decorator so that it can be imported.

```
    cache = generate(redis_url="redis://:foobared@localhost:6379/0")

    @cache(ttl=60)
    def my_func(*args: Any, **kwargs: Any) -> Any:
        sarg = ":".join([str(arg) for arg in args])
        skwarg = ":".join([f"{key}={str(value)}" for key, value in kwargs.items()])
        return sarg + "::" + skwarg
```

### Example 3
With attempting to test, I came across the `fakeredis` package.  This package returns a connection
to the fake Redis server, which can then be passed into `generate` as `redis_client` key word argument.
This allows to initialize the `RedisCache.from_pool()` to be able directly interact with the fake Redis
instance setup for unit testing.


[Example Code Found Here](https://github.com/bkmetzler/redis-decorator-generator/blob/main/tests/test_redis_client.py#L7-L20)
