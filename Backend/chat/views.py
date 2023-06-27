from collections import defaultdict

from django.shortcuts import render
from django.db import transaction
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import Room, RoomJoin, Message
from accounts.models import User, Profile
from .serializers import RoomSerializer
from .methods import find_dicts_with_value


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


# 현재 살아있는 채팅방 목록
@api_view(('GET',))
def room_list(request):
    # 유저의 채팅방 목록 + 접속 유저가 마지막으로 읽은 시간
    rooms = list(RoomJoin.objects.filter(user_id=request.user).values('room_id','last_read_at'))
    rooms_idxs = [ room.get('room_id') for room in rooms ]
    
    # 채팅방의 to user
    to_users = RoomJoin.objects.filter(room_id__in=rooms_idxs).filter(~Q(user_id=request.user)).values('user_id','room_id')
    to_users_idxs = [ user.get('user_id') for user in to_users ]
    
    # user, profile 정보를 response에 추가
    profiles = Profile.objects.filter(user_id__in=to_users_idxs).values('user_id', 'image_raw')
    for room in rooms:
        user_in_user_info = find_dicts_with_value(to_users, 'room_id', room.get('room_id'))[0].get('user_id')
        for profile in profiles:
            if user_in_user_info == profile.get('user_id'):
                room.update(dict(user={'user_id':user_in_user_info, 'image_raw':profile.get('image_raw')}))
                break
    
    # 메세지 가져오기 
    messages = Message.objects.filter(room_id__in=rooms_idxs).values('content','created_at', 'user_id','room_id')
    
    del_list = []
    # 메시지 정보를 response에 추가 
    for room in rooms[:]:
        room_messages = find_dicts_with_value(messages, 'room_id', room.get('room_id'))
        
        # 메세지 없는 경우에는 채팅방을 화면에 보여주지 않음. 
        if not room_messages:
            rooms.remove(room)
            continue
            
        room_messages.sort(key=lambda x:x.get('created_at'))
        last_message = room_messages[-1]
        message_unread_cnt = 0
        for message in reversed(room_messages):
            if message.get('created_at') > room.get('last_read_at'):
                message_unread_cnt += 1
            else:
                break
        room.update(dict(message_unread_cnt=message_unread_cnt, last_message=last_message))
   
    # 안읽은 메시지 순으로 정렬 
    rooms.sort(key=lambda x : x['last_message']['created_at'])
    
    paginator = PageNumberPagination()
    paginator.page_size = 12
    return_list = paginator.paginate_queryset(rooms, request)
    response = paginator.get_paginated_response(return_list)
    return Response(response.data, status=status.HTTP_200_OK) # response.data, 


# 채팅방의 메세지 
@api_view(('GET',))
def message_list(request, room_pk):
    # 상대방 유저가 마지막으로 읽은 시간 가져옴.
    to_user_read_info = RoomJoin.objects.filter(room_id=room_pk).filter(~Q(user_id=request.user)).values('last_read_at', 'created_at')[0]
    to_user_last_read_at = to_user_read_info.get('last_read_at') if to_user_read_info.get('last_read_at') else to_user_read_info.get('created_at')
    
    # 채팅방의 모든 메시지 시간순 정렬
    messages = Message.objects.filter(room_id=room_pk).values(
        'user_id', 'content','created_at'
        ).order_by('-created_at') 
    
    for message in messages:
        is_read = False if message.get('created_at') < to_user_last_read_at else True
        message.update(dict(is_read=is_read))
    
    paginator = PageNumberPagination()
    paginator.page_size = 30
    return_list = paginator.paginate_queryset(messages, request)
    response = paginator.get_paginated_response(return_list)
    return Response(response.data, status=status.HTTP_200_OK)