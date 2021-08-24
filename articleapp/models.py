from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               related_name='article',
                               null = True)
    # project앱과 연결하기
    project = models.ForeignKey(Project,
                                on_delete=models.SET_NULL,
                                related_name='article',
                                null=True)
    # ForeignKey : 다른 데이터 베이스와 연결해주는 1:다로 연결해주는 필드
    title = models.CharField(max_length=200, null=True)
    # CharField() : 짧은 내용을 넣을때
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    # TextField() : 긴 내용을 넗을 때

    #     작성한 시간이 자동으로 설정
    created_at = models.DateField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)


