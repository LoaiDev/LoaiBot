import discord
from discord.ext import commands


def setup(bot):
    bot.add_command(nickname)


@commands.command(aliases=["nick"])
@commands.has_permissions(manage_nicknames=True)
async def nickname(ctx, member: discord.Member, *, nick):
    if nick == "reset":
        nick = member.name
    await member.edit(nick=nick)
    await ctx.send(f"Set {member.mention}'s nickname to {nick}")
