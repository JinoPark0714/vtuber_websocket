from aiohttp import web
from aiohttp_src.controller import aiohttp_handler
from aiohttp_src.service import VTubeStudioHandler


# 메인 애플리케이션 설정
vtube_handler = VTubeStudioHandler()

async def start_vtube_service(app):
    await app['vtube_handler'].fff()

app = web.Application()
app['vtube_handler'] = vtube_handler
app.router.add_get('/', aiohttp_handler)
app.on_startup.append(start_vtube_service)
web.run_app(app, host='localhost', port=8000)


