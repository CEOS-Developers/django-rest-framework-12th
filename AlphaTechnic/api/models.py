from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.TextField(max_length=1000)
    posted_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:15] + '...'

    def num_of_comments(self):
        return Comment.objects.filter(connected_post=self).count()


class Comment(models.Model):
    connected_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    posted_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:15] + '.. -> ' + str(self.connected_post)[:8] + '..'


class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + '.. : ' + str(self.post) + ' : \"' + str(self.likes) + '\" likes'
