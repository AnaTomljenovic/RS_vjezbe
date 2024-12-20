import aiohttp
import asyncio

async def send_request(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            return await response.json()

async def main():
    brojevi = {"brojevi": [4, 7, 11, 21]}

    print("Konkurentno šaljem zahtjeve za zbroj i umnožak...")
    task1 = asyncio.create_task(send_request("http://localhost:8083/zbroj", brojevi))
    task2 = asyncio.create_task(send_request("http://localhost:8084/umnozak", brojevi))

    zbroj_response, umnozak_response = await asyncio.gather(task1, task2)

    print("Odgovor servisa 8083 (Zbroj):", zbroj_response)
    print("Odgovor servisa 8084 (Umnožak):", umnozak_response)

    if "zbroj" in zbroj_response and "umnozak" in umnozak_response:
        kolicnik_data = {"zbroj": zbroj_response["zbroj"], "umnozak": umnozak_response["umnozak"]}
        print("\nSekvencijalno šaljem zahtjev za količnik...")
        kolicnik_response = await send_request("http://localhost:8085/kolicnik", kolicnik_data)
        print("Odgovor servisa 8085 (Količnik):", kolicnik_response)
    else:
        print("Greška: Neuspjeli odgovori s prvog ili drugog servisa.")

if __name__ == "__main__":
    asyncio.run(main())
