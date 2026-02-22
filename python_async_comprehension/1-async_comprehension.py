#!/usr/bin/env python3
"""
Async comprehension over async_generator
"""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension
    and returns them as a list.
    """
    return [i async for i in async_generator()]
