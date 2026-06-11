#!/usr/bin/env python3
"""
<<<<<<< HEAD
Module providing coroutine that takes no arguments
will loop 10 times, each time async. wait 1 second
then yield a random number between 0 and 10
"""


=======
Asynchronous generator that yields random numbers
"""

>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
<<<<<<< HEAD
    Wait 1 second,return
    random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        i = random.uniform(0, 10)
        yield i
=======
    Asynchronously generates 10 random numbers between 0 and 10,
    waiting 1 second between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
