import aiohttp
import asyncio

async def fetch_proizvodi(session):
    async with session.get("http://localhost:8081/proizvodi") as response:
        print("Svi proizvodi:", await response.json())

async def fetch_proizvod_po_id(session, proizvod_id):
    async with session.get(f"http://localhost:8081/proizvodi/{proizvod_id}") as response:
        if response.status == 404:
            print(f"Proizvod s ID-om {proizvod_id} ne postoji:", await response.json())
        else:
            print(f"Proizvod s ID-om {proizvod_id}:", await response.json())

async def main():
    async with aiohttp.ClientSession() as session:
        await fetch_proizvodi(session)
        await fetch_proizvod_po_id(session, 2)
        await fetch_proizvod_po_id(session, 10)

asyncio.run(main())
