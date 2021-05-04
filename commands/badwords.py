from discord.ext import commands
import discord
import services.badwords as badwordsService
from permissions import is_developer


def setup(bot):
    bot.add_command(badwords)


@commands.has_permissions(administrator=True)
@commands.group()
async def badwords(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"```py\nhatespeech = {badwordsService.get_badwords()}\n```")


@commands.has_permissions(administrator=True)
@badwords.command()
async def add(ctx, *words):
    affected_words = badwordsService.add_badwords(words)
    if affected_words:
        await ctx.send(f"```js\nAdded {affected_words} to the list```")
    else:
        await ctx.send("```No words added```")


@commands.has_permissions(administrator=True)
@badwords.command()
async def remove(ctx, *words):
    affected_words = badwordsService.remove_badwords(words)
    if affected_words:
        await ctx.send(f"```js\nRemoved {affected_words} from the list```")
    else:
        await ctx.send("```No words removed```")


@commands.has_permissions(administrator=True)
@badwords.command()
async def list(ctx):
    await ctx.invoke(ctx.bot.get_command("badwords"))


@is_developer()
@badwords.command()
async def file(ctx):
    file = discord.File(badwordsService.get_file())
    await ctx.send(file=file)
