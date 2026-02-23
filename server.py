from aiohttp import web
import os

CURRENT_VERSION = "0.1"

async def check_version(request):
    # Получаем параметр 'v' из URL: /check_version?v=0.1
    user_version = request.query.get('v')
    
    if not user_version:
        return web.Response(text="error: missing version", status=400)
        
    if user_version == CURRENT_VERSION:
        return web.Response(text="ok")
    else:
        return web.Response(text="update")

# Создаем приложение
app = web.Application()
app.add_routes([web.get('/check_version', check_version)])

if __name__ == "__main__":
    # Для локального запуска на Arch
    port = int(os.environ.get("PORT", 8080))
    web.run_app(app, host='0.0.0.0', port=port)
