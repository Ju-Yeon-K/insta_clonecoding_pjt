from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<str:user>', views.user_post_list, name='user_post_list'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:post_pk>/likes/', views.likes, name='likes'),
]
