import asyncio
import itertools
import math
from time import perf_counter

def find_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True

async def spin(msg: str) -> None:  # (1)
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)  # (2)
        except asyncio.CancelledError:  # (3)
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

async def calculate_async() -> int:
    start = perf_counter()
    find_prime(5_000_111_000_222_021)
    print(f"Time taken: {perf_counter() - start}")
    return 42

async def slow() -> int:
    await calculate_async()
    return 42


def main() -> None:  # (1)
    result = asyncio.run(supervisor())  # (2)
    print(f'Answer: {result}')

async def supervisor() -> int:  # (3)
    spinner = asyncio.create_task(spin('thinking!'))  # (4)
    print(f'spinner object: {spinner}')  # (5)
    result = await slow()  # (6)
    spinner.cancel()  # (7)
    return result

if __name__ == '__main__':
    main()