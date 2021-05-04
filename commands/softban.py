from discord.ext import commands
import discord
from helpers import config
from services.roles import get_role


def setup(bot):
    bot.add_command(softban)


@commands.command()
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member):
    if member.id in config("immunes"):
        await ctx.send(f"You can not ban this user")
        return
    role_id = int(get_role(ctx.guild.id, "b"))
    if not role_id:
        await ctx.send(f"No Banned role found. Use {ctx.prefix}setbannedrole (role) command to set it")
        return
    role = discord.utils.get(ctx.guild.roles, id=role_id)
    if discord.utils.get(member.roles, id=role_id):
        await ctx.send("User Already Banned")
        return
    await member.add_roles(role)
    await ctx.send(f"soft banned {member.display_name}")

