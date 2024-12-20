from aiohttp import web

async def handle_zbroj(request):
    try:
        data = await request.json()
        brojevi = data.get("brojevi")
        if not brojevi or not isinstance(brojevi, list):
            return web.json_response({"error": "Lista brojeva nije proslijeđena"}, status=400)
        rezultat = sum(brojevi)
        return web.json_response({"zbroj": rezultat})
    except Exception:
        return web.json_response({"error": "Neispravan zahtjev"}, status=400)

app = web.Application()
app.router.add_post('/zbroj', handle_zbroj)

if __name__ == "__main__":
    web.run_app(app, port=8083)
