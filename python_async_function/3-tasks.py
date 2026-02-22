#!/usr/bin/env python3
"""
Task creation module
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task
    that wraps the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
