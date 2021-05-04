import json
import discord
from discord.ext import commands
from services.prefix import get_prefix


def setup(bot):
    bot.add_command(help)


@commands.command()
async def help(ctx):
    newprefix = get_prefix(ctx.guild.id)
    embed = discord.Embed(title = f"**Commands For SniffBot and SugarBot**", color = (0x2ACCCF))
    embed.add_field(name=f"**Both Bot's Commands**", value=f"**{newprefix}addserver** ~ Sends an invite link to add the bot to your personal server\n**{newprefix}uptime** ~ Gets the bot's uptime\n**{newprefix}ping** ~ Gets the bot's connection strength\n**{newprefix}sourcecode** ~ Sends a link to the bot's source code")
    embed.add_field(name="**SugarBot Commands**", value=f"**{newprefix}vote** ~ Gets the vote links when not in game", inline=False)
    embed.add_field(name="**SniffBot Commands**", value=f"**{newprefix}f** ~ Many f's in chat\n**{newprefix}sus** ~ Shows how sus somebody is\n**{newprefix}selfping** ~ Literally just pings yourself\n**{newprefix}roast** ~ sends an insult to yourself\n**{newprefix}reverse** ~ Reverses your message you put after\n**{newprefix}mock** ~ Sends your message in a mocking way\n**{newprefix}8ball** ~ Answers a yes or no question\n**{newprefix}slots** ~ Fills your gambling addiction")
    embed.add_field(name=f"**Staff Commands**", value=f"**{newprefix}prefix** ~ Changes the server's command prefix\n**{newprefix}nick** ~ Changes the pinged user's nickname to what you put\n**{newprefix}mute** ~ Mutes the pinged user\n**{newprefix}unmute** ~ Unmutes the pinged user\n**{newprefix}banrole** ~ revokes the pinged user's Torus role and replaces it with Banned role\n**{newprefix}unbanrole** ~ revokes the pinged user's Banned role and replaces it with Torus role\n**{newprefix}clear** ~ Delete's the given amount of messages\n**{newprefix}userinfo** ~ Gets the user information of the given user\n**{newprefix}ban** ~ bans the pinged user\n**{newprefix}unban** ~ unbans the user (needs full discord username")
    embed.set_footer(text=f"These commands are for Discord only.")
    await ctx.send(embed=embed)