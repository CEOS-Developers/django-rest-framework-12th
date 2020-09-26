from django.db import models

# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)

<<<<<<< HEAD
class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom'),
    ]

    name = models.CharField(blank=True, max_length=255)
    website = models.URLField(blank=True)
    email = models.CharField(blank=True, max_length=255)
    phone_number = models.CharField(blank=True, max_length=255)
    gender = models.CharField(blank=True, choices=GENDER_CHOICES, max_length=255)
=======
# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)
>>>>>>> parent of 06f2ae3... posts model made
