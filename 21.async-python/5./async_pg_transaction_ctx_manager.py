from asyncpg import connection

async def main():
    async with connection.transaction():
        await connection.execute("INSERT INTO mytable VALUES (1, 2, 3)")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
