#!/usr/bin/env python3
"""
Bu modul paralel şəkildə icra olunan asinxron tapşırıqların
ümumi işləmə müddətini ölçmək üçün funksionallıq təmin edir.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    async_comprehension funksiyasını asyncio.gather ilə paralel
    olaraq 4 dəfə icra edir və ümumi keçən vaxtı qaytarır.
    """
    start_time = time.perf_counter()

    # 4 ədəd tapşırığı paralel (in parallel) şəkildə başladırıq
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
