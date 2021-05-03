from tasks.change_status import change_status

def setup(bot):
    bot.add_listener(setup_listener(bot))


def setup_listener(bot):
    async def on_ready():
        print("Bot running with:")
        print("Username: ", bot.user.name)
        print("User ID: ", bot.user.id)
        change_status.start(bot)
    return on_ready
