import disnake
from disnake.ext import commands
from aiohttp import ClientSession

class Hent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name = 'nsfw', description = 'постит хорни картиночки по вашему запросу', nsfw = True)
    async def hent(self, inter, limit: str, filters: str):
        arguments = '+'.join(filters.split())
        url = f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&limit={limit}&tags={arguments}&json=1'
        async with ClientSession() as session:
            async with session.get(url=url) as resp:
                data = await resp.json()
        all_hent = ''
        lim = 0
        for d in data:
           d = data[lim]
           all_hent += str(d['file_url']) + '\n'
           lim += 1
        await inter.response.send_message(f'Держи картиночки, пошляк: \n {all_hent}')
    
def setup(bot):
    bot.add_cog(Hent(bot))