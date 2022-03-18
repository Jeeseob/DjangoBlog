from django.urls import path
from . import views

# 해당앱 내부의 url패턴
urlpatterns =[
    # class-based views ( 장고에서 제공하는 것)
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),

    # function view (내가 만든 것)
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page),
]