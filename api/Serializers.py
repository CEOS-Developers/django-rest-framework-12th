from django.contrib.auth.models import User, Group  # 기존 장고 모델
from rest_framework import serializers
from api.models import Routine, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User                                     # 사용할 모델
        fields = ['url', 'username', 'email', 'groups']  # 사용할 모델의 필드


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta :
        model = Profile
        fields = ['firebaseUid, deviceUid']


class RoutineSerializer(serializers.ModelSerializer):
    Profile = ProfileSerializer()
    class Meta:
        model = Routine
        fields = ['uuid, name, bgImage, doneAt']
