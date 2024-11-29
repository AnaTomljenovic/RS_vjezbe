import asyncio
import time

async def korisnici():
    print("Dohvaćam podatke o korisnicima...")
    korisnici = [
        {"user": 1, "ime": "Mirko", "prezime": "Mirković"},
        {"user": 2, "ime": "Ana", "prezime": "Anić"},
        {"user": 3, "ime": "Maja", "prezime": "Majić"},
        {"user": 4, "ime": "Zdeslav", "prezime": "Horvat"}
    ]
    await asyncio.sleep(3)
    print("Podaci o korisnicima dohvaćeni.")
    return korisnici

async def proizvodi():
    print("Dohvaćam podatke o proizvodima...")
    proizvodi = [
        {"šifra": 11, "naziv": "čokolada", "količina": 4},
        {"šifra": 12, "naziv": "keksi", "količina": 7},
        {"šifra": 13, "naziv": "bomboni", "količina": 11},
        {"šifra": 14, "naziv": "sladoled", "količina": 21}
    ]
    await asyncio.sleep(5)
    print("Podaci o proizvodima dohvaćeni.")
    return proizvodi

async def main():
    start = time.time()
    rezultat_1, rezultat_2 = await asyncio.gather(korisnici(), proizvodi())
    end = time.time()

    print(f"Vrijeme izvršavanja programa je {end - start:.2f} sekundi.")
    print(f"Podaci o korisnicima: {rezultat_1}")
    print(f"Podaci o proizvodima: {rezultat_2}")

asyncio.run(main())
