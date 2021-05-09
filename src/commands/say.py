from discord.ext import commands
from src.permissions import is_developer


def setup(bot):
    bot.add_command(say)


@is_developer()
@commands.command(cog_name="main")
async def say(ctx, *, msg):
    await ctx.send(msg)
    await ctx.message.delete()
