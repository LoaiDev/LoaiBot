from discord.ext import commands
from services.prefix import set_prefix


def setup(bot):
    bot.add_command(prefix)


@commands.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, *, prefix):
    set_prefix(ctx.guild.id, prefix)
    await ctx.send(f"Your server's prefix is now: `{prefix}`")
