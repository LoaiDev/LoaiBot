import discord
from discord.ext import commands

from src.services.roles import set_role


def setup(bot):
    bot.add_command(setbannedrole)


@commands.command()
@commands.has_permissions(administrator=True)
async def setbannedrole(ctx, role: discord.Role):
    set_role(ctx.guild.id, "b", role.id)
    await ctx.send("Role has been set!")
