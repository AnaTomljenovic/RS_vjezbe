from aiohttp import web

def filter_facts(facts):
    return [fact for fact in facts if "cat" in fact.lower()]

async def check_facts(request):
    try:
        data = await request.json()
        facts = data.get("facts")

        if not isinstance(facts, list):
            return web.json_response({"error": "Neispravan unos. 'facts' mora biti lista."}, status=400)

        filtered_facts = filter_facts(facts)
        return web.json_response({"filtered_facts": filtered_facts})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)

app = web.Application()
app.router.add_post('/facts', check_facts)

if __name__ == "__main__":
    web.run_app(app, port=8087)
