from django.db import models
from api import models as user_model


# data가 만들어진 time을 기록하기 위해 만듬
class TimeStamp(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # 별도의 테이블을 생성하지 않게 함
    class Meta:
        abstract = True


# 제품 포스트란
class Post(TimeStamp):
    image = models.ImageField(blank=True)
    caption = models.TextField(blank=True)


# 제품란
class Product(TimeStamp):
    name = models.CharField(blank=True, max_length=255)
    price = models.IntegerField(max_length=255)


# 제품 포스트에 달리는 댓글란
class Comment(TimeStamp):
    # model의 사용자 이름을 fk로 갖는다
    author = models.ForeignKey(
        user_model.User,
        null=True,
        on_delete=models.CASCADE,
        related_name='post_author'
    )
    # 댓글은 post를 fk로 갖는다
    posts = models.ForeignKey(
        Post,
        null=True,
        on_delete=models.CASCADE,
        related_name='comment_post'
    )
    contents = models.TextField(blank=True)
