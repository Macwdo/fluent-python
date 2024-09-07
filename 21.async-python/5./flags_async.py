import asyncio
from flags import BASE_URL, main, save_flag
from httpx import AsyncClient

async def get_flag(client: AsyncClient, cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=6.1, follow_redirects=True)
    return resp.read()

async def download_one(client: AsyncClient, cc: str):
    image = await get_flag(client, cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

def download_many(cc_list: list[str]) -> int:  # (1)
    return asyncio.run(supervisor(cc_list))  # (2)

async def supervisor(cc_list: list[str]) -> int:
    async with AsyncClient() as client:  # (3)
        to_do = [download_one(client, cc) for cc in sorted(cc_list)]  # (4)
        res = await asyncio.gather(*to_do)  # (5)

    return len(res)  # (6)


if __name__ == "__main__":
    main(download_many)
