from django.contrib import admin
from .models import Movie, Actor, Screen, Profile, Comment

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Screen)