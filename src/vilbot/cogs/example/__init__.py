from discord.bot import Bot
from .cog import ExampleCog


def setup(bot: Bot):
    bot.add_cog(ExampleCog(bot))
