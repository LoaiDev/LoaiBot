import discord
from discord.ext import commands
from helpers import config


def setup(bot):
    bot.add_command(vote)


@commands.command()
async def vote(ctx):
    embed = discord.Embed(title="Vote Links", color=0x2ACCCF)
    embed.set_footer(text=f"Voting While Not In Game May Not Give Vote Key")
    value = ""
    for index, link in enumerate(config("vote.links")):
        value += f"[Vote {index + 1}]({link})\n"
    embed.add_field(name=f"**Torus Vote Links**", value=value)
    await ctx.send(embed=embed)
