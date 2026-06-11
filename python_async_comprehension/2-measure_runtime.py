#!/usr/bin/env python3
"""
<<<<<<< HEAD
Module that imports function
the coroutine will execute it 4 times in parallel
using asyncio.gather
measure runtime and return it
"""


import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Return measured runtime"""
    start = time.time()

    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    end = time.time()

    return end - start
=======
Measure runtime of async_comprehension executed in parallel
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension 4 times in
    parallel and returns total runtime"""
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    total_time = time.time() - start_time
    return total_time
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
