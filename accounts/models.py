from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from PIL import Image
from io import BytesIO
from django.core.files import File
from pilkit.processors import Thumbnail
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
    pass