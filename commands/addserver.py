from discord.ext import commands
import discord
from helpers import config
from permissions import is_developer


def setup(bot):
    bot.add_command(addserver)

@is_developer()
@commands.command()
async def addserver(ctx):
    link = config("invite.link").replace("{client_id}", config("invite.client_id"))
    embed = discord.Embed(
        title="Add Me To Your Server",
        description=f"[Click To Add]({link})",
        color=0x2ACCCF)
    await ctx.send(embed=embed)
