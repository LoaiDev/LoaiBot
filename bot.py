import discord, datetime, time
from discord.ext import commands, tasks
from discord.ext.commands import Cog, Greedy
from discord.ext.commands import CheckFailure
import asyncio
from discord.utils import get

import json
from discord.ext.commands import has_permissions, MissingPermissions
import time
from random import randint
import random
from random import choice
client = discord.Client()
# def get_prefix(client, message):
#     with open('prefix.json', 'r') as f:
#         prefixes = json.load(f)
#     return prefixes[str(message.guild.id)]
# client = commands.Bot(command_prefix= get_prefix, case_insensitive=True)
# client.remove_command("help")
# hatespeech = ["cracker", "faggot", "nigga", "nigger", "niqqa", "niqqer", "dike", "dyke", "n1g", "nibba", "nibber", "chink", "kike", "zipperhead", "zipper head", "jew"]
# status = ["DontSniffSugar#5524 is my author!", f'"-" is default prefix', f'say "prefixhelp" to get your prefix if you forget', 'sniffhelp is the help command']
start_time = time.time()

# @client.event
# async def on_ready():
#     print("Bot running with:")
#     print("Username: ", client.user.name)
#     print("User ID: ", client.user.id)
#     change_status.start()

# @client.event
# async def on_guild_join(guild):
#     with open('prefix.json', 'r') as f:
#         prefixes = json.load(f)
#     prefixes[str(guild.id)] = "-"
#     with open('prefix.json', 'w') as f:
#         json.dump(prefixes, f, indent=4)

# @client.event
# async def on_guild_remove(guild):
#     with open('prefix.json', 'r') as f:
#         prefixes = json.load(f)
#     prefixes.pop(str(guild.id))
#     with open('prefix.json', 'w') as f:
#         json.dump(prefixes, f, indent=4)

# @client.command(pass_context=True)
# @commands.has_permissions(administrator=True)
# async def prefix(ctx, *, prefix):
#     with open('prefix.json', 'r') as f:
#         prefixes = json.load(f)
#     prefixes[str(ctx.guild.id)] = prefix
#     with open('prefix.json', 'w') as f:
#         json.dump(prefixes, f, indent=4)
#     await ctx.send(f"Your server's prefix is now: `{prefix}`")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user = message.author
    if any(word in message.content.lower() for word in hatespeech):
        ignorerole = discord.utils.get(user.roles, name="Admin")
        if message.author.id == 474566033798332417:
            return
        if message.content.startswith("DontSniffSugar »"):
            return
        if ignorerole in user.roles:
            return
        pingrole = discord.utils.get(message.guild.roles, id=835323285230845952)
        channel = client.get_channel(833894094723481620)
        embed = discord.Embed(title = f"**{message.author} Was Detected For Hate Speech**", color = (0x2ACCCF))
        embed.add_field(name="**Direct Ping**", value=f"{message.author.mention}", inline=False)
        embed.add_field(name="**Message**", value=f"{message.content}", inline=False)
        embed.add_field(name="**Channel**", value=f"{message.channel.mention}", inline=False)
        embed.add_field(name="**Time**", value=message.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="**Go To Message**", value=f"[Jump To Message]({message.jump_url})")
        await channel.send(f"{pingrole.mention}")
        await channel.send(embed = embed)

    if message.content.startswith("prefixhelp"):
        with open('prefix.json', 'r') as f:
            prefixes = json.load(f)
        await message.channel.send(f"Your server's prefix is : `{prefixes[str(message.guild.id)]}`")

    if message.mention_everyone:
        await message.channel.send("You can't mention everyone")
        return
    
    user = message.author
    mutedrole = discord.utils.get(user.roles, id=835226308513890405)
    if mutedrole in user.roles:
        if not mutedrole in message.author.roles:
            return
        await message.delete()

    await client.process_commands(message)

# @client.command(pass_context=True)
# async def ping(ctx):
#     embed = discord.Embed(title="**This bot's ping is:**", description=f"***{round(client.latency * 1000)}ms***", color = (0x2ACCCF))
#     await ctx.send(embed=embed)

# @client.command(pass_context=True)
# async def getprefix(ctx):
#     with open('prefix.json', 'r') as f:
#         prefixes = json.load(f)
#     await ctx.send(f"Your server's prefix is: `{prefixes[str(ctx.guild.id)]}`")

# @client.command(pass_context=True)
# async def addserver(ctx):
#     embed = discord.Embed(title="Add Me To Your Server", description=f"[Click To Add](https://discord.com/api/oauth2/authorize?client_id=819425223328661504&scope=bot)", color = (0x2ACCCF))
#     await ctx.send(em bed=embed)

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def badwords(ctx):
    await ctx.send(f"```py\nhatespeech = {hatespeech}\n```")

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    if member.id == 474566033798332417:
        await ctx.send("Could not ban that user.")
        return
    if member.id == 820361265087643699:
        await ctx.send("Could not ban that user.")
        return
    await member.ban(reason=f"{ctx.author} banned them for {reason}")

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def prefixjson(ctx):
    file = discord.File("prefix.json")
    await ctx.author.send(file=file)

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {member_name}#{member_discriminator}")
            return

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    if member.id == 474566033798332417:
        await ctx.send("Could not kick that user.")
        return
    if member.id == 820361265087643699:
        await ctx.send("Could not kick that user.")
        return
    await member.kick(reason=f"{reason}, Kicked by: {ctx.author}")

@client.command(pass_context=True)
async def sniffhelp(ctx):
    with open('prefix.json', 'r') as f:
        prefixes = json.load(f)
    newprefix = prefixes[str(ctx.guild.id)]
    embed = discord.Embed(title = f"**Commands For SniffBot and SugarBot**", color = (0x2ACCCF))
    embed.add_field(name=f"**Both Bot's Commands**", value=f"**{newprefix}addserver** ~ Sends an invite link to add the bot to your personal server\n**{newprefix}uptime** ~ Gets the bot's uptime\n**{newprefix}ping** ~ Gets the bot's connection strength\n**{newprefix}sourcecode** ~ Sends a link to the bot's source code")
    embed.add_field(name="**SugarBot Commands**", value=f"**{newprefix}vote** ~ Gets the vote links when not in game", inline=False)
    embed.add_field(name="**SniffBot Commands**", value=f"**{newprefix}f** ~ Many f's in chat\n**{newprefix}sus** ~ Shows how sus somebody is\n**{newprefix}selfping** ~ Literally just pings yourself\n**{newprefix}roast** ~ sends an insult to yourself\n**{newprefix}reverse** ~ Reverses your message you put after\n**{newprefix}mock** ~ Sends your message in a mocking way\n**{newprefix}8ball** ~ Answers a yes or no question\n**{newprefix}slots** ~ Fills your gambling addiction")
    embed.add_field(name=f"**Staff Commands**", value=f"**{newprefix}prefix** ~ Changes the server's command prefix\n**{newprefix}nick** ~ Changes the pinged user's nickname to what you put\n**{newprefix}mute** ~ Mutes the pinged user\n**{newprefix}unmute** ~ Unmutes the pinged user\n**{newprefix}banrole** ~ revokes the pinged user's Torus role and replaces it with Banned role\n**{newprefix}unbanrole** ~ revokes the pinged user's Banned role and replaces it with Torus role\n**{newprefix}clear** ~ Delete's the given amount of messages\n**{newprefix}userinfo** ~ Gets the user information of the given user\n**{newprefix}ban** ~ bans the pinged user\n**{newprefix}unban** ~ unbans the user (needs full discord username")
    embed.set_footer(text=f"These commands are for Discord only.")
    await ctx.send(embed=embed)

@client.command(pass_context=True, aliases=["nick"])
@commands.has_permissions(manage_nicknames=True)
async def nickname(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.send(f"Set {member.mention}'s nickname to {nick}")

@client.command(pass_context=True)
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(color=0x2ACCCF)
    embed.add_field(name="***SugarBot Has Been Alive For***", value=text)
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        await ctx.send("Current uptime: " + text)

@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, id=835226308513890405)
    SugarsBots = discord.utils.get(guild.roles, id=833892814302740481)
    if SugarsBots in member.roles:
        await ctx.send(f"{ctx.author.mention} that user cannot be muted")
        return
    if member.id == 474566033798332417:
        await ctx.send(f"{ctx.author.mention} that user cannot be muted")
        return
    if member.id == 820361265087643699:
        await ctx.send(f"{ctx.author.mention} that user cannot be muted")
        return
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def banrole(ctx, member: discord.Member):
    bannedrole = discord.utils.get(ctx.guild.roles, id=834239934969544765)
    torusrole = discord.utils.get(ctx.guild.roles, id=833495947526930513)
    await member.add_roles(bannedrole)
    await member.remove_roles(torusrole)
    await ctx.author.send(f"Don't forget to remove their pungent role if they had it too.")

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unbanrole(ctx, member: discord.Member):
    bannedrole = discord.utils.get(ctx.guild.roles, id=834239934969544765)
    torusrole = discord.utils.get(ctx.guild.roles, id=833495947526930513)
    await member.remove_roles(bannedrole)
    await member.add_roles(torusrole)
    await ctx.author.send(f"If they were pungent don't forgot to add their role back too.")

@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, id=835226308513890405)
    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def poll(ctx, *, message):
    embed = discord.Embed(title="Poll", description=f"{message}", color = (0x2ACCCF))
    embed.set_footer(text=f"Poll started by {ctx.author}", icon_url=ctx.author.avatar_url)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await ctx.message.delete()

@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)

@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def userinfo(ctx, member: discord.Member):
    roles = [role for role in member.roles]
    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="**ID:**", value=member.id)
    embed.add_field(name="**Nickname:**", value=member.display_name)
    embed.add_field(name="**Account Created At:**", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="**Joined This Server At:**", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name=f"**Roles ({len(roles)})**", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="**Top Role:**", value=member.top_role.mention)
    embed.add_field(name="**Bot?**", value=member.bot)
    await ctx.send(embed=embed)

@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="**User Not Found**", description="**Did you spell it right?**", color = (0x2ACCCF))
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def vote(ctx):
    embed = discord.Embed(title="Vote Links", color = (0x2ACCCF))
    embed.set_footer(text=f"Voting While Not In Game May Not Give Vote Key")
    embed.add_field(name=f"**Torus Vote Links**", value="[Vote 1](https://minecraftservers.biz/servers/149924/)\n[Vote 2](https://minecraftlist.org/vote/22622)\n[Vote 3](https://minecraft-mp.com/server/284916/vote/)\n[Vote 4](https://www.planetminecraft.com/server/torussmp-whitelist-survival-no-afk-kick-no-land-claim-community-dreamsmp-like-brand-new/vote/)\n[Vote 5](https://topg.org/minecraft-servers/server-628267)\n[Vote 6](https://minecraftservers.biz/servers/148916/)\n[Vote 7](https://topservers.com/minecraft/in-1866)\n[Vote 8](https://minecraft-server-list.com/server/474969/vote/)")
    await ctx.send(embed=embed)

@client.command(pass_context=True, aliases=["source"])
async def sourcecode(ctx):
    embed = discord.Embed(title = f"Source Code", description = f"[Source Code Is Here!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)", color = (0x2ACCCF))
    await ctx.send(embed = embed)
        
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send(f"{ctx.author.mention} You are missing permission(s) to run this command.")
        return

@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

client.run("TOKEN")