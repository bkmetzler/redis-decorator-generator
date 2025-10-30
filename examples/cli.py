from time import sleep

from redis_decorator_generator import generate


def main() -> None:
    cache = generate("redis://:foobared@localhost:6379/0")

    @cache(ttl=60)
    def func1(flag: str) -> str:
        sleep(10)
        return flag

    result = func1("flag1")
    print(result)


if __name__ == "__main__":
    main()
