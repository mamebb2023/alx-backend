#!/usr/bin/env python3
""" A caching system """

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache class
    """
    def put(self, key, item):
        """ Insert a cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get a cache
        """
        return self.cache_data.get(key)
