# Redis Decorator Generator

![deploy](https://github.com/github/bkmetzler/redis-decorator-generator/actions/workflows/deploy.yaml/badge.svg)

![pull requests](https://github.com/github/bkmetzler/redis-decorator-generator/actions/workflows/pull_request.yaml/badge.svg)

## Description
This package is a simple wrapper around the standard redis.Redis package `pip install redis`.

The 'generate' function is meant to help speed up the integration process.

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
