from discord.ext import commands
from services.prefix import get_current_prefix
from helpers import config
from registrar import Registrar

from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix=get_current_prefix, case_insensitive=True)
bot.remove_command("help")

Registrar(bot).register_commands().register_listeners()

bot.run(config("bot.token"))
