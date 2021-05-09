import discord

from src.services.channels import get_channel, set_channel


def setup(bot):
    bot.add_listener(setup_listener(bot))


def setup_listener(bot):
    async def on_member_unban(guild, user):
        channel = bot.get_channel(840757849683918854)
        if not channel:
            channel = await bot.fetch_channel(840757849683918854)
        embed = discord.Embed(title=f"**{user} Has Been UnBanned From {guild}**", color=0x2ACCCF)
        embed.set_thumbnail(url=user.avatar_url)
        await channel.send(embed=embed)

    return on_member_unban
