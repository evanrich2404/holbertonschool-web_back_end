#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
import time
import importlib
from typing import Callable

module = importlib.import_module('1-concurrent_coroutines')
wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime."""
    start_time = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    total_time = time.perf_counter() - start_time

    return total_time / n
