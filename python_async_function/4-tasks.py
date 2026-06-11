#!/usr/bin/env python3
"""
<<<<<<< HEAD
Module that imports function
and alter it into a new function
"""


import asyncio
from typing import List
=======
Task-based concurrent execution
"""

import asyncio
from typing import List

>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
<<<<<<< HEAD
    """Return the list of delays"""
    delays = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
=======
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
