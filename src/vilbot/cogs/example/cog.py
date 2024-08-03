import discord
from discord import ApplicationContext
from discord.bot import Bot
from discord.cog import Cog


class ExampleCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @discord.slash_command(name="example")  # type: ignore[reportUnknownMemberType]
    async def example_slash(self, ctx: ApplicationContext):
        _ = await ctx.respond("Slash commands are working")
