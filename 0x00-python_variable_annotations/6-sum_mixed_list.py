#!/usr/bin/env python3

""" how to sums mixed variables int and float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """computes the sum of mixed variables"""

    return float(sum(mxd_lst))
