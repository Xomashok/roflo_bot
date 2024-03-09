from aiohttp import ClientSession
import random
import asyncio

async def hent( filters: str):
        arguments = '+'.join(filters.split())
        url = f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&limit=1000&tags={arguments}&json=1'
        async with ClientSession() as session:
            async with session.get(url=url) as resp:
                data = await resp.json()
        all_hent = ''
        lim = 0  
        while lim < 5:
            l = random.randint(0, 1000)
            d = data[int(l)]
            all_hent += str(d['file_url']) + '\n'
            lim += 1
        return all_hent

async def main():
    result = await hent('anal')
    print(result)

asyncio.run(main())