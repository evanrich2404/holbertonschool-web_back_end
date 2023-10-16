#!/usr/bin/env python3
import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        self.redis = redis.Redis()
        self.redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())
        self.redis.set(random_key, data)
        return random_key
