from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)