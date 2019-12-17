"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import post_list, post_detail, post_delete_confirm

urlpatterns = [
    path('admin/', admin.site.urls),
    # post-list라는 URL에 온 요청을 post_list 함수가 처리
    path('post-list/', post_list),
    path('post-detail/<int:pk>/', post_detail)
]
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import post_list, post_detail, post_add, post_delete, post_edit, post_publish, post_unpublish

urlpatterns = [
    path('admin/', admin.site.urls),
    # post-list라는 URL에 온 요청을 post_list 함수가 처리
    # url 에 이름을 줘서 html 문서에 동저으로 할당할 수 있음.
    path('posts/', post_list, name='url-name-post-list'),
    path('post-detail/<int:pk>/', post_detail, name='url-name-post-detail'),
    path('posts/add/', post_add, name='url-name-post-add'),
    path('posts-delete/<int:pk>/', post_delete, name='url-name-post-delete'),
    path('posts-edit/<int:pk>/', post_edit, name='url-name-post-edit'),
    path('posts-publish/<int:pk>/', post_publish, name='url-name-post-publish'),
    path('posts-unpublish/<int:pk>/', post_unpublish, name='url-name-post-unpublish'),
    path('post-delete-conf/<int:pk>', post_delete_confirm, name='url-name-post-del-conf')
]
