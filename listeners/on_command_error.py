from discord.ext.commands import CommandNotFound, MissingPermissions



def setup(bot):
    bot.add_listener(on_command_error)


async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    if isinstance(error, MissingPermissions):
        await ctx.send(f"{ctx.author.mention} You are missing permission(s) to run this command.")
        return
