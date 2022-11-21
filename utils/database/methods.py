import aiosqlite

from utils import Settings


async def create_tables() -> None:
    async with aiosqlite.connect(Settings.database_path) as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER
        )""")
        await db.commit()


async def select_user(user_id: int):
    async with aiosqlite.connect(Settings.database_path) as db:
        user = await db.execute("SELECT * FROM users WHERE user_id = (?)",
                                (user_id, ))
        return await user.fetchone()


async def register_user(user_id: int) -> None:
    async with aiosqlite.connect(Settings.database_path) as db:
        await db.execute("INSERT INTO users (`user_id`) VALUES (?)",
                         (user_id, ))
        await db.commit()
