from django.db import models
from django.db.models import Model

# Create your models here.

from django.db.models import Model, SmallIntegerField, ImageField, DateTimeField
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField

class Student(Model):
    class Gender(TextChoices):
        MAN = 'man', 'Man'
        WOMEN = 'women', 'Women'

    class Course(TextChoices):
        PYTHON = 'python', 'Python'
        JAVA = 'java', 'Java'
        REACT = 'react', 'React'

    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    age = SmallIntegerField()
    gender = CharField(choices=Gender)
    address = CharField()
    course = CharField(choices=Course)
    photo = ImageField(upload_to='products/')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
