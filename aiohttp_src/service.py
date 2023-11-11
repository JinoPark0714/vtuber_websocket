# 비즈니스 로직 계층
import json
import aiohttp
from websocket_src.vtuber_service import VtuberService
import websockets
# 토큰 생성
token_create_request = {
    "apiName": "VTubeStudioPublicAPI",
    "apiVersion": "1.0",
    "requestID": "Authentication_MAO_01",
    "messageType": "AuthenticationTokenRequest",
    "data": {
            "pluginName": "MAO_Plugin",
            "pluginDeveloper": "Mind_of_MAO",
            "pluginIcon": ""
    }
}
class VTubeStudioHandler:
    def __init__(self):
        self.clients = set()
        self.vtuber_service = VtuberService()
        self.token = ''

    async def fff(self):
        t = await self.call_vtube_api(json.dumps(token_create_request))

    async def connect(self, websocket):
        self.clients.add(websocket)
        print(self.clients)

    def disconnect(self, websocket):
        self.clients.remove(websocket)

    async def handle_message(self, websocket, message):
        # print(f"하하하 : {message}")
        t = await self.call_vtube_api(json.dumps(message))

        return t
    
    async def call_vtube_api(self, message):
        print(message)

        # VTube Studio API의 실제 엔드포인트 URL로 대체해야 합니다.
        vtube_api_url = "ws://localhost:8001"
        async with websockets.connect(vtube_api_url) as websocket:
            await websocket.send(message)
            response = await websocket.recv()
            print(f"response : {response}")
            return response