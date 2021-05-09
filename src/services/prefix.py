from src.helpers import storage, config, write_json, read_json
from typing import Optional, Union
from discord.ext import commands


def get_file():
    return storage(config("prefix.file_name"))


file = get_file()


def check_file():
    try:
        read_json(file)
    except FileNotFoundError:
        write_json(file, {})


def get_prefixes():
    check_file()
    return read_json(file)


def set_prefixes(prefixes):
    check_file()
    write_json(file, prefixes)


def get_prefix(guild_id):
    default_prefix = config("prefix.default")
    prefixes = get_prefixes()
    if str(guild_id) not in prefixes:
        set_prefix(guild_id, default_prefix)
        return default_prefix
    return prefixes[str(guild_id)]


def set_prefix(guild_id: Union[str, int], prefix: Optional[str] = None):
    prefixes = get_prefixes()
    prefixes[str(guild_id)] = prefix if prefix else config("prefix.default")
    set_prefixes(prefixes)


def remove_prefix(guild_id: Union[str, int]):
    prefixes = get_prefixes()
    prefixes.pop(str(guild_id))
    set_prefixes(prefixes)


async def get_current_prefix(bot, message):
    server_prefix = get_prefix(message.guild.id)
    return commands.when_mentioned_or(server_prefix)(bot, message)
