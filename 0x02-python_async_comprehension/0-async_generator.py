#!/usr/bin/env python3
"""Task 0 """

import random
import asyncio
from typing import Generator


async def async_generator() -> [float, None, None]:
    """Generates a sequence of ten numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
