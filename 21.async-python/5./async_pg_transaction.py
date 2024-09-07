from asyncpg import connection

async def main():

    tr = connection.transaction()
    await tr.start()
    try:
        await connection.execute("INSERT INTO mytable VALUES (1, 2, 3)")
    except:
        await tr.rollback()
        raise
    else:
        await tr.commit()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
