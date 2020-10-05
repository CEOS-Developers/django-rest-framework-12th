from .models import Post
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ['posted_date']
        extra_kwargs = {'posted_date': {'read_only': True}}