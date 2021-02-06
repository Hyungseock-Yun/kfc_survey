from django.shortcuts import render, get_object_or_404
from .models import Post


def posts(request):
    ## published_at 컬럼이 null이 아닐 경우, 데이터를 내림차순(order by) 정렬하여 가져온다.
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')

    ## 가져온 데이터를 blog/posts.html 페이지에 posts라는 key값으로 전달
    return render(request, 'blog/posts.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})
