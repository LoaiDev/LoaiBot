import discord

from services.filteredwords import get_channel, get_ignored_roles, get_ping_role, get_filteredwords
from helpers import config


def generate_embed(message):
    embed = discord.Embed(title=f"**{message.author} Was Detected For Hate Speech**", color=0x2ACCCF)
    embed.add_field(name="**Direct Ping**", value=f"{message.author.mention}", inline=False)
    embed.add_field(name="**Message**", value=f"{message.content}", inline=False)
    embed.add_field(name="**Channel**", value=f"{message.channel.mention}", inline=False)
    embed.add_field(name="**Time**", value=message.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name="**Go To Message**", value=f"[Jump To Message]({message.jump_url})")
    return embed


async def check_for_filteredwords(message, bot):
    channel_id = get_channel(message.guild.id)
    user = message.author
    if (not channel_id) or (user.id in config("immunes")):
        print("no channel")
        return

    if not any(word in message.content.lower() for word in get_filteredwords()):
        return

    ignored_roles = get_ignored_roles(message.guild.id)
    if ignored_roles:
        if any(role.id in ignored_roles for role in user.roles):
            print("ignored")
            return

    channel = bot.get_channel(channel_id)
    embed = generate_embed(message)
    ping_role_id = get_ping_role(message.guild.id)
    if ping_role_id:
        ping_role = discord.utils.get(message.guild.roles, id=ping_role_id)
        await channel.send(f"{ping_role.mention}")
    await channel.send(embed=embed)


def setup(bot):
    bot.add_listener(setup_listener(bot))


def setup_listener(bot):
    async def on_message(message):
        if message.author == bot.user:
            return
        await check_for_filteredwords(message, bot)

    return on_message
