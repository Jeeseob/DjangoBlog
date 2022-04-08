from django.shortcuts import render

# Create your views here.

# CBV를 사용하기 위함.
from django.views.generic import ListView, DetailView

# url패턴에서 실행하는 함수
from blog.models import Post, Category


# class based views (CBV)
class PostList(ListView):
    model = Post  # 모델 객체 설정
    ordering = '-pk'  # 정렬 방식 설정(pk 역순)

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context


def category_posts(request, slug):
    category = Category.objects.filter(slug=slug)
    if slug == 'no-category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = category.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    context = {
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count(),
        'category': category,
        'post_list': post_list
    }
    return render(
        request,
        'blog/post_list.html',
        context
    )

# 템플릿 이름을 강제하는 방법. -> 하지만, name convention에 익숙해진 사람들에게 혼선을 줄 수 있어, 지정한 대로 하는 것이 생산성이 높다.
# template_name = 'blog/index.html'


# function views를 위해 만든 함수.
# def index(request):
#
#     # DB에서 object를 가져오는 함수 (model기본 내장인듯)
#     posts = Post.objects.all().order_by('-pk');
#     # order_by('-pk') -> pk를 역순으로 정렬
#
#     return render(
#         request, # request에는 많은 정보가 들어있어, 이를 분석해서 처리할 수 있다.(os, 해상도, 등등 다양하게)
#         'blog/post_list.html', # 정적 rendering이기 때문에 일단 템플릿을 그대로 전달.
#         {
#             'posts' : posts,  # context를 보내는 형태.(
#         }
#     )

# def single_post_page(request, pk) :
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post' : post,
#         }
#     )
