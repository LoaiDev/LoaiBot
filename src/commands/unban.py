from discord.ext import commands
from src.services.bans import generate_embed, search_bans


def setup(bot):
    bot.add_command(unban)


@commands.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member: str):
    banned_users = await ctx.guild.bans()
    filtered_entries = search_bans(banned_users, member)

    if len(filtered_entries) < 1:
        await ctx.send(f"```No users found by the name of \"{member}\"```")
    elif 2 <= len(filtered_entries) <= 10:
        await ctx.send(f"```Found Multiple Users with the name \"{member}\"```")
        for filtered_entry in filtered_entries:
            embed = generate_embed(filtered_entry)
            await ctx.send(embed=embed)
    elif len(filtered_entries) > 10:
        await ctx.send(f"```Found more than 10 bans with the name \"{member}\"\nPlease use a more specific search```")
    elif len(filtered_entries) == 1:
        user = filtered_entries[0].user
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned {user.name}#{user.discriminator}")
