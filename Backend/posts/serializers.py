from rest_framework import serializers
from .models import Post, Comment
from accounts.models import User

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    like_cnt = serializers.SerializerMethodField()
    like_users_name = serializers.SerializerMethodField()
    
    def get_comments(self, obj):
        comments_list = obj.comments.all().values(
            'content', 'user_id', 'id' , 'created_at', 'updated_at'
            ).order_by('-created_at')
        return comments_list
    def get_user_name(self, obj):
        name = obj.user.username
        return name
    def get_like_cnt(self, obj):
        cnt = obj.like_users.count()
        return cnt
    def get_like_users_name(self, obj):
        res_list = []
        for user in obj.like_users.all():
            res_list.append(user.username)
        return res_list

    class Meta:
        model = Post
        fields = ('pk', 'user', 'content', 'image', 'created_at', 'updated_at', 'comments','user_name','like_cnt','like_users_name')
        # read_only_fields = ['user', 'like_users']
        
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