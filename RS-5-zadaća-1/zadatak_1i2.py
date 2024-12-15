from aiohttp import web

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "količina": 10},
    {"naziv": "Miš", "cijena": 100, "količina": 50},
    {"naziv": "Tipkovnica", "cijena": 200, "količina": 20},
]

# GET
async def get_proizvodi(request):
    return web.json_response(proizvodi)

# POST
async def post_proizvodi(request):
    novi_proizvod = await request.json()
    proizvodi.append(novi_proizvod)
    print("Novi proizvod dodan:", novi_proizvod)
    return web.json_response({"message": "Proizvod uspješno dodan", "proizvodi": proizvodi})

app = web.Application()
app.router.add_routes([
    web.get('/proizvodi', get_proizvodi),
    web.post('/proizvodi', post_proizvodi),
])

web.run_app(app, port=8081)
