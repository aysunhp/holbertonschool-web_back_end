#!/usr/bin/env python3
"""
<<<<<<< HEAD
Module for async coroutine that takes integer
and waits for a random delay and returns it
=======
Basic async coroutine that waits for a random delay
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
<<<<<<< HEAD
    """Return random delay time"""
=======
    """
    Waits for a random delay between 0 and max_delay (included)
    and returns the delay.
    """
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
