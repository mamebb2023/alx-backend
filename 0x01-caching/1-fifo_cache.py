#!/usr/bin/env python3
""" Cacheing System """

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache Basic class
    """
    def __init__(self):
        """ Constructor
        """
        self.__key_order = []
        super().__init__()

    def put(self, key, item):
        """ Inerts a cache
        """
        if key is None or item is None:
            return
        self.__key_order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.__key_order[0]
            self.cache_data.pop(discarded)
            self.__key_order.pop(0)
            print(f"DISCARD: {discarded}")

    def get(self, key):
        """ Get a cache data
        """
        return self.cache_data.get(key)
