from rest_framework import serializers
from .models import Post, Comment
from accounts.models import User

class PostDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    like_cnt = serializers.SerializerMethodField()
    
    def get_comments(self, obj):
        comments_list = obj.comments.all().values(
            'content', 'user', 'id' , 'created_at', 'updated_at'
            ).order_by('created_at')
        return comments_list

    def get_like_cnt(self, obj):
        return obj.like_users.count()
    
    class Meta:
        model = Post
        fields = ('pk', 'user', 'like_users', 'content', 'image', 'created_at', 'updated_at', 'comments', 'like_cnt',)

class PostSerializer(serializers.ModelSerializer):
    like_cnt = serializers.SerializerMethodField()

    def get_like_cnt(self, obj):
        return obj.like_users.count()
    
    class Meta:
        model = Post
        fields = ('pk', 'user', 'like_users', 'content', 'image', 'created_at', 'updated_at', 'like_cnt',)

class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user', 'like_users']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'post']