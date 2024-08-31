import requests
import itertools
import time
from threading import Thread, Event

global count
count = 0

def slow() -> int:
    sec = 1
    time.sleep(sec)  # (7)
    return sec

def request_and_print(times):
    global count
    for _ in range(times):
        start = time.perf_counter()
        requests.get("http://127.0.0.1:8000/")
        result_time = time.perf_counter() - start
        count += 1
        print(f"Request time: {result_time}")

def request(done):
    while True:
        request_and_print(1)
        if done.wait(0.1):
            break

def create_request_threads(thread_count: int) -> list[tuple[Thread, Event]]:
    threads = []
    for _ in range(thread_count):
        done = Event()
        thread = Thread(target=request, args=(done,))
        thread = (thread, done)
        threads.append(thread)
    
    return threads

def start_request_threads(threads):
    for thread in threads:
        thread, _ = thread
        thread.start()
        
    return threads
    
def stop_request_threads(threads):
    for thread in threads:
        thread, done = thread
        
        done.set()
        thread.join()

def supervisor() -> int:  # (1)
    request_threads = create_request_threads(6)
    request_threads = start_request_threads(request_threads)

    start = time.perf_counter()

    result = slow()
    stop_request_threads(request_threads)

    done_time = time.perf_counter() - start
    print(f"Done time: {done_time}")
    return result

def main() -> None:
    result = supervisor()  # (9)
    print(f"Stopped after {result} seconds")
    print(f"Total requests: {count}")


if __name__ == "__main__":
    main()
