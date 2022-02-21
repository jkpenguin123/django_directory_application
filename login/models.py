# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_coach = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    name_first = models.CharField(max_length=25)
    mobile_number = models.CharField(max_length=10, unique=True)


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coach_center = models.CharField(max_length=20)


class Tournament(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=24)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_parent = models.CharField(max_length=25)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    tournament = models.ManyToManyField(Tournament)
