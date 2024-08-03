from discord.bot import Bot
from .cog import Meta


def setup(bot: Bot):
    bot.add_cog(Meta(bot))
