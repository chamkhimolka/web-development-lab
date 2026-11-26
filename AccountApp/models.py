from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.utils import timezone


def validate_past_date(value):
    """La date doit être strictement antérieure à aujourd'hui."""
    if value >= timezone.localdate():
        raise ValidationError("La date de naissance doit être dans le passé.")


phone_validator = RegexValidator(
    r'^\d{8}$', "Le numéro de téléphone doit contenir exactement 8 chiffres."
)


class User(AbstractUser):
    pass


class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(User):
    license_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[MinLengthValidator(6)],
    )
    phone = models.CharField(max_length=8, validators=[phone_validator])
    specialties = models.ManyToManyField(
        Specialty, related_name='doctors', blank=True
    )

    def __str__(self):
        return f"Dr {self.last_name} {self.first_name}"


class Patient(User):
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[RegexValidator(r'^\d{8}$', "Le CIN doit contenir exactement 8 chiffres.")],
    )
    phone = models.CharField(max_length=8, validators=[phone_validator])
    birth_date = models.DateField(validators=[validate_past_date])

    def __str__(self):
        return f"{self.last_name} {self.first_name}"