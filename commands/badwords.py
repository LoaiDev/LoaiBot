from discord.ext import commands
import discord
import services.badwords as badwordsService


def setup(bot):
    bot.add_command(badwords)


@commands.group()
async def badwords(ctx):
    if ctx.invoked_subcommand is None:
        file = discord.File(badwordsService.get_file())
        await ctx.send(file=file)


@badwords.command()
async def add(ctx, *words):
    words = list(words)
    badwordsService.add_badwords(words)
    await ctx.send(f"```js\nAdded {words} to the list```")


@badwords.command()
async def remove(ctx, *words):
    words = list(words)
    badwordsService.remove_badwords(words)
    await ctx.send(f"```js\nRemoved {words} from the list```")


@badwords.command()
async def list(ctx):
    await ctx.invoke(ctx.bot.get_command("badwords"))
