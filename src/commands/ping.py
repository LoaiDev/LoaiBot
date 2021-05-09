from discord.ext import commands
import discord

def setup(bot):
    bot.add_command(ping)


@commands.command()
async def ping(ctx):
    embed = discord.Embed(
        title="**This bot's ping is:**",
        description=f"***{round(ctx.bot.latency * 1000)}ms***",
        color=0x2ACCCF)
    await ctx.send(embed=embed)