from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, null=True, blank=True)
    introduction  = models.TextField(null=True, blank=True)
    image_raw = models.ImageField(null=True, blank=True)
    image_file = ImageSpecField(source='image_raw', processors = [ResizeToFill(300,300)], format='jpeg', options={'quality': 90})
    
    
class User(AbstractUser):
    username = models.CharField(max_length=10, primary_key=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name="followers")
