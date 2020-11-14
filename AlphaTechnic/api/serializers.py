from .models import Post, Comment
from rest_framework.serializers import ModelSerializer


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'content')


class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    #username = ModelSerializer.SerializerMethodField()

    #def get_username(self, obj):
    #    return obj.author
    class Meta:
        model = Post
        # exclude = ['posted_date']
        # extra_kwargs = {'posted_date': {'read_only': True}}
        fields = ('content', 'author', 'comments', 'likes', 'dislikes')
