from discord.ext import commands


def setup(bot):
    bot.add_command(spam)


@commands.command()
async def spam(ctx, number=100, *, message="spam"):
    for x in range(number):
        await ctx.send(message)
    await ctx.send(f"spammed \"{message}\" {number} time(s)")
