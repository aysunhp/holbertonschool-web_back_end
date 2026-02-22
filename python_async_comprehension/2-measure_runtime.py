#!/usr/bin/env python3
"""
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
