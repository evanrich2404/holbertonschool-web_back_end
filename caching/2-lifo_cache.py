#!/usr/bin/env python3
"""Creating a LIFO caching system that inherits from BasicCache"""
from collections import deque
BasicCache = __import__('0-basic_cache').BasicCache


class LIFOCache(BasicCache):
    """A LIFO caching system that inherits from BasicCache
    and uses put and get to add and retrieve items from a dictionary
    """
    def __init__(self):
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """Adds key/value pair to cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            popped = self.queue.pop()
            del self.cache_data[popped]
            print('DISCARD: {}'.format(popped))
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves value from cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
