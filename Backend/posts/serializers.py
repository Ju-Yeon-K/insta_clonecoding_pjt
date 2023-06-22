from rest_framework import serializers
from .models import Post, Comment
from accounts.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user', 'like_users']