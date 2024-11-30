import asyncio
import aiohttp

async def get_dog_fact():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dogapi.dog/api/v2/facts") as response:
            return (await response.json())["data"][0]["attributes"]["body"]

async def get_cat_fact():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://catfact.ninja/fact") as response:
            return (await response.json())["fact"]

async def mix_facts(dog_facts, cat_facts):
    return [
        dog_fact if len(dog_fact) > len(cat_fact) else cat_fact
        for dog_fact, cat_fact in zip(dog_facts, cat_facts)
    ]

async def main():
    dog_facts_tasks = [get_dog_fact() for _ in range(5)]
    cat_facts_tasks = [get_cat_fact() for _ in range(5)]
    
    dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)
    
    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]
    
    mixed_facts = await mix_facts(dog_facts, cat_facts)
    
    print("Mixane činjenice o psima i mačkama:")
    for fact in mixed_facts:
        print("-", fact)

asyncio.run(main())
