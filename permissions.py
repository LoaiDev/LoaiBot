from discord.ext import commands
from helpers import config


def is_developer():
    async def predicate(ctx):
        return ctx.author.id in config("developers")

    return commands.check(predicate)
