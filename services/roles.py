from helpers import read_json, write_json, storage, config
from typing import Union, Optional


def get_file():
    return storage(config("roles.file_name"))


file = get_file()


def check_file():
    try:
        read_json(file)
    except FileNotFoundError:
        write_json(file, {})


def get_roles():
    check_file()
    return read_json(file)


def set_roles(roles):
    check_file()
    write_json(file, roles)


def set_role(guild_id: Union[int, str], name, role):
    guild_id = str(guild_id)
    roles = get_roles()
    if guild_id not in roles:
        roles[guild_id] = {}
    roles[guild_id][name] = role
    set_roles(roles)


def get_role(guild_id: Union[int, str], name):
    guild_id = str(guild_id)
    roles = get_roles()
    if guild_id not in roles:
        return False
    if name not in roles[guild_id]:
        return False
    return roles[guild_id][name]


def remove_role(guild_id: Union[int, str], name):
    guild_id = str(guild_id)
    roles = get_roles()
    if guild_id not in roles:
        return False
    if name not in roles[guild_id]:
        return False
    roles[guild_id].pop(name)
    return True
