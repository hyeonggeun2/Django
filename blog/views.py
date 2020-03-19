from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post


def post_list(request):
    # Template을 찾을 경로에서 '입력한 .html' 파일을 찾아서
    # 텍스트로 만들어서 HttpResponse 형태로 돌려줌

    posts = Post.objects.order_by('-pk')
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
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        text = request.POST['text']

        # 포스트를 만들어줌
        Post.objects.create(author=author, title=title, text=text)

        # post_list_url = reverse('url-name-post-list')
        # return HttpResponseRedirect(post_list_url)

        # shortcut 함수
        return redirect('url-name-post-list')
    else:
        return render(request, 'post_add.html')


def post_delete(request, pk):
    if request.method == 'POST':
        Post.objects.get(pk=pk).delete()
        return redirect('url-name-post-list')


def post_delete_confirm(request, pk):
    return render(request, 'post_delete_confirm.html', {'post': Post.objects.get(pk=pk)})


def post_edit(request, pk):
    # pk에 해당하는 Post를 수정한다
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        # 값을 업데이트
        Post.objects.filter(pk=pk).update(title=title, text=text)
        return redirect('url-name-post-detail', pk)
    else:
        post = Post.objects.get(pk=pk)
        context = {
            'post': post,
        }
        return render(request, 'post_edit.html', context)


def post_publish(request, pk):
    if request.method == 'POST':
        time = request.POST['date']
        Post.objects.filter(pk=pk).update(published_date=time)
        return redirect('url-name-post-detail', pk)
    else:
        return render(request, 'post_publish.html')


def post_unpublish(request, pk):
    Post.objects.filter(pk=pk).update(published_date=None)
    return redirect('url-name-post-detail', pk)


def naver_login(request):
    pass
