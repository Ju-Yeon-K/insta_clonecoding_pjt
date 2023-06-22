from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination

@api_view(('GET',))
def post_list(request):
    posts = Post.objects.all().values(
            'image', 'content', 'user', 'like_users'
    ).order_by('-created_at')
    
    paginator = PageNumberPagination()
    paginator.page_size = 12
    return_list = paginator.paginate_queryset(posts, request)
    response = paginator.get_paginated_response(return_list)
    return Response(response.data, status=status.HTTP_200_OK)


@api_view(('POST',))
def create(request):
    content = request.data.get('content')
    src = request.FILES['image']
    Post.objects.create(image=src, user=request.user, content=content)
    return Response({'msg':'게시물이 작성됨.'}, status=status.HTTP_201_CREATED)

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == post.user:
            post.delete()
            return redirect('posts:index')
    return redirect('posts:detail', post.pk)

def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            form.save()
            return redirect('posts:index')
        else:
            form = PostForm(instance=post)
        context = {
            'form':form, 
            'post':post
        }
        return render(request, 'posts/form.html', context)
    return redirect('posts:detail', post.pk)

@require_POST
def comments_create(request, pk): # detail 이 아니니까 index 에 연결하면에러뜸 ㅠ
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

        return redirect('posts:detail', post.pk)
    return redirect('accounts:login')

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comment_set.all()
    comment_form = CommentForm()

    count_a = post.comment_set.filter().count()

    context = {'post':post, 'comments' : comments,'comment_form':comment_form,}
    return render(request, 'posts/detail.html', context)

def comments_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('posts:detail', post_pk)

def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        if post.like_users.filter(pk=request.user.pk).last():
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
    return redirect('posts:detail', post_pk)