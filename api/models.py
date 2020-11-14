from django.db import models
from django.contrib.auth.models import User
# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)

# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    device_uid = models.CharField(max_length=128)
    firebase_uid = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username

class Routine(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='routines')
    uuid = models.CharField(max_length=128)
    name = models.CharField(max_length=128, null=True, blank=True)
    bgImage = models.IntegerField(default=0)
    doneAt = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return self.name


class Workout(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='workouts')
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='workouts')
    uuid = models.CharField(max_length=128)
    name = models.CharField(max_length=128, null=True, blank=True)
    memo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name if self.name else self.routine.name


class Training(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='trainings')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='trainings')
    uuid = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    memo = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=128, default='normal')

    def __str__(self):
        return self.name


class Set(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sets')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='sets')
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='sets')
    idx = models.IntegerField(default = -1)
    is_done = models.BooleanField(default = False);
    # if type is normal, val1 = weight, val2 = reps.
    # else if type is time, val1 = hour, val2 = min, val3 = sec
    val1 = models.IntegerField(null=True, blank=True)
    val2 = models.IntegerField(null=True, blank=True)
    val2 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
