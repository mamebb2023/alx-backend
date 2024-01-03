#!/usr/bin/env python3

""" Caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Caching system
    using LRU policy
    """

    def __init__(self):
        """Constructor for class
        """
        self.__access_order = []
        super().__init__()

    def put(self, key, item):
        """Insert cache data
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.__access_order.remove(key)
            self.__access_order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = self.__access_order.pop()
            print(f"DISCARD: {discarded}")
            self.cache_data.pop(discarded)

        self.cache_data[key] = item
        self.__access_order.append(key)

    def get(self, key):
        """Get cache data
        """
        if key is None or key not in self.cache_data:
            return None

        if key in self.__access_order:
            self.__access_order.remove(key)
        self.__access_order.append(key)
        return self.cache_data.get(key)
