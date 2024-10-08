from flags import save_flag, get_flag, main  # (1)
from flags_threadpool import download_one
from concurrent import futures

def download_many(cc_list: list[str]) -> int:
    cc_list = cc_list[:5]  # (1)
    with futures.ThreadPoolExecutor(max_workers=3) as executor:  # (2)
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):  # (3)
            future = executor.submit(download_one, cc)  # (4)
            to_do.append(future)  # (5)
            print(f'Scheduled for {cc}: {future}')  # (6)

        for count, future in enumerate(futures.as_completed(to_do), 1):  # (7)
            res: str = future.result()  # (8)
            print(f'{future} result: {res!r}')  # (9)

    return count
if __name__ == '__main__':
    main(download_many)  # (6)
