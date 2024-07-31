from discord import ApplicationContext
from discord.ext import commands
from discord.ext.commands import Cog


class ExampleCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="example")
    async def example_slash(self, ctx: ApplicationContext):
        await ctx.respond("Slash commands are working")

