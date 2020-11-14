from django.contrib.auth.models import User, Group  # 기존 장고 모델
from rest_framework import serializers
from api.models import Routine, Profile, Workout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User                                     # 사용할 모델
        fields = ['url', 'username', 'email', 'groups']  # 사용할 모델의 필드


class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta :
        model = Profile
        fields = '__all__'


class RoutineSerializer(serializers.ModelSerializer):
    # Profile = ProfileSerializer()

    class Meta:
        model = Routine
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'