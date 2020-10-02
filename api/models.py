from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

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


class Actor(models.Model):
    name = models.CharField(max_length=20, default='')
    age = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return '<%s: %d, %d>' % (self.name, self.age, self.height)


class Movie(models.Model):
    # Actor와 Movie를 M:N으로 연결
    actors = models.ManyToManyField(Actor,
                                    related_name='movies'
                                    )
    title = models.CharField(max_length=30)
    director = models.CharField(max_length=20)
    synopsis = models.TextField()
    published_date = models.DateField(auto_now=True)
    running_time = models.IntegerField()

    class Meta:
        managed = True

    def __str__(self):
        return self.title

    # 영화에 달린 comment 개수
    def comment_count(self):
        return self.comments.count()


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15, verbose_name='user nickname')
    movie = models.ManyToManyField(Movie,
                                   related_name='movies',
                                   blank=True
                                   )

    def __str__(self):
        return f'{self.user.username} profile'


class Comment(models.Model):
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              related_name='comments')
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='profile')
    # ForeignKey 설정할 때 받아오는 모델에 ''을 추가해주면 나중에 선언한 Model을 받아올 수 있음
    review = models.TextField()
    written_date = models.DateField(auto_now=True)  # comment를 가장 처음 작성한 시간
    update_date = models.DateField(auto_now_add=True)  # comment를 수정한 경우 수정한 시간
    rating = models.IntegerField(default=5,
                                 validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return '<%s, %s>' % (self.movie.title, self.review)


class Screen(models.Model):
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              related_name='screens')
    container = models.PositiveIntegerField(primary_key=True,
                                            unique=True,
                                            default=1)
    startTime = models.DateField(auto_now=True)
    price = models.IntegerField(blank=True, null=True)
    seat = models.IntegerField(blank=True, null=True)
