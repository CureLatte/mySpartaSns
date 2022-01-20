# user/models.py
from django.db import models

# 장고의 기본 유저 불러 오기
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    # 테이블에 대한 속성들
    class Meta:
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')


