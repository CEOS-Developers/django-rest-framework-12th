from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    age = models.IntegerField()
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    address = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    GENRE_CHOICES = (('Thriller', 'Thriller'), ('SF', 'SF'), ('Horror', 'Horror'),
                     ('Drama', 'Drama'), ('Romance', 'Romance'), ('Action', 'Action'),
                     ('Fantasy', 'Fantasy'), ('Mystery', 'Mystery'), ('Animation', 'Animation'))
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    running_time = models.IntegerField()

class Timetable(models.Model):
    start_time = models.DateTimeField()
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="movie_play_info"),
    user = models.ManyToManyField(User, blank=True)

    def count_spare_seat(self):
        MAX_SEATS = 200
        return MAX_SEATS - self.user.all().count()

class Comment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_comment")




