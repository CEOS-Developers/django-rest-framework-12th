from .models import *
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'running_time']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['title', 'content', 'create_time', 'modify_time', 'movie', 'user']
        #serializer 필드에 연결시켜준 모델도 이어줘야하는지??

