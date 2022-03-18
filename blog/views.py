from django.shortcuts import render

# Create your views here.

# url패턴에서 실행하는 함수
from blog.models import Post


def index(request):

    # DB에서 object를 가져오는 함수 (model기본 내장인듯)
    posts = Post.objects.all().order_by('-pk');
    # order_by('-pk') -> pk를 역순으로 정렬

    return render(
        request, # request에는 많은 정보가 들어있어, 이를 분석해서 처리할 수 있다.(os, 해상도, 등등 다양하게)
        'blog/index.html', # 정적 rendering이기 때문에 일단 템플릿을 그대로 전달.
        {
            'posts' : posts,  # context를 보내는 형태.(
        }
    )