from django.db import models
from django.conf import settings

class Room(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rooms', through="RoomJoin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RoomJoin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    last_read_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    content = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    
    created_at = models.DateTimeField(auto_now_add=True)

