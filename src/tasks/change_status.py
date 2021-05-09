import discord
import random
from discord.ext import tasks
from src.helpers import read_json, storage, config


@tasks.loop(seconds=5)
async def change_status(bot):
    try:
        status = read_json(storage(config("status.file_name")))
    except FileNotFoundError:
        status = [config("status.default")]
    await bot.change_presence(activity=discord.Game(random.choice(status)))
