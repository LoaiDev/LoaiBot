from helpers import read_json, write_json, storage, config


def get_file():
    return storage(config("badwords.file_name"))


file = get_file()


def check_file():
    try:
        read_json(file)
    except FileNotFoundError:
        write_json(file, {})


def get_badwords():
    check_file()
    return read_json(file)


def set_badwords(badwords):
    check_file()
    write_json(file, badwords)


def add_badwords(badwords):
    new_badwords = get_badwords()
    for badword in badwords:
        if badword not in new_badwords:
            new_badwords.append(badword)
    set_badwords(new_badwords)
    return


def remove_badwords(badwords):
    new_badwords = get_badwords()
    for badword in badwords:
        if badword in new_badwords:
            new_badwords.remove(badword)
    set_badwords(new_badwords)
    return
