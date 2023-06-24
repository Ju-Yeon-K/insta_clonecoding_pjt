from django.urls import path
from django.conf.urls import url

from . import views
from . import consumer

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]

websocket_urlpatterns = [
    url(r'ws/chat/(?P<room_name>\w+)/$', consumer.ChatConsumer),
]
