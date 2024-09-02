import aiohttp
import asyncpg
import asyncio

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/starwars"

async def fetch_character(session, url):
    async with session.get(url) as response:
        return await response.json()

async def fetch_all_characters():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://swapi.dev/api/people/") as response:
            data = await response.json()
            tasks = [fetch_character(session, char['url']) for char in data['results']]
            return await asyncio.gather(*tasks)

async def insert_character(conn, character):
    await conn.execute('''
        INSERT INTO characters (birth_year, eye_color, films, gender, hair_color, height, homeworld, mass, name, skin_color, species, starships, vehicles)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13)
    ''', character['birth_year'], character['eye_color'], ', '.join(character['films']), character['gender'], character['hair_color'], int(character['height']), character['homeworld'], int(character['mass']), character['name'], character['skin_color'], ', '.join(character['species']), ', '.join(character['starships']), ', '.join(character['vehicles']))

async def main():
    characters = await fetch_all_characters()
    conn = await asyncpg.connect(DATABASE_URL)
    for character in characters:
        await insert_character(conn, character)
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())
