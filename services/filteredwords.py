from helpers import read_json, write_json, storage, config
from typing import Union, Optional
from services.channels import get_channel as channels_get
from services.channels import set_channel as channels_set

from services.roles import get_role as roles_get
from services.roles import set_role as roles_set


def get_file():
    return storage(config("filteredwords.file_name"))


file = get_file()


def check_file():
    try:
        read_json(file)
    except FileNotFoundError:
        write_json(file, {})


def get_filteredwords():
    check_file()
    return read_json(file)


def set_filteredwords(filteredwords):
    check_file()
    write_json(file, filteredwords)


def add_filteredwords(filteredwords):
    affected_words = list()
    new_filteredwords = get_filteredwords()
    for filteredword in filteredwords:
        if filteredword not in new_filteredwords:
            new_filteredwords.append(filteredword)
            affected_words.append(filteredword)
    set_filteredwords(new_filteredwords)
    return affected_words


def remove_filteredwords(filteredwords):
    affected_words = list()
    new_filteredwords = get_filteredwords()
    for filteredword in filteredwords:
        if filteredword in new_filteredwords:
            new_filteredwords.remove(filteredword)
            affected_words.append(filteredword)
    set_filteredwords(new_filteredwords)
    return affected_words


def get_channel(guild_id: Union[int, str]):
    return channels_get(guild_id, config("filteredwords.channel_storage_name"))


def set_channel(guild_id: Union[int, str], channel_id):
    return channels_set(guild_id, config("filteredwords.channel_storage_name"), int(channel_id))


def get_ping_role(guild_id: Union[int, str]):
    return roles_get(guild_id, config("filteredwords.ping_role_storage_name"))


def set_ping_role(guild_id: Union[int, str], role_id):
    return roles_set(guild_id, config("filteredwords.ping_role_storage_name"), int(role_id))


def get_ignored_roles(guild_id: Union[int, str]):
    return roles_get(guild_id, config("filteredwords.ignored_roles_storage_name"))


def set_ignored_roles(guild_id: Union[int, str], roles):
    return roles_set(guild_id, config("filteredwords.ignored_roles_storage_name"), list(map(lambda role: role.id, roles)))
