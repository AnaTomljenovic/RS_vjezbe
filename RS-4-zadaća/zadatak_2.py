import asyncio
import aiohttp

async def get_cat_fact():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://catfact.ninja/fact") as response:
            return (await response.json())["fact"]

async def filter_cat_facts(facts):
    return [fact for fact in facts if "cat" in fact.lower() or "cats" in fact.lower()]

async def main():
    tasks = [get_cat_fact() for _ in range(20)]
    facts = await asyncio.gather(*tasks)
    
    filtered_facts = await filter_cat_facts(facts)
    
    print("Filtrirane činjenice o mačkama:")
    for fact in filtered_facts:
        print("-", fact)

asyncio.run(main())
