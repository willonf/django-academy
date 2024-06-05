from channels.generic.websocket import AsyncJsonWebsocketConsumer


class SaleConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print(f'CONECTADO: {self.scope}')

        await self.accept()
        await self.channel_layer.group_add('sale', self.channel_name)

    async def disconnect(self):
        print(f'DESCONECTADO!')
        await self.channel_layer.group_discard('sale', self.channel_name)

    async def receive_json(self, event, **kwargs):
        await self.send_json(content=event['content'])

    async def group_message(self, event):
        await self.send_json(content=event['content'])
