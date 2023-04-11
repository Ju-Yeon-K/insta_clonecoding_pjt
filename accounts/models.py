from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from PIL import Image
from io import BytesIO
from django.core.files import File

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, null=True, blank=True)
    introduction  = models.TextField(null=True, blank=True)
    image_file = models.ImageField(height_field=300, width_field=300, null=True, blank=True) 

    def save(self):
        raw = self.compressImage(self.image_file)
        if raw:
            self.image_file = raw
        super(Profile, self).save()

    def compressImage(self,image):
        if not image:
            return None
        
        img = Image.open(image).convert("RGB")
        im_io = BytesIO()
       
        if image.name.split('.')[-1].lower() == 'jpeg':
            img.save(im_io , format='jpeg', optimize=True, quality=90)
            new_image = File(im_io, name="%s.jpeg" %image.name.split('.')[0],)
        else:
            return None

        return new_image
    
class User(AbstractUser):
    pass