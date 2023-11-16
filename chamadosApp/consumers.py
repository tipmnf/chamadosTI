#This file is using channels daphne to consume the WebSocket
import json

from channels.generic.websocket import AsyncWebsocketConsumer

class OSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self, close_code):
        pass
    
    #Receive the message from the WebSocket
    async def receive(self):
        pass

    #Receive message from the group
    async def chat_message(self, ):
        #Send message to WebSocket
        await self.send(text_data = json.dumps({'message':True}))
