from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileForm
from .models import User, Profile


# Create your views here.
def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index') 
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user_id=user.id)
            profile.save()
            auth_login(request, user)
            return redirect('posts:index') 
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)

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
    
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('posts:index') 
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form':form}
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('posts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'accounts/password.html', context)

def profile(request, user_name):
    user = User.objects.get(username=user_name)
    profile = Profile.objects.get(user_id=user.id)
    posts = user.post_set.all()
    context = {
        'profile':profile,
        'posts':posts
    }
    return render(request, 'accounts/profile.html', context)

def profile_update(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=request.user.id)
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile', request.user.username)
     

        form = ProfileForm(instance=profile)
        context = {
            'form':form
        }
        return render(request, 'accounts/profile_update.html', context)
    return redirect('accounts:login')