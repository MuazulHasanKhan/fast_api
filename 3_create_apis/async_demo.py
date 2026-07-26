import asyncio
from timeit import default_timer as timer

async def run_task(name, seconds):
    print(f"Task {name} started at {timer()}")
    await asyncio.sleep(seconds)
    print(f"Task {name} completed at {timer()}")


async def main():
    start = timer()
    await asyncio.gather(
        run_task("A", 2),
        run_task("B", 3),
        run_task("C", 1)
    )
    end = timer()
    print(f"Total time taken: {end - start} seconds")


asyncio.run(main())