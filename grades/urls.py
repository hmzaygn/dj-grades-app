from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    TeacherView,
    LessonsView,
    StudentView,
    GradeView
)

router = DefaultRouter()
router.register("teacher", TeacherView)
router.register("lessons", LessonsView)
router.register("student", StudentView)
router.register("grade", GradeView)

urlpatterns = []

urlpatterns += router.urls

