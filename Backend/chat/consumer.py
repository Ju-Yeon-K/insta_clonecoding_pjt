import json

from datetime import datetime

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async

from .models import RoomJoin, Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.username = self.scope["url_route"]["kwargs"]["username"]
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    # last read 저장
    def disconnect(self, close_code):
        # Leave room group
        self.update_last_read_at()
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # DB에 저장
        self.save_message(message)
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
    
    def save_message(self, data):
        return Message.objects.create(
            content=data,
            user_id=self.username,
            room_id=self.room_name,
        )
    
    def update_last_read_at(self):
        room_info = RoomJoin.objects.filter(room=self.room_name, user=self.username).last()
        room_info.last_read_at = datetime.now()
        room_info.save()

    