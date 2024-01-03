#!/usr/bin/env python3

""" Caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Caching system using LIFO policy"""

    def __init__(self):
        """Constructor for class
        """
        self.__key_order = []
        super().__init__()

    def put(self, key, item):
        """Insert cache data
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.__key_order.pop()
            self.cache_data.pop(discarded)
            print(f"DISCARD: {discarded}")
        self.__key_order.append(key)

    def get(self, key):
        """Get cache data
        """
        return self.cache_data.get(key)
