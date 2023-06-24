from rest_framework import serializers
from .models import Room, RoomJoin, Message
from accounts.models import User

# 채팅방 안읽은 메시지 순으로 정렬하게 해야함. 
class RoomSerializer(serializers.ModelSerializer):
    # room_order_by_last_send_message = serializers.SerializerMethodField()
    
    # def get_room_order_by_last_send_message(self, obj):
    #     rooms = RoomJoin.objects.filter(user_id=obj.username).values(
    #         'room_id', 'last_read_at'
    #     ).order_by('last_read_at')
    #     return rooms
    
    class Meta:
        model = RoomJoin
        fields = ('room_id','last_read_at',)


