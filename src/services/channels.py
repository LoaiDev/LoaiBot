from src.helpers import read_json, write_json, storage, config
from typing import Union


def get_file():
    return storage(config("channels.file_name"))


file = get_file()


def check_file():
    try:
        read_json(file)
    except FileNotFoundError:
        write_json(file, {})


def get_channels():
    check_file()
    return read_json(file)


def set_channels(channels):
    check_file()
    write_json(file, channels)


def set_channel(guild_id: Union[int, str], name, channel):
    guild_id = str(guild_id)
    channels = get_channels()
    if guild_id not in channels:
        channels[guild_id] = {}
    channels[guild_id][name] = channel
    set_channels(channels)


def get_channel(guild_id: Union[int, str], name):
    guild_id = str(guild_id)
    channels = get_channels()
    if guild_id not in channels:
        return False
    if name not in channels[guild_id]:
        return False
    return channels[guild_id][name]


def remove_channel(guild_id: Union[int, str], name):
    guild_id = str(guild_id)
    channels = get_channels()
    if guild_id not in channels:
        return False
    if name not in channels[guild_id]:
        return False
    channels[guild_id].pop(name)
    return True
