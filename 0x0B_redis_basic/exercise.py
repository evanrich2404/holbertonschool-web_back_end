#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional
import functools


ByteProcessor = Callable[[bytes], Union[str, int, bytes]]
OptionalByteProcessor = Optional[ByteProcessor]
ReturnValue = Union[str, int, bytes, None]


def count_calls(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args):
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        output = str(method(self, *args))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper

def replay(method: Callable):
    r = redis.Redis()
    method_name = method.__qualname__
    count = r.get(method_name)
    inputs = r.lrange(method_name + ":inputs", 0, -1)
    outputs = r.lrange(method_name + ":outputs", 0, -1)
    print("{} was called {} times:".format(method_name, count))
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method_name, i.decode("utf-8"),
                                     o.decode("utf-8")))

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: OptionalByteProcessor = None) -> ReturnValue:

        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)
