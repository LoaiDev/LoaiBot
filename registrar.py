from glob import glob
from helpers import root_path
import os


class Registrar:
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def get_module_name(path, package):
        name = (os.path.splitext(os.path.basename(path)))[0]
        return f"{package}.{name}"

    @staticmethod
    def find_commands():
        commands_directory = root_path("commands/")
        return glob(commands_directory + "*.py")

    @staticmethod
    def find_listeners():
        listeners_directory = root_path("listeners/")
        return glob(listeners_directory + "*.py")

    def register_commands(self):
        commands = self.find_commands()
        for command in commands:
            self.bot.load_extension(self.get_module_name(command, "commands"))
        return self

    def register_listeners(self):
        listeners = self.find_listeners()
        for listener in listeners:
            self.bot.load_extension(self.get_module_name(listener, "listeners"))
        return self
