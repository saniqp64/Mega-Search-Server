from aiohttp import web

async def check_version(request):
    v = request.query.get('v')
    return web.Response(text="ok" if v == "0.1" else "update")

# Создаем объект приложения
app = web.Application()
app.add_routes([web.get('/check_version', check_version)])
# Все. Больше никакого кода внизу для Render не нужно.
