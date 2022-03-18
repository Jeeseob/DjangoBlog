from django.urls import path
from . import views

# 해당앱 내부의 url패턴
urlpatterns =[
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]