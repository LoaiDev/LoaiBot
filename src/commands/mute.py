from discord.ext import commands
import discord
from src.helpers import config
from src.services.roles import get_role


def setup(bot):
    bot.add_command(mute)


@commands.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    if member.id in config("immunes"):
        await ctx.send(f"You can not mute this user")
        return
    role_id = int(get_role(ctx.guild.id, "m"))
    if not role_id:
        await ctx.send(f"No Muted role found. Use {ctx.prefix}setmutedrole (role) command to set it")
        return
    role = discord.utils.get(ctx.guild.roles, id=role_id)
    if discord.utils.get(member.roles, id=role_id):
        await ctx.send("User Already Muted")
        return
    await member.add_roles(role, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {ctx.guild.name} for {reason}")
