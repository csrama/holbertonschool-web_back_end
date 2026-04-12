#!/usr/bin/env python3
"""Module that contains a coroutine to run multiple async tasks concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return list of delays in ascending order."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []

    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results
