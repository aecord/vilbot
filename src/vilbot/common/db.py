import os

import asyncpg


async def connect():
    DB = os.getenv("POSTGRES_DB")
    USER = os.getenv("POSTGRES_USER")
    PASSWORD = os.getenv("POSTGRES_PASSWORD")
    HOST = os.getenv("POSTGRES_HOST", "db")

    if not DB:
        raise EnvironmentError("Missing POSTGRES_DB")
    if not USER:
        raise EnvironmentError("Missing POSTGRES_USER")
    if not PASSWORD:
        raise EnvironmentError("Missing POSTGRES_PASSWORD")

    return await asyncpg.connect(user=USER, password=PASSWORD, database=DB, host=HOST)
