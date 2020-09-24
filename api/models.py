from django.db import models
from .validators import validate_score

# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)

# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)

class Movies(models.Model):
    title = models.CharField(max_length=30, primary_key='TRUE')
    house = models.IntegerField(default=0)
    price = models.IntegerField(default=10000)

    def __str__(self):
        return '<%s: at %s>' % (self.title, self.house)


class Comments(models.Model):
    movies = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='comment')
    review = models.TextField(max_length=1000)
    """ 평점에 대한 부분은 0~10으로 제한했고, validators.py를 통해 구현 """
    grade = models.IntegerField(default=5, validators=[validate_score])
    count = models.IntegerField()

    def __str__(self):
        return '<%s: %s comments>' % (self.movies, self.count)


class Descriptions(models.Model):
    movies = models.OneToOneField(Movies, on_delete=models.CASCADE, related_name='description')
    director = models.TextField(max_length=20)
    descrip = models.TextField(max_length=1000)

    def __str__(self):
        return '<%s, dir: %s>' % (self.movies, self.director)