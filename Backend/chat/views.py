from django.shortcuts import render
from django.db import transaction

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import Room, RoomJoin, Message
from accounts.models import User
from .serializers import RoomSerializer


def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

# 채팅방 연결 
@api_view(('POST',))
def room_create(request):
    '''
    {
        "to_user" : username
    }
    '''
    to_user_name = request.data.get('to_user')
    
    my_room_list = RoomJoin.objects.filter(user_id=request.user.username).values('room_id')
    rooms1 = []
    for my_room in my_room_list:
        rooms1.append(my_room['room_id'])
    
    to_user_room_list = RoomJoin.objects.filter(user_id=to_user_name).values('room_id')
    rooms2 = []
    for my_room in my_room_list:
        rooms2.append(my_room['room_id'])

    now_room_id = list(set(rooms1) & set(rooms2))
    
    if now_room_id:
        return Response({'room_id':now_room_id}, status=status.HTTP_200_OK)
    
    # 채팅방 생성 후 연결
    with transaction.atomic():
        new_room = Room.objects.create()
        RoomJoin.objects.create(room_id=new_room.pk, user_id=to_user_name)
        RoomJoin.objects.create(room_id=new_room.pk, user_id=request.user.username)
        return Response({'room_id':new_room.pk}, status=status.HTTP_200_OK)

# 현재 살아있는 채팅방 목록 - 안읽은 메시지 순으로 정렬해야함. 
@api_view(('GET',))
def room_list(request):
    rooms = RoomJoin.objects.filter(user_id=request.user)
    serializers = RoomSerializer(rooms, many=True)
    
    paginator = PageNumberPagination()
    paginator.page_size = 12
    return_list = paginator.paginate_queryset(serializers.data, request)
    response = paginator.get_paginated_response(return_list)
    return Response(response.data, status=status.HTTP_200_OK)

# 채팅방의 메세지 
@api_view(('GET',))
def message_list(request, room_pk):
    messages = Message.objects.filter(room_id=room_pk).values(
        'user_id', 'content','created_at'
        ).order_by('created_at')
    
    paginator = PageNumberPagination()
    paginator.page_size = 30
    return_list = paginator.paginate_queryset(messages, request)
    response = paginator.get_paginated_response(return_list)
    return Response(response.data, status=status.HTTP_200_OK)