from django.shortcuts import render


def post_list(request):
    # Template을 찾을 경로에서 '입력한 .html' 파일을 찾아서
    # 텍스트로 만들어서 HttpResponse 형태로 돌려줌
    return render(request, 'post_list.html')