from django.db import models
from .validators import validate_score
from django.utils import timezone


# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)

# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1. 3개의 모델: Movie, Comment, Description.
2. Movie와 Comment는 1:N으로 연결하였다. 한 개의 영화에 여러 코멘크가 달리기 때문이다.
3. Movie와 Description은 1:1로 연결하였다. 한 영화에 대해 하나의 설명이 존재하고, 하나의 설명은 하나의 영화를 다루기 때문이다
    (비슷한 이야기의 영화는 배제하자...)
    
4. 영화에 출연한 배우들을 구현하고 싶긴한데, 시간이 되련지 모르겠다. Movie와 Actor의 관계는 N:M이 될 것이다.
5. 이용자 모델도 구현하고 싶긴한데, 시간이 되련지 모르겠다... 하루는 왜 24시간일까? 좀 더 길었으면 좋겠다.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

html_text = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Page Title</title>
    </head>
    <body>

    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>

    </body>
    </html>
"""


class Actor(models.Model):
    name = models.CharField(primary_key='TRUE', max_length=20)
    age = models.IntegerField()
    height = models.FloatField()


class Movie(models.Model):
    actor = models.ManyToManyField(Actor)
    title = models.CharField(max_length=30)
    house = models.PositiveIntegerField(unique='TRUE', default=0)
    price = models.IntegerField(default=10000)
    seat = models.IntegerField(default=100, null='TRUE')

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              related_name='comment')
    review = models.TextField(max_length=1000)
    written_date = models.DateField(default=timezone.now)
    """ 평점에 대한 부분은 0~10으로 제한했고, validators.py를 통해 구현 """
    grade = models.IntegerField(default=5, validators=[validate_score])
    count = models.IntegerField(default=0)

    def __str__(self):
        return '<%s, %s>' % (self.movie.title, self.review)


class Description(models.Model):
    movie = models.OneToOneField(Movie,
                                 on_delete=models.CASCADE)
    director = models.TextField(max_length=20)
    des = models.TextField(max_length=1000)
    published_date = models.DateField(default=timezone.now)
