from discord import ApplicationContext
from discord.bot import Bot
from discord.cog import Cog
from discord.commands.permissions import (
    default_permissions,  # pyright: ignore[reportUnknownVariableType]
)
from discord.ext import commands

from vilbot.cogs.meta.database_functions import update_releases
from vilbot.common.db import connect


class Meta(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.slash_command(  # pyright: ignore[reportUnknownMemberType]
        name="refresh_releases"
    )
    @default_permissions(  # pyright: ignore[reportUntypedFunctionDecorator]
        administrator=True
    )
    async def refresh_releases(self, ctx: ApplicationContext):
        conn = await connect()

        await update_releases(conn)

        _ = await ctx.respond("Refreshed tracks")
