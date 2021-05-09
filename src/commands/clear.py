from discord.ext import commands


def setup(bot):
    bot.add_command(clear)


@commands.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount + 1)
