from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def post_api(request):
    total_posts = Post.objects.all()
    serializer = PostSerializer(total_posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def selected_post_api(request, pk):
    try:
        selected_post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PostSerializer(selected_post)
    return Response(serializer.data)

@api_view(['POST'])
def create_post_api(request):
    create_post = Post.objects.all()
    serializer = PostSerializer(create_post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)