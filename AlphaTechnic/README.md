# django-rest-framework-12th

## 유의사항
* 본 레포지토리는 백엔드 스터디 2-3주차의 과제를 위한 레포입니다.
* 따라서 해당 레포를 fork 및 clone 후 local에서 본인의 깃헙 ID 브랜치로 작업한 후 커밋/푸시하고,
PR 보낼 때도 `본인의 브랜치-> 본인의 브랜치`로 해야 합니다.

## 2주차 과제 (기한: 9/26 토요일까지)
노션 링크 (https://www.notion.so/2-Django-ORM-c46e2d2f88ac4d948d012c07605d8e03)

-------------------------

### 서비스 설명
twitter

좋아요를 누르고 댓글을 달고 follow하는 등등의 sns 방식이 많은 앱 기획에서 구현하고 싶어하는 기본 요소여서, 가장 간단한 형식의 sns라고 생각되는 twitter를 copy해보려고 한다.

### 모델 설명
- model 구조

```
- AlphaTechnic
	- api
		- Post
		- Comment
		- Preference
	- users
		- Profile
		- Follow
```



- api

```python
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.TextField(max_length=1000)
    posted_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 장고의 User 모델을 이용
    likes = models.IntegerField(default=0)       ## Post가 가지고 있는 좋아요, 싫어요
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:15] + '...'  # Post 객체의 content가 앞 15자만 보여지도록. 

    def num_of_comments(self):      ## 해당 Post 객체가 가지고 있는 comment 수를 알려줌. 
        return Comment.objects.filter(connected_post=self).count()
    
    @property  ## 외부에서 post_obj.comments하면 post_obj의 comment들이 조회되도록(마치 Profile객체가 가진 속성인 것처럼) @property를 이용하여 getter를 구현
    def comments(self):
        return Comment.objects.filter(connected_post=self)


class Comment(models.Model):
    ## Post : Comment = 1 : N 관계가 되도록 Post를 외래키로 지정
    connected_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    posted_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  ## object가 조회되었을 때, 보여지는 string 형식을 지정
        return self.content[:15] + '.. -> ' + str(self.connected_post)[:8] + '..'


class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + '.. : ' + str(self.post) + ' : \"' + str(self.likes) + '\" likes'

```



- users

```python
from django.db import models
from django.contrib.auth.models import User
from PIL import Image ## image를 재가공할 수 있는 패키지 설치


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to="users/profile_pic")
    ## 이미지 등록 안했을 경우의 default 이미지를 설정해줌.

    def __str__(self):
        return f'{self.user.username} Profile'

    @property  
    def followers(self):
        return Follow.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()

        ## 이미지 사이즈를 300*300으로 재가공하여 저장하기 위한 작업
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            size = (300, 300)
            img.thumbnail(size)
            img.save(self.image.path)


class Follow(models.Model):
    ## User를 통해 user 혹은 follow_user를 역참조하기 위한 related_name 설정
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
```



#### 관련 개념

- models.DateTimeField(`setting`) : `default=timezone.now` vs `auto_now=True` vs `auto_now_add=True`
    - `default=timezone.now` : 현재 시간을 default 값으로 저장.
        - posted_date를 이 설정으로 저장하였다. 사용자가 과거의 일기같은 것을 현재 작성하고 있는 경우, posted_date를 과거로 바꿀 수도 있을 것이다.
    - `auto_now=True` : '수정 일자'를 등록하는 데 사용. model이 save 될 때마다 현재날짜(date.today()) 로 **갱신된다.**
        - 좋아요를 누른 date를 이 설정으로 저장하였다. model을 다시 save하면, date가 갱신된다.
    - `auto_now_add=True` : '생성 일자'를 등록하는 데 사용. model을 최초 저장(insert) 시에만 현재날짜(date.today()) 를 적용한다.
        - Follow를 시작한 date를 이 설정으로 저장하였다. model이 save 되어도 date가 **갱신되지 않는다.**

- `@property` : class 내의 메서드들을 외부에서 사용할 때, 마치 '속성(attribute)'인 것처럼 사용할 수 있게하는 장치

> `getter_setter.py`

```python
class Person:
    def __init__(self):
        self.__age = 0
 
    def get_age(self):           # getter
        return self.__age
    
    def set_age(self, value):    # setter
        self.__age = value
 
james = Person()
james.set_age(20)
print(james.get_age())
## 실행 결과 20
```

> property.py

```python
class Person:
    def __init__(self):
        self.__age = 0
 
    @property
    def age(self):           # getter
        return self.__age
 
    @age.setter
    def age(self, value):    # setter
        self.__age = value
 
james = Person()
james.age = 20      # 인스턴스.속성 형식으로 접근하여 값 저장
print(james.age)    # 인스턴스.속성 형식으로 값을 가져옴
## 실행 결과 20
```





### ORM 적용해보기

```python
In [1]: from api.models import Post, Comment, Preference

In [2]: from users.models import Profile, Follow

In [3]: post_obj = Post.objects.all()[0]

In [4]: post_obj.num_of_comments()
Out[4]: 2

In [5]: post_obj.comments
Out[5]: <QuerySet [<Comment: lol!!!!!!!!!.. -> Lorem Ip..>, <Comment: What a wonderfu.. -> Lorem
Ip..>]>

In [6]: Preference.objects.all()
Out[6]: <QuerySet [<Preference: kind_user.. : It is a long es... : "3" likes>, <Preference: kind_
user.. : It is a long es... : "1" likes>]>

In [7]: profile_obj = Profile.objects.all()[0]

In [8]: profile_obj
Out[8]: <Profile: kind_user Profile>

In [9]: profile_obj.followers
Out[9]: 1

In [10]: profile_obj.following
Out[10]: 0
```



### 간단한 회고 

1. 장고의 admin 페이지가 모델들 생성, 삭제를 매우 쉽게 해주고, 조회도 정말 편하게 할 수 있어 좋다.
2. mysql workbench가 내가 생성한 모델들을 table로 보여주어서, 해당 속성에 어떻게 접근해야하는지 쉽게 알 수 있었다.
3. ForeignKey가 model을 어떻게 만들어 주는지 더 와닿게 느끼게 되었다.

