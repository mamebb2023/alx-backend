#!/usr/bin/env python3

""" Caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
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

        if len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.__access_order.append(key)
        else:
            discarded = self.__access_order[0]
            self.cache_data.pop(discarded)
            if discarded != key:
                print(f"DISCARD: {discarded}")
            self.__access_order = self.__access_order[1:]
            self.__access_order.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """Get cache data
        """
        if key is None or key not in self.cache_data:
            return None

        self.__access_order.remove(key)
        self.__access_order.append(key)
        return self.cache_data.get(key)
