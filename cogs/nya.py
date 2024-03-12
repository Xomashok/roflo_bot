import disnake 
from disnake.ext import tasks, commands
import random
import re

class Nya(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.nya.start()

    @commands.command()
    async def Nya(self, inter, chanel : str):
        guild_id = inter.guild.id
        wr = re.sub(r'\D', '', chanel)
        data = open('data\\nya.txt', 'w')
        data.write(f'{guild_id}\n{wr}')
        data.close()
        await inter.send(f'Канал записан')

    @tasks.loop(hours=1)
    async def nya(self):
        nya = ('Мя', 'Мяу', 'Ня')
        with open('data\\nya.txt') as data:
            lines = data.readlines()
            guild_id = int(lines[0])
            channel_id = int(lines[1])
            guild = self.bot.get_guild(guild_id)
            if guild:
                channel = guild.get_channel(channel_id)
                if channel:
                    await channel.send(random.choice(nya))


def setup(bot):
    bot.add_cog(Nya(bot))