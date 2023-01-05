from rest_framework import serializers

from .models import (
    Teacher,
    Lessons,
    Student,
    Grade
)

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = (
            "id",
            "name"
        )

class LessonsSerializer(serializers.ModelSerializer):

    teacher = serializers.StringRelatedField()
    teacher_id = serializers.IntegerField()

    class Meta:
        model = Lessons
        fields = (
            # "id",
            "name",
            "teacher",
            "teacher_id"
        )

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = (
            "id",
            "number",
            "first_name",
            "last_name"
        )

class GradeSerializer(serializers.ModelSerializer):

    student = StudentSerializer(read_only=True)
    student_id = serializers.IntegerField(write_only=True)
    lessons = serializers.StringRelatedField(read_only=True)
    lessons_id = serializers.IntegerField()

    class Meta:
        model = Grade
        fields = (
            "id",
            "student",
            "student_id",
            "lessons",
            "lessons_id",
            "grade"
        )
    
    # def create(self, validated_data):
    #     return super().create(validated_data)