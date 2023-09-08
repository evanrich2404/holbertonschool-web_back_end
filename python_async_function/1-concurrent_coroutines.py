#!/usr/bin/env python3
"""element_length module"""

import asyncio
import importlib
from typing import List

module = importlib.import_module('0-basic_async_syntax')
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
