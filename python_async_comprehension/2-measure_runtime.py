#!/usr/bin/env python3
"""Module for measuring runtime of parallel async comprehensions."""

import asyncio
import time
from typing import float

# Import async_comprehension from the previous file
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using asyncio.gather.
    
    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.perf_counter()
    
    # Run async_comprehension 4 times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = time.perf_counter()
    return end_time - start_time
    
