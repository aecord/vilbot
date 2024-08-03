from __future__ import annotations

import random

import asyncpg

from vilbot.common.releases import ReleaseType


async def generate_hottake(
    conn: asyncpg.Connection[asyncpg.Record], *, exclude: list[ReleaseType]
) -> tuple[str, str]:
    query = """
    SELECT t.id, t.title
    FROM Track t
    JOIN ReleaseTrack rt ON t.id = rt.track_id
    JOIN Release r ON rt.release_id = r.id
    """

    exclude_values = [rt.value for rt in exclude]

    if exclude:
        placeholders = ", ".join(f"${i+1}" for i in range(len(exclude_values)))
        query += f"WHERE r.release_type NOT IN ({placeholders})"

    tracks = await conn.fetch(query, *exclude_values)

    if len(tracks) < 2:
        raise ValueError("Not enough tracks available to generate a hottake")

    track_a = random.choice(tracks)
    tracks.remove(track_a)
    track_b = random.choice(tracks)

    return (track_a["title"], track_b["title"])


async def generate_top_ten_tracks(
    conn: asyncpg.Connection[asyncpg.Record],
) -> list[str]:
    tracks = await conn.fetch("SELECT id, title FROM Track")

    top_ten: list[str] = []

    for _ in range(10):
        track: asyncpg.Record = random.choice(tracks)
        tracks.remove(track)
        track_title: str = track["title"]
        top_ten.append(track_title)

    return top_ten
