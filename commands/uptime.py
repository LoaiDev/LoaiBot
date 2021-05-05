from discord.ext import commands
from permissions import is_developer
import discord
import datetime
import time


def setup(bot):
    bot.add_command(setup_command(time.time()))


def setup_command(start_time):
    @commands.command()
    @is_developer()
    async def uptime(ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(color=0x2ACCCF)
        embed.add_field(name="***LoaiBot Has Been Alive For***", value=text)
        await ctx.send(embed=embed)

    return uptime
