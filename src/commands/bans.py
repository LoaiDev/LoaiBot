from discord.ext import commands
from src.services.bans import generate_embed, search_bans
from typing import Optional


def setup(bot):
    bot.add_command(bans)


@commands.command()
async def bans(ctx, search: Optional[str] = None):
    bans = await ctx.guild.bans()
    if search:
        bans = search_bans(bans, search)
    if len(bans) < 1:
        await ctx.send(f"```No users found by the name of \"{search}\"```")
    elif 1 <= len(bans) <= 10:
        for ban in bans:
            embed = generate_embed(ban)
            await ctx.send(embed=embed)
    elif len(bans) > 10:
        await ctx.send(f"```Found more than 10 bans with the name \"{search}\"\n Please use a more specific search```")
