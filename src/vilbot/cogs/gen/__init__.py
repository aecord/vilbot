from discord.bot import Bot

from .cog import Gen


def setup(bot: Bot):
    bot.add_cog(Gen(bot))
