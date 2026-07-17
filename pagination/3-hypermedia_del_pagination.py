#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict:
        """
        Silinmələrə qarşı dayanıqlı indeks əsaslı səhifələmə.
        İstifadəçinin elementləri qaçırmamasını təmin edir.
        """
        indexed_data = self.indexed_dataset()

        if index is not None:
            assert isinstance(index, int)
            assert 0 <= index < len(indexed_data)

        assert isinstance(page_size, int) and page_size > 0

        if index is None:
            index = 0

        data_page = []
        current_index = index

        while len(data_page) < page_size and current_index < len(indexed_data):
            if current_index in indexed_data:
                data_page.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index if current_index < len(indexed_data) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data_page),
            "data": data_page
        }
