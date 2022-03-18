"""blog_main URL Configuration

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
from django.urls import path, include

# url 패턴 목록 - 위에가 특별한 케이스, 아래가 일반적인 케이스 (위에서 부터 탐색하기 때문에)
urlpatterns = [
    path('blog/', include('blog.urls')),
    # include는 django.urls 라이브러리에 존재한다. import 해줘야함.
    # 해당 패턴을 사용하는 것을 cunsume이라고 한다.
    path('admin/', admin.site.urls),

    path('', include('single_pages.urls')),
]
