from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def BasicView(requeset):
    return HttpResponse("hi")


def MovieListView(request):
    return HttpResponse("movielistview")

def CommentsView(request):
    return HttpResponse("commentsview")

def DescriptionView(request):
    return HttpResponse("descri")