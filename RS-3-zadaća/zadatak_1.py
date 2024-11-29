import asyncio

async def dohvati():
    print("Dohvaćam podatke...")
    podaci = [x for x in range(1, 11)]
    await asyncio.sleep(3)
    print("Podaci dohvaćeni.")
    return podaci

async def main():
    podaci = await dohvati()
    print(f"Podaci: {podaci}")

asyncio.run(main())
