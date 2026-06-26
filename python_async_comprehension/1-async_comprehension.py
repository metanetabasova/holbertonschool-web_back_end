#!/usr/bin/env python3
"""
Bu modul asinxron generator üzərində async comprehension
istifadə edərək məlumatların toplanmasını təmin edir.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_generator-dan gələn 10 təsadüfi ədədi asinxron
    list comprehension vasitəsilə toplayır və siyahını qaytarır.
    """
    return [number async for number in async_generator()]
