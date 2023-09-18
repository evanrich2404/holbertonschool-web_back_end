#!/usr/bin/env python3
"""Creating a basic dictionary from the parent class BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system that inherits from BaseCaching
    and uses put and get to add and retrieve items from a dictionary
    """

    def put(self, key, item):
        """Adds key/value pair to cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves value from cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
