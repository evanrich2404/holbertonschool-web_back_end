#!/usr/bin/env python3
"""async generator"""
import asyncio
import random


async def async_generator() -> float:
    """Asynchronous generator yielding random numbers between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
