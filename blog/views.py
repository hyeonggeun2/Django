from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def post_list(request):
    # Template을 찾을 경로에서 '입력한 .html' 파일을 찾아서
    # 텍스트로 만들어서 HttpResponse 형태로 돌려줌

    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse('없음')

    context = {
        'post': post
    }

    return render(request, 'post_detail.html', context)

def post_add(request):
    print(request)
    return render(request, 'post_add.html')