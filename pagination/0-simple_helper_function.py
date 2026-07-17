#!/usr/bin/env python3
"""
Main module documentation for the pagination helper.
This module contains simple utility functions for computing page indexes.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the start and end indexes for a 1-indexed pagination system.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index (inclusive)
                         and the end index (exclusive).
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
