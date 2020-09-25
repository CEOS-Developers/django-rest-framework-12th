from django.db import models
from django.contrib.auth.models import User
# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)

# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)

class Profile(models.Model):
    age = models.IntegerField()
    gender = models.BooleanField()
    address = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    running_time = models.IntegerField()

class PlayInfo(models.Model):
    time = models.DateTimeField()
    seat_left = models.IntegerField(default=200)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="movie_play_info")
    profile = models.ManyToManyField(Profile, null=True)


class Comment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    on_create = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="movie_comment")




