import fakeredis
import pytest
from redis import Redis

from redis_decorator import RedisCache


@pytest.fixture
def redis_url() -> str:
    # return "redis://:foobared@localhost:6379/0"
    return "redis://localhost:6379/0"


@pytest.fixture
def fake_redis(redis_url: str) -> Redis:
    """Return a fake Redis instance for tests."""
    # return fakeredis.FakeRedis(decode_responses=True)
    return fakeredis.FakeRedis.from_url(redis_url, decode_responses=False)


@pytest.fixture
def redis(fake_redis: Redis) -> RedisCache:
    return RedisCache.from_pool(fake_redis.connection_pool)
