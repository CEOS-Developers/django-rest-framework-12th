from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def post_api(request):
    total_posts = Post.objects.all()
    serializer = PostSerializer(total_posts, many=True)
    return Response(serializer.data)
