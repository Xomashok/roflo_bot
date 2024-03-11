import disnake 
from disnake.ext import tasks, commands
import random

class Nya(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.nya.start()

    @commands.command()
    async def Nya(self, inter, chanel : str):
        data = open('data/nya.txt', 'w')
        data.write(chanel)
        data.close
        await inter.response.send_message(f'Канал записан')

    @tasks.loop(hours=1)
    async def nya():
        nya = ('Мя', 'Мяу', 'Ня')
        ran = random.randint(0, 2)
        data = open('data/nya.txt')
        channel = bot.get_channel(data.read())
        await channel.send(nya[ran])

def setup(bot):
    bot.add_cog(Nya(bot))