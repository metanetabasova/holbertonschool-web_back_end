#!/usr/bin/env python3
"""
Server sinfi vasitəsilə verilənlər bazasının requlyasiyası (pagination).
"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    1-indeksli requlyasiya sistemi üçün başlanğıc və son indeksləri hesablayır.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Populyar uşaq adları bazasını səhifələmək (paginate) üçün Server sinfi.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Keşlənmiş məlumat bazası (Cached dataset)
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Göstərilən səhifə və ölçüyə uyğun olaraq verilənlər
        bazasından lazımi sətirləri qaytarır.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Başlanğıc və son indeksləri əldə edirik
        start, end = index_range(page, page_size)

        # Məlumat bazasını yükləyirik
        data = self.dataset()

        # Əgər indekslər mövcud məlumatların hüdudlarından kənardırsa
        if start >= len(data):
            return []

        # Lazımi aralığı kəsib (slice) qaytarırıq
        return data[start:end]
