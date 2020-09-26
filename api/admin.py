from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_code',
        'student_name',
        'student_department'
    )

    list_display_links = (
        'student_code',
    )


class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'professor_code',
        'professor_name',
        'professor_department'
    )

    list_display_links = (
        'professor_code',
    )


admin.site.register(Contact)
admin.site.register(Student,StudentAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Course)
admin.site.register(Enrollment)
