import discord
from discord.ext import commands

from src.services.roles import get_role


def setup(bot):
    bot.add_command(softunban)


@commands.command()
@commands.has_permissions(ban_members=True)
async def softunban(ctx, member: discord.Member):
    role_id = int(get_role(ctx.guild.id, "b"))
    if not role_id:
        await ctx.send(f"No Banned role found. Use {ctx.prefix}setbannedrole (role) command to set it")
        return
    role = discord.utils.get(ctx.guild.roles, id=role_id)
    if not discord.utils.get(member.roles, id=role_id):
        await ctx.send("User Is Not Banned")
        return
    await member.remove_roles(role)
    await ctx.send(f"Unbanned {member.mention}")