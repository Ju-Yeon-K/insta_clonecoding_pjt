from django.db import models
from django.conf import settings

class Room(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rooms', through="RoomJoin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RoomJoin(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    last_read_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    content = models.CharField(max_length=300)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    room_id = models.ForeignKey(Room, on_delete=models.PROTECT)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def last_30_messages(self, room_id):
        return Message.objects.filter(room_id=room_id).order_by('-created_at')[:30]
