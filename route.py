from aiohttp import web

async def root_handler(request):
    return web.json_response("Online")

async def run_web_server():
    app = web.Application()
    app.add_routes([web.get("/", root_handler)])
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", 3000).start()
