import asyncio
import itertools


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

async def slow() -> int:
    await asyncio.sleep(3)  # (4)
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