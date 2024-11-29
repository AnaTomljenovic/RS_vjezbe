import asyncio
import hashlib

async def secure_data(osjetljivo):
    await asyncio.sleep(3)
    enkripcija = {
        "prezime": osjetljivo["prezime"],
        "broj_kartice": hash(osjetljivo["broj_kartice"]),
        "CVV": hash(osjetljivo["CVV"])
    }
    return enkripcija

async def main():
    lista = [
        {"prezime": "Majić", "broj_kartice": "1234567890123456", "CVV": "000"},
        {"prezime": "Horvat", "broj_kartice": "1231231231231231", "CVV": "123"},
        {"prezime": "Balić", "broj_kartice": "1111222233334444", "CVV": "555"}
    ]

    zadaci = [secure_data(zapis) for zapis in lista]
    enkriptirano = await asyncio.gather(*zadaci)

    for zapis in enkriptirano:
        print(zapis)

asyncio.run(main())
