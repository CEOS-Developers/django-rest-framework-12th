from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Contact)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Enrollment)
