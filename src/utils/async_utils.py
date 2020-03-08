import asyncio
import signal
from typing import Any, Awaitable, Sequence

"""
Handling asynchronous shenanigans in Python3 can be somewhat annoying, so we use 
the function run_event_loop to allow for an easy useage of it. In case we have multiple
modules in the future that require asynchronous communicating, we can use this. 
"""

def run_event_loop(coroutines: Sequence[Awaitable[Any]], exit_when_complete: bool = False) -> None:
    eloop = asyncio.get_event_loop()
    tasks = [eloop.create_task(coro) for coro in coroutines]
    eloop.add_signal_handler(signal.SIGINT, stop_all_tasks)
    if exit_when_complete:
        for task in tasks:
            eloop.run_until_complete(task)
    else:
        eloop.run_forever()
    eloop.close()

def stop_all_tasks() -> None:
    eloop = asyncio.get_event_loop()
    asyncio.ensure_future(cancel_all_tasks(eloop))

async def cancel_all_tasks(loop: asyncio.AbstractEventLoop) -> None:
    tasks = asyncio.Task.all_tasks(loop)
    this_task = asyncio.Task.current_task(loop)
    tasks = []
    for task in all_tasks:
    	if task != this_task:
    		tasks.append(task)
    		task.cancel()
    results = await asyncio.gather(*tasks, return_exceptions=True)  # NOQA: F841
    loop.stop()