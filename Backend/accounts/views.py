
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import User, Profile
from .serializers import UserProfileSerializer, ProfileSerializer


@api_view(('GET',))
def profile_detail(request, user_name):
    user = get_object_or_404(User, username=user_name)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(('GET',))
def profile(request, user_name):
    user = get_object_or_404(Profile, username=user_name)
    serializer = ProfileSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(('POST',))
def follow(request, user_name):
    person = User.objects.get(username=user_name)
    if request.user != person:
        if person.followers.filter(pk=request.user.pk).last():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return Response(status=status.HTTP_201_CREATED)

@api_view(('POST',))
def update_profile(request):
    nickname = request.data.get('nickname')
    introduction = request.data.get('introduction')
    src = request.FILES['image_raw']
    profile = Profile.objects.filter(user=request.user).last()
    if profile:
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=status.HTTP_200_OK)
    Profile.objects.create(image_raw=src, user=request.user, introduction=introduction, nickname=nickname)
    return Response(status=status.HTTP_201_CREATED)


# def delete(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             user = request.user 
#             user.delete()
#             auth_logout(request)
#             return redirect('posts:index')
#         else:
#             return render(request, 'accounts/delete.html')
#     else:
#         return redirect('accounts:login')
