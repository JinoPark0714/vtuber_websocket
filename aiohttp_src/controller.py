from aiohttp import web

# 프레젠테이션 계층
async def aiohttp_handler(request):
    websocket_response = web.WebSocketResponse()
    await websocket_response.prepare(request)
    await request.app['vtube_handler'].connect(websocket_response)

    async for msg in websocket_response:
        if msg.type == web.WSMsgType.TEXT:
            await request.app['vtube_handler'].handle_message(websocket_response, msg.data)
        elif msg.type == web.WSMsgType.ERROR:
            print(f'ws connection closed with exception {websocket_response.exception()}')
        else:
            print("에러가 발생했습니다.")

    request.app['vtube_handler'].disconnect(websocket_response)
    print('websocket connection closed')

    return websocket_response