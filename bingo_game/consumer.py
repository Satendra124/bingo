from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class LiveGame(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['game_id']
        self.room_group_name = "room_%s" % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,self.channel_name
        )
        self.accept()
        #self.send(text_data="hello")
    def receive(self,text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type':'move',
                'number':text_data
            }
        )
    def move(self,event):
        data = event['number']
        self.send(text_data=data)
    def disconnect(self, code):
        return super().disconnect(code)