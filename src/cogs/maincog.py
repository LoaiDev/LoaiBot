from discord.ext import commands


class MainCog(commands.Cog, name="Main"):

    def __init__(self, bot):
        self.bot = bot
