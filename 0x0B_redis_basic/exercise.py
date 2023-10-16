#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional
import functools

# Define type aliases for better readability and maintainability.
ByteProcessor = Callable[[bytes], Union[str, int, bytes]]
OptionalByteProcessor = Optional[ByteProcessor]
ReturnValue = Union[str, int, bytes, None]


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.

    Args:
    - method (Callable): The method to wrap.

    Returns:
    - Callable: The wrapped method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increase call count in Redis and invoke the original method."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a method.

    Args:
    - method (Callable): The method to wrap.

    Returns:
    - Callable: The wrapped method.
    """
    @functools.wraps(method)
    def wrapper(self, *args):
        """Log inputs and outputs in Redis and invoke the original method."""
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        output = str(method(self, *args))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper


def replay(method: Callable):
    """
    Function to display the history of calls of a particular function.

    Args:
    - method (Callable): The method whose call history needs to be displayed.
    """
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
    """Class to interface with a Redis-based cache system."""

    def __init__(self):
        """Initialize the Cache instance and connect to Redis."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.

        Args:
        - data (Union[str, bytes, int, float]): Data to be stored in Redis.

        Returns:
        - str: Randomly generated key corresponding to the stored data.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: OptionalByteProcessor = None) -> ReturnValue:
        """
        Retrieve data from Redis based on a given key.

        Args:
        - key (str): Key corresponding to the data in Redis.
        - fn (OptionalByteProcessor, optional): Optional function
        to process the data. Defaults to None.

        Returns:
        - ReturnValue: Data retrieved from Redis.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve string data from Redis based on a given key.

        Args:
        - key (str): Key corresponding to the data in Redis.

        Returns:
        - str: Data retrieved from Redis in string format.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve integer data from Redis based on a given key.

        Args:
        - key (str): Key corresponding to the data in Redis.

        Returns:
        - int: Data retrieved from Redis in integer format.
        """
        return self.get(key, fn=int)
