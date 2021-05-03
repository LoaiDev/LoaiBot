from services.prefix import remove_prefix


def setup(bot):
    bot.add_listener(on_guild_remove)


async def on_guild_remove(guild):
    remove_prefix(guild.id)
