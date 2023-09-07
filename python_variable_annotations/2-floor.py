#!/usr/bin/env python3
"""basic annotation: floor"""


def floor(n: float) -> int:
    """returns floor of float"""
    if n < 0:
        return int(n) - 1
    return int(n)
