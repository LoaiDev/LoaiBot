import discord
from discord.ext import commands
from src.services.roles import get_role


def setup(bot):
    bot.add_command(unmute)


@commands.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    role_id = int(get_role(ctx.guild.id, "m"))
    if not role_id:
        await ctx.send("No Muted role found. Use -setmutedrole (role) command to set it")
        return
    role = discord.utils.get(ctx.guild.roles, id=role_id)
    if not discord.utils.get(member.roles, id=role_id):
        await ctx.send("User Is Not Muted")
        return
    await member.remove_roles(role)
    await ctx.send(f"Unmuted {member.mention}")

