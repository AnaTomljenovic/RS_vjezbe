from aiohttp import web

async def handle_kolicnik(request):
    try:
        data = await request.json()
        zbroj = data.get("zbroj")
        umnozak = data.get("umnozak")

        if zbroj is None or umnozak is None:
            return web.json_response({"error": "Zbroj ili umnozak nije proslijeđen"}, status=400)
        if zbroj == 0:
            return web.json_response({"error": "Dijeljenje s nulom nije dozvoljeno"}, status=400)
        
        rezultat = umnozak / zbroj
        return web.json_response({"kolicnik": rezultat})
    except Exception:
        return web.json_response({"error": "Neispravan zahtjev"}, status=400)

app = web.Application()
app.router.add_post('/kolicnik', handle_kolicnik)

if __name__ == "__main__":
    web.run_app(app, port=8085)
