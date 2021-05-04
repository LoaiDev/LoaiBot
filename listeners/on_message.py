from tasks.change_status import change_status

#
# def check_for_filteredwords(message):
#
#
#


def setup(bot):
    bot.add_listener(setup_listener(bot))


def setup_listener(bot):
    async def on_message(message):
        if message.author == bot.user:
            return


    return on_message
