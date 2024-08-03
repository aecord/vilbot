import logging
import os
from dotenv import load_dotenv
from discord import ApplicationContext
from discord.ext import bridge, commands

from vilbot.log_config import configure_logger

_ = load_dotenv()

LOG = logging.getLogger("vilbot")

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise EnvironmentError("No Discord token found in the environment")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_LEVEL_INT: int = getattr(logging, LOG_LEVEL.upper())


bot = bridge.Bot(
    command_prefix=commands.when_mentioned_or("/"),
)


@bot.event
async def on_application_command_error(ctx: ApplicationContext, error: BaseException):
    _ = await ctx.respond(f"Something went wrong:\n{error}", ephemeral=True)
    raise error  # NOTE: Full stacktrace


def load_extensions():
    cogs_path = os.path.dirname(__file__) + "/cogs/"
    for cogname in sorted(os.listdir(cogs_path), key=len):
        path = cogs_path + cogname
        if os.path.isdir(path):
            if "__init__.py" in os.listdir(path):
                LOG.info(f"Loading cog {cogname}")
                _ = bot.load_extension(f"vilbot.cogs.{cogname}")


if __name__ == "__main__":
    configure_logger("vilbot", log_level=LOG_LEVEL_INT)
    configure_logger("discord", log_level=logging.WARNING)
    load_extensions()
    bot.run(TOKEN, reconnect=True)
