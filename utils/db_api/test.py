import asyncio

from utils.db_api.postresql import Database

db = Database()


async def test():
    await db.create()
    await db.create_table_users()
    await db.add_user('Polnoe Name', 'Username', 156548651)
    await db.drop_table_users()

asyncio.run(test())

