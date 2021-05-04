from discord.ext import commands
import discord
from helpers import config


def setup(bot):
    bot.add_command(ban)


@commands.has_permissions(ban_members=True)
@commands.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if member.id in config("immunes"):
        await ctx.send(f"You can not ban this user")
        return
    await member.ban(reason=f"{ctx.author} banned them for {reason}")