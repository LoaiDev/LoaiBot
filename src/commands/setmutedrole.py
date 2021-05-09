from discord.ext import commands
import discord
from src.services.roles import set_role


def setup(bot):
    bot.add_command(setmutedrole)


@commands.command()
@commands.has_permissions(administrator=True)
async def setmutedrole(ctx, role: discord.Role):
    set_role(ctx.guild.id, "m", role.id)
    await ctx.send("Role has been set!")
