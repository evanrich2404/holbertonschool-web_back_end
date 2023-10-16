#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional
import functools


ByteProcessor = Callable[[bytes], Union[str, int, bytes]]
OptionalByteProcessor = Optional[ByteProcessor]
ReturnValue = Union[str, int, bytes, None]


def count_calls(method: Callable) -> Callable:
    """Count the number of times a method is called."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a particular function."""
    @functools.wraps(method)
    def wrapper(self, *args):
        """Wrapper function."""
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        output = str(method(self, *args))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


def replay(method: Callable):
    """Display the history of calls of a particular function."""
    r = redis.Redis()
    method_name = method.__qualname__
    count = r.get(method_name).decode("utf-8")
    inputs = r.lrange("{}:inputs".format(method_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(method_name), 0, -1)
    print("{} was called {} times:".format(method_name, count))
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method_name, i.decode("utf-8"),
                                     o.decode("utf-8")))


class Cache:
    """Cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in redis"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: OptionalByteProcessor = None) -> ReturnValue:
        """get data from redis"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """get string from redis"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """get int from redis"""
        return self.get(key, fn=int)
