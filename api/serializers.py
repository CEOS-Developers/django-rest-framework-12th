from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # exclude와 field는 동시에 사용 불가능