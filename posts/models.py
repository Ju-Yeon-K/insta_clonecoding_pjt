from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # , related_name='comments' 넣ㅇ면 _set 대신 요거 사용 가능
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
