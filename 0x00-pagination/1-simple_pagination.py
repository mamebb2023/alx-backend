#!/usr/bin/env python3
""" Pagination module
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """
    Return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters
    """
    start = (page - 1) * page_size
    return (start, start + page_size)


class Server:
    """ Server class to paginate a database of popular baby names """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Gets a page for the requeted parameters """
        assert type(page) is int and \
            type(page_size) is int and \
            page > 0 and \
            page_size > 0

        idx = index_range(page, page_size)
        data = self.dataset()

        try:
            return [data[i] for i in range(idx[0], idx[1])]
        except IndexError:
            return []
