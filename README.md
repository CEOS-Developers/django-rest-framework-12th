# django-rest-framework-12th

## 유의사항
* 본 레포지토리는 백엔드 스터디 2-3주차의 과제를 위한 레포입니다.
* 따라서 해당 레포를 fork 및 clone 후 local에서 본인의 깃헙 ID 브랜치로 작업한 후 커밋/푸시하고,
PR 보낼 때도 `본인의 브랜치-> 본인의 브랜치`로 해야 합니다.

## 2주차 과제 (기한: 9/26 토요일까지)
노션 링크 (https://www.notion.so/2-Django-ORM-c46e2d2f88ac4d948d012c07605d8e03)

### 서비스 설명

영화 목록 서비스로, 현재 상영 중인 영화와 이에 대한 정보(리뷰, 평점, 등장배우, 설명서.. 등)을 볼 수 있도록 하는 서비스이다. 현재는 모델링만 했지만, 좀 더 구현해서 User에 대한 부분도 추가하도록 노력해볼 것이다.

기능의 경우 역시 아직 구현하지 않았지만, 기존에 존재하는 영화 어플처럼 사용자가 영화를 구매하고 평점과 리뷰를 달아 그것들을 볼 수 있게 해주는 서비스를 구현해보려한다.



### 모델 설명

Actor

```python
class Actor(models.Model):
    name = models.CharField(primary_key='TRUE', max_length=20)
    age = models.IntegerField()
    height = models.FloatField()
```

- name을 기본 키로 설정하고 그 외 배우에 대한 신상 정보를 넣었다.

Movie

```python
class Movie(models.Model):
    # Actor와 Movie를 M:N으로 연결
    actor = models.ManyToManyField(Actor)
    title = models.CharField(max_length=30)
    house = models.PositiveIntegerField(unique='TRUE', default=0)
    price = models.IntegerField(default=10000)
    seat = models.IntegerField(default=100, null='TRUE')

    def __str__(self):
        return self.title
```

- 해당 서비스에서 가장 중심이 되는 모델
- Actor와 M:N 구현을 했다. 따라서 각 영화 당 등장 배우들을 볼 수 있고, 반대로 각 배우 당 참여한 영화들을 볼 수 있다.

Comment

```python
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
```

- Movie의 외래 키로 설정했다. 영화 한 편에 많은 코멘트가 생길 수 있으므로 영화와 1:M 관계를 구축했다.

- 개선해야 할 점

  - grade에 대한 부분: default를 validators=[validate_score]

    ```python
    # validators.py
    from django.core.exceptions import ValidationError
    
    
    def validate_score(value):
        """평점(score)이 10보다 크면 Validation Error 를 일으킨다."""
        if (value > 10) | (value < 0):
            msg = u"'평점은 0 이상 10 이하로 매겨주세요."
            raise ValidationError(msg)
    ```

    으로 구현했는데, 원했던 점은 0~10 외의 grade가 입력되면 오류가 나도록 하는 것이었다.

    ```python
    >>> c3=m1.comment.create(review="review3 of movie1", grade=11, count=3) # 오류가 나길 간절히 빕니다.
    >>> c3.save() # 저장이 되네;
    >>> m1.comment.all() # 출력되길 바라지 않았던 게 출력된다.
    <QuerySet [<Comment: <movie1, review1 of movie1>>, <Comment: <movie1, review3 of movie1>>]>
    ```

  - count에 대한 부분: 해당 영화의 코멘트가 작성될 때마다 자동으로 1씩 증가하길 원했다. 질문했던 부분이긴 한데, 답변을 보고 구현할 수 있도록 노력해봤는데 안됐다.

Description

```python
class Description(models.Model):
    movie = models.OneToOneField(Movie,
                                 on_delete=models.CASCADE)
    director = models.TextField(max_length=20)
    des = models.TextField(max_length=1000)
    published_date = models.DateField(default=timezone.now)
```

- 영화의 설명서(팜플렛 같은 거)를 보여주는 Model.
- 영화와 1:1 관계를 이뤘다. 물론 비슷한 스토리의 영화가 있지만 내가 만든 서비스에는 모든 영화가 다 서로 구별되는 영화로 제작된다고 가정했다. 이게 안되면 힘들어진다. 내 삶이.



### ORM 적용해보기

A. 개체 생성 및 쿼리

1. Actor 객체 3개를 생선한다.

   ```python
   >>> a1=Actor.objects.create(name="andy", age=30, height=170)
   >>> a1.save()
   >>> a2=Actor.objects.create(name="bobby", age=35, height=175)
   >>> a2.save()
   >>> a3=Actor.objects.create(name="chris", age=40, height=180)
   >>> a3.save()
   >>> Actor.objects.all()
   <QuerySet [<Actor: Actor object (andy)>, <Actor: Actor object (bobby)>, <Actor: Actor object (chris)>]>
   ```

2. Movie 객체 3개를 생성한다.

   ```python
   >>> m1=Movie.objects.create(title="movie1", house=1, price=10000,seat=80)
   >>> m1.save()
   >>> m2=Movie.objects.create(title="movie2", house=2, price=13000,seat=90)
   >>> m2.save()
   >>> m3=Movie.objects.create(title="movie3", house=3, price=8000,seat=40)
   >>> m3.save()
   ```

3. Actor와 Movie를 연결짓는다. '영화 m에 배우 a가 출연한다.'의 형식이다.

   ```python
   >>> m1.actor.add(a1)
   >>> m2.actor.add(a2,a3)
   >>> m3.actor.add(a1,a2,a3)
   # 결과1: 배우가 출연한 영화들
   >>> a1.movie_set.all()
   <QuerySet [<Movie: movie1>, <Movie: movie3>]>
   >>> a2.movie_set.all()
   <QuerySet [<Movie: movie2>, <Movie: movie3>]>
   >>> a3.movie_set.all()
   <QuerySet [<Movie: movie2>, <Movie: movie3>]>
   # 결과2: 영화에 등장한 배우들
   >>> m1.actor.all()
   <QuerySet [<Actor: Actor object (andy)>]>
   >>> m2.actor.all()
   <QuerySet [<Actor: Actor object (bobby)>, <Actor: Actor object (chris)>]>
   >>> m3.actor.all()
   <QuerySet [<Actor: Actor object (andy)>, <Actor: Actor object (bobby)>, <Actor: Actor object (chris)>]>
   
   ```

4. Comment 객체 3개를 m1에 연결한다.

   ```python
   >>> c1=m1.comment.create(review="review1 of movie1", grade=3, count=1)
   >>> c1.save()
   >>> c2=m1.comment.create(review="review2 of movie1", grade=2, count=2)
   >>> c2.save()
   >>> c3=m1.comment.create(review="review3 of movie1", grade=11, count=3)  # 오류가 나길 바랬던 부분
   >>> c3.save()
   # 결과: 영화 m1에 단 코멘트들 출력 <영화제목, 해당 코멘트 내용> 구조로 출력했다.
   >>> m1.comment.all()
   <QuerySet [<Comment: <movie1, review1 of movie1>>, <Comment: <movie1, review3 of movie1>>, <Comment: <movie1, review2 of movie1>>]>
   ```

5. Description

   ```python
   >>> d1=Description(director="movie1 director", des="about movie1")
   >>> d1.movie=m1
   >>> d1.save()
   >>> m1.description
   <Description: Description object (1)>
   >>> d1.movie
   <Movie: movie1>
   ```



B. filter 이용

1. exclude함수

   ```python
   # Description 객체들 중에 director 항목 중 2가 포함된 Description 객체를 제외한 나머지 Description 쿼리셋을 query_set에 저장 및 출력
   >>> query_set = Description.objects.exclude(director__icontains='2')
   >>> query_set
   <QuerySet [<Description: <about movie1: about movie1>>, <Description: <about movie3: about movie3>>]>
   # query_set에 포함된 각 객체의 모든 필드를 출력하는 values()함수
   >>> query_set.values()
   <QuerySet [{'id': 1, 'movie_id': 1, 'director': 'movie1 director', 'des': 'about movie1', 'published_date': datetime.date(2020, 9, 25)}, {'id': 3, 'movie_id': 3, 'director': 'movie3 director', 'des': 'about movie3', 'published_date': datetime.date(2020, 9, 25)}]>
   ```

2. filter 함수

   ```python
   >>> Movie.objects.filter(price__gt=9000)
   <QuerySet [<Movie: movie1>, <Movie: movie2>]>
   >>> Movie.objects.filter(price__gt=9000).last()
   <Movie: movie2>
   >>> Movie.objects.filter(price__gt=9000).last().actor.all()
   <QuerySet [<Actor: Actor object (bobby)>, <Actor: Actor object (chris)>]>
   ```

   - Movie 객체 중 가격이 9000원이 넘는 것들을 필터링한 쿼리셋 중 마지막 인자에 해당하는 영화에 출연한 배우들을 출력해보았다.

   ```python
   >>> Comment.objects.filter(movie_id=1)
   <QuerySet [<Comment: <movie1, review1 of movie1>>, <Comment: <movie1, review3 of movie1>>, <Comment: <movie1, review2 of movie1>>]>
   >>> Comment.objects.filter(movie_id=1).filter(review__icontains='2')
   <QuerySet [<Comment: <movie1, review2 of movie1>>]>
   >>> Actor.objects.get(name='andy').movie_set.all()
   <QuerySet [<Movie: movie1>, <Movie: movie3>]>
   ```

   - Comment 중 movie1에 대한 comment를 필터링하였다.
   - 위에서 한 번 필터링 된 comment 중에서 다시 한 번 필터링을 했는데, __icontains를 이용해 review 중 2가 포함된 review만 출력했다.
   - 역참조를 할 때 filter를 사용할 수도 있고, get을 사용할 수도 있다.



### 간단한 회고 

재밌는 시간이었다. 수요일 정도부터 시작했는데, 도중에 한 번 날려먹어서 금요일 새벽? 정도부터 다시 시작하게 되었다. 조금 더 시간이 있었고 python, django에 대한 경험이 있었으면 위에서 언급한 개선해야 할 점들도 충분히 구현할 수 있었을 것 같은 아쉬움이 많이 남는다.

모델링을 하고 모델 간에 관계를 연결하다보니 계속해서 추가적으로 구현해야 하는 부분이 생겼고, 그러다보니 외래키를 사용하는 부분이 바뀌거나(ex. 영화->코멘트에서 코멘트->영화 등 순서 바꾸기) 필드를 없애고 다른 모델을 참조해 구현하게 되는 경우도 있었다. 그러다보니 전체 모델링이 바뀌고, makemigration, migrate를 하면 갑자기 오류가 나는 경우가 종종 있었다. 그럴 때마다 겁먹지 않고 migrate폴더 내용물을 삭제하는 대담함은 생겼지만 언제까지고 삭제만 하고 있으면 오류를 고치는 실력은 안 늘 것 같다.

과제가 무엇인지 잘 읽어봐야겠다 라는 생각을 했다. 단순히 모델링만 하는 줄 모르고 view를 구현하려다 현타가 오고 멘탈이 터졌다(카톡에 질문 올린 시점). 그러다가 진호님과 줌도 하면서 멘탈 케어도 해주셨는데 그게 참 감사했다. 좋으신 분이다.