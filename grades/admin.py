from django.contrib import admin
from .models import (
    Teacher,
    Lessons,
    Student,
    Grade
)

admin.site.register(Teacher)
admin.site.register(Lessons)
admin.site.register(Student)
admin.site.register(Grade)