from discord.ext import commands
from services.prefix import get_current_prefix
from helpers import config
from registrar import Registrar

bot = commands.Bot(command_prefix=get_current_prefix, case_insensitive=True)


Registrar(bot).register_commands().register_listeners()


bot.run(config("bot.token"))
