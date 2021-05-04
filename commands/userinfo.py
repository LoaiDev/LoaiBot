import discord
from discord.ext import commands


def setup(bot):
    bot.add_command(userinfo)


@commands.command()
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
        embed = discord.Embed(title="**User Not Found**", description="**Did you spell it right?**", color=0x2ACCCF)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
