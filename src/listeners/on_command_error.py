import sys
import traceback

import discord.ext.commands as commands
import discord


def setup(bot):
    bot.add_listener(on_command_error)


async def on_command_error(ctx, error):
    if hasattr(ctx.command, 'on_error'):
        return

    cog = ctx.cog
    if cog:
        if cog._get_overridden_method(cog.cog_command_error) is not None:
            return

    ignored = commands.CommandNotFound
    error = getattr(error, 'original', error)

    if isinstance(error, ignored):
        return

    if isinstance(error, commands.DisabledCommand):
        await ctx.send(f'{ctx.command} has been disabled.')

    elif isinstance(error, commands.NoPrivateMessage):
        try:
            await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
        except discord.HTTPException:
            pass

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} You are missing permission(s) to run this command.")
        return

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.author.mention} You are missing required arguments to run this command.")
        return

    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
