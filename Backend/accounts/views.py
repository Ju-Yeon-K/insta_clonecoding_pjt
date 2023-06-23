from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileForm
from .models import User, Profile


# Create your views here.

def delete(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user 
            user.delete()
            auth_logout(request)
            return redirect('posts:index')
        else:
            return render(request, 'accounts/delete.html')
    else:
        return redirect('accounts:login')
    
# def update(request):
#     if request.method == "POST":
#         form = CustomUserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:index') 
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#     context = {'form':form}
#     return render(request, 'accounts/update.html', context)


def profile(request, user_name):
    # 만약 커스텀 유저모델이라면 아래 추가
    # from django.contrib.auth import get_user_model
    # User = get_user_model()
    user = User.objects.get(username=user_name)
    profile = Profile.objects.get(user_id=user.id)
    posts = user.post_set.all()
    context = {
        'profile':profile,
        'posts':posts
    }
    return render(request, 'accounts/profile.html', context)

# def profile_update(request):
#     if request.user.is_authenticated:
#         profile = Profile.objects.get(user_id=request.user.id)
#         if request.method == "POST":
#             form = ProfileForm(request.POST, request.FILES, instance=profile)
#             if form.is_valid():
#                 form.save()
#                 return redirect('profile', request.user.username)
     

#         form = ProfileForm(instance=profile)
#         context = {
#             'form':form
#         }
#         return render(request, 'accounts/profile_update.html', context)
#     return redirect('accounts:login')

# def follow(request, user_pk):
#     if request.method=="POST":
#         person = User.objects.get(pk=user_pk)
#         if request.user != person:
#             if person.followers.filter(pk=request.user.pk).last():
#                 person.followers.remove(request.user)
#             else:
#                 person.followers.add(request.user)
#     return redirect('profile', person.username)
    