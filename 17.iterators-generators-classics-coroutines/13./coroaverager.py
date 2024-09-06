from collections.abc import Generator


def averager() -> Generator[float, float, None]:
    total = 0.0
    count = 0
    average = 0
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
        
r1 = averager()
next(r1)
print(r1.send(2))
print(r1.send(5))

            
