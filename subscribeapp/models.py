from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    # CSCADE는 종속의 뜻, 계정 정보가 삭제되면 Subscription정보도 삭제된다.
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)

    # Meta는 외부정보(예를들어 사진이 언제찍혔든지, 사이즈는 얼마인지 하는등의 정보)
    class Meta:
        # 구독정보 쌍(user, project)를 유니크하게 지정
        unique_together = ['user', 'project']


