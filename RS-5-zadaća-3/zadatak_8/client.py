import aiohttp
import asyncio

URL_1 = "http://localhost:8086/cats"
URL_2 = "http://localhost:8087/facts"

async def fetch_cat_facts(amount):
    url = f"{URL_1}?amount={amount}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("facts", [])
            else:
                print(f"Greška pri dohvaćanju činjenica: {response.status}")
                return []

async def filter_cat_facts(facts):
    async with aiohttp.ClientSession() as session:
        async with session.post(URL_2, json={"facts": facts}) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("filtered_facts", [])
            else:
                print(f"Greška pri filtriranju činjenica: {response.status}")
                return []

async def main():
    amount = 50
    print(f"Dohvaćam {amount} činjenica o mačkama...")

    facts = await fetch_cat_facts(amount)
    print("Činjenice o mačkama:")
    for i, fact in enumerate(facts, 1):
        print(f"{i}. {fact}")

    print("\nFiltriram činjenice koje sadrže 'cat' ili 'cats'...")
    filtered_facts = await filter_cat_facts(facts)

    print("\nFiltrirane činjenice:")
    for i, fact in enumerate(filtered_facts, 1):
        print(f"{i}. {fact}")

if __name__ == "__main__":
    asyncio.run(main())
