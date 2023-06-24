from django.shortcuts import render
from django.db import transaction
from collections import defaultdict

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import Room, RoomJoin, Message
from accounts.models import User
from .serializers import RoomSerializer


# 채팅방 연결 
@api_view(('POST',))
def room_create(request):
    '''
    {
        "to_user" : username
    }
    '''
    to_user_name = request.data.get('to_user')
    if to_user_name == request.user.username:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    room_id_list = RoomJoin.objects.filter(user_id__in=[request.user.username, to_user_name]).values_list('room_id', flat=True)
    
    now_room_id = 0
    rooms_dict = defaultdict(int)
    for room_id in room_id_list:
        rooms_dict[room_id] += 1
        if rooms_dict[room_id] == 2:
            now_room_id = room_id
            break
    
    if now_room_id:
        return Response({'room_id':now_room_id}, status=status.HTTP_200_OK)
    
    # 채팅방 생성 후 연결
    with transaction.atomic():
        new_room = Room.objects.create()
        RoomJoin.objects.create(room_id=new_room.pk, user_id=to_user_name)
        RoomJoin.objects.create(room_id=new_room.pk, user_id=request.user.username)
        return Response({'room_id':new_room.pk}, status=status.HTTP_200_OK)

# 현재 살아있는 채팅방 목록 - 안읽은 메시지 순으로 정렬해야함. + 메세지 있는 경우에만 전송 + 상대방 user 정보
@api_view(('GET',))
def room_list(request):
    rooms = RoomJoin.objects.filter(user_id=request.user)
    
    # to_users = RoomJoin.objects.filter(room_id=rooms.)
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
        ).order_by('-created_at')
    
    paginator = PageNumberPagination()
    paginator.page_size = 30
    return_list = paginator.paginate_queryset(messages, request)
    response = paginator.get_paginated_response(return_list)
    return Response(response.data, status=status.HTTP_200_OK)