from .pensive import Pensive


def setup(bot):
    cog = Pensive(bot)
    bot.add_cog(cog)
