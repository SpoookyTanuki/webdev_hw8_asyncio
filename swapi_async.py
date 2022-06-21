import asyncio
import aiohttp
import time
from more_itertools import chunked

URL = 'https://swapi.dev/api/people/'

MAX = 60
PARTITION = 10


async def get_person(person_id, session):
    async with session.get(f'{URL}{person_id}') as response:
        return await response.json()


async def get_people(all_ids, partition, session):
    for chunk_ids in chunked(all_ids, partition):
        tasks = []
        for person_id in chunk_ids:
            get_person_task = asyncio.create_task(get_person(person_id, session))
            tasks.append(get_person_task)
        for task in tasks:
            task_result = await task
            yield task_result


async def main():
    all_ids = range(1, MAX + 1)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        for chunk_ids in chunked(all_ids, PARTITION):
            coros = [get_person(person_id, session) for person_id in chunk_ids]
            people = await asyncio.gather(*coros)
            for character in people:
            #     character_id = character['id']
                name = character['name']

                birth_year = character['birth_year']
                eye_color = character['eye_color']
                films = character['films']
                gender = character['gender']
                hair_color = character['hair_color']
                height = character['height']
                homeworld = character['homeworld']
                mass = character['mass']
                skin_color =character['skin_color']
                species = character['species']
                starships = character['starships']
                vehicles = character['vehicles']

                print(name, birth_year, eye_color, films, gender,
                      hair_color, height, homeworld, mass,
                      skin_color, species, starships, vehicles)


start = time.time()
asyncio.run(main())
print(time.time() - start)
