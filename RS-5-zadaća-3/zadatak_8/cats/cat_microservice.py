from aiohttp import web
import aiohttp
import asyncio

URL = "https://catfact.ninja/fact"

async def fetch_single_fact(session):
    async with session.get(URL) as response:
        data = await response.json()
        return data.get("fact")

async def fetch_multiple_facts(amount):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_single_fact(session) for _ in range(amount)]
        return await asyncio.gather(*tasks)

async def get_facts(request):
    try:
        amount = int(request.query.get("amount", 1))
        if amount <= 0:
            return web.json_response({"error": "Parametar 'amount' mora biti pozitivan cijeli broj."}, status=400)

        facts = await fetch_multiple_facts(amount)
        return web.json_response({"facts": facts})
    except ValueError:
        return web.json_response({"error": "Neispravan parametar. Mora biti cijeli broj."}, status=400)
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)

app = web.Application()
app.router.add_get('/cats', get_facts)

if __name__ == "__main__":
    web.run_app(app, port=8086)
