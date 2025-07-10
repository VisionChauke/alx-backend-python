import aiosqlite
import asyncio

DB_NAME = "users.db"

# Fetch all users
async def async_fetch_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            rows = await cursor.fetchall()
            print("[ALL USERS]")
            for row in rows:
                print(row)

# Fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            rows = await cursor.fetchall()
            print("\n[USERS OLDER THAN 40]")
            for row in rows:
                print(row)

# Run both queries concurrently
async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

# Execute
asyncio.run(fetch_concurrently())
# This script uses aiosqlite to fetch user data from a SQLite database concurrently.
# It defines two asynchronous functions to fetch all users and users older than 40,