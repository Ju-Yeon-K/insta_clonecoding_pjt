from django.urls import path
from . import views
from dj_rest_auth.views import LoginView, LogoutView, PasswordChangeView
from dj_rest_auth.registration.views import RegisterView
from django.views.generic import TemplateView

app_name = 'accounts'
urlpatterns = [
    path('signup/', RegisterView.as_view(), name='rest_register'),
    path(
        'account-email-verification-sent/', TemplateView.as_view(),
        name='account_email_verification_sent',
    ),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('profile/update/', views.update_profile, name='profile_update'),
    
    path('profile_info/<str:user_name>/', views.profile, name="profile"),
    path('profile/detail/<str:user_name>/', views.profile_detail, name="profile_detail"),
    # path('delete/', views.delete, name='delete'),
    path('follow/<str:user_name>/', views.follow, name='follow'),
]
