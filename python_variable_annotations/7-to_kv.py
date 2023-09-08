#!/usr/bin/env python3
"""
to_kv takes a string k and an int OR float v as arguments and returns a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple of a string and a float.
    """
    return (k, v * v)
