from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.files.uploadedfile import *

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, null=True, blank=True)
    introduction  = models.TextField(null=True, blank=True)
    image_file = models.ImageField( height_field=300, width_field=300, null=True, blank=True) 

class User(AbstractUser):
    pass