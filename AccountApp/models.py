from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(AbstractUser):
    pass
class doctor(user):
    phone=models.CharField(max_length=8)
    licene_number=models.CharField(max_length=6,unique=True)
    specialities=models.ManyToManyField('Speciality', related_name='doctors',blank=True)
class Patient(user):
    phone=models.CharField(max_length=8)
    birth_date=models.DateField()
    national_id = models.CharField(max_length=8, unique=True)
class Speciality(models.Model):
    name = models.CharField(max_length=100)
