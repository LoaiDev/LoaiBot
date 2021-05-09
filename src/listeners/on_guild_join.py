from src.services.prefix import set_prefix


def setup(bot):
    bot.add_listener(on_guild_join)


async def on_guild_join(guild):
    set_prefix(guild.id)
