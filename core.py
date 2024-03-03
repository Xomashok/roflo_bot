import disnake
import os
from disnake.ext import commands

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())

@bot.command()
@commands.is_owner()
async def load(ctx, ext):
    bot.load_extension(f'cogs.{ext}')

@bot.command()
@commands.is_owner()
async def unload(ctx, ext):
    bot.unload_extension(f'cogs.{ext}')

@bot.command()
@commands.is_owner()
async def reload(ctx, ext):
    bot.reload_extension(f'cogs.{ext}')

for file_name in os.listdir('cogs'):
    if file_name.endswith('.py'):
        bot.load_extension(f'cogs.{file_name[:-3]}')

bot.run('BOT_TOKEN')

