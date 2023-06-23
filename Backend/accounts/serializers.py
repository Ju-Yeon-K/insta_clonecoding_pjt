from rest_framework import serializers
from .models import User, Profile
from posts.models import Post


class UserProfileSerializer(serializers.ModelSerializer):
    profile_info = serializers.SerializerMethodField()
    following_cnt = serializers.SerializerMethodField()
    post_cnt = serializers.SerializerMethodField()
    
    def get_profile_info(self, obj):
        profile = Profile.objects.filter(user=obj.username).values(
            'nickname', 'introduction', 'image_raw'
            )
        return profile
    
    def get_following_cnt(self, obj):
        return obj.followings.count()


    def get_post_cnt(self, obj):
        return Post.objects.filter(user=obj.username).count()
    
    class Meta:
        model = User
        fields = ('profile_info', 'post_cnt', 'following_cnt','followers')

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = '__all__'