from rest_framework import serializers
from .models import Post, Comment
from accounts.models import User

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    
    def get_comments(self, obj):
        comments_list = obj.comments.all().order_by('-created_at')
        return comments_list
    class Meta:
        model = Post
        fields = ('user', 'content', 'like_users', 'image', 'created_at', 'updated_at', 'comments')
        # read_only_fields = ['user', 'like_users']