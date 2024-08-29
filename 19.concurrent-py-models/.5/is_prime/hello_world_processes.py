import itertools
import math
import os
import time
from multiprocessing import Process, Event  # (1)
from multiprocessing import synchronize  # (2)

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

def spin(msg: str, done: synchronize.Event) -> None:
    print("Spinner pid: ", os.getpid())

    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        if done.wait(0.1):
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


def slow() -> int:
    start = time.perf_counter()
    find_prime(5_000_111_000_222_021)
    print(f"Time taken: {time.perf_counter() - start}")
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Process(
        target=spin,  # (4)
        args=("thinking!", done),
    )
    
    print("Main pid:", os.getpid())
    print(f"spinner object: {spinner}")  # (5)
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()  # (9)
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()