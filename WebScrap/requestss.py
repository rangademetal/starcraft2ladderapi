import aiohttp
import asyncio


async def post_data():
    async with aiohttp.ClientSession() as session:
        async with session.post(url='http://127.0.0.1:8000/insert_ladder/') as response:
            if response.status == 200:
                print('done')


async def update_data():
    async with aiohttp.ClientSession() as session:
        async with session.put(url='http://127.0.0.1:8000/update_ladder/') as response:
            if response.status == 200:
                print('done')


if __name__ == '__main__':
    asyncio.run(update_data())
