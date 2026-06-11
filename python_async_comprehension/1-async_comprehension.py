#!/usr/bin/env python3
"""
<<<<<<< HEAD
Module that imports function
the coroutine collect 10 random numbers
and return it
"""


from typing import List
=======
Async comprehension over async_generator
"""

from typing import List

>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
<<<<<<< HEAD
    """Return collected 10 random numbers"""
    return [number async for number in async_generator()]
=======
    """
    Collects 10 random numbers from async_generator using async comprehension
    and returns them as a list.
    """
    return [i async for i in async_generator()]
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
