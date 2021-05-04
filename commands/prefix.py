from discord.ext import commands
import discord
from permissions import is_developer
from services.prefix import set_prefix, get_prefix, get_file


def setup(bot):
    bot.add_command(prefix)


@commands.group()
async def prefix(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"Your server's prefix is `{get_prefix(ctx.guild.id)}`")


@commands.has_permissions(administrator=True)
@prefix.command(name="set")
async def prefix_set(ctx, *, prefix):
    set_prefix(ctx.guild.id, prefix)
    await ctx.send(f"Your server's prefix is now: `{prefix}`")


@is_developer()
@prefix.command()
async def file(ctx):
    file = discord.File(get_file())
    await ctx.send(file=file)
