from rest_framework import serializers
from .models import Room, RoomJoin, Message
from accounts.models import User

# 채팅방 안읽은 메시지 순으로 정렬하게 해야함. 
class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RoomJoin
        fields = ('room_id','last_read_at',)


