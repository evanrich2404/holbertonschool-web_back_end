#!/usr/bin/env python3
"""element_length module"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length: takes a list of strings and returns a list of"""
    return [(i, len(i)) for i in lst]
