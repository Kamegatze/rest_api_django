from django.db import models


# Create your models here.

class Student(models.Model):
    last_name = models.CharField(verbose_name='last_name', max_length=100)
    first_name = models.CharField(verbose_name='first_name', max_length=100)
    patronymic = models.CharField(verbose_name='patronymic', max_length=100)
    email = models.CharField(verbose_name='email', max_length=100)
