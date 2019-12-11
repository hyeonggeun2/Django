import os

from django.http import HttpResponse


def post_list(request):
    cur_file_path = os.path.abspath(__file__) # 현재파일의 절대경로
    blog_dir_path = os.path.dirname(cur_file_path)

    root_dir_path = os.path.dirname(blog_dir_path)
    templates_dir_path = os.path.join(root_dir_path, 'templates')
    post_list_html_path = os.path.join(templates_dir_path, 'post_list.html')

    f = open(post_list_html_path, 'rt')
    html = f.read()
    f.close()
    return HttpResponse(html)