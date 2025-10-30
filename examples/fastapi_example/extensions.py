from .settings import get_settings
from redis_decorator_generator import generate

settings = get_settings()

cache = generate(settings.redis_url)
