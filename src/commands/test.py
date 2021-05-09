from discord.ext import commands
import discord


def setup(bot):
    bot.add_command(test)


@commands.command()
async def test(ctx):
    invite = await ctx.guild.text_channels[0].create_invite()
    await ctx.send(invite)
