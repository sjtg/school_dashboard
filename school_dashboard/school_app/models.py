# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser



# Create your models here.


class User(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	quizzes = models.ManyToManyField(Quiz, through="TakenQuize")
	interests = models.ManyToManyField(Subject, related_name='interested_students')
