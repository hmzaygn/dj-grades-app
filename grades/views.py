from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import (
    Teacher,
    Lessons,
    Student,
    Grade
)
from .serializers import (
    TeacherSerializer,
    LessonsSerializer,
    StudentSerializer,
    GradeSerializer
)

class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class LessonsView(ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer

class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class GradeView(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer