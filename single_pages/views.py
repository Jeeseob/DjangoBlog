from django.shortcuts import render
from blog.models import Post
from blog.models import Category
# Create your views here.


def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )


def landing(request):
    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': Post.objects.order_by('-pk')[:3],
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
        })