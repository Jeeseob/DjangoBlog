from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

# CBV를 사용하기 위함.
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# url패턴에서 실행하는 함수
from blog.models import Post, Category, Tag

# 로그인 방문자 접근
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'hook_message', 'content', 'head_image', 'attached_file', 'category']

    template_name = "blog/post_form_update.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_message', 'content', 'head_image', 'attached_file', 'category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog')


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


# def category_posts(request, slug):
#     if slug == 'no-category':
#         category = '미분류'
#         post_list = Post.objects.filter(category=None)
#     else:
#         category = Category.objects.get(slug=slug)
#         post_list = Post.objects.filter(category=category)
#
#     context = {
#         'categories': Category.objects.all(),
#         'no_category_post_count': Post.objects.filter(category=None).count(),
#         'category': category,
#         'post_list': post_list
#     }
#     return render(
#         request,
#         'blog/post_list.html',
#         context
#     )


class CategoryPostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(CategoryPostList, self).get_context_data()
        if self.kwargs['slug'] == 'no-category':
            context['post_list'] = Post.objects.filter(category__slug=None)
            context['category'] = '미분류'
        else:
            context['post_list'] = Post.objects.filter(category__slug=self.kwargs['slug'])
            context['category'] = Category.objects.get(slug=self.kwargs['slug'])

        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context


def show_tag_posts(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()
    context = {
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count(),
        'tag': tag,
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
