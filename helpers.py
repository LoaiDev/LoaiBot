import json
import os
from typing import Optional
from config import config as configList


def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def config(name: Optional[str] = None):
    config = configList()
    if name:
        keywords = name.split('.')
        for keyword in keywords:
            config = config[keyword]
    return config


def root_path(directory: Optional[str] = None):
    path = os.path.dirname(os.path.realpath(__file__))
    if directory:
        path = os.path.join(path, directory)
    return path


def storage(directory: Optional[str] = None):
    path = os.path.join(root_path(), config("storage.folder_name"))
    if directory:
        path = os.path.join(path, directory)
    return path
