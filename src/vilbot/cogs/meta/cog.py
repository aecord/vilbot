from discord import ApplicationContext
from discord.bot import Bot
from discord.commands.permissions import default_permissions  # type: ignore[reportUnknownVariableType]
from discord.ext import commands
from discord.cog import Cog


class Meta(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.slash_command(name="refresh_tracks")  # type: ignore[reportUnknownMemberType]
    @default_permissions(administrator=True)  # type: ignore[reportUntypedFunctionDecorator]
    async def refresh_tracks(self, ctx: ApplicationContext):
        # TODO: Refresh the tracks from the autechre tracks json
        _ = await ctx.respond("Refreshed tracks")
