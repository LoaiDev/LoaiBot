from discord.ext import commands
from helpers import config
import discord


def setup(bot):
    bot.add_command(kick)


@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if member.id in config("immunes"):
        await ctx.send(f"You can not kick this user")
        return
    await member.kick(reason=f"{reason}, Kicked by: {ctx.author}")