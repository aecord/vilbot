import logging

from discord import ApplicationContext, commands
from discord.bot import Bot
from discord.cog import Cog

from vilbot.cogs.hottake.common import generate_hottake, generate_top_ten_tracks
from vilbot.common.db import connect
from vilbot.common.releases import ReleaseType

LOG = logging.getLogger(__name__)


class Hottake(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.slash_command(name="hottake")  # pyright: ignore[reportUnknownMemberType]
    async def hottake(self, ctx: ApplicationContext):
        conn = await connect()

        track_a, track_b = await generate_hottake(conn, exclude=[ReleaseType.LIVE])

        _ = await ctx.respond(f"{track_a} > {track_b}")

    @commands.slash_command(name="topten")  # pyright: ignore[reportUnknownMemberType]
    async def top_ten(self, ctx: ApplicationContext):
        conn = await connect()

        top_ten = await generate_top_ten_tracks(conn)

        formatted_text = "Top 10 Autechre Tracks:\n"
        for i, track in enumerate(top_ten, start=1):
            formatted_text += f"{i}: {track}\n"

        _ = await ctx.respond(formatted_text)
