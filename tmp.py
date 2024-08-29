import asyncio


async def my_result():
    return 42

my_task = asyncio.create_task(my_result())

result = asyncio.run(my_result())
print(f'Answer: {result}')

