#!/usr/bin/env python3
"""
<<<<<<< HEAD
Module that imports function
and measures the total execution time
"""


import asyncio
import time
from typing import Callable
=======
Measure the runtime of wait_n
"""

import asyncio
import time

>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
<<<<<<< HEAD
    """Return average runtime of wait_n"""
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    total_time = end - start
=======
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per coroutine (total_time / n).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
    return total_time / n
