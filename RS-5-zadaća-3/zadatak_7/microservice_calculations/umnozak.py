from aiohttp import web
import math

async def handle_umnozak(request):
    try:
        data = await request.json()
        brojevi = data.get("brojevi")
        if not brojevi or not isinstance(brojevi, list):
            return web.json_response({"error": "Lista brojeva nije proslijeđena"}, status=400)
        rezultat = math.prod(brojevi)
        return web.json_response({"umnozak": rezultat})
    except Exception:
        return web.json_response({"error": "Neispravan zahtjev"}, status=400)

app = web.Application()
app.router.add_post('/umnozak', handle_umnozak)

if __name__ == "__main__":
    web.run_app(app, port=8084)
