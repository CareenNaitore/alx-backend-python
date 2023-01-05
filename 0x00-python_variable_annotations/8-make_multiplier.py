#!/usr/bin/env python3

""" how to multiply float numbers"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """computes the multiplication of a float number"""

    return lambda x: x * multiplier
