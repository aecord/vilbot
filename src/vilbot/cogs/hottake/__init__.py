from discord.bot import Bot

from .cog import Hottake


def setup(bot: Bot):
    bot.add_cog(Hottake(bot))
