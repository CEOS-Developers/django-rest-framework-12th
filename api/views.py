from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Routine
from .Serializers import RoutineSerializer
from rest_framework import viewsets

class RoutineViewSet(viewsets.ModelViewSet) :
    serializer_class = RoutineSerializer
    queryset = Routine.objects.all()

class RoutineList(APIView):
    """
    insert routine
    /routine/
    """
    def post(self, request, format=None):
        serializer = RoutineSerializer(data=request.data)
        print(request.data)
        # raise_excptions 이용하면 코드 간소화 가능
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    selsect all routine
    /routine/
    """
    def get(self, request, format=None):
        queryset = Routine.objects.all()
        serializer = RoutineSerializer(queryset, many=True)
        return Response(serializer.data)


class RoutineDetail(APIView):
    def get_object(self, pk):
        try:
            return Routine.objects.get(pk=pk)
        except Routine.DoesNotExist:
            raise Http404

    """
    select rotuine
    /routine/{pk}/
    """
    def get(self, request, pk):
        routine = self.get_object(pk)
        serializer = RoutineSerializer(routine)
        return Response(serializer.data)

    """
    update rotine
    /routine/{pk}/
    """
    def put(self, request, pk, format=None):
        routine = self.get_object(pk)
        serializer = RoutineSerializer(routine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    delete routine
    /routine/{pk}/
    """
    def delete(self, request, pk, format=None):
        routine = self.get_object(pk)
        routine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)