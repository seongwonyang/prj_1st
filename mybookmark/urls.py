"""mybookmark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.urls import path

from django.conf.urls import re_path        # Django의 내장함수를 import
from bookmark.views import *       # 각 url에 매핑시킬 뷰들을 bookmark의 views.py에서 가져와 import

"""
re_path(regex, view, name): re_path()는 세 개의 인자를 가집니다.
                            regex는 정규식, view는 해당 url 패턴에 매핑시킬 뷰,
                            name은 해당 url 패턴에 붙일 이름을 의미합니다.
"""
urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^admin/', admin.site.urls),

    re_path(r'^bookmark/$', BookmarkListView, name='list'),
    re_path(r'^bookmark/(?P<pk>\d+)/$', BookmarkDetailView, name='detail'),
]
"""
r'^bookmark/$'에 일치하는 url이 들어오면 BookmarkListView에 매핑할거고
이 패턴의 이름은 list로 지정할 것이다는 의미
"""
