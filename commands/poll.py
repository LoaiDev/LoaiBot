import discord
from discord.ext import commands


def setup(bot):
    bot.add_command(poll)


@commands.command()
@commands.has_permissions(administrator=True)
async def poll(ctx, *, message):
    embed = discord.Embed(title="Poll", description=f"{message}", color=0x2ACCFF, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Poll started by {ctx.author}", icon_url=ctx.author.avatar_url)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await ctx.message.delete()
