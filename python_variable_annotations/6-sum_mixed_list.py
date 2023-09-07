#!/usr/bin/env python3
"""
sum_mixed_list takes a mixed list of integers and floats and returns their sum
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of a mixed list of integers and floats as a float"""
    return sum(mxd_lst)
