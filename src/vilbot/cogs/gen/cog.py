import logging
import random

from discord import ApplicationContext, commands
from discord.bot import Bot
from discord.cog import Cog
import pyphen  # pyright: ignore[reportMissingTypeStubs]

from vilbot.common.releases import AE_RELEASES, ReleaseType

LOG = logging.getLogger(__name__)


class Gen(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.slash_command(  # pyright: ignore[reportUnknownMemberType]
        name="generate_track_name"
    )
    async def generate_track_name(self, ctx: ApplicationContext):
        # NOTE: BOOO THIS SUCKS
        track_set: list[str] = []
        for release in AE_RELEASES:
            if release["type"] == ReleaseType.LIVE:
                continue
            track_set.extend(release["tracks"])

        ppen = pyphen.Pyphen(lang="en")

        syllables: set[str] = set()
        for track in track_set:
            words = track.split(" ")
            for word in words:
                LOG.debug(f"word: {word}")
                inserted = ppen.inserted(  # pyright: ignore[reportUnknownMemberType]
                    word
                )
                LOG.debug(f"Inserted: {inserted}")
                syllables.update(inserted.split("-"))

        LOG.debug(f"syllables: {syllables}")

        length = random.randint(3, 7)

        new_name = ""
        for syl in random.sample(list(syllables), length):
            if bool(random.getrandbits(1)):
                new_name += f"{syl} "
            else:
                new_name += syl

        _ = await ctx.respond(new_name.lower())
