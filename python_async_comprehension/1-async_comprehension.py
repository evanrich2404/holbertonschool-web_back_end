#!/usr/bin/env python3
"""async comprehension"""
import importlib
from typing import List

async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine that collects 10 random numbers using async comprehending over async_generator"""
    return [number async for number in async_generator()]
