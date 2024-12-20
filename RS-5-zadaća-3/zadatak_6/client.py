import asyncio
import aiohttp

async def fetch_pozdrav(url, port):
    async with aiohttp.ClientSession() as session:
        full_url = f"http://{url}:{port}/pozdrav"
        async with session.get(full_url) as response:
            return await response.json()

async def sekvencijalno():
    print("Pokrećem sekvencijalno slanje zahtjeva...")
    response1 = await fetch_pozdrav('localhost', 8081)
    print(f"Odgovor sa servisa 8081: {response1}")
    response2 = await fetch_pozdrav('localhost', 8082)
    print(f"Odgovor sa servisa 8082: {response2}")

async def konkurentno():
    print("Pokrećem konkurentno slanje zahtjeva...")
    task1 = asyncio.create_task(fetch_pozdrav('localhost', 8081))
    task2 = asyncio.create_task(fetch_pozdrav('localhost', 8082))
    response1, response2 = await asyncio.gather(task1, task2)
    print(f"Odgovor sa servisa 8081: {response1}")
    print(f"Odgovor sa servisa 8082: {response2}")

async def main():
    await sekvencijalno()
    print()
    await konkurentno()

if __name__ == "__main__":
    asyncio.run(main())
