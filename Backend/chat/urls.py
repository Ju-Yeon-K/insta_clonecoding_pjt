from django.urls import path
from django.conf.urls import url

from . import views
from . import consumer

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('create/', views.room_create, name='room_create'),
    path('<int:room_pk>/messages/', views.message_list, name='message_list'),
]

websocket_urlpatterns = [
    url(r'ws/chat/(?P<room_name>\w+)/$', consumer.ChatConsumer),
]
