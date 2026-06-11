#!/usr/bin/env python3
"""
<<<<<<< HEAD
Module that imports function
takes an integer and returns asyncio.Task
"""


import asyncio
=======
Task creation module
"""

import asyncio

>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
<<<<<<< HEAD
    """Return asyncio.Task"""
=======
    """
    Takes an integer max_delay and returns an asyncio.Task
    that wraps the wait_random coroutine.
    """
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
    return asyncio.create_task(wait_random(max_delay))
