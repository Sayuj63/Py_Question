import asyncio

async def async_function():
    print("Start Async Function")
    await asyncio.sleep(1)
    print("End Async Function")

asyncio.run(async_function())
