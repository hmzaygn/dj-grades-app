from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Lessons(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.PROTECT,
        primary_key=True
        )

    class Meta:
        verbose_name = "lesson"
        verbose_name_plural = "lessons"

    def __str__(self):
        return self.name

class Student(models.Model):
    number = models.PositiveSmallIntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Grade(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="student"
        )
    lessons = models.ForeignKey(
        Lessons,
        on_delete=models.CASCADE,
        related_name="lessons"
        )
    grade = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.student} - {self.lessons} - {self.grade}"