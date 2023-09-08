#!/usr/bin/env python3
"""measure runtime"""
import asyncio
import time
import importlib
from typing import List
module = importlib.import_module('1-async_comprehension')
async_comprehension = module.async_comprehension


async def measure_runtime() -> float:
    """Measure total execution time
    for running async_comprehenion four times in parallel."""
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()
    return end_time - start_time
