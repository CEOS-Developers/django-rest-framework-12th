from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def helloAPI(request):
    return Response("hello World!")