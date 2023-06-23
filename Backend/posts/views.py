from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, PostUpdateSerializer, PostDetailSerializer


@api_view(('GET',))
def post_list(request):
    posts = Post.objects.all()
    serializers = PostSerializer(posts, many=True)

    paginator = PageNumberPagination()
    paginator.page_size = 12
    return_list = paginator.paginate_queryset(serializers.data, request)
    response = paginator.get_paginated_response(return_list)
    return Response(response.data, status=status.HTTP_200_OK)

@api_view(('POST',))
def create(request):
    content = request.data.get('content')
    src = request.FILES['image']
    Post.objects.create(image=src, user=request.user, content=content)
    return Response({'msg':'게시물이 작성됨.'}, status=status.HTTP_201_CREATED)

@api_view(('DELETE',))
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user == post.user:
        post.delete()
        return Response({'msg':'게시물이 삭제됨.'}, status=status.HTTP_200_OK)

@api_view(('GET',))
def detail(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostDetailSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(('PUT',))
def update(request, pk):
    post = Post.objects.get(pk=pk)
    content = request.data.get('content')
    src = request.FILES.get('image')
    serializer = PostUpdateSerializer(post, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
    return Response(status=status.HTTP_201_CREATED)

@api_view(('POST',))
def comments_create(request, pk): 
    post = Post.objects.get(pk=pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, post=post)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(('DELETE',))
def comments_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(('POST',))
def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.like_users.filter(pk=request.user.pk).last():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return Response(status=status.HTTP_200_OK)