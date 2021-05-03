from discord.ext import commands
from services.prefix import get_prefix


def setup(bot):
    bot.add_command(getprefix)


@commands.command()
async def getprefix(ctx):
    await ctx.send(f"Your server's prefix is: `{get_prefix(ctx.guild.id)}`")