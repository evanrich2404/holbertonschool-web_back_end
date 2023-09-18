#!/usr/bin/env python3
"""Creating a LFU caching system that inherits from BasicCache"""
from collections import defaultdict, deque
BasicCache = __import__('0-basic_cache').BasicCache

class LFUCache(BasicCache):
    def __init__(self):
        super().__init__()
        self.key_frequency = defaultdict(int)  # {key: frequency}
        self.frequency_list = defaultdict(deque)  # {frequency: deque([keys])}
        self.min_frequency = 0

    def put(self, key, item):
        """Adds key/value pair to cache"""
        if key is None or item is None:
            return
        freq = self.key_frequency[key]
        self.key_frequency[key] = freq + 1

        # Remove the key from the current frequency list, if it's present
        if freq and key in self.frequency_list[freq]:  # Check if key is in the frequency list
            self.frequency_list[freq].remove(key)

        # Add the key to the new frequency list
        self.frequency_list[freq + 1].append(key)
        
        # If cache is full, pop the least frequently used item
        if len(self.cache_data) >= self.MAX_ITEMS:
            while not self.frequency_list[self.min_frequency]:
                self.min_frequency += 1
            to_discard = self.frequency_list[self.min_frequency].popleft()
            del self.cache_data[to_discard]
            del self.key_frequency[to_discard]
            print('DISCARD: {}'.format(to_discard))

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves value from cache"""
        if key is None or key not in self.cache_data:
            return None

        # Increase key's frequency
        freq = self.key_frequency[key]
        self.key_frequency[key] = freq + 1

        # Move the key to the new frequency list
        self.frequency_list[freq].remove(key)
        self.frequency_list[freq + 1].append(key)

        # Reset the minimum frequency
        if not self.frequency_list[self.min_frequency]:
            self.min_frequency += 1

        return self.cache_data[key]
