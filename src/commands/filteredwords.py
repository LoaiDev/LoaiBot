from discord.ext import commands
from discord.ext.commands import RoleConverter
import discord
import src.services.filteredwords as filteredwordsService
from src.permissions import is_developer
from src.services.filteredwords import get_channel, set_channel, get_ping_role, set_ping_role, get_ignored_roles, \
    set_ignored_roles


def setup(bot):
    bot.add_command(filteredwords)


@commands.has_permissions(administrator=True)
@commands.group(aliases=["words", "filtered"])
async def filteredwords(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"```py\nhatespeech = {filteredwordsService.get_filteredwords()}\n```")


@commands.has_permissions(administrator=True)
@filteredwords.command()
async def add(ctx, *words):
    affected_words = filteredwordsService.add_filteredwords(words)
    if affected_words:
        await ctx.send(f"```js\nAdded {affected_words} to the list```")
    else:
        await ctx.send("```No words added```")


@commands.has_permissions(administrator=True)
@filteredwords.command()
async def remove(ctx, *words):
    affected_words = filteredwordsService.remove_filteredwords(words)
    if affected_words:
        await ctx.send(f"```js\nRemoved {affected_words} from the list```")
    else:
        await ctx.send("```No words removed```")


@is_developer()
@filteredwords.command()
async def file(ctx):
    file = discord.File(filteredwordsService.get_file())
    await ctx.send(file=file)


@filteredwords.group()
@commands.has_permissions(administrator=True)
async def channel(ctx):
    if ctx.invoked_subcommand is None:
        channel_id = get_channel(ctx.guild.id)
        if not channel_id:
            await ctx.send(
                f"No Filtered Words Alert channel found. Use \"{ctx.prefix}filteredwords channel set (channel)\" "
                "command to set it")
            return
        await ctx.send(f"Filtered Words Alert channel is {ctx.bot.get_channel(channel_id).mention}")


@channel.command(name="set")
@commands.has_permissions(administrator=True)
async def channel_set(ctx, channel: discord.TextChannel):
    set_channel(ctx.guild.id, channel.id)
    await ctx.send("Channel has been set!")


@filteredwords.group()
@commands.has_permissions(administrator=True)
async def pingrole(ctx):
    if ctx.invoked_subcommand is None:
        role_id = get_ping_role(ctx.guild.id)
        if not role_id:
            await ctx.send(
                f"No Filtered Words Ping role found. Use \"{ctx.prefix}filteredwords pingrole set (role)\" command to "
                "set it")
            return
        await ctx.send(f"Filtered Words Ping role is {discord.utils.get(ctx.guild.roles, id=role_id).mention}")


@pingrole.command(name="set")
@commands.has_permissions(administrator=True)
async def pingrole_set(ctx, role: discord.Role):
    set_ping_role(ctx.guild.id, role.id)
    await ctx.send("Role has been set!")


@filteredwords.group()
@commands.has_permissions(administrator=True)
async def ignoredroles(ctx):
    if ctx.invoked_subcommand is None:
        roles_ids = get_ignored_roles(ctx.guild.id)
        if not roles_ids:
            await ctx.send(
                f"No Ignored roles found. Use \"{ctx.prefix}filteredwords ignoredroles set (roles)\" "
                f"command to set it")
            return
        await ctx.channel.send(
            f"Filtered Words Ping role are {list(map(role.mention for role in list(filter(lambda role: (role.id in roles_ids), ctx.guild.roles))))} ")


@ignoredroles.command(name="set")
@commands.has_permissions(administrator=True)
async def ignoredroles_set(ctx, *roles: RoleConverter):
    set_ignored_roles(ctx.guild.id, roles)
    await ctx.send("Roles has been set")
