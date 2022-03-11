from django.contrib import admin

# 현재 디렉토리의 하위 디렉토리인 models에서 Post객체 import
from .models import Post

# Register your models here.

admin.site.register(Post)
