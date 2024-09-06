from collections.abc import Generator
from typing import TypeAlias, Union, NamedTuple

class Result(NamedTuple):  # (1)
    count: int  # type: ignore  # (2)
    average: float

class Sentinel:  # (3)
    def __repr__(self):
        return f'<Sentinel>'

STOP = Sentinel()  # (4)

SendType: TypeAlias = float | Sentinel  # (5)

def averager2(verbose: bool = False) -> Generator[None, SendType, Result]:  # (1)
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield  # (2)
        if verbose:
            print('received:', term)
        if isinstance(term, Sentinel):  # (3)
            break
        total += term  # (4)
        count += 1
        average = total / count
    return Result(count, average)  # (5)

coroutine = averager2(True)
next(coroutine)
coroutine.send(1)
coroutine.send(3)

try:
    coroutine.send(STOP)
except StopIteration as exec:
    result = exec.value

print(result)


