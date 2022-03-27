import os.path

from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)  # 제목
    content = models.TextField()  # 내용
    hook_message = models.TextField(blank=True)  # 미리보기 내용

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)  # upload_to는 디렉토리 지정, blank는 없어도
    attached_file = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    create_at = models.DateTimeField(auto_now_add=True)  # 업로드 날짜 : auto_now_add는 최초 생성시에만 적용
    update_at = models.DateTimeField(auto_now=True)  # auto_now는 업데이트 될 때마다 수정

    def __str__(self):
        # f는 formated string형태, python 기능.
        # '' 내부의 내용을 알맞은 포멧에 맞춰 데이터를 가져온다.
        # {}안에 변수를 넣으면, 해당 변수의 값이 나온다.
        return f'[{self.pk}] {self.title}'

    # 인터페이슬로 만들어져 있음.
    # Convention over configuration 이라고, 정해진 이름을 함수를 만들면, 일반적인 기능이 자동으로 추가된다.

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.attached_file.name)

## DB의 테이블 선언 느낌으로 객체 생성(Model) ORM 방식
## DB 생성 후, makemigrations를 통해 DB에 적용할 수 있다.
## 이후 migrate로 실제로 적용할 수 있다.

# 모델을 만들면 기본적인 CRUD는 자동적으로 적용된다.

# 각각의 Model객체마다 존재하는 함수를 model Method라고 한다.
