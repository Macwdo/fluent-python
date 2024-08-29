import itertools
import os
import time
from multiprocessing import Process, Event  # (1)
from multiprocessing import synchronize  # (2)


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
    time.sleep(20)
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