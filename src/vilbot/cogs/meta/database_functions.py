from __future__ import annotations

import asyncpg

from vilbot.common.releases import AE_RELEASES


async def update_releases(conn: asyncpg.Connection[asyncpg.Record]) -> None:
    INSERT_TRACK = """
    INSERT INTO Track (title)
    VALUES ($1)
    RETURNING id
    """

    INSERT_RELEASE = """
    INSERT INTO Release (title, release_date, release_type)
    VALUES ($1, $2, $3)
    RETURNING id
    """

    INSERT_RELEASE_TRACK = """
    INSERT INTO ReleaseTrack (release_id, track_id, track_index)
    VALUES ($1, $2, $3)
    """

    for release in AE_RELEASES:
        release_title = release["title"]
        release_type = release["type"]
        release_year = release["year"]
        release_tracks = release["tracks"]

        release_id: int = await conn.fetchval(
            INSERT_RELEASE, release_title, release_year, release_type.value
        )

        for index, track in enumerate(release_tracks, start=1):
            track_id: int = await conn.fetchval(INSERT_TRACK, track)

            _ = await conn.execute(INSERT_RELEASE_TRACK, release_id, track_id, index)
