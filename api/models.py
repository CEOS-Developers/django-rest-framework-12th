from django.db import models
from django.contrib.auth.models import User
# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)

# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    device_uid = models.CharField(max_length=128)
    firebase_uid = models.CharField(max_length=128)

class Routine(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='routines')
    routine_id = models.CharField(max_length=128)
    data = models.TextField()

class History(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='histories')
    history_id = models.CharField(max_length=128)
    data = models.TextField()

class MyTraining(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='myTrainings')
    my_training_id = models.CharField(max_length=128)
    data = models.TextField()