#!/usr/bin/env python3
"""
Pagination
"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int):
    """ Return a tuple of size two containing a start index
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
        if idx[0] >= len(data) or idx[1] >= len(data):
            return []

        return [data[i] for i in range(idx[0], idx[1])]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Returns a dictionary containing the specified key-value pairs
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
            }
