from discord.ext import commands
from permissions import is_developer


def setup(bot):
    bot.add_command(say)


@is_developer()
@commands.command()
async def say(ctx, *, msg):
    await ctx.send(msg)
    await ctx.message.delete()
